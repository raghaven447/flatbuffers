--[[ MyGame.Example.Test

  Automatically generated by the FlatBuffers compiler, do not modify.
  Or modify. I'm a message, not a cop.

  flatc version: 23.5.9

  Declared by  : //monster_test.fbs
  Rooting type : MyGame.Example.Monster (//monster_test.fbs)

--]]

local flatbuffers = require('flatbuffers')

local Test = {}
local mt = {}

function Test.New()
  local o = {}
  setmetatable(o, {__index = mt})
  return o
end

function mt:Init(buf, pos)
  self.view = flatbuffers.view.New(buf, pos)
end

function mt:A()
  return self.view:Get(flatbuffers.N.Int16, self.view.pos + 0)
end

function mt:B()
  return self.view:Get(flatbuffers.N.Int8, self.view.pos + 2)
end

function Test.CreateTest(builder, a, b)
  builder:Prep(2, 4)
  builder:Pad(1)
  builder:PrependInt8(b)
  builder:PrependInt16(a)
  return builder:Offset()
end

return Test