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

import os.path
import sys

PY_VERSION = sys.version_info[:2]

import ctypes
from collections import defaultdict
import timeit
import unittest

import flatbuffers.builder
from flatbuffers import compat
from flatbuffers.compat import range_func as compat_range

import flatbuffers
from flatbuffers import number_types as N

from MyGame.Example import (
    Any,  # refers to generated code
    Color,  # refers to generated code
    Monster,  # refers to generated code
    Test,  # refers to generated code
    Stat,  # refers to generated code
    Vec3,  # refers to generated code
)


def assertRaises(test_case, fn, exception_class):
    ''' Backwards-compatible assertion for exceptions raised. '''

    exc = None
    try:
        fn()
    except Exception as e:
        exc = e
    test_case.assertTrue(exc is not None)
    test_case.assertTrue(isinstance(exc, exception_class))


class TestWireFormat(unittest.TestCase):
    def test_wire_format(self):
        # Verify that using the generated Python code builds a buffer without
        # returning errors, and is interpreted correctly:
        gen_buf, gen_off = make_monster_from_generated_code()
        CheckReadBuffer(gen_buf, gen_off)

        # Verify that the canonical flatbuffer file is readable by the
        # generated Python code. Note that context managers are not part of
        # Python 2.5, so we use the simpler open/close methods here:
        f = open('monsterdata_test.mon', 'rb')
        canonicalWireData = f.read()
        f.close()
        CheckReadBuffer(bytearray(canonicalWireData), 0)

        # Write the generated buffer out to a file:
        f = open('monsterdata_python_wire.mon', 'wb')
        f.write(gen_buf[gen_off:])
        f.close()


def CheckReadBuffer(buf, offset):
    ''' CheckReadBuffer checks that the given buffer is evaluated correctly
        as the example Monster. '''

    def asserter(stmt):
        ''' An assertion helper that is separated from TestCase classes. '''
        if not stmt:
            raise AssertionError('CheckReadBuffer case failed')

    monster = Monster.Monster.GetRoot(buf, offset)

    asserter(monster.hp == 80)
    asserter(monster.mana == 150)
    asserter(monster.name == b'MyMonster')

    # initialize a Vec3 from pos
    vec = monster.pos
    asserter(vec is not None)

    # verify the properties of the Vec3
    asserter(vec.x == 1.0)
    asserter(vec.y == 2.0)
    asserter(vec.z == 3.0)
    asserter(vec.test1 == 3.0)
    asserter(vec.test2 == 2)

    # initialize a Test from Test3(...)
    t = vec.test3
    asserter(t is not None)

    # verify the properties of the Test
    asserter(t.a == 5)
    asserter(t.b == 6)

    # verify that the enum code matches the enum declaration:
    union_type = Any.Any
    asserter(monster.test_type == union_type.Monster)

    # initialize a Table from a union field Test(...)
    table2 = monster.test
    asserter(type(table2) is flatbuffers.Table)

    # initialize a Monster from the Table from the union
    monster2 = Monster.Monster()
    monster2.Init(table2.Bytes, table2.Pos)

    asserter(monster2.name == b"Fred")

    # iterate through the first monster's inventory:
    asserter(monster.inventory_length == 5)

    invsum = 0
    for v in monster.inventory:
        invsum += int(v)
    asserter(invsum == 10)

    asserter(monster.test4_length == 2)

    # create a 'Test' object and populate it:
    test0, test1 = tuple(monster.test4)[:2]
    asserter(type(test0) is Test.Test)
    asserter(type(test1) is Test.Test)

    # the position of test0 and test1 are swapped in monsterdata_java_wire
    # and monsterdata_test_wire, so ignore ordering
    v0 = test0.a
    v1 = test0.b
    v2 = test1.a
    v3 = test1.b
    sumtest12 = int(v0) + int(v1) + int(v2) + int(v3)

    asserter(sumtest12 == 100)

    asserter(monster.testarrayofstring_length == 2)
    asserter(tuple(monster.testarrayofstring)[0] == b"test1")
    asserter(tuple(monster.testarrayofstring)[1] == b"test2")

    asserter(monster.enemy is None)

    asserter(monster.testarrayoftables_length == 0)
    asserter(monster.testnestedflatbuffer_length == 0)
    asserter(monster.testempty is None)


