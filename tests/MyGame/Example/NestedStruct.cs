// <auto-generated>
//  automatically generated by the FlatBuffers compiler, do not modify
// </auto-generated>

namespace MyGame.Example
{

using global::System;
using global::System.Collections.Generic;
using global::FlatBuffers;

public struct NestedStruct : IFlatbufferObject
{
  private Struct __p;
  public ByteBuffer ByteBuffer { get { return __p.bb; } }
  public void __init(int _i, ByteBuffer _bb) { __p = new Struct(_i, _bb); }
  public NestedStruct __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public int A(int j) { return __p.bb.GetInt(__p.bb_pos + 0 + j * 4); }
  public void MutateA(int j, int a) { __p.bb.PutInt(__p.bb_pos + 0 + j * 4, a); }
  public MyGame.Example.TestEnum B { get { return (MyGame.Example.TestEnum)__p.bb.GetSbyte(__p.bb_pos + 8); } }
  public void MutateB(MyGame.Example.TestEnum b) { __p.bb.PutSbyte(__p.bb_pos + 8, (sbyte)b); }
  public MyGame.Example.TestEnum C(int j) { return (MyGame.Example.TestEnum)__p.bb.GetSbyte(__p.bb_pos + 9 + j * 1); }
  public void MutateC(int j, MyGame.Example.TestEnum c) { __p.bb.PutSbyte(__p.bb_pos + 9 + j * 1, (sbyte)c); }
  public long D(int j) { return __p.bb.GetLong(__p.bb_pos + 16 + j * 8); }
  public void MutateD(int j, long d) { __p.bb.PutLong(__p.bb_pos + 16 + j * 8, d); }

  public static Offset<MyGame.Example.NestedStruct> CreateNestedStruct(FlatBufferBuilder builder, int[] A, MyGame.Example.TestEnum B, MyGame.Example.TestEnum[] C, long[] D) {
    builder.Prep(8, 32);
    for (int _idx0 = 2; _idx0 > 0; _idx0--) {
      builder.PutLong(D[_idx0-1]);
    }
    builder.Pad(5);
    for (int _idx0 = 2; _idx0 > 0; _idx0--) {
      builder.PutSbyte((sbyte)C[_idx0-1]);
    }
    builder.PutSbyte((sbyte)B);
    for (int _idx0 = 2; _idx0 > 0; _idx0--) {
      builder.PutInt(A[_idx0-1]);
    }
    return new Offset<MyGame.Example.NestedStruct>(builder.Offset);
  }
  public NestedStructT UnPack() {
    var _o = new NestedStructT();
    this.UnPackTo(_o);
    return _o;
  }
  public void UnPackTo(NestedStructT _o) {
    _o.A = new int[2];
    for (var _j = 0; _j < 2; ++_j) { _o.A[_j] = this.A(_j); }
    _o.B = this.B;
    _o.C = new MyGame.Example.TestEnum[2];
    for (var _j = 0; _j < 2; ++_j) { _o.C[_j] = this.C(_j); }
    _o.D = new long[2];
    for (var _j = 0; _j < 2; ++_j) { _o.D[_j] = this.D(_j); }
  }
  public static Offset<MyGame.Example.NestedStruct> Pack(FlatBufferBuilder builder, NestedStructT _o) {
    if (_o == null) return default(Offset<MyGame.Example.NestedStruct>);
    var _a = _o.A;
    var _c = _o.C;
    var _d = _o.D;
    return CreateNestedStruct(
      builder,
      _a,
      _o.B,
      _c,
      _d);
  }
};

public class NestedStructT
{
#if ENABLE_JSON_SERIALIZATION
  [Newtonsoft.Json.JsonProperty("a")]
#endif
  public int[] A { get; set; }
#if ENABLE_JSON_SERIALIZATION
  [Newtonsoft.Json.JsonProperty("b")]
#endif
  public MyGame.Example.TestEnum B { get; set; }
#if ENABLE_JSON_SERIALIZATION
  [Newtonsoft.Json.JsonProperty("c")]
#endif
  public MyGame.Example.TestEnum[] C { get; set; }
#if ENABLE_JSON_SERIALIZATION
  [Newtonsoft.Json.JsonProperty("d")]
#endif
  public long[] D { get; set; }

  public NestedStructT() {
    this.A = new int[2];
    this.B = MyGame.Example.TestEnum.A;
    this.C = new MyGame.Example.TestEnum[2];
    this.D = new long[2];
  }
}


}
