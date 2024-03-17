// <auto-generated>
//  automatically generated by the FlatBuffers compiler, do not modify
// </auto-generated>

namespace KeywordTest
{

using global::System;
using global::System.Collections.Generic;
using global::Google.FlatBuffers;

public struct Table2 : IFlatbufferObject
{
  private Table __p;
  public ByteBuffer ByteBuffer { get { return __p.bb; } }
  public static void ValidateVersion() { FlatBufferConstants.FLATBUFFERS_24_3_7(); }
  public static Table2 GetRootAsTable2(ByteBuffer _bb) { return GetRootAsTable2(_bb, new Table2()); }
  public static Table2 GetRootAsTable2(ByteBuffer _bb, Table2 obj) { return (obj.__assign(_bb.GetInt(_bb.Position) + _bb.Position, _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __p = new Table(_i, _bb); }
  public Table2 __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public KeywordTest.KeywordsInUnion TypeType { get { int o = __p.__offset(4); return o != 0 ? (KeywordTest.KeywordsInUnion)__p.bb.Get(o + __p.bb_pos) : KeywordTest.KeywordsInUnion.NONE; } }
  public TTable? Type<TTable>() where TTable : struct, IFlatbufferObject { int o = __p.__offset(6); return o != 0 ? (TTable?)__p.__union<TTable>(o + __p.bb_pos) : null; }
  public KeywordTest.KeywordsInTable TypeAsstatic() { return Type<KeywordTest.KeywordsInTable>().Value; }
  public KeywordTest.KeywordsInTable TypeAsinternal() { return Type<KeywordTest.KeywordsInTable>().Value; }

  public static Offset<KeywordTest.Table2> CreateTable2(FlatBufferBuilder builder,
      KeywordTest.KeywordsInUnion type_type = KeywordTest.KeywordsInUnion.NONE,
      int typeOffset = 0) {
    builder.StartTable(2);
    Table2.AddType(builder, typeOffset);
    Table2.AddTypeType(builder, type_type);
    return Table2.EndTable2(builder);
  }

  public static void StartTable2(FlatBufferBuilder builder) { builder.StartTable(2); }
  public static void AddTypeType(FlatBufferBuilder builder, KeywordTest.KeywordsInUnion typeType) { builder.AddByte(0, (byte)typeType, 0); }
  public static void AddType(FlatBufferBuilder builder, int typeOffset) { builder.AddOffset(1, typeOffset, 0); }
  public static Offset<KeywordTest.Table2> EndTable2(FlatBufferBuilder builder) {
    int o = builder.EndTable();
    return new Offset<KeywordTest.Table2>(o);
  }
  public Table2T UnPack() {
    var _o = new Table2T();
    this.UnPackTo(_o);
    return _o;
  }
  public void UnPackTo(Table2T _o) {
    _o.Type = new KeywordTest.KeywordsInUnionUnion();
    _o.Type.Type = this.TypeType;
    switch (this.TypeType) {
      default: break;
      case KeywordTest.KeywordsInUnion.static:
        _o.Type.Value = this.Type<KeywordTest.KeywordsInTable>().HasValue ? this.Type<KeywordTest.KeywordsInTable>().Value.UnPack() : null;
        break;
      case KeywordTest.KeywordsInUnion.internal:
        _o.Type.Value = this.Type<KeywordTest.KeywordsInTable>().HasValue ? this.Type<KeywordTest.KeywordsInTable>().Value.UnPack() : null;
        break;
    }
  }
  public static Offset<KeywordTest.Table2> Pack(FlatBufferBuilder builder, Table2T _o) {
    if (_o == null) return default(Offset<KeywordTest.Table2>);
    var _type_type = _o.Type == null ? KeywordTest.KeywordsInUnion.NONE : _o.Type.Type;
    var _type = _o.Type == null ? 0 : KeywordTest.KeywordsInUnionUnion.Pack(builder, _o.Type);
    return CreateTable2(
      builder,
      _type_type,
      _type);
  }
}

public class Table2T
{
  [Newtonsoft.Json.JsonProperty("type_type")]
  private KeywordTest.KeywordsInUnion TypeType {
    get {
      return this.Type != null ? this.Type.Type : KeywordTest.KeywordsInUnion.NONE;
    }
    set {
      this.Type = new KeywordTest.KeywordsInUnionUnion();
      this.Type.Type = value;
    }
  }
  [Newtonsoft.Json.JsonProperty("type")]
  [Newtonsoft.Json.JsonConverter(typeof(KeywordTest.KeywordsInUnionUnion_JsonConverter))]
  public KeywordTest.KeywordsInUnionUnion Type { get; set; }

  public Table2T() {
    this.Type = null;
  }
}


static public class Table2Verify
{
  static public bool Verify(Google.FlatBuffers.Verifier verifier, uint tablePos)
  {
    return verifier.VerifyTableStart(tablePos)
      && verifier.VerifyField(tablePos, 4 /*TypeType*/, 1 /*KeywordTest.KeywordsInUnion*/, 1, false)
      && verifier.VerifyUnion(tablePos, 4, 6 /*Type*/, KeywordTest.KeywordsInUnionVerify.Verify, false)
      && verifier.VerifyTableEnd(tablePos);
  }
}

}
