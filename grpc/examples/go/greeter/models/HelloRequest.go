// Code generated by the FlatBuffers compiler. DO NOT EDIT.

package models

import (
	flatbuffers "github.com/google/flatbuffers/go"
)

type HelloRequest struct {
	_tab flatbuffers.Table
}

func GetRootAsHelloRequest(buf []byte, offset flatbuffers.UOffsetT) *HelloRequest {
	n := flatbuffers.GetUOffsetT(buf[offset:])
	x := &HelloRequest{}
	x.Init(buf, n+offset)
	return x
}

func FinishHelloRequestBuffer(builder *flatbuffers.Builder, offset flatbuffers.UOffsetT) {
	builder.Finish(offset)
}

func VerifyHelloRequest(buf []byte) bool {
	return flatbuffers.NewVerifier(buf).VerifyBuffer(nil, false, HelloRequestVerify)

}

func GetSizePrefixedRootAsHelloRequest(buf []byte, offset flatbuffers.UOffsetT) *HelloRequest {
	n := flatbuffers.GetUOffsetT(buf[offset+flatbuffers.SizeUint32:])
	x := &HelloRequest{}
	x.Init(buf, n+offset+flatbuffers.SizeUint32)
	return x
}

func FinishSizePrefixedHelloRequestBuffer(builder *flatbuffers.Builder, offset flatbuffers.UOffsetT) {
	builder.FinishSizePrefixed(offset)
}

func SizePrefixedVerifyHelloRequest(buf []byte) bool {
	return flatbuffers.NewVerifier(buf).VerifyBuffer(nil, true, HelloRequestVerify)

}

func (rcv *HelloRequest) Init(buf []byte, i flatbuffers.UOffsetT) {
	rcv._tab.Bytes = buf
	rcv._tab.Pos = i
}

func (rcv *HelloRequest) Table() flatbuffers.Table {
	return rcv._tab
}

func (rcv *HelloRequest) Name() []byte {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(4))
	if o != 0 {
		return rcv._tab.ByteVector(o + rcv._tab.Pos)
	}
	return nil
}

func HelloRequestStart(builder *flatbuffers.Builder) {
	builder.StartObject(1)
}
func HelloRequestAddName(builder *flatbuffers.Builder, name flatbuffers.UOffsetT) {
	builder.PrependUOffsetTSlot(0, flatbuffers.UOffsetT(name), 0)
}
func HelloRequestEnd(builder *flatbuffers.Builder) flatbuffers.UOffsetT {
	return builder.EndObject()
}

// Verification function for 'HelloRequest' table.
func HelloRequestVerify(verifier *flatbuffers.Verifier, tablePos flatbuffers.UOffsetT) bool {
	result := true
	result = result && verifier.VerifyTableStart(tablePos)
	result = result && verifier.VerifyString(tablePos, 4 /*Name*/, false)
	result = result && verifier.VerifyTableEnd(tablePos)
	return result
}
