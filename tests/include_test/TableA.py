# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TableA(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsTableA(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TableA()
        x.Init(buf, n + offset)
        return x

    # TableA
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TableA
    def B(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from MyGame.OtherNameSpace.TableB import TableB
            obj = TableB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def TableAStart(builder): builder.StartObject(1)
def TableAAddB(builder, b): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(b), 0)
def TableAEnd(builder): return builder.EndObject()
