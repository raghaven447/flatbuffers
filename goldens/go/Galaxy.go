// Code generated by the FlatBuffers compiler. DO NOT EDIT.

package Galaxy

import (
	flatbuffers "github.com/google/flatbuffers/go"
)

type Galaxy struct {
	_tab flatbuffers.Table
}

func GetRootAsGalaxy(buf []byte, offset flatbuffers.UOffsetT) *Galaxy {
	n := flatbuffers.GetUOffsetT(buf[offset:])
	x := &Galaxy{}
	x.Init(buf, n+offset)
	return x
}

func FinishGalaxyBuffer(builder *flatbuffers.Builder, offset flatbuffers.UOffsetT) {
	builder.Finish(offset)
}

func GetSizePrefixedRootAsGalaxy(buf []byte, offset flatbuffers.UOffsetT) *Galaxy {
	n := flatbuffers.GetUOffsetT(buf[offset+flatbuffers.SizeUint32:])
	x := &Galaxy{}
	x.Init(buf, n+offset+flatbuffers.SizeUint32)
	return x
}

func FinishSizePrefixedGalaxyBuffer(builder *flatbuffers.Builder, offset flatbuffers.UOffsetT) {
	builder.FinishSizePrefixed(offset)
}

func (rcv *Galaxy) Init(buf []byte, i flatbuffers.UOffsetT) {
	rcv._tab.Bytes = buf
	rcv._tab.Pos = i
}

func (rcv *Galaxy) Table() flatbuffers.Table {
	return rcv._tab
}

func (rcv *Galaxy) NumStars() int64 {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(4))
	if o != 0 {
		return rcv._tab.GetInt64(o + rcv._tab.Pos)
	}
	return 0
}

func (rcv *Galaxy) MutateNumStars(n int64) bool {
	return rcv._tab.MutateInt64Slot(4, n)
}

func GalaxyStart(builder *flatbuffers.Builder) {
	builder.StartObject(1)
}
func GalaxyAddNumStars(builder *flatbuffers.Builder, numStars int64) {
	builder.PrependInt64Slot(0, numStars, 0)
}
func GalaxyEnd(builder *flatbuffers.Builder) flatbuffers.UOffsetT {
	return builder.EndObject()
}
