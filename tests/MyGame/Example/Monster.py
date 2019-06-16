# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Example

import flatbuffers

# an example documentation comment: monster object
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
            from MyGame.Example.Vec3 import Vec3
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
        return None

    # Monster
    def Inventory(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Monster
    def InventoryAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
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
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
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

    # an example documentation comment: this will end up in the generated code
    # multiline too
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
            from MyGame.Example.Monster import Monster
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
    def TestnestedflatbufferAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
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
            from MyGame.Example.Stat import Stat
            obj = Stat()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Monster
    def Testbool(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

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
    def TestarrayofboolsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.BoolFlags, o)
        return 0

    # Monster
    def TestarrayofboolsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Monster
    def Testf(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 3.14159

    # Monster
    def Testf2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 3.0

    # Monster
    def Testf3(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Monster
    def Testarrayofstring2(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # Monster
    def Testarrayofstring2Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Monster
    def Testarrayofsortedstruct(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 8
            from .Ability import Ability
            obj = Ability()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Monster
    def TestarrayofsortedstructLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Monster
    def Flex(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Monster
    def FlexAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Monster
    def FlexLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Monster
    def Test5(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            from .Test import Test
            obj = Test()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Monster
    def Test5Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Monster
    def VectorOfLongs(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # Monster
    def VectorOfLongsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # Monster
    def VectorOfLongsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Monster
    def VectorOfDoubles(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # Monster
    def VectorOfDoublesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float64Flags, o)
        return 0

    # Monster
    def VectorOfDoublesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Monster
    def ParentNamespaceTest(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from MyGame.InParentNamespace import InParentNamespace
            obj = InParentNamespace()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Monster
    def VectorOfReferrables(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Referrable import Referrable
            obj = Referrable()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Monster
    def VectorOfReferrablesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Monster
    def SingleWeakReference(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Monster
    def VectorOfWeakReferences(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # Monster
    def VectorOfWeakReferencesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint64Flags, o)
        return 0

    # Monster
    def VectorOfWeakReferencesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Monster
    def VectorOfStrongReferrables(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(80))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Referrable import Referrable
            obj = Referrable()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Monster
    def VectorOfStrongReferrablesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(80))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Monster
    def CoOwningReference(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(82))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Monster
    def VectorOfCoOwningReferences(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(84))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # Monster
    def VectorOfCoOwningReferencesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(84))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint64Flags, o)
        return 0

    # Monster
    def VectorOfCoOwningReferencesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(84))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Monster
    def NonOwningReference(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(86))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Monster
    def VectorOfNonOwningReferences(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(88))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # Monster
    def VectorOfNonOwningReferencesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(88))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint64Flags, o)
        return 0

    # Monster
    def VectorOfNonOwningReferencesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(88))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Monster
    def AnyUniqueType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(90))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Monster
    def AnyUnique(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(92))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # Monster
    def AnyAmbiguousType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(94))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Monster
    def AnyAmbiguous(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(96))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # Monster
    def VectorOfEnums(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(98))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Monster
    def VectorOfEnumsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(98))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Monster
    def VectorOfEnumsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(98))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def MonsterStart(builder): builder.StartObject(48)
