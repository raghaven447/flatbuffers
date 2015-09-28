# automatically generated, do not modify

# namespace: Example

import flatbuffers

# /// an example documentation comment: monster object
class Monster(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMonster(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Monster()
        x.Init(buf, n + offset)
        return x


    # Monster
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Monster
    def Pos(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from .Vec3 import Vec3
            obj = Vec3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Monster
    def Mana(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 150

    # Monster
    def Hp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 100

    # Monster
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # Monster
    def Inventory(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Monster
    def InventoryLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Monster
    def Color(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 8

    # Monster
    def TestType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Monster
    def Test(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # Monster
    def Test4(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            from .Test import Test
            obj = Test()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Monster
    def Test4Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Monster
    def Testarrayofstring(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # Monster
    def TestarrayofstringLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

# /// an example documentation comment: this will end up in the generated code
# /// multiline too
    # Monster
    def Testarrayoftables(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Monster import Monster
            obj = Monster()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Monster
    def TestarrayoftablesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Monster
    def Enemy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Monster import Monster
            obj = Monster()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Monster
    def Testnestedflatbuffer(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Monster
    def TestnestedflatbufferLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Monster
    def Testempty(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Stat import Stat
            obj = Stat()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Monster
    def Testbool(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

    # Monster
    def Testhashs32Fnv1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Monster
    def Testhashu32Fnv1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # Monster
    def Testhashs64Fnv1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # Monster
    def Testhashu64Fnv1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Monster
    def Testhashs32Fnv1a(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Monster
    def Testhashu32Fnv1a(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # Monster
    def Testhashs64Fnv1a(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # Monster
    def Testhashu64Fnv1a(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Monster
    def Testarrayofbools(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.BoolFlags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Monster
    def TestarrayofboolsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def MonsterStart(builder): builder.StartObject(25)
def MonsterAddPos(builder, pos): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(pos), 0)
def MonsterAddMana(builder, mana): builder.PrependInt16Slot(1, mana, 150)
def MonsterAddHp(builder, hp): builder.PrependInt16Slot(2, hp, 100)
def MonsterAddName(builder, name): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def MonsterAddInventory(builder, inventory): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(inventory), 0)
def MonsterStartInventoryVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def MonsterAddColor(builder, color): builder.PrependInt8Slot(6, color, 8)
def MonsterAddTestType(builder, testType): builder.PrependUint8Slot(7, testType, 0)
def MonsterAddTest(builder, test): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(test), 0)
def MonsterAddTest4(builder, test4): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(test4), 0)
def MonsterStartTest4Vector(builder, numElems): return builder.StartVector(4, numElems, 2)
def MonsterAddTestarrayofstring(builder, testarrayofstring): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(testarrayofstring), 0)
def MonsterStartTestarrayofstringVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MonsterAddTestarrayoftables(builder, testarrayoftables): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(testarrayoftables), 0)
def MonsterStartTestarrayoftablesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MonsterAddEnemy(builder, enemy): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(enemy), 0)
def MonsterAddTestnestedflatbuffer(builder, testnestedflatbuffer): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(testnestedflatbuffer), 0)
def MonsterStartTestnestedflatbufferVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def MonsterAddTestempty(builder, testempty): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(testempty), 0)
def MonsterAddTestbool(builder, testbool): builder.PrependBoolSlot(15, testbool, 0)
def MonsterAddTesthashs32Fnv1(builder, testhashs32Fnv1): builder.PrependInt32Slot(16, testhashs32Fnv1, 0)
def MonsterAddTesthashu32Fnv1(builder, testhashu32Fnv1): builder.PrependUint32Slot(17, testhashu32Fnv1, 0)
def MonsterAddTesthashs64Fnv1(builder, testhashs64Fnv1): builder.PrependInt64Slot(18, testhashs64Fnv1, 0)
def MonsterAddTesthashu64Fnv1(builder, testhashu64Fnv1): builder.PrependUint64Slot(19, testhashu64Fnv1, 0)
def MonsterAddTesthashs32Fnv1a(builder, testhashs32Fnv1a): builder.PrependInt32Slot(20, testhashs32Fnv1a, 0)
def MonsterAddTesthashu32Fnv1a(builder, testhashu32Fnv1a): builder.PrependUint32Slot(21, testhashu32Fnv1a, 0)
def MonsterAddTesthashs64Fnv1a(builder, testhashs64Fnv1a): builder.PrependInt64Slot(22, testhashs64Fnv1a, 0)
def MonsterAddTesthashu64Fnv1a(builder, testhashu64Fnv1a): builder.PrependUint64Slot(23, testhashu64Fnv1a, 0)
def MonsterAddTestarrayofbools(builder, testarrayofbools): builder.PrependUOffsetTRelativeSlot(24, flatbuffers.number_types.UOffsetTFlags.py_type(testarrayofbools), 0)
def MonsterStartTestarrayofboolsVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def MonsterEnd(builder): return builder.EndObject()
