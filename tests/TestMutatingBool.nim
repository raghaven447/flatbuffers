#[ TestMutatingBool
  Automatically generated by the FlatBuffers compiler, do not modify.
  Or modify. I'm a message, not a cop.

  flatc version: 22.9.29

  Declared by  : 
]#

import Property as Property
import flatbuffers
import std/options

type TestMutatingBool* = object of FlatObj
func b*(self: TestMutatingBool): Option[Property.Property] =
  let o = self.tab.Offset(4)
  if o != 0:
    return some(Property.Property(tab: Vtable(Bytes: self.tab.Bytes, Pos: self.tab.Pos + o)))
proc TestMutatingBoolStart*(builder: var Builder) =
  builder.StartObject(1)
proc TestMutatingBoolAddb*(builder: var Builder, b: uoffset) =
  builder.PrependStructSlot(0, b, default(uoffset))
proc TestMutatingBoolEnd*(builder: var Builder): uoffset =
  return builder.EndObject()