class TestFuzz(unittest.TestCase):
    ''' Low level stress/fuzz test: serialize/deserialize a variety of
        different kinds of data in different combinations '''

    ofInt32Bytes = compat.binary_type([0x83, 0x33, 0x33, 0x33])
    ofInt64Bytes = compat.binary_type([0x84, 0x44, 0x44, 0x44,
                                       0x44, 0x44, 0x44, 0x44])
    overflowingInt32Val = flatbuffers.Get(N.Int32Flags.packer_type,
                                          ofInt32Bytes, 0)
    overflowingInt64Val = flatbuffers.Get(N.Int64Flags.packer_type,
                                          ofInt64Bytes, 0)

    # Values we're testing against: chosen to ensure no bits get chopped
    # off anywhere, and also be different from eachother.
    boolVal = True
    int8Val = N.Int8Flags.py_type(-127)  # 0x81
    uint8Val = N.Uint8Flags.py_type(0xFF)
    int16Val = N.Int16Flags.py_type(-32222)  # 0x8222
    uint16Val = N.Uint16Flags.py_type(0xFEEE)
    int32Val = N.Int32Flags.py_type(overflowingInt32Val)
    uint32Val = N.Uint32Flags.py_type(0xFDDDDDDD)
    int64Val = N.Int64Flags.py_type(overflowingInt64Val)
    uint64Val = N.Uint64Flags.py_type(0xFCCCCCCCCCCCCCCC)
    # Python uses doubles, so force it here
    float32Val = N.Float32Flags.py_type(ctypes.c_float(3.14159).value)
    float64Val = N.Float64Flags.py_type(3.14159265359)

    def test_fuzz(self):
        return self.check_once(11, 100)

    def check_once(self, fuzzFields, fuzzObjects):
        testValuesMax = 11  # hardcoded to the number of scalar types

        builder = flatbuffers.Builder(0)
        l = LCG()

        objects = [0 for _ in compat_range(fuzzObjects)]

        # Generate fuzzObjects random objects each consisting of
        # fuzzFields fields, each of a random type.
        for i in compat_range(fuzzObjects):
            builder.StartObject(fuzzFields)

            for j in compat_range(fuzzFields):
                choice = int(l.Next()) % testValuesMax
                if choice == 0:
                    builder.PrependBoolSlot(int(j), self.boolVal, False)
                elif choice == 1:
                    builder.PrependInt8Slot(int(j), self.int8Val, 0)
                elif choice == 2:
                    builder.PrependUint8Slot(int(j), self.uint8Val, 0)
                elif choice == 3:
                    builder.PrependInt16Slot(int(j), self.int16Val, 0)
                elif choice == 4:
                    builder.PrependUint16Slot(int(j), self.uint16Val, 0)
                elif choice == 5:
                    builder.PrependInt32Slot(int(j), self.int32Val, 0)
                elif choice == 6:
                    builder.PrependUint32Slot(int(j), self.uint32Val, 0)
                elif choice == 7:
                    builder.PrependInt64Slot(int(j), self.int64Val, 0)
                elif choice == 8:
                    builder.PrependUint64Slot(int(j), self.uint64Val, 0)
                elif choice == 9:
                    builder.PrependFloat32Slot(int(j), self.float32Val, 0)
                elif choice == 10:
                    builder.PrependFloat64Slot(int(j), self.float64Val, 0)
                else:
                    raise RuntimeError('unreachable')

            off = builder.EndObject()

            # store the offset from the end of the builder buffer,
            # since it will keep growing:
            objects[i] = off

        # Do some bookkeeping to generate stats on fuzzes:
        stats = defaultdict(int)

        def check(table, desc, want, got):
            stats[desc] += 1
            self.assertEqual(want, got, "%s != %s, %s" % (want, got, desc))

        l = LCG()  # Reset.

        # Test that all objects we generated are readable and return the
        # expected values. We generate random objects in the same order
        # so this is deterministic.
        for i in compat_range(fuzzObjects):

            table = flatbuffers.Table(builder.Bytes,
                                      len(builder.Bytes) - objects[i])

            for j in compat_range(fuzzFields):
                field_count = flatbuffers.builder.VtableMetadataFields + j
                f = N.VOffsetTFlags.py_type(field_count *
                                            N.VOffsetTFlags.bytewidth)
                choice = int(l.Next()) % testValuesMax

                if choice == 0:
                    check(table, "bool", self.boolVal,
                          table.GetSlot(f, False, N.BoolFlags))
                elif choice == 1:
                    check(table, "int8", self.int8Val,
                          table.GetSlot(f, 0, N.Int8Flags))
                elif choice == 2:
                    check(table, "uint8", self.uint8Val,
                          table.GetSlot(f, 0, N.Uint8Flags))
                elif choice == 3:
                    check(table, "int16", self.int16Val,
                          table.GetSlot(f, 0, N.Int16Flags))
                elif choice == 4:
                    check(table, "uint16", self.uint16Val,
                          table.GetSlot(f, 0, N.Uint16Flags))
                elif choice == 5:
                    check(table, "int32", self.int32Val,
                          table.GetSlot(f, 0, N.Int32Flags))
                elif choice == 6:
                    check(table, "uint32", self.uint32Val,
                          table.GetSlot(f, 0, N.Uint32Flags))
                elif choice == 7:
                    check(table, "int64", self.int64Val,
                          table.GetSlot(f, 0, N.Int64Flags))
                elif choice == 8:
                    check(table, "uint64", self.uint64Val,
                          table.GetSlot(f, 0, N.Uint64Flags))
                elif choice == 9:
                    check(table, "float32", self.float32Val,
                          table.GetSlot(f, 0, N.Float32Flags))
                elif choice == 10:
                    check(table, "float64", self.float64Val,
                          table.GetSlot(f, 0, N.Float64Flags))
                else:
                    raise RuntimeError('unreachable')

        # If enough checks were made, verify that all scalar types were used:
        self.assertEqual(testValuesMax, len(stats),
                         "fuzzing failed to test all scalar types: %s" % stats)


