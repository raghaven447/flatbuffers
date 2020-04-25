// Code generated by the FlatBuffers compiler. DO NOT EDIT.

package Example

import (
	flatbuffers "github.com/google/flatbuffers/go"
)

type AbilityT struct {
	Id uint32
	Distance uint32
}

func (t *AbilityT) Pack(builder *flatbuffers.Builder) flatbuffers.UOffsetT {
	if t == nil {
		return 0
	}
	return CreateAbility(builder, t.Id, t.Distance)
}
func (rcv *Ability) UnPackTo(t *AbilityT) {
	t.Id = rcv.Id()
	t.Distance = rcv.Distance()
}

func (rcv *Ability) UnPack() *AbilityT {
	if rcv == nil {
		return nil
	}
	t := &AbilityT{}
	rcv.UnPackTo(t)
	return t
}

type Ability struct {
	_tab flatbuffers.Struct
}

// GetStructVectorAsAbility shortcut to access struct in vector of unions
func GetStructVectorAsAbility(table *flatbuffers.Table) *Ability {
	n := flatbuffers.GetUOffsetT(table.Bytes[table.Pos:])
	x := &Ability{}
	x.Init(table.Bytes, n+table.Pos)
	return x
}

// GetStructAsAbility shortcut to access struct in single union field
func GetStructAsAbility(table *flatbuffers.Table) *Ability {
	x := &Ability{}
	x.Init(table.Bytes, table.Pos)
	return x
}

func (rcv *Ability) Init(buf []byte, i flatbuffers.UOffsetT) {
	rcv._tab.Bytes = buf
	rcv._tab.Pos = i
}

func (rcv *Ability) Table() flatbuffers.Table {
	return rcv._tab.Table
}

func (rcv *Ability) Id() uint32 {
	return rcv._tab.GetUint32(rcv._tab.Pos + flatbuffers.UOffsetT(0))
}
func (rcv *Ability) MutateId(n uint32) bool {
	return rcv._tab.MutateUint32(rcv._tab.Pos + flatbuffers.UOffsetT(0), n)
}

func (rcv *Ability) Distance() uint32 {
	return rcv._tab.GetUint32(rcv._tab.Pos + flatbuffers.UOffsetT(4))
}
func (rcv *Ability) MutateDistance(n uint32) bool {
	return rcv._tab.MutateUint32(rcv._tab.Pos + flatbuffers.UOffsetT(4), n)
}

func CreateAbility(builder *flatbuffers.Builder, id uint32, distance uint32) flatbuffers.UOffsetT {
	builder.Prep(4, 8)
	builder.PrependUint32(distance)
	builder.PrependUint32(id)
	return builder.Offset()
}
