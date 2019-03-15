// Code generated by the FlatBuffers compiler. DO NOT EDIT.

package Example

import (
	flatbuffers "github.com/google/flatbuffers/go"
)

type TestSimpleTableWithEnum struct {
	_tab flatbuffers.Table
}

func GetRootAsTestSimpleTableWithEnum(buf []byte, offset flatbuffers.UOffsetT) *TestSimpleTableWithEnum {
	n := flatbuffers.GetUOffsetT(buf[offset:])
	x := &TestSimpleTableWithEnum{}
	x.Init(buf, n+offset)
	return x
}

func (rcv *TestSimpleTableWithEnum) Init(buf []byte, i flatbuffers.UOffsetT) {
	rcv._tab.Init(buf, i)
}

func (rcv *TestSimpleTableWithEnum) Table() flatbuffers.Table {
	return rcv._tab
}

func (rcv *TestSimpleTableWithEnum) Color() Color {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(4))
	if o != 0 {
		return rcv._tab.GetByte(o + rcv._tab.Pos())
	}
	return 2
}

func (rcv *TestSimpleTableWithEnum) MutateColor(n Color) bool {
	return rcv._tab.MutateByteSlot(4, n)
}

func TestSimpleTableWithEnumStart(builder *flatbuffers.Builder) {
	builder.StartObject(1)
}
func TestSimpleTableWithEnumAddColor(builder *flatbuffers.Builder, color byte) {
	builder.PrependByteSlot(0, color, 2)
}
func TestSimpleTableWithEnumEnd(builder *flatbuffers.Builder) flatbuffers.UOffsetT {
	return builder.EndObject()
}