class TestByteLayout(unittest.TestCase):
    ''' TestByteLayout checks the bytes of a Builder in various scenarios. '''

    def assertBuilderEquals(self, builder, want_chars_or_ints):
        def integerize(x):
            if isinstance(x, compat.string_types):
                return ord(x)
            return x

        want_ints = list(map(integerize, want_chars_or_ints))
        want = bytearray(want_ints)
        got = builder.Output()
        self.assertEqual(want, got)

    def test_numbers(self):
        b = flatbuffers.Builder(0)
        self.assertBuilderEquals(b, [])
        b.PrependBool(True)
        self.assertBuilderEquals(b, [1])
        b.PrependInt8(-127)
        self.assertBuilderEquals(b, [129, 1])
        b.PrependUint8(255)
        self.assertBuilderEquals(b, [255, 129, 1])
        b.PrependInt16(-32222)
        self.assertBuilderEquals(b, [0x22, 0x82, 0, 255, 129, 1])  # first pad
        b.PrependUint16(0xFEEE)
        # no pad this time:
        self.assertBuilderEquals(b, [0xEE, 0xFE, 0x22, 0x82, 0, 255, 129, 1])
        b.PrependInt32(-53687092)
        self.assertBuilderEquals(b, [204, 204, 204, 252, 0xEE, 0xFE,
                                     0x22, 0x82, 0, 255, 129, 1])
        b.PrependUint32(0x98765432)
        self.assertBuilderEquals(b, [0x32, 0x54, 0x76, 0x98,
                                     204, 204, 204, 252,
                                     0xEE, 0xFE, 0x22, 0x82,
                                     0, 255, 129, 1])

    def test_numbers64(self):
        b = flatbuffers.Builder(0)
        b.PrependUint64(0x1122334455667788)
        self.assertBuilderEquals(b, [0x88, 0x77, 0x66, 0x55,
                                     0x44, 0x33, 0x22, 0x11])

        b = flatbuffers.Builder(0)
        b.PrependInt64(0x1122334455667788)
        self.assertBuilderEquals(b, [0x88, 0x77, 0x66, 0x55,
                                     0x44, 0x33, 0x22, 0x11])

    def test_1xbyte_vector(self):
        b = flatbuffers.Builder(0)
        self.assertBuilderEquals(b, [])
        b.StartVector(flatbuffers.Uint8Flags.bytewidth, 1, 1)
        self.assertBuilderEquals(b, [0, 0, 0])  # align to 4bytes
        b.PrependByte(1)
        self.assertBuilderEquals(b, [1, 0, 0, 0])
        b.EndVector(1)
        self.assertBuilderEquals(b, [1, 0, 0, 0, 1, 0, 0, 0])  # padding

    def test_2xbyte_vector(self):
        b = flatbuffers.Builder(0)
        b.StartVector(flatbuffers.Uint8Flags.bytewidth, 2, 1)
        self.assertBuilderEquals(b, [0, 0])  # align to 4bytes
        b.PrependByte(1)
        self.assertBuilderEquals(b, [1, 0, 0])
        b.PrependByte(2)
        self.assertBuilderEquals(b, [2, 1, 0, 0])
        b.EndVector(2)
        self.assertBuilderEquals(b, [2, 0, 0, 0, 2, 1, 0, 0])  # padding

    def test_1xuint16_vector(self):
        b = flatbuffers.Builder(0)
        b.StartVector(flatbuffers.Uint16Flags.bytewidth, 1, 1)
        self.assertBuilderEquals(b, [0, 0])  # align to 4bytes
        b.PrependUint16(1)
        self.assertBuilderEquals(b, [1, 0, 0, 0])
        b.EndVector(1)
        self.assertBuilderEquals(b, [1, 0, 0, 0, 1, 0, 0, 0])  # padding

    def test_2xuint16_vector(self):
        b = flatbuffers.Builder(0)
        b.StartVector(flatbuffers.Uint16Flags.bytewidth, 2, 1)
        self.assertBuilderEquals(b, [])  # align to 4bytes
        b.PrependUint16(0xABCD)
        self.assertBuilderEquals(b, [0xCD, 0xAB])
        b.PrependUint16(0xDCBA)
        self.assertBuilderEquals(b, [0xBA, 0xDC, 0xCD, 0xAB])
        b.EndVector(2)
        self.assertBuilderEquals(b, [2, 0, 0, 0, 0xBA, 0xDC, 0xCD, 0xAB])

    def test_create_ascii_string(self):
        b = flatbuffers.Builder(0)
        b.CreateString(u"foo".encode('ascii'))
        # 0-terminated, no pad:
        self.assertBuilderEquals(b, [3, 0, 0, 0, 'f', 'o', 'o', 0])
        b.CreateString(u"moop".encode('ascii'))
        # 0-terminated, 3-byte pad:
        self.assertBuilderEquals(b, [4, 0, 0, 0, 'm', 'o', 'o', 'p',
                                     0, 0, 0, 0,
                                     3, 0, 0, 0, 'f', 'o', 'o', 0])

    def test_create_arbitrary_string(self):
        b = flatbuffers.Builder(0)
        s = "\x01\x02\x03".encode('utf-8')
        b.CreateString(s)
        # 0-terminated, no pad:
        self.assertBuilderEquals(b, [3, 0, 0, 0, 1, 2, 3, 0])
        s2 = "\x04\x05\x06\x07".encode('utf-8')
        b.CreateString(s2)
        # 0-terminated, 3-byte pad:
        self.assertBuilderEquals(b, [4, 0, 0, 0, 4, 5, 6, 7, 0, 0, 0, 0,
                                     3, 0, 0, 0, 1, 2, 3, 0])

    def test_empty_vtable(self):
        b = flatbuffers.Builder(0)
        b.StartObject(0)
        self.assertBuilderEquals(b, [])
        b.EndObject()
        self.assertBuilderEquals(b, [4, 0, 4, 0, 4, 0, 0, 0])

    def test_vtable_with_one_true_bool(self):
        b = flatbuffers.Builder(0)
        self.assertBuilderEquals(b, [])
        b.StartObject(1)
        self.assertBuilderEquals(b, [])
        b.PrependBoolSlot(0, True, False)
        b.EndObject()
        self.assertBuilderEquals(b, [
            6, 0,  # vtable bytes
            8, 0,  # length of object including vtable offset
            7, 0,  # start of bool value
            6, 0, 0, 0,  # offset for start of vtable (int32)
            0, 0, 0,  # padded to 4 bytes
            1,  # bool value
        ])

    def test_vtable_with_one_default_bool(self):
        b = flatbuffers.Builder(0)
        self.assertBuilderEquals(b, [])
        b.StartObject(1)
        self.assertBuilderEquals(b, [])
        b.PrependBoolSlot(0, False, False)
        b.EndObject()
        self.assertBuilderEquals(b, [
            6, 0,  # vtable bytes
            4, 0,  # end of object from here
            0, 0,  # entry 1 is zero
            6, 0, 0, 0,  # offset for start of vtable (int32)
        ])

    def test_vtable_with_one_int16(self):
        b = flatbuffers.Builder(0)
        b.StartObject(1)
        b.PrependInt16Slot(0, 0x789A, 0)
        b.EndObject()
        self.assertBuilderEquals(b, [
            6, 0,  # vtable bytes
            8, 0,  # end of object from here
            6, 0,  # offset to value
            6, 0, 0, 0,  # offset for start of vtable (int32)
            0, 0,  # padding to 4 bytes
            0x9A, 0x78,
        ])

    def test_vtable_with_two_int16(self):
        b = flatbuffers.Builder(0)
        b.StartObject(2)
        b.PrependInt16Slot(0, 0x3456, 0)
        b.PrependInt16Slot(1, 0x789A, 0)
        b.EndObject()
        self.assertBuilderEquals(b, [
            8, 0,  # vtable bytes
            8, 0,  # end of object from here
            6, 0,  # offset to value 0
            4, 0,  # offset to value 1
            8, 0, 0, 0,  # offset for start of vtable (int32)
            0x9A, 0x78,  # value 1
            0x56, 0x34,  # value 0
        ])

    def test_vtable_with_int16_and_bool(self):
        b = flatbuffers.Builder(0)
        b.StartObject(2)
        b.PrependInt16Slot(0, 0x3456, 0)
        b.PrependBoolSlot(1, True, False)
        b.EndObject()
        self.assertBuilderEquals(b, [
            8, 0,  # vtable bytes
            8, 0,  # end of object from here
            6, 0,  # offset to value 0
            5, 0,  # offset to value 1
            8, 0, 0, 0,  # offset for start of vtable (int32)
            0,  # padding
            1,  # value 1
            0x56, 0x34,  # value 0
        ])

    def test_vtable_with_empty_vector(self):
        b = flatbuffers.Builder(0)
        b.StartVector(flatbuffers.Uint8Flags.bytewidth, 0, 1)
        vecend = b.EndVector(0)
        b.StartObject(1)
        b.PrependUOffsetTRelativeSlot(0, vecend, 0)
        b.EndObject()
        self.assertBuilderEquals(b, [
            6, 0,  # vtable bytes
            8, 0,
            4, 0,  # offset to vector offset
            6, 0, 0, 0,  # offset for start of vtable (int32)
            4, 0, 0, 0,
            0, 0, 0, 0,  # length of vector (not in struct)
        ])

    def test_vtable_with_empty_vector_of_byte_and_some_scalars(self):
        b = flatbuffers.Builder(0)
        b.StartVector(flatbuffers.Uint8Flags.bytewidth, 0, 1)
        vecend = b.EndVector(0)
        b.StartObject(2)
        b.PrependInt16Slot(0, 55, 0)
        b.PrependUOffsetTRelativeSlot(1, vecend, 0)
        b.EndObject()
        self.assertBuilderEquals(b, [
            8, 0,  # vtable bytes
            12, 0,
            10, 0,  # offset to value 0
            4, 0,  # offset to vector offset
            8, 0, 0, 0,  # vtable loc
            8, 0, 0, 0,  # value 1
            0, 0, 55, 0,  # value 0

            0, 0, 0, 0,  # length of vector (not in struct)
        ])

    def test_vtable_with_1_int16_and_2vector_of_int16(self):
        b = flatbuffers.Builder(0)
        b.StartVector(flatbuffers.Int16Flags.bytewidth, 2, 1)
        b.PrependInt16(0x1234)
        b.PrependInt16(0x5678)
        vecend = b.EndVector(2)
        b.StartObject(2)
        b.PrependUOffsetTRelativeSlot(1, vecend, 0)
        b.PrependInt16Slot(0, 55, 0)
        b.EndObject()
        self.assertBuilderEquals(b, [
            8, 0,  # vtable bytes
            12, 0,  # length of object
            6, 0,  # start of value 0 from end of vtable
            8, 0,  # start of value 1 from end of buffer
            8, 0, 0, 0,  # offset for start of vtable (int32)
            0, 0,  # padding
            55, 0,  # value 0
            4, 0, 0, 0,  # vector position from here
            2, 0, 0, 0,  # length of vector (uint32)
            0x78, 0x56,  # vector value 1
            0x34, 0x12,  # vector value 0
        ])

    def test_vtable_with_1_struct_of_1_int8__1_int16__1_int32(self):
        b = flatbuffers.Builder(0)
        b.StartObject(1)
        b.Prep(4 + 4 + 4, 0)
        b.PrependInt8(55)
        b.Pad(3)
        b.PrependInt16(0x1234)
        b.Pad(2)
        b.PrependInt32(0x12345678)
        structStart = b.Offset()
        b.PrependStructSlot(0, structStart, 0)
        b.EndObject()
        self.assertBuilderEquals(b, [
            6, 0,  # vtable bytes
            16, 0,  # end of object from here
            4, 0,  # start of struct from here
            6, 0, 0, 0,  # offset for start of vtable (int32)
            0x78, 0x56, 0x34, 0x12,  # value 2
            0, 0,  # padding
            0x34, 0x12,  # value 1
            0, 0, 0,  # padding
            55,  # value 0
        ])

    def test_vtable_with_1_vector_of_2_struct_of_2_int8(self):
        b = flatbuffers.Builder(0)
        b.StartVector(flatbuffers.Int8Flags.bytewidth * 2, 2, 1)
        b.PrependInt8(33)
        b.PrependInt8(44)
        b.PrependInt8(55)
        b.PrependInt8(66)
        vecend = b.EndVector(2)
        b.StartObject(1)
        b.PrependUOffsetTRelativeSlot(0, vecend, 0)
        b.EndObject()
        self.assertBuilderEquals(b, [
            6, 0,  # vtable bytes
            8, 0,
            4, 0,  # offset of vector offset
            6, 0, 0, 0,  # offset for start of vtable (int32)
            4, 0, 0, 0,  # vector start offset

            2, 0, 0, 0,  # vector length
            66,  # vector value 1,1
            55,  # vector value 1,0
            44,  # vector value 0,1
            33,  # vector value 0,0
        ])

    def test_table_with_some_elements(self):
        b = flatbuffers.Builder(0)
        b.StartObject(2)
        b.PrependInt8Slot(0, 33, 0)
        b.PrependInt16Slot(1, 66, 0)
        off = b.EndObject()
        b.Finish(off)

        self.assertBuilderEquals(b, [
            12, 0, 0, 0,  # root of table: points to vtable offset

            8, 0,  # vtable bytes
            8, 0,  # end of object from here
            7, 0,  # start of value 0
            4, 0,  # start of value 1

            8, 0, 0, 0,  # offset for start of vtable (int32)

            66, 0,  # value 1
            0,  # padding
            33,  # value 0
        ])

    def test__one_unfinished_table_and_one_finished_table(self):
        b = flatbuffers.Builder(0)
        b.StartObject(2)
        b.PrependInt8Slot(0, 33, 0)
        b.PrependInt8Slot(1, 44, 0)
        off = b.EndObject()
        b.Finish(off)

        b.StartObject(3)
        b.PrependInt8Slot(0, 55, 0)
        b.PrependInt8Slot(1, 66, 0)
        b.PrependInt8Slot(2, 77, 0)
        off = b.EndObject()
        b.Finish(off)

        self.assertBuilderEquals(b, [
            16, 0, 0, 0,  # root of table: points to object
            0, 0,  # padding

            10, 0,  # vtable bytes
            8, 0,  # size of object
            7, 0,  # start of value 0
            6, 0,  # start of value 1
            5, 0,  # start of value 2
            10, 0, 0, 0,  # offset for start of vtable (int32)
            0,  # padding
            77,  # value 2
            66,  # value 1
            55,  # value 0

            12, 0, 0, 0,  # root of table: points to object

            8, 0,  # vtable bytes
            8, 0,  # size of object
            7, 0,  # start of value 0
            6, 0,  # start of value 1
            8, 0, 0, 0,  # offset for start of vtable (int32)
            0, 0,  # padding
            44,  # value 1
            33,  # value 0
        ])

    def test_a_bunch_of_bools(self):
        b = flatbuffers.Builder(0)
        b.StartObject(8)
        b.PrependBoolSlot(0, True, False)
        b.PrependBoolSlot(1, True, False)
        b.PrependBoolSlot(2, True, False)
        b.PrependBoolSlot(3, True, False)
        b.PrependBoolSlot(4, True, False)
        b.PrependBoolSlot(5, True, False)
        b.PrependBoolSlot(6, True, False)
        b.PrependBoolSlot(7, True, False)
        off = b.EndObject()
        b.Finish(off)

        self.assertBuilderEquals(b, [
            24, 0, 0, 0,  # root of table: points to vtable offset

            20, 0,  # vtable bytes
            12, 0,  # size of object
            11, 0,  # start of value 0
            10, 0,  # start of value 1
            9, 0,  # start of value 2
            8, 0,  # start of value 3
            7, 0,  # start of value 4
            6, 0,  # start of value 5
            5, 0,  # start of value 6
            4, 0,  # start of value 7
            20, 0, 0, 0,  # vtable offset

            1,  # value 7
            1,  # value 6
            1,  # value 5
            1,  # value 4
            1,  # value 3
            1,  # value 2
            1,  # value 1
            1,  # value 0
        ])

    def test_three_bools(self):
        b = flatbuffers.Builder(0)
        b.StartObject(3)
        b.PrependBoolSlot(0, True, False)
        b.PrependBoolSlot(1, True, False)
        b.PrependBoolSlot(2, True, False)
        off = b.EndObject()
        b.Finish(off)

        self.assertBuilderEquals(b, [
            16, 0, 0, 0,  # root of table: points to vtable offset

            0, 0,  # padding

            10, 0,  # vtable bytes
            8, 0,  # size of object
            7, 0,  # start of value 0
            6, 0,  # start of value 1
            5, 0,  # start of value 2
            10, 0, 0, 0,  # vtable offset from here

            0,  # padding
            1,  # value 2
            1,  # value 1
            1,  # value 0
        ])

    def test_some_floats(self):
        b = flatbuffers.Builder(0)
        b.StartObject(1)
        b.PrependFloat32Slot(0, 1.0, 0.0)
        off = b.EndObject()

        self.assertBuilderEquals(b, [
            6, 0,  # vtable bytes
            8, 0,  # size of object
            4, 0,  # start of value 0
            6, 0, 0, 0,  # vtable offset

            0, 0, 128, 63,  # value 0
        ])


