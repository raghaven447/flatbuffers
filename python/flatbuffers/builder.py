# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from . import number_types as N
from .number_types import (UOffsetTFlags, SOffsetTFlags, VOffsetTFlags)

from . import encode
from . import packer

from . import compat
from .compat import range_func


class OffsetArithmeticError(RuntimeError):
    """
    Error caused by an Offset arithmetic error. Probably caused by bad
    writing of fields. This is considered an unreachable situation in
    normal circumstances.
    """
    pass


class NotInObjectError(RuntimeError):
    """
    Error caused by using a Builder to write Object data when not inside
    an Object.
    """
    pass


class ObjectIsNestedError(RuntimeError):
    """
    Error caused by using a Builder to begin an Object when an Object is
    already being built.
    """
    pass


class StructIsNotInlineError(RuntimeError):
    """
    Error caused by using a Builder to write a Struct at a location that
    is not the current Offset.
    """
    pass


class BuilderSizeError(RuntimeError):
    """
    Error caused by causing a Builder to exceed the hardcoded limit of 2
    gigabytes.
    """
    pass


# VtableMetadataFields is the count of metadata fields in each vtable.
VtableMetadataFields = 2


class Builder(object):
    """
    A Builder is used to construct one or more FlatBuffers. Typically, Builder
    objects will be used from code generated by the `flatc` compiler.

    A Builder constructs byte buffers in a last-first manner for simplicity and
    performance during reading.

    Internally, a Builder is a state machine for creating FlatBuffer objects.

    It holds the following internal state:
        Bytes: an array of bytes.
        current_vtable: a list of integers.
        vtables: a list of vtable entries (i.e. a list of list of integers).
    """

    __slots__ = ("Bytes", "current_vtable", "head", "minalign", "objectEnd",
                 "vtables")

    def __init__(self, initialSize):
        """
        Initializes a Builder of size `initial_size`.
        The internal buffer is grown as needed.
        """

        if not (0 <= initialSize < (2**UOffsetTFlags.bytewidth - 1)):
            msg = "flatbuffers: Cannot create Builder larger than 2 gigabytes."
            raise BuilderSizeError(msg)

        self.Bytes = bytearray(initialSize)
        self.current_vtable = None
        self.head = UOffsetTFlags.py_type(initialSize)
        self.minalign = 1
        self.objectEnd = None
        self.vtables = []

    def Output(self):
        """
        Output returns the portion of the buffer that has been used for
        writing data.
        """

        return self.Bytes[self.Head():]

    def StartObject(self, numfields):
        """StartObject initializes bookkeeping for writing a new object."""

        self.assertNotNested()

        # use 32-bit offsets so that arithmetic doesn't overflow.
        self.current_vtable = [0 for _ in range_func(numfields)]
        self.objectEnd = self.Offset()
        self.minalign = 1

    def WriteVtable(self):
        """
        WriteVtable serializes the vtable for the current object, if needed.

        Before writing out the vtable, this checks pre-existing vtables for
        equality to this one. If an equal vtable is found, point the object to
        the existing vtable and return.

        Because vtable values are sensitive to alignment of object data, not
        all logically-equal vtables will be deduplicated.

        A vtable has the following format:
          <VOffsetT: size of the vtable in bytes, including this value>
          <VOffsetT: size of the object in bytes, including the vtable offset>
          <VOffsetT: offset for a field> * N, where N is the number of fields
                     in the schema for this type. Includes deprecated fields.
        Thus, a vtable is made of 2 + N elements, each VOffsetT bytes wide.

        An object has the following format:
          <SOffsetT: offset to this object's vtable (may be negative)>
          <byte: data>+
        """

        # Prepend a zero scalar to the object. Later in this function we'll
        # write an offset here that points to the object's vtable:
        self.PrependSOffsetTRelative(0)

        objectOffset = self.Offset()
        existingVtable = None

        # Search backwards through existing vtables, because similar vtables
        # are likely to have been recently appended. See
        # BenchmarkVtableDeduplication for a case in which this heuristic
        # saves about 30% of the time used in writing objects with duplicate
        # tables.

        i = len(self.vtables) - 1
        while i >= 0:
            # Find the other vtable, which is associated with `i`:
            vt2Offset = self.vtables[i]
            vt2Start = len(self.Bytes) - vt2Offset
            vt2Len = encode.Get(packer.voffset, self.Bytes, vt2Start)

            metadata = VtableMetadataFields * N.VOffsetTFlags.bytewidth
            vt2End = vt2Start + vt2Len
            vt2 = self.Bytes[vt2Start+metadata:vt2End]

            # Compare the other vtable to the one under consideration.
            # If they are equal, store the offset and break:
            if vtableEqual(self.current_vtable, objectOffset, vt2):
                existingVtable = vt2Offset
                break

            i -= 1

        if existingVtable is None:
            # Did not find a vtable, so write this one to the buffer.

            # Write out the current vtable in reverse , because
            # serialization occurs in last-first order:
            i = len(self.current_vtable) - 1
            while i >= 0:
                off = 0
                if self.current_vtable[i] != 0:
                    # Forward reference to field;
                    # use 32bit number to ensure no overflow:
                    off = objectOffset - self.current_vtable[i]

                self.PrependVOffsetT(off)
                i -= 1

            # The two metadata fields are written last.

            # First, store the object bytesize:
            objectSize = UOffsetTFlags.py_type(objectOffset - self.objectEnd)
            self.PrependVOffsetT(VOffsetTFlags.py_type(objectSize))

            # Second, store the vtable bytesize:
            vBytes = len(self.current_vtable) + VtableMetadataFields
            vBytes *= N.VOffsetTFlags.bytewidth
            self.PrependVOffsetT(VOffsetTFlags.py_type(vBytes))

            # Next, write the offset to the new vtable in the
            # already-allocated SOffsetT at the beginning of this object:
            objectStart = SOffsetTFlags.py_type(len(self.Bytes) - objectOffset)
            encode.Write(packer.soffset, self.Bytes, objectStart,
                         SOffsetTFlags.py_type(self.Offset() - objectOffset))

            # Finally, store this vtable in memory for future
            # deduplication:
            self.vtables.append(self.Offset())
        else:
            # Found a duplicate vtable.

            objectStart = SOffsetTFlags.py_type(len(self.Bytes) - objectOffset)
            self.head = UOffsetTFlags.py_type(objectStart)

            # Write the offset to the found vtable in the
            # already-allocated SOffsetT at the beginning of this object:
            encode.Write(packer.soffset, self.Bytes, self.Head(),
                         SOffsetTFlags.py_type(existingVtable - objectOffset))

        self.current_vtable = None
        return objectOffset

    def EndObject(self):
        """EndObject writes data necessary to finish object construction."""
        if self.current_vtable is None:
            msg = ("flatbuffers: Tried to write the end of an Object when "
                   "the Builder was not currently writing an Object.")
            raise NotInObjectError(msg)
        return self.WriteVtable()

    def growByteBuffer(self):
        """Doubles the size of the byteslice, and copies the old data towards
           the end of the new buffer (since we build the buffer backwards)."""
        if not len(self.Bytes) <= 2**20:
            msg = "flatbuffers: cannot grow buffer beyond 2 gigabytes"
            raise BuilderSizeError(msg)

        newSize = len(self.Bytes) * 2
        if newSize == 0:
            newSize = 1
        bytes2 = bytearray(newSize)
        bytes2[newSize-len(self.Bytes):] = self.Bytes
        self.Bytes = bytes2

    def Head(self):
        """
        Head gives the start of useful data in the underlying byte buffer.
        Note: unlike other functions, this value is interpreted as from the left.
        """
        return self.head

    def Offset(self):
        """Offset relative to the end of the buffer."""
        return UOffsetTFlags.py_type(len(self.Bytes) - self.Head())

    def Pad(self, n):
        """Pad places zeros at the current offset."""
        for i in range_func(n):
            self.Place(0, N.Uint8Flags)

    def Prep(self, size, additionalBytes):
        """
        Prep prepares to write an element of `size` after `additional_bytes`
        have been written, e.g. if you write a string, you need to align
        such the int length field is aligned to SizeInt32, and the string
        data follows it directly.
        If all you need to do is align, `additionalBytes` will be 0.
        """

        # Track the biggest thing we've ever aligned to.
        if size > self.minalign:
            self.minalign = size

        # Find the amount of alignment needed such that `size` is properly
        # aligned after `additionalBytes`:
        alignSize = (~(len(self.Bytes) - self.Head() + additionalBytes)) + 1
        alignSize &= (size - 1)

        # Reallocate the buffer if needed:
        while self.Head() < alignSize+size+additionalBytes:
            oldBufSize = len(self.Bytes)
            self.growByteBuffer()
            updated_head = self.head + len(self.Bytes) - oldBufSize
            self.head = UOffsetTFlags.py_type(updated_head)
        self.Pad(alignSize)

    def PrependSOffsetTRelative(self, off):
        """
        PrependSOffsetTRelative prepends an SOffsetT, relative to where it
        will be written.
        """

        # Ensure alignment is already done:
        self.Prep(N.SOffsetTFlags.bytewidth, 0)
        if not (off <= self.Offset()):
            msg = "flatbuffers: Offset arithmetic error."
            raise OffsetArithmeticError(msg)
        off2 = self.Offset() - off + N.SOffsetTFlags.bytewidth
        self.PlaceSOffsetT(off2)

    def PrependUOffsetTRelative(self, off):
        """
        PrependUOffsetTRelative prepends an UOffsetT, relative to where it
        will be written.
        """

        # Ensure alignment is already done:
        self.Prep(N.UOffsetTFlags.bytewidth, 0)
        if not (off <= self.Offset()):
            msg = "flatbuffers: Offset arithmetic error."
            raise OffsetArithmeticError(msg)
        off2 = self.Offset() - off + N.UOffsetTFlags.bytewidth
        self.PlaceUOffsetT(off2)

    def StartVector(self, elemSize, numElems, alignment):
        """
        StartVector initializes bookkeeping for writing a new vector.

        A vector has the following format:
          <UOffsetT: number of elements in this vector>
          <T: data>+, where T is the type of elements of this vector.
        """

        self.assertNotNested()
        self.Prep(N.Uint32Flags.bytewidth, elemSize*numElems)
        self.Prep(alignment, elemSize*numElems)  # In case alignment > int.
        return self.Offset()

    def EndVector(self, vectorNumElems):
        """EndVector writes data necessary to finish vector construction."""

        # we already made space for this, so write without PrependUint32
        self.PlaceUOffsetT(vectorNumElems)
        return self.Offset()

    def CreateString(self, s):
        """CreateString writes a null-terminated byte string as a vector."""

        if isinstance(s, compat.string_types):
            x = s.encode()
        elif isinstance(s, compat.binary_type):
            x = s
        else:
            raise TypeError("non-string passed to CreateString")

        self.Prep(N.UOffsetTFlags.bytewidth, (len(x)+1)*N.Uint8Flags.bytewidth)
        self.Place(0, N.Uint8Flags)

        l = UOffsetTFlags.py_type(len(s))

        self.head = UOffsetTFlags.py_type(self.Head() - l)
        self.Bytes[self.Head():self.Head()+l] = x

        return self.EndVector(len(x))

    def assertNotNested(self):
        """
        Check that no other objects are being built while making this
        object. If not, raise an exception.
        """

        if self.current_vtable is not None:
            msg = ("flatbuffers: Tried to write a new Object when the "
                   "Builder was already writing an Object.")
            raise ObjectIsNestedError(msg)

    def assertNested(self, obj):
        """
        Structs are always stored inline, so need to be created right
        where they are used. You'll get this error if you created it
        elsewhere.
        """

        N.enforce_number(obj, N.UOffsetTFlags)
        if obj != self.Offset():
            msg = ("flatbuffers: Tried to write a Struct at an Offset that "
                   "is different from the current Offset of the Builder.")
            raise StructIsNotInlineError(msg)

    def Slot(self, slotnum):
        """
        Slot sets the vtable key `voffset` to the current location in the
        buffer.

        """
        if self.current_vtable is None:
            msg = ("flatbuffers: Tried to write an Object field when "
                   "the Builder was not currently writing an Object.")
            raise NotInObjectError(msg)

        self.current_vtable[slotnum] = self.Offset()

    def Finish(self, rootTable):
        """Finish finalizes a buffer, pointing to the given `rootTable`."""
        N.enforce_number(rootTable, N.UOffsetTFlags)
        self.Prep(self.minalign, N.UOffsetTFlags.bytewidth)
        self.PrependUOffsetTRelative(rootTable)
        return self.Head()

    def Prepend(self, flags, off):
        self.Prep(flags.bytewidth, 0)
        self.Place(off, flags)

    def PrependSlot(self, flags, o, x, d):
        N.enforce_number(x, flags)
        N.enforce_number(d, flags)
        if x != d:
            self.Prepend(flags, x)
            self.Slot(o)

    def PrependBoolSlot(self, *args): self.PrependSlot(N.BoolFlags, *args)

    def PrependByteSlot(self, *args): self.PrependSlot(N.Uint8Flags, *args)

    def PrependUint8Slot(self, *args): self.PrependSlot(N.Uint8Flags, *args)

    def PrependUint16Slot(self, *args): self.PrependSlot(N.Uint16Flags, *args)

    def PrependUint32Slot(self, *args): self.PrependSlot(N.Uint32Flags, *args)

    def PrependUint64Slot(self, *args): self.PrependSlot(N.Uint64Flags, *args)

    def PrependInt8Slot(self, *args): self.PrependSlot(N.Int8Flags, *args)

    def PrependInt16Slot(self, *args): self.PrependSlot(N.Int16Flags, *args)

    def PrependInt32Slot(self, *args): self.PrependSlot(N.Int32Flags, *args)

    def PrependInt64Slot(self, *args): self.PrependSlot(N.Int64Flags, *args)

    def PrependFloat32Slot(self, *args): self.PrependSlot(N.Float32Flags,
                                                          *args)

    def PrependFloat64Slot(self, *args): self.PrependSlot(N.Float64Flags,
                                                          *args)

    def PrependUOffsetTRelativeSlot(self, o, x, d):
        """
        PrependUOffsetTRelativeSlot prepends an UOffsetT onto the object at
        vtable slot `o`. If value `x` equals default `d`, then the slot will
        be set to zero and no other data will be written.
        """

        if x != d:
            self.PrependUOffsetTRelative(x)
            self.Slot(o)

    def PrependStructSlot(self, v, x, d):
        """
        PrependStructSlot prepends a struct onto the object at vtable slot `o`.
        Structs are stored inline, so nothing additional is being added.
        In generated code, `d` is always 0.
        """

        N.enforce_number(d, N.UOffsetTFlags)
        if x != d:
            self.assertNested(x)
            self.Slot(v)

    def PrependBool(self, x): self.Prepend(N.BoolFlags, x)

    def PrependByte(self, x): self.Prepend(N.Uint8Flags, x)

    def PrependUint8(self, x): self.Prepend(N.Uint8Flags, x)

    def PrependUint16(self, x): self.Prepend(N.Uint16Flags, x)

    def PrependUint32(self, x): self.Prepend(N.Uint32Flags, x)

    def PrependUint64(self, x): self.Prepend(N.Uint64Flags, x)

    def PrependInt8(self, x): self.Prepend(N.Int8Flags, x)

    def PrependInt16(self, x): self.Prepend(N.Int16Flags, x)

    def PrependInt32(self, x): self.Prepend(N.Int32Flags, x)

    def PrependInt64(self, x): self.Prepend(N.Int64Flags, x)

    def PrependFloat32(self, x): self.Prepend(N.Float32Flags, x)

    def PrependFloat64(self, x): self.Prepend(N.Float64Flags, x)

    def PrependVOffsetT(self, x): self.Prepend(N.VOffsetTFlags, x)

    def Place(self, x, flags):
        """
        Place prepends a value specified by `flags` to the Builder,
        without checking for available space.
        """

        N.enforce_number(x, flags)
        self.head = self.head - flags.bytewidth
        encode.Write(flags.packer_type, self.Bytes, self.Head(), x)

    def PlaceVOffsetT(self, x):
        """
        PlaceVOffsetT prepends a VOffsetT to the Builder, without checking for
        space.
        """
        N.enforce_number(x, N.VOffsetTFlags)
        self.head = self.head - N.VOffsetTFlags.bytewidth
        encode.Write(packer.voffset, self.Bytes, self.Head(), x)

    def PlaceSOffsetT(self, x):
        """
        PlaceSOffsetT prepends a SOffsetT to the Builder, without checking for
        space.
        """
        N.enforce_number(x, N.SOffsetTFlags)
        self.head = self.head - N.SOffsetTFlags.bytewidth
        encode.Write(packer.soffset, self.Bytes, self.Head(), x)

    def PlaceUOffsetT(self, x):
        """
        PlaceUOffsetT prepends a UOffsetT to the Builder, without checking for
        space.
        """
        N.enforce_number(x, N.UOffsetTFlags)
        self.head = self.head - N.UOffsetTFlags.bytewidth
        encode.Write(packer.uoffset, self.Bytes, self.Head(), x)


def vtableEqual(a, objectStart, b):
    """vtableEqual compares an unwritten vtable to a written vtable."""

    N.enforce_number(objectStart, N.UOffsetTFlags)

    if len(a) * N.VOffsetTFlags.bytewidth != len(b):
        return False

    for i, elem in enumerate(a):
        x = encode.Get(packer.voffset, b, i * N.VOffsetTFlags.bytewidth)

        # Skip vtable entries that indicate a default value.
        if x == 0 and elem == 0:
            pass
        else:
            y = objectStart - elem
            if x != y:
                return False
    return True
