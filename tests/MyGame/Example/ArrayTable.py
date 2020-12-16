# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Example

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ArrayTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ArrayTable()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsArrayTable(cls, buf, offset=0):
        """This method is deprecated. Please switch to Start."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def ArrayTableBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x41\x52\x52\x54", size_prefixed=size_prefixed)

    # ArrayTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ArrayTable
    def A(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from MyGame.Example.ArrayStruct import ArrayStruct
            obj = ArrayStruct()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def Start(builder): builder.StartObject(1)
def ArrayTableStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddA(builder, a): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(a), 0)
def ArrayTableAddA(builder, a):
    """This method is deprecated. Please switch to Start."""
    return AddA(builder, a)
def End(builder): return builder.EndObject()
def ArrayTableEnd(builder):
    """This method is deprecated. Please switch to Start."""
    return End(builder)
import MyGame.Example.ArrayStruct
try:
    from typing import Optional
except:
    pass

class ArrayTableT(object):

    # ArrayTableT
    def __init__(self):
        self.a = None  # type: Optional[MyGame.Example.ArrayStruct.ArrayStructT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        arrayTable = ArrayTable()
        arrayTable.Init(buf, pos)
        return cls.InitFromObj(arrayTable)

    @classmethod
    def InitFromObj(cls, arrayTable):
        x = ArrayTableT()
        x._UnPack(arrayTable)
        return x

    # ArrayTableT
    def _UnPack(self, arrayTable):
        if arrayTable is None:
            return
        if arrayTable.A() is not None:
            self.a = MyGame.Example.ArrayStruct.ArrayStructT.InitFromObj(arrayTable.A())

    # ArrayTableT
    def Pack(self, builder):
        Start(builder)
        if self.a is not None:
            a = self.a.Pack(builder)
            AddA(builder, a)
        arrayTable = End(builder)
        return arrayTable