def make_monster_from_generated_code():
    ''' Use generated code to build the example Monster. '''

    b = flatbuffers.Builder(0)
    string = b.CreateString("MyMonster")
    test1 = b.CreateString("test1")
    test2 = b.CreateString("test2")
    fred = b.CreateString("Fred")

    Monster.MonsterStartInventoryVector(b, 5)
    b.PrependByte(4)
    b.PrependByte(3)
    b.PrependByte(2)
    b.PrependByte(1)
    b.PrependByte(0)
    inv = b.EndVector(5)

    Monster.MonsterStart(b)
    Monster.MonsterAddName(b, fred)
    mon2 = Monster.MonsterEnd(b)
    # b.Finish(mon2) not be called, why?

    Monster.MonsterStartTest4Vector(b, 2)
    Test.CreateTest(b, 10, 20)
    Test.CreateTest(b, 30, 40)
    test4 = b.EndVector(2)

    Monster.MonsterStartTestarrayofstringVector(b, 2)
    b.PrependUOffsetTRelative(test2)
    b.PrependUOffsetTRelative(test1)
    testArrayOfString = b.EndVector(2)

    Monster.MonsterStart(b)

    pos = Vec3.CreateVec3(b, 1.0, 2.0, 3.0, 3.0, 2, 5, 6)
    Monster.MonsterAddPos(b, pos)

    Monster.MonsterAddHp(b, 80)
    Monster.MonsterAddName(b, string)
    Monster.MonsterAddInventory(b, inv)
    Monster.MonsterAddTestType(b, 1)
    Monster.MonsterAddTest(b, mon2)
    Monster.MonsterAddTest4(b, test4)
    Monster.MonsterAddTestarrayofstring(b, testArrayOfString)
    mon = Monster.MonsterEnd(b)

    b.Finish(mon)

    return b.Bytes, b.Head()


