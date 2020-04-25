// Code generated by the FlatBuffers compiler. DO NOT EDIT.

package Example

import (
	flatbuffers "github.com/google/flatbuffers/go"
)

type Vec3T struct {
	X float32
	Y float32
	Z float32
	Test1 float64
	Test2 Color
	Test3 *TestT
}

func (t *Vec3T) Pack(builder *flatbuffers.Builder) flatbuffers.UOffsetT {
	if t == nil {
		return 0
	}
	return CreateVec3(builder, t.X, t.Y, t.Z, t.Test1, t.Test2, t.Test3.A, t.Test3.B)
}
func (rcv *Vec3) UnPackTo(t *Vec3T) {
	t.X = rcv.X()
	t.Y = rcv.Y()
	t.Z = rcv.Z()
	t.Test1 = rcv.Test1()
	t.Test2 = rcv.Test2()
	t.Test3 = rcv.Test3(nil).UnPack()
}

func (rcv *Vec3) UnPack() *Vec3T {
	if rcv == nil {
		return nil
	}
	t := &Vec3T{}
	rcv.UnPackTo(t)
	return t
}

type Vec3 struct {
	_tab flatbuffers.Struct
}

// GetStructVectorAsVec3 shortcut to access struct in vector of unions
func GetStructVectorAsVec3(table *flatbuffers.Table) *Vec3 {
	n := flatbuffers.GetUOffsetT(table.Bytes[table.Pos:])
	x := &Vec3{}
	x.Init(table.Bytes, n+table.Pos)
	return x
}

// GetStructAsVec3 shortcut to access struct in single union field
func GetStructAsVec3(table *flatbuffers.Table) *Vec3 {
	x := &Vec3{}
	x.Init(table.Bytes, table.Pos)
	return x
}

func (rcv *Vec3) Init(buf []byte, i flatbuffers.UOffsetT) {
	rcv._tab.Bytes = buf
	rcv._tab.Pos = i
}

func (rcv *Vec3) Table() flatbuffers.Table {
	return rcv._tab.Table
}

func (rcv *Vec3) X() float32 {
	return rcv._tab.GetFloat32(rcv._tab.Pos + flatbuffers.UOffsetT(0))
}
func (rcv *Vec3) MutateX(n float32) bool {
	return rcv._tab.MutateFloat32(rcv._tab.Pos + flatbuffers.UOffsetT(0), n)
}

func (rcv *Vec3) Y() float32 {
	return rcv._tab.GetFloat32(rcv._tab.Pos + flatbuffers.UOffsetT(4))
}
func (rcv *Vec3) MutateY(n float32) bool {
	return rcv._tab.MutateFloat32(rcv._tab.Pos + flatbuffers.UOffsetT(4), n)
}

func (rcv *Vec3) Z() float32 {
	return rcv._tab.GetFloat32(rcv._tab.Pos + flatbuffers.UOffsetT(8))
}
func (rcv *Vec3) MutateZ(n float32) bool {
	return rcv._tab.MutateFloat32(rcv._tab.Pos + flatbuffers.UOffsetT(8), n)
}

func (rcv *Vec3) Test1() float64 {
	return rcv._tab.GetFloat64(rcv._tab.Pos + flatbuffers.UOffsetT(16))
}
func (rcv *Vec3) MutateTest1(n float64) bool {
	return rcv._tab.MutateFloat64(rcv._tab.Pos + flatbuffers.UOffsetT(16), n)
}

func (rcv *Vec3) Test2() Color {
	return Color(rcv._tab.GetByte(rcv._tab.Pos + flatbuffers.UOffsetT(24)))
}
func (rcv *Vec3) MutateTest2(n Color) bool {
	return rcv._tab.MutateByte(rcv._tab.Pos + flatbuffers.UOffsetT(24), byte(n))
}

func (rcv *Vec3) Test3(obj *Test) *Test {
	if obj == nil {
		obj = new(Test)
	}
	obj.Init(rcv._tab.Bytes, rcv._tab.Pos+26)
	return obj
}

func CreateVec3(builder *flatbuffers.Builder, x float32, y float32, z float32, test1 float64, test2 Color, test3_a int16, test3_b int8) flatbuffers.UOffsetT {
	builder.Prep(8, 32)
	builder.Pad(2)
	builder.Prep(2, 4)
	builder.Pad(1)
	builder.PrependInt8(test3_b)
	builder.PrependInt16(test3_a)
	builder.Pad(1)
	builder.PrependByte(byte(test2))
	builder.PrependFloat64(test1)
	builder.Pad(4)
	builder.PrependFloat32(z)
	builder.PrependFloat32(y)
	builder.PrependFloat32(x)
	return builder.Offset()
}
