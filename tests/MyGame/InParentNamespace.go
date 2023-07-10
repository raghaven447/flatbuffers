// Code generated by the FlatBuffers compiler. DO NOT EDIT.

package MyGame

import (
	flatbuffers "github.com/google/flatbuffers/go"
)

type InParentNamespaceT struct {
}

func (t *InParentNamespaceT) Pack(builder *flatbuffers.Builder) flatbuffers.UOffsetT {
	if t == nil {
		return 0
	}
	InParentNamespaceStart(builder)
	return InParentNamespaceEnd(builder)
}

func (rcv *InParentNamespace) UnPackTo(t *InParentNamespaceT) {
}

func (rcv *InParentNamespace) UnPack() *InParentNamespaceT {
	if rcv == nil {
		return nil
	}
	t := &InParentNamespaceT{}
	rcv.UnPackTo(t)
	return t
}

type InParentNamespace struct {
	_tab flatbuffers.Table
}

func GetRootAsInParentNamespace(buf []byte, offset flatbuffers.UOffsetT) *InParentNamespace {
	n := flatbuffers.GetUOffsetT(buf[offset:])
	x := &InParentNamespace{}
	x.Init(buf, n+offset)
	return x
}

func FinishInParentNamespaceBuffer(builder *flatbuffers.Builder, offset flatbuffers.UOffsetT) {
	builder.Finish(offset)
}

func VerifyInParentNamespace(buf []byte) bool {
	return flatbuffers.NewVerifier(buf).VerifyBuffer(nil, false, InParentNamespaceVerify)

}

func GetSizePrefixedRootAsInParentNamespace(buf []byte, offset flatbuffers.UOffsetT) *InParentNamespace {
	n := flatbuffers.GetUOffsetT(buf[offset+flatbuffers.SizeUint32:])
	x := &InParentNamespace{}
	x.Init(buf, n+offset+flatbuffers.SizeUint32)
	return x
}

func FinishSizePrefixedInParentNamespaceBuffer(builder *flatbuffers.Builder, offset flatbuffers.UOffsetT) {
	builder.FinishSizePrefixed(offset)
}

func SizePrefixedVerifyInParentNamespace(buf []byte) bool {
	return flatbuffers.NewVerifier(buf).VerifyBuffer(nil, true, InParentNamespaceVerify)

}

func (rcv *InParentNamespace) Init(buf []byte, i flatbuffers.UOffsetT) {
	rcv._tab.Bytes = buf
	rcv._tab.Pos = i
}

func (rcv *InParentNamespace) Table() flatbuffers.Table {
	return rcv._tab
}

func InParentNamespaceStart(builder *flatbuffers.Builder) {
	builder.StartObject(0)
}
func InParentNamespaceEnd(builder *flatbuffers.Builder) flatbuffers.UOffsetT {
	return builder.EndObject()
}

// Verification function for 'InParentNamespace' table.
func InParentNamespaceVerify(verifier *flatbuffers.Verifier, tablePos flatbuffers.UOffsetT) bool {
	result := true
	result = result && verifier.VerifyTableStart(tablePos)
	result = result && verifier.VerifyTableEnd(tablePos)
	return result
}