def make_monster_from_generated_code_with_dump_order():
    ''' Use generated code to build the example Monster. '''

    b = flatbuffers.Builder(0)

    Monster.MonsterStart(b)
    fred = b.CreateString("Fred")
    Monster.MonsterAddName(b, fred)
    mon2 = Monster.MonsterEnd(b)

    Monster.MonsterStartInventoryVector(b, 5)
    b.PrependByte(4)
    b.PrependByte(3)
    b.PrependByte(2)
    b.PrependByte(1)
    b.PrependByte(0)
    inv = b.EndVector(5)

    Monster.MonsterStartTest4Vector(b, 2)
    Test.CreateTest(b, 10, 20)
    Test.CreateTest(b, 30, 40)
    test4 = b.EndVector(2)

    Monster.MonsterStartTestarrayofstringVector(b, 2)
    test2 = b.CreateString("test2")
    test1 = b.CreateString("test1")
    b.PrependUOffsetTRelative(test2)
    b.PrependUOffsetTRelative(test1)
    testArrayOfString = b.EndVector(2)

    Monster.MonsterStart(b)

    pos = Vec3.CreateVec3(b, 1.0, 2.0, 3.0, 3.0, 2, 5, 6)
    Monster.MonsterAddPos(b, pos)

    Monster.MonsterAddHp(b, 80)
    string = b.CreateString("MyMonster")
    Monster.MonsterAddName(b, string)
    Monster.MonsterAddInventory(b, inv)
    Monster.MonsterAddTestType(b, 1)
    Monster.MonsterAddTest(b, mon2)
    Monster.MonsterAddTest4(b, test4)
    Monster.MonsterAddTestarrayofstring(b, testArrayOfString)
    mon = Monster.MonsterEnd(b)

    b.Finish(mon)

    return b.Bytes, b.Head()


def dump_monster_from_generated_code():
    ''' Use generated code to build the example Monster. '''
    b = flatbuffers.Builder(0)

    test = Monster.Monster.CreateObject(b, {'name': "Fred"}, finished=False)
    d = {
        'pos': {'x': 1.0, 'y': 2.0, 'z': 3.0, 'test1': 3.0, 'test2': 2,
                'test3': {'a': 5, 'b': 6}},
        'hp': 80,
        'name': "MyMonster",
        'inventory': [4, 3, 2, 1, 0],
        'test_type': 1,
        'test': test,
        'test4': [{'a': 10, 'b': 20}, {'a': 30, 'b': 40}],
        'testarrayofstring': ["test2", "test1"]
    }
    Monster.Monster.CreateObject(b, d)

    return b.Bytes, b.Head()


