// <auto-generated>
//  automatically generated by the FlatBuffers compiler, do not modify
// </auto-generated>

namespace MyGame.Example
{

using global::System;
using global::System.Collections.Generic;
using global::FlatBuffers;

public struct NativeInlineTable : IFlatbufferObject
{
  private Table __p;
  public ByteBuffer ByteBuffer { get { return __p.bb; } }
  public static void ValidateVersion() { FlatBufferConstants.FLATBUFFERS_2_0_0(); }
  public static NativeInlineTable GetRootAsNativeInlineTable(ByteBuffer _bb) { return GetRootAsNativeInlineTable(_bb, new NativeInlineTable()); }
  public static NativeInlineTable GetRootAsNativeInlineTable(ByteBuffer _bb, NativeInlineTable obj) { return (obj.__assign(_bb.GetInt(_bb.Position) + _bb.Position, _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __p = new Table(_i, _bb); }
  public NativeInlineTable __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public int A { get { int o = __p.__offset(4); return o != 0 ? __p.bb.GetInt(o + __p.bb_pos) : (int)0; } }
  public bool MutateA(int a) { int o = __p.__offset(4); if (o != 0) { __p.bb.PutInt(o + __p.bb_pos, a); return true; } else { return false; } }

  public static Offset<MyGame.Example.NativeInlineTable> CreateNativeInlineTable(FlatBufferBuilder builder,
      int a = 0) {
    builder.StartTable(1);
    NativeInlineTable.AddA(builder, a);
    return NativeInlineTable.EndNativeInlineTable(builder);
  }

  public static void StartNativeInlineTable(FlatBufferBuilder builder) { builder.StartTable(1); }
  public static void AddA(FlatBufferBuilder builder, int a) { builder.AddInt(0, a, 0); }
  public static Offset<MyGame.Example.NativeInlineTable> EndNativeInlineTable(FlatBufferBuilder builder) {
    int o = builder.EndTable();
    return new Offset<MyGame.Example.NativeInlineTable>(o);
  }
  public NativeInlineTableT UnPack() {
    var _o = new NativeInlineTableT();
    this.UnPackTo(_o);
    return _o;
  }
  public void UnPackTo(NativeInlineTableT _o) {
    _o.A = this.A;
  }
  public static Offset<MyGame.Example.NativeInlineTable> Pack(FlatBufferBuilder builder, NativeInlineTableT _o) {
    if (_o == null) return default(Offset<MyGame.Example.NativeInlineTable>);
    return CreateNativeInlineTable(
      builder,
      _o.A);
  }
}

public class NativeInlineTableT
{
  [Newtonsoft.Json.JsonProperty("a")]
  public int A { get; set; }

  public NativeInlineTableT() {
    this.A = 0;
  }
}


}
