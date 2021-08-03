// <auto-generated>
//  automatically generated by the FlatBuffers compiler, do not modify
// </auto-generated>

namespace MyGame.Example
{

using global::System;
using global::System.Collections.Generic;
using global::FlatBuffers;

internal partial struct TestSimpleTableWithEnum : IFlatbufferObject
{
  private Table __p;
  public ByteBuffer ByteBuffer { get { return __p.bb; } }
  public static void ValidateVersion() { FlatBufferConstants.FLATBUFFERS_2_0_0(); }
  public static TestSimpleTableWithEnum GetRootAsTestSimpleTableWithEnum(ByteBuffer _bb) { return GetRootAsTestSimpleTableWithEnum(_bb, new TestSimpleTableWithEnum()); }
  public static TestSimpleTableWithEnum GetRootAsTestSimpleTableWithEnum(ByteBuffer _bb, TestSimpleTableWithEnum obj) { return (obj.__assign(_bb.GetInt(_bb.Position) + _bb.Position, _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __p = new Table(_i, _bb); }
  public TestSimpleTableWithEnum __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public global::MyGame.Example.Color Color { get { int o = __p.__offset(4); return o != 0 ? (global::MyGame.Example.Color)__p.bb.Get(o + __p.bb_pos) : global::MyGame.Example.Color.Green; } }
  public bool MutateColor(global::MyGame.Example.Color color) { int o = __p.__offset(4); if (o != 0) { __p.bb.Put(o + __p.bb_pos, (byte)color); return true; } else { return false; } }

  public static Offset<global::MyGame.Example.TestSimpleTableWithEnum> CreateTestSimpleTableWithEnum(FlatBufferBuilder builder,
      global::MyGame.Example.Color color = global::MyGame.Example.Color.Green) {
    builder.StartTable(1);
    TestSimpleTableWithEnum.AddColor(builder, color);
    return TestSimpleTableWithEnum.EndTestSimpleTableWithEnum(builder);
  }

  public static void StartTestSimpleTableWithEnum(FlatBufferBuilder builder) { builder.StartTable(1); }
  public static void AddColor(FlatBufferBuilder builder, global::MyGame.Example.Color color) { builder.AddByte(0, (byte)color, 2); }
  public static Offset<global::MyGame.Example.TestSimpleTableWithEnum> EndTestSimpleTableWithEnum(FlatBufferBuilder builder) {
    int o = builder.EndTable();
    return new Offset<global::MyGame.Example.TestSimpleTableWithEnum>(o);
  }
  public TestSimpleTableWithEnumT UnPack() {
    var _o = new TestSimpleTableWithEnumT();
    this.UnPackTo(_o);
    return _o;
  }
  public void UnPackTo(TestSimpleTableWithEnumT _o) {
    _o.Color = this.Color;
  }
  public static Offset<global::MyGame.Example.TestSimpleTableWithEnum> Pack(FlatBufferBuilder builder, TestSimpleTableWithEnumT _o) {
    if (_o == null) return default(Offset<global::MyGame.Example.TestSimpleTableWithEnum>);
    return CreateTestSimpleTableWithEnum(
      builder,
      _o.Color);
  }
};

internal partial class TestSimpleTableWithEnumT
{
  [Newtonsoft.Json.JsonProperty("color")]
  public global::MyGame.Example.Color Color { get; set; }

  public TestSimpleTableWithEnumT() {
    this.Color = global::MyGame.Example.Color.Green;
  }
}


}