class TestAllCodePathsOfExampleSchema(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        super(TestAllCodePathsOfExampleSchema, self).setUp(*args, **kwargs)

        b = flatbuffers.Builder(0)
        Monster.MonsterStart(b)
        gen_mon = Monster.MonsterEnd(b)
        b.Finish(gen_mon)

        self.mon = Monster.Monster.GetRoot(b.Bytes,
                                           b.Head())

    def test_default_monster_pos(self):
        self.assertTrue(self.mon.pos is None)

    def test_nondefault_monster_mana(self):
        b = flatbuffers.Builder(0)
        Monster.MonsterStart(b)
        Monster.MonsterAddMana(b, 50)
        mon = Monster.MonsterEnd(b)
        b.Finish(mon)

        got_mon = Monster.Monster.GetRoot(b.Bytes,
                                          b.Head())
        self.assertEqual(50, got_mon.mana)

    def test_nondefault_monster_mana_by_dump(self):
        b = flatbuffers.Builder(0)
        Monster.Monster.CreateObject(b, {'mana': 50})

        got_mon = Monster.Monster.GetRoot(b.Bytes,
                                          b.Head())
        self.assertEqual(50, got_mon.mana)

    def test_default_monster_hp(self):
        self.assertEqual(100, self.mon.hp)

    def test_default_monster_name(self):
        self.assertEqual('', self.mon.name)

    def test_default_monster_inventory_item(self):
        self.assertEqual((), self.mon.inventory)

    def test_default_monster_inventory_length(self):
        self.assertEqual(0, self.mon.inventory_length)

    def test_default_monster_color(self):
        self.assertEqual(Color.Color.Blue, self.mon.color)

    def test_nondefault_monster_color(self):
        b = flatbuffers.Builder(0)
        color = Color.Color.Red
        Monster.MonsterStart(b)
        Monster.MonsterAddColor(b, color)
        mon = Monster.MonsterEnd(b)
        b.Finish(mon)

        mon2 = Monster.Monster.GetRoot(b.Bytes,
                                       b.Head())
        self.assertEqual(Color.Color.Red, mon2.color)

    def test_nondefault_monster_color_by_dump(self):
        b = flatbuffers.Builder(0)
        Monster.Monster.CreateObject(b, {'color': Color.Color.Red})

        mon2 = Monster.Monster.GetRoot(b.Bytes,
                                       b.Head())
        self.assertEqual(Color.Color.Red, mon2.color)

    def test_default_monster_testtype(self):
        self.assertEqual(0, self.mon.test_type)

    def test_default_monster_test_field(self):
        self.assertEqual(None, self.mon.test)

    def test_default_monster_test4_item(self):
        self.assertEqual((), tuple(self.mon.test4))

    def test_default_monster_test4_length(self):
        self.assertEqual(0, self.mon.test4_length)

    def test_default_monster_testarrayofstring(self):
        self.assertEqual((), tuple(self.mon.testarrayofstring))

    def test_default_monster_testarrayofstring_length(self):
        self.assertEqual(0, self.mon.testarrayofstring_length)

    def test_default_monster_testarrayoftables(self):
        self.assertEqual((), tuple(self.mon.testarrayoftables))

    def test_nondefault_monster_testarrayoftables(self):
        b = flatbuffers.Builder(0)

        # make a child Monster within a vector of Monsters:
        Monster.MonsterStartTestarrayoftablesVector(b, 1)

        Monster.MonsterStart(b)
        Monster.MonsterAddHp(b, 99)
        sub_monster = Monster.MonsterEnd(b)
        b.Finish(sub_monster)

        tables = b.EndVector(1)

        # make the parent monster and include the vector of Monster:
        Monster.MonsterStart(b)
        Monster.MonsterAddTestarrayoftables(b, tables)
        mon = Monster.MonsterEnd(b)
        b.Finish(mon)

        # inspect the resulting data:
        mon2 = Monster.Monster.GetRoot(b.Bytes,
                                       b.Head())
        self.assertEqual(99, tuple(mon2.testarrayoftables)[0].hp)
        self.assertEqual(1, mon2.testarrayoftables_length)

    def test_nondefault_monster_testarrayoftables_by_dump(self):
        b = flatbuffers.Builder(0)
        d = {
            'testarrayoftables': [{'hp': 99}]
        }
        Monster.Monster.CreateObject(b, d)

        # inspect the resulting data:
        mon2 = Monster.Monster.GetRoot(b.Bytes,
                                       b.Head())
        self.assertEqual(99, tuple(mon2.testarrayoftables)[0].hp)
        self.assertEqual(1, mon2.testarrayoftables_length)

    def test_default_monster_testarrayoftables_length(self):
        self.assertEqual(0, self.mon.testarrayoftables_length)

    def test_nondefault_monster_enemy(self):
        b = flatbuffers.Builder(0)

        # make an Enemy object:
        Monster.MonsterStart(b)
        Monster.MonsterAddHp(b, 88)
        enemy = Monster.MonsterEnd(b)
        b.Finish(enemy)

        # make the parent monster and include the vector of Monster:
        Monster.MonsterStart(b)
        Monster.MonsterAddEnemy(b, enemy)
        mon = Monster.MonsterEnd(b)
        b.Finish(mon)

        # inspect the resulting data:
        mon2 = Monster.Monster.GetRoot(b.Bytes,
                                       b.Head())
        self.assertEqual(88, mon2.enemy.hp)

    def test_nondefault_monster_enemy_by_dump(self):
        b = flatbuffers.Builder(0)

        # make an Enemy object:
        d = {'enemy': {'hp': 88}}
        Monster.Monster.CreateObject(b, d)

        # inspect the resulting data:
        mon2 = Monster.Monster.GetRoot(b.Bytes,
                                       b.Head())
        self.assertEqual(88, mon2.enemy.hp)

    def test_default_monster_testnestedflatbuffer(self):
        self.assertEqual((), self.mon.testnestedflatbuffer)

    def test_default_monster_testnestedflatbuffer_length(self):
        self.assertEqual(0, self.mon.testnestedflatbuffer_length)

    def test_nondefault_monster_testnestedflatbuffer(self):
        b = flatbuffers.Builder(0)

        Monster.MonsterStartTestnestedflatbufferVector(b, 3)
        b.PrependByte(4)
        b.PrependByte(2)
        b.PrependByte(0)
        sub_buf = b.EndVector(3)

        # make the parent monster and include the vector of Monster:
        Monster.MonsterStart(b)
        Monster.MonsterAddTestnestedflatbuffer(b, sub_buf)
        mon = Monster.MonsterEnd(b)
        b.Finish(mon)

        # inspect the resulting data:
        mon2 = Monster.Monster.GetRoot(b.Bytes,
                                       b.Head())
        self.assertEqual(3, mon2.testnestedflatbuffer_length)
        self.assertEqual(0, tuple(mon2.testnestedflatbuffer)[0])
        self.assertEqual(2, tuple(mon2.testnestedflatbuffer)[1])
        self.assertEqual(4, tuple(mon2.testnestedflatbuffer)[2])

    def test_nondefault_monster_testnestedflatbuffer_by_dump(self):
        b = flatbuffers.Builder(0)
        d = {'testnestedflatbuffer': [4, 2, 0]}
        Monster.Monster.CreateObject(b, d)

        # inspect the resulting data:
        mon2 = Monster.Monster.GetRoot(b.Bytes,
                                       b.Head())
        self.assertEqual(3, mon2.testnestedflatbuffer_length)
        self.assertEqual(0, tuple(mon2.testnestedflatbuffer)[0])
        self.assertEqual(2, tuple(mon2.testnestedflatbuffer)[1])
        self.assertEqual(4, tuple(mon2.testnestedflatbuffer)[2])

    def test_nondefault_monster_testempty(self):
        b = flatbuffers.Builder(0)

        # make a Stat object:
        Stat.StatStart(b)
        Stat.StatAddVal(b, 123)
        my_stat = Stat.StatEnd(b)
        b.Finish(my_stat)

        # include the stat object in a monster:
        Monster.MonsterStart(b)
        Monster.MonsterAddTestempty(b, my_stat)
        mon = Monster.MonsterEnd(b)
        b.Finish(mon)

        # inspect the resulting data:
        mon2 = Monster.Monster.GetRoot(b.Bytes,
                                       b.Head())
        self.assertEqual(123, mon2.testempty.val)

    def test_nondefault_monster_testempty_by_dump(self):
        b = flatbuffers.Builder(0)
        d = {'testempty': {'val': 123}}
        Monster.Monster.CreateObject(b, d)

        # inspect the resulting data:
        mon2 = Monster.Monster.GetRoot(b.Bytes,
                                       b.Head())
        self.assertEqual(123, mon2.testempty.val)

    def test_default_monster_testbool(self):
        self.assertFalse(self.mon.testbool)

    def test_nondefault_monster_testbool(self):
        b = flatbuffers.Builder(0)
        Monster.MonsterStart(b)
        Monster.MonsterAddTestbool(b, True)
        mon = Monster.MonsterEnd(b)
        b.Finish(mon)

        # inspect the resulting data:
        mon2 = Monster.Monster.GetRoot(b.Bytes,
                                       b.Head())
        self.assertTrue(mon2.testbool)

    def test_nondefault_monster_testbool_by_dump(self):
        b = flatbuffers.Builder(0)
        d = {'testbool': True}
        Monster.Monster.CreateObject(b, d)

        # inspect the resulting data:
        mon2 = Monster.Monster.GetRoot(b.Bytes,
                                       b.Head())
        self.assertTrue(mon2.testbool)

    def test_default_monster_testhashes(self):
        self.assertEqual(0, self.mon.testhashs32_fnv1)
        self.assertEqual(0, self.mon.testhashu32_fnv1)
        self.assertEqual(0, self.mon.testhashs64_fnv1)
        self.assertEqual(0, self.mon.testhashu64_fnv1)
        self.assertEqual(0, self.mon.testhashs32_fnv1a)
        self.assertEqual(0, self.mon.testhashu32_fnv1a)
        self.assertEqual(0, self.mon.testhashs64_fnv1a)
        self.assertEqual(0, self.mon.testhashu64_fnv1a)

    def test_nondefault_monster_testhashes(self):
        b = flatbuffers.Builder(0)
        Monster.MonsterStart(b)
        Monster.MonsterAddTesthashs32Fnv1(b, 1)
        Monster.MonsterAddTesthashu32Fnv1(b, 2)
        Monster.MonsterAddTesthashs64Fnv1(b, 3)
        Monster.MonsterAddTesthashu64Fnv1(b, 4)
        Monster.MonsterAddTesthashs32Fnv1a(b, 5)
        Monster.MonsterAddTesthashu32Fnv1a(b, 6)
        Monster.MonsterAddTesthashs64Fnv1a(b, 7)
        Monster.MonsterAddTesthashu64Fnv1a(b, 8)
        mon = Monster.MonsterEnd(b)
        b.Finish(mon)

        # inspect the resulting data:
        mon2 = Monster.Monster.GetRoot(b.Bytes,
                                       b.Head())
        self.assertEqual(1, mon2.testhashs32_fnv1)
        self.assertEqual(2, mon2.testhashu32_fnv1)
        self.assertEqual(3, mon2.testhashs64_fnv1)
        self.assertEqual(4, mon2.testhashu64_fnv1)
        self.assertEqual(5, mon2.testhashs32_fnv1a)
        self.assertEqual(6, mon2.testhashu32_fnv1a)
        self.assertEqual(7, mon2.testhashs64_fnv1a)
        self.assertEqual(8, mon2.testhashu64_fnv1a)

    def test_nondefault_monster_testhashes_by_dump(self):
        b = flatbuffers.Builder(0)
        d = {
            'testhashs32_fnv1': 1,
            'testhashu32_fnv1': 2,
            'testhashs64_fnv1': 3,
            'testhashu64_fnv1': 4,
            'testhashs32_fnv1a': 5,
            'testhashu32_fnv1a': 6,
            'testhashs64_fnv1a': 7,
            'testhashu64_fnv1a': 8,
        }
        Monster.Monster.CreateObject(b, d)

        # inspect the resulting data:
        mon2 = Monster.Monster.GetRoot(b.Bytes,
                                       b.Head())
        self.assertEqual(1, mon2.testhashs32_fnv1)
        self.assertEqual(2, mon2.testhashu32_fnv1)
        self.assertEqual(3, mon2.testhashs64_fnv1)
        self.assertEqual(4, mon2.testhashu64_fnv1)
        self.assertEqual(5, mon2.testhashs32_fnv1a)
        self.assertEqual(6, mon2.testhashu32_fnv1a)
        self.assertEqual(7, mon2.testhashs64_fnv1a)
        self.assertEqual(8, mon2.testhashu64_fnv1a)

    def test_check_dump_data_against_build_data(self):
        dump_buf, dump_off = dump_monster_from_generated_code()
        build_buf, build_off = \
            make_monster_from_generated_code_with_dump_order()

        self.assertEqual(bytes(build_buf), bytes(dump_buf))
        self.assertEqual(build_off, dump_off)


class TestVtableDeduplication(unittest.TestCase):
    ''' TestVtableDeduplication verifies that vtables are deduplicated. '''

    def test_vtable_deduplication(self):
        b = flatbuffers.Builder(0)

        b.StartObject(4)
        b.PrependByteSlot(0, 0, 0)
        b.PrependByteSlot(1, 11, 0)
        b.PrependByteSlot(2, 22, 0)
        b.PrependInt16Slot(3, 33, 0)
        obj0 = b.EndObject()

        b.StartObject(4)
        b.PrependByteSlot(0, 0, 0)
        b.PrependByteSlot(1, 44, 0)
        b.PrependByteSlot(2, 55, 0)
        b.PrependInt16Slot(3, 66, 0)
        obj1 = b.EndObject()

        b.StartObject(4)
        b.PrependByteSlot(0, 0, 0)
        b.PrependByteSlot(1, 77, 0)
        b.PrependByteSlot(2, 88, 0)
        b.PrependInt16Slot(3, 99, 0)
        obj2 = b.EndObject()

        got = b.Output()

        want = bytearray([
            240, 255, 255, 255,  # == -12. offset to dedupped vtable.
            99, 0,
            88,
            77,
            248, 255, 255, 255,  # == -8. offset to dedupped vtable.
            66, 0,
            55,
            44,
            12, 0,
            8, 0,
            0, 0,
            7, 0,
            6, 0,
            4, 0,
            12, 0, 0, 0,
            33, 0,
            22,
            11,
        ])

        self.assertEqual((len(want), want), (len(got), got))

        table0 = flatbuffers.Table(b.Bytes, len(b.Bytes) - obj0)
        table1 = flatbuffers.Table(b.Bytes, len(b.Bytes) - obj1)
        table2 = flatbuffers.Table(b.Bytes, len(b.Bytes) - obj2)

        def _checkTable(tab, voffsett_value, b, c, d):
            # vtable size
            got = tab.GetVOffsetTSlot(0, 0)
            self.assertEqual(12, got, 'case 0, 0')

            # object size
            got = tab.GetVOffsetTSlot(2, 0)
            self.assertEqual(8, got, 'case 2, 0')

            # default value
            got = tab.GetVOffsetTSlot(4, 0)
            self.assertEqual(voffsett_value, got, 'case 4, 0')

            got = tab.GetSlot(6, 0, N.Uint8Flags)
            self.assertEqual(b, got, 'case 6, 0')

            val = tab.GetSlot(8, 0, N.Uint8Flags)
            self.assertEqual(c, val, 'failed 8, 0')

            got = tab.GetSlot(10, 0, N.Uint8Flags)
            self.assertEqual(d, got, 'failed 10, 0')

        _checkTable(table0, 0, 11, 22, 33)
        _checkTable(table1, 0, 44, 55, 66)
        _checkTable(table2, 0, 77, 88, 99)


class TestExceptions(unittest.TestCase):
    def test_not_in_object_error(self):
        b = flatbuffers.Builder(0)
        exc = None
        assertRaises(self, lambda: b.EndObject(),
                     flatbuffers.builder.NotInObjectError)

    def test_object_is_nested_error(self):
        b = flatbuffers.Builder(0)
        b.StartObject(0)
        assertRaises(self, lambda: b.StartObject(0),
                     flatbuffers.builder.ObjectIsNestedError)

    def test_struct_is_not_inline_error(self):
        b = flatbuffers.Builder(0)
        b.StartObject(0)
        assertRaises(self, lambda: b.PrependStructSlot(0, 1, 0),
                     flatbuffers.builder.StructIsNotInlineError)

    def test_unreachable_error(self):
        b = flatbuffers.Builder(0)
        assertRaises(self, lambda: b.PrependUOffsetTRelative(1),
                     flatbuffers.builder.OffsetArithmeticError)


def CheckAgainstGoldDataGo():
    try:
        gen_buf, gen_off = make_monster_from_generated_code()
        fn = 'monsterdata_go_wire.mon'
        if not os.path.exists(fn):
            print('Go-generated data does not exist, failed.')
            return False

        # would like to use a context manager here, but it's less
        # backwards-compatible:
        f = open(fn, 'rb')
        go_wire_data = f.read()
        f.close()

        CheckReadBuffer(bytearray(go_wire_data), 0)
        if not bytearray(gen_buf[gen_off:]) == bytearray(go_wire_data):
            raise AssertionError('CheckAgainstGoldDataGo failed')
    except:
        print('Failed to test against Go-generated test data.')
        return False

    print(
        'Can read Go-generated test data, and Python generates bytewise identical data.')
    return True


def CheckAgainstGoldDataJava():
    try:
        gen_buf, gen_off = make_monster_from_generated_code()
        fn = 'monsterdata_java_wire.mon'
        if not os.path.exists(fn):
            print('Java-generated data does not exist, failed.')
            return False
        f = open(fn, 'rb')
        java_wire_data = f.read()
        f.close()

        CheckReadBuffer(bytearray(java_wire_data), 0)
    except:
        print('Failed to read Java-generated test data.')
        return False

    print('Can read Java-generated test data.')
    return True


class LCG(object):
    ''' Include simple random number generator to ensure results will be the
        same cross platform.
        http://en.wikipedia.org/wiki/Park%E2%80%93Miller_random_number_generator '''

    __slots__ = ['n']

    InitialLCGSeed = 48271

    def __init__(self):
        self.n = self.InitialLCGSeed

    def Reset(self):
        self.n = self.InitialLCGSeed

    def Next(self):
        self.n = ((self.n * 279470273) % 4294967291) & 0xFFFFFFFF
        return self.n


def BenchmarkVtableDeduplication(count):
    '''
    BenchmarkVtableDeduplication measures the speed of vtable deduplication
    by creating `prePop` vtables, then populating `count` objects with a
    different single vtable.

    When count is large (as in long benchmarks), memory usage may be high.
    '''

    prePop = 10
    builder = flatbuffers.Builder(0)

    # pre-populate some vtables:
    for i in compat_range(prePop):
        builder.StartObject(i)
        for j in compat_range(i):
            builder.PrependInt16Slot(j, j, 0)
        builder.EndObject()

    # benchmark deduplication of a new vtable:
    def f():
        builder.StartObject(prePop)
        for j in compat_range(prePop):
            builder.PrependInt16Slot(j, j, 0)
        builder.EndObject()

    duration = timeit.timeit(stmt=f, number=count)
    rate = float(count) / duration
    print(('vtable deduplication rate: %.2f/sec' % rate))


def BenchmarkCheckReadBuffer(count, buf, off):
    '''
    BenchmarkCheckReadBuffer measures the speed of flatbuffer reading
    by re-using the CheckReadBuffer function with the gold data.
    '''

    def f():
        CheckReadBuffer(buf, off)

    duration = timeit.timeit(stmt=f, number=count)
    rate = float(count) / duration
    data = float(len(buf) * count) / float(1024 * 1024)
    data_rate = data / float(duration)

    print(('traversed %d %d-byte flatbuffers in %.2fsec: %.2f/sec, %.2fMB/sec')
          % (count, len(buf), duration, rate, data_rate))


def BenchmarkMakeMonsterFromGeneratedCode(count, length):
    '''
    BenchmarkMakeMonsterFromGeneratedCode measures the speed of flatbuffer
    creation by re-using the make_monster_from_generated_code function for
    generating gold data examples.
    '''

    duration = timeit.timeit(stmt=make_monster_from_generated_code,
                             number=count)
    rate = float(count) / duration
    data = float(length * count) / float(1024 * 1024)
    data_rate = data / float(duration)

    print(('built %d %d-byte flatbuffers in %.2fsec: %.2f/sec, %.2fMB/sec' % \
           (count, length, duration, rate, data_rate)))


def backward_compatible_run_tests(**kwargs):
    if PY_VERSION < (2, 6):
        sys.stderr.write("Python version less than 2.6 are not supported")
        sys.stderr.flush()
        return False

    # python2.6 has a reduced-functionality unittest.main function:
    if PY_VERSION == (2, 6):
        try:
            unittest.main(**kwargs)
        except SystemExit as e:
            if not e.code == 0:
                return False
        return True

    # python2.7 and above let us not exit once unittest.main is run: 
    kwargs['exit'] = False
    kwargs['verbosity'] = 0
    ret = unittest.main(**kwargs)
    if ret.result.errors or ret.result.failures:
        return False

    return True


def main():
    import os
    import sys

    if not len(sys.argv) == 4:
        sys.stderr.write('Usage: %s <benchmark vtable count>'
                         '<benchmark read count> <benchmark build count>\n'
                         % sys.argv[0])
        sys.stderr.write('       Provide COMPARE_GENERATED_TO_GO=1   to check'
                         'for bytewise comparison to Go data.\n')
        sys.stderr.write('       Provide COMPARE_GENERATED_TO_JAVA=1 to check'
                         'for bytewise comparison to Java data.\n')
        sys.stderr.flush()
        sys.exit(1)

    kwargs = dict(argv=sys.argv[:-3])

    # run tests, and run some language comparison checks if needed:
    success = backward_compatible_run_tests(**kwargs)
    if success and os.environ.get('COMPARE_GENERATED_TO_GO', 0) == "1":
        success = success and CheckAgainstGoldDataGo()
    if success and os.environ.get('COMPARE_GENERATED_TO_JAVA', 0) == "1":
        success = success and CheckAgainstGoldDataJava()

    if not success:
        sys.stderr.write('Tests failed, skipping benchmarks.\n')
        sys.stderr.flush()
        sys.exit(1)

    # run benchmarks (if 0, they will be a noop):
    bench_vtable = int(sys.argv[1])
    bench_traverse = int(sys.argv[2])
    bench_build = int(sys.argv[3])
    if bench_vtable:
        BenchmarkVtableDeduplication(bench_vtable)
    if bench_traverse:
        buf, off = make_monster_from_generated_code()
        BenchmarkCheckReadBuffer(bench_traverse, buf, off)
    if bench_build:
        buf, off = make_monster_from_generated_code()
        BenchmarkMakeMonsterFromGeneratedCode(bench_build, len(buf))


if __name__ == '__main__':
    main()
