# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Example

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TypeAliases(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        buf = flatbuffers.compat.memoryview_type(buf) if not isinstance(buf, flatbuffers.compat.memoryview_type) else buf
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TypeAliases()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTypeAliases(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def TypeAliasesBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x4D\x4F\x4E\x53", size_prefixed=size_prefixed)

    # TypeAliases
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TypeAliases
    def I8(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # TypeAliases
    def U8(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # TypeAliases
    def I16(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

    # TypeAliases
    def U16(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # TypeAliases
    def I32(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TypeAliases
    def U32(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # TypeAliases
    def I64(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TypeAliases
    def U64(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # TypeAliases
    def F32(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # TypeAliases
    def F64(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

    # TypeAliases
    def V8(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # TypeAliases
    def V8AsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int8Flags, o)
        return 0

    # TypeAliases
    def V8Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TypeAliases
    def V8IsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        return o == 0

    # TypeAliases
    def Vf64(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # TypeAliases
    def Vf64AsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float64Flags, o)
        return 0

    # TypeAliases
    def Vf64Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TypeAliases
    def Vf64IsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        return o == 0

def Start(builder): builder.StartObject(12)
def TypeAliasesStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddI8(builder, i8): builder.PrependInt8Slot(0, i8, 0)
def TypeAliasesAddI8(builder, i8):
    """This method is deprecated. Please switch to AddI8."""
    return AddI8(builder, i8)
def AddU8(builder, u8): builder.PrependUint8Slot(1, u8, 0)
def TypeAliasesAddU8(builder, u8):
    """This method is deprecated. Please switch to AddU8."""
    return AddU8(builder, u8)
def AddI16(builder, i16): builder.PrependInt16Slot(2, i16, 0)
def TypeAliasesAddI16(builder, i16):
    """This method is deprecated. Please switch to AddI16."""
    return AddI16(builder, i16)
def AddU16(builder, u16): builder.PrependUint16Slot(3, u16, 0)
def TypeAliasesAddU16(builder, u16):
    """This method is deprecated. Please switch to AddU16."""
    return AddU16(builder, u16)
def AddI32(builder, i32): builder.PrependInt32Slot(4, i32, 0)
def TypeAliasesAddI32(builder, i32):
    """This method is deprecated. Please switch to AddI32."""
    return AddI32(builder, i32)
def AddU32(builder, u32): builder.PrependUint32Slot(5, u32, 0)
def TypeAliasesAddU32(builder, u32):
    """This method is deprecated. Please switch to AddU32."""
    return AddU32(builder, u32)
def AddI64(builder, i64): builder.PrependInt64Slot(6, i64, 0)
def TypeAliasesAddI64(builder, i64):
    """This method is deprecated. Please switch to AddI64."""
    return AddI64(builder, i64)
def AddU64(builder, u64): builder.PrependUint64Slot(7, u64, 0)
def TypeAliasesAddU64(builder, u64):
    """This method is deprecated. Please switch to AddU64."""
    return AddU64(builder, u64)
def AddF32(builder, f32): builder.PrependFloat32Slot(8, f32, 0.0)
def TypeAliasesAddF32(builder, f32):
    """This method is deprecated. Please switch to AddF32."""
    return AddF32(builder, f32)
def AddF64(builder, f64): builder.PrependFloat64Slot(9, f64, 0.0)
def TypeAliasesAddF64(builder, f64):
    """This method is deprecated. Please switch to AddF64."""
    return AddF64(builder, f64)
def AddV8(builder, v8): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(v8), 0)
def TypeAliasesAddV8(builder, v8):
    """This method is deprecated. Please switch to AddV8."""
    return AddV8(builder, v8)
def StartV8Vector(builder, numElems): return builder.StartVector(1, numElems, 1)
def TypeAliasesStartV8Vector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartV8Vector(builder, numElems)
def AddVf64(builder, vf64): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(vf64), 0)
def TypeAliasesAddVf64(builder, vf64):
    """This method is deprecated. Please switch to AddVf64."""
    return AddVf64(builder, vf64)
def StartVf64Vector(builder, numElems): return builder.StartVector(8, numElems, 8)
def TypeAliasesStartVf64Vector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartVf64Vector(builder, numElems)
def End(builder): return builder.EndObject()
def TypeAliasesEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)
try:
    from typing import List
except:
    pass

class TypeAliasesT(object):

    # TypeAliasesT
    def __init__(self):
        self.i8 = 0  # type: int
        self.u8 = 0  # type: int
        self.i16 = 0  # type: int
        self.u16 = 0  # type: int
        self.i32 = 0  # type: int
        self.u32 = 0  # type: int
        self.i64 = 0  # type: int
        self.u64 = 0  # type: int
        self.f32 = 0.0  # type: float
        self.f64 = 0.0  # type: float
        self.v8 = None  # type: List[int]
        self.vf64 = None  # type: List[float]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        typeAliases = TypeAliases()
        typeAliases.Init(buf, pos)
        return cls.InitFromObj(typeAliases)

    @classmethod
    def InitFromObj(cls, typeAliases):
        x = TypeAliasesT()
        x._UnPack(typeAliases)
        return x

    # TypeAliasesT
    def _UnPack(self, typeAliases):
        if typeAliases is None:
            return
        self.i8 = typeAliases.I8()
        self.u8 = typeAliases.U8()
        self.i16 = typeAliases.I16()
        self.u16 = typeAliases.U16()
        self.i32 = typeAliases.I32()
        self.u32 = typeAliases.U32()
        self.i64 = typeAliases.I64()
        self.u64 = typeAliases.U64()
        self.f32 = typeAliases.F32()
        self.f64 = typeAliases.F64()
        if not typeAliases.V8IsNone():
            if np is None:
                self.v8 = []
                for i in range(typeAliases.V8Length()):
                    self.v8.append(typeAliases.V8(i))
            else:
                self.v8 = typeAliases.V8AsNumpy()
        if not typeAliases.Vf64IsNone():
            if np is None:
                self.vf64 = []
                for i in range(typeAliases.Vf64Length()):
                    self.vf64.append(typeAliases.Vf64(i))
            else:
                self.vf64 = typeAliases.Vf64AsNumpy()

    # TypeAliasesT
    def Pack(self, builder):
        if self.v8 is not None:
            if np is not None and type(self.v8) is np.ndarray:
                v8 = builder.CreateNumpyVector(self.v8)
            else:
                StartV8Vector(builder, len(self.v8))
                for i in reversed(range(len(self.v8))):
                    builder.PrependByte(self.v8[i])
                v8 = builder.EndVector()
        if self.vf64 is not None:
            if np is not None and type(self.vf64) is np.ndarray:
                vf64 = builder.CreateNumpyVector(self.vf64)
            else:
                StartVf64Vector(builder, len(self.vf64))
                for i in reversed(range(len(self.vf64))):
                    builder.PrependFloat64(self.vf64[i])
                vf64 = builder.EndVector()
        Start(builder)
        AddI8(builder, self.i8)
        AddU8(builder, self.u8)
        AddI16(builder, self.i16)
        AddU16(builder, self.u16)
        AddI32(builder, self.i32)
        AddU32(builder, self.u32)
        AddI64(builder, self.i64)
        AddU64(builder, self.u64)
        AddF32(builder, self.f32)
        AddF64(builder, self.f64)
        if self.v8 is not None:
            AddV8(builder, v8)
        if self.vf64 is not None:
            AddVf64(builder, vf64)
        typeAliases = End(builder)
        return typeAliases