def MonsterAddPos(builder, pos): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(pos), 0)
def MonsterAddMana(builder, mana): builder.PrependInt16Slot(1, mana, 150)
def MonsterAddHp(builder, hp): builder.PrependInt16Slot(2, hp, 100)
def MonsterAddName(builder, name): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def MonsterAddInventory(builder, inventory): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(inventory), 0)
def MonsterStartInventoryVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def MonsterAddColor(builder, color): builder.PrependUint8Slot(6, color, 8)
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
def MonsterAddTestf(builder, testf): builder.PrependFloat32Slot(25, testf, 3.14159)
def MonsterAddTestf2(builder, testf2): builder.PrependFloat32Slot(26, testf2, 3.0)
def MonsterAddTestf3(builder, testf3): builder.PrependFloat32Slot(27, testf3, 0.0)
def MonsterAddTestarrayofstring2(builder, testarrayofstring2): builder.PrependUOffsetTRelativeSlot(28, flatbuffers.number_types.UOffsetTFlags.py_type(testarrayofstring2), 0)
def MonsterStartTestarrayofstring2Vector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MonsterAddTestarrayofsortedstruct(builder, testarrayofsortedstruct): builder.PrependUOffsetTRelativeSlot(29, flatbuffers.number_types.UOffsetTFlags.py_type(testarrayofsortedstruct), 0)
def MonsterStartTestarrayofsortedstructVector(builder, numElems): return builder.StartVector(8, numElems, 4)
def MonsterAddFlex(builder, flex): builder.PrependUOffsetTRelativeSlot(30, flatbuffers.number_types.UOffsetTFlags.py_type(flex), 0)
def MonsterStartFlexVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def MonsterAddTest5(builder, test5): builder.PrependUOffsetTRelativeSlot(31, flatbuffers.number_types.UOffsetTFlags.py_type(test5), 0)
def MonsterStartTest5Vector(builder, numElems): return builder.StartVector(4, numElems, 2)
def MonsterAddVectorOfLongs(builder, vectorOfLongs): builder.PrependUOffsetTRelativeSlot(32, flatbuffers.number_types.UOffsetTFlags.py_type(vectorOfLongs), 0)
def MonsterStartVectorOfLongsVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def MonsterAddVectorOfDoubles(builder, vectorOfDoubles): builder.PrependUOffsetTRelativeSlot(33, flatbuffers.number_types.UOffsetTFlags.py_type(vectorOfDoubles), 0)
def MonsterStartVectorOfDoublesVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def MonsterAddParentNamespaceTest(builder, parentNamespaceTest): builder.PrependUOffsetTRelativeSlot(34, flatbuffers.number_types.UOffsetTFlags.py_type(parentNamespaceTest), 0)
def MonsterAddVectorOfReferrables(builder, vectorOfReferrables): builder.PrependUOffsetTRelativeSlot(35, flatbuffers.number_types.UOffsetTFlags.py_type(vectorOfReferrables), 0)
def MonsterStartVectorOfReferrablesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MonsterAddSingleWeakReference(builder, singleWeakReference): builder.PrependUint64Slot(36, singleWeakReference, 0)
def MonsterAddVectorOfWeakReferences(builder, vectorOfWeakReferences): builder.PrependUOffsetTRelativeSlot(37, flatbuffers.number_types.UOffsetTFlags.py_type(vectorOfWeakReferences), 0)
def MonsterStartVectorOfWeakReferencesVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def MonsterAddVectorOfStrongReferrables(builder, vectorOfStrongReferrables): builder.PrependUOffsetTRelativeSlot(38, flatbuffers.number_types.UOffsetTFlags.py_type(vectorOfStrongReferrables), 0)
def MonsterStartVectorOfStrongReferrablesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MonsterAddCoOwningReference(builder, coOwningReference): builder.PrependUint64Slot(39, coOwningReference, 0)
def MonsterAddVectorOfCoOwningReferences(builder, vectorOfCoOwningReferences): builder.PrependUOffsetTRelativeSlot(40, flatbuffers.number_types.UOffsetTFlags.py_type(vectorOfCoOwningReferences), 0)
def MonsterStartVectorOfCoOwningReferencesVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def MonsterAddNonOwningReference(builder, nonOwningReference): builder.PrependUint64Slot(41, nonOwningReference, 0)
def MonsterAddVectorOfNonOwningReferences(builder, vectorOfNonOwningReferences): builder.PrependUOffsetTRelativeSlot(42, flatbuffers.number_types.UOffsetTFlags.py_type(vectorOfNonOwningReferences), 0)
def MonsterStartVectorOfNonOwningReferencesVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def MonsterAddAnyUniqueType(builder, anyUniqueType): builder.PrependUint8Slot(43, anyUniqueType, 0)
def MonsterAddAnyUnique(builder, anyUnique): builder.PrependUOffsetTRelativeSlot(44, flatbuffers.number_types.UOffsetTFlags.py_type(anyUnique), 0)
def MonsterAddAnyAmbiguousType(builder, anyAmbiguousType): builder.PrependUint8Slot(45, anyAmbiguousType, 0)
def MonsterAddAnyAmbiguous(builder, anyAmbiguous): builder.PrependUOffsetTRelativeSlot(46, flatbuffers.number_types.UOffsetTFlags.py_type(anyAmbiguous), 0)
def MonsterAddVectorOfEnums(builder, vectorOfEnums): builder.PrependUOffsetTRelativeSlot(47, flatbuffers.number_types.UOffsetTFlags.py_type(vectorOfEnums), 0)
def MonsterStartVectorOfEnumsVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def MonsterEnd(builder): return builder.EndObject()
