// Code generated by the FlatBuffers compiler. DO NOT EDIT.

package 

import (
	flatbuffers "github.com/google/flatbuffers/go"

	MyGame__OtherNameSpace "MyGame/OtherNameSpace"
)

type TableA struct {
	_tab flatbuffers.Table
}

func GetRootAsTableA(buf []byte, offset flatbuffers.UOffsetT) *TableA {
	n := flatbuffers.GetUOffsetT(buf[offset:])
	x := &TableA{}
	x.Init(buf, n+offset)
	return x
}

func (rcv *TableA) Init(buf []byte, i flatbuffers.UOffsetT) {
	rcv._tab.Bytes = buf
	rcv._tab.Pos = i
}

func (rcv *TableA) Table() flatbuffers.Table {
	return rcv._tab
}

func (rcv *TableA) B(obj *MyGame__OtherNameSpace.TableB) *MyGame__OtherNameSpace.TableB {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(4))
	if o != 0 {
		x := rcv._tab.Indirect(o + rcv._tab.Pos)
		if obj == nil {
			obj = new(MyGame__OtherNameSpace.TableB)
		}
		obj.Init(rcv._tab.Bytes, x)
		return obj
	}
	return nil
}

func TableAStart(builder *flatbuffers.Builder) {
	builder.StartObject(1)
}
func TableAAddB(builder *flatbuffers.Builder, b flatbuffers.UOffsetT) {
	builder.PrependUOffsetTSlot(0, flatbuffers.UOffsetT(b), 0)
}
func TableAEnd(builder *flatbuffers.Builder) flatbuffers.UOffsetT {
	return builder.EndObject()
}
