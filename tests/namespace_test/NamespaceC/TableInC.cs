// <auto-generated>
//  automatically generated by the FlatBuffers compiler, do not modify
// </auto-generated>

namespace NamespaceC
{

using global::System;
using global::System.Collections.Generic;
using global::FlatBuffers;

public struct TableInC : IFlatbufferObject
{
  private Table __p;
  public ByteBuffer ByteBuffer { get { return __p.bb; } }
  public static void ValidateVersion() { FlatBufferConstants.FLATBUFFERS_1_11_1(); }
  public static TableInC GetRootAsTableInC(ByteBuffer _bb) { return GetRootAsTableInC(_bb, new TableInC()); }
  public static TableInC GetRootAsTableInC(ByteBuffer _bb, TableInC obj) { return (obj.__assign(_bb.GetInt(_bb.Position) + _bb.Position, _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __p = new Table(_i, _bb); }
  public TableInC __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public NamespaceA.TableInFirstNS? ReferToA1 { get { int o = __p.__offset(4); return o != 0 ? (NamespaceA.TableInFirstNS?)(new NamespaceA.TableInFirstNS()).__assign(__p.__indirect(o + __p.bb_pos), __p.bb) : null; } }
  public NamespaceA.SecondTableInA? ReferToA2 { get { int o = __p.__offset(6); return o != 0 ? (NamespaceA.SecondTableInA?)(new NamespaceA.SecondTableInA()).__assign(__p.__indirect(o + __p.bb_pos), __p.bb) : null; } }

  public static Offset<NamespaceC.TableInC> CreateTableInC(FlatBufferBuilder builder,
      Offset<NamespaceA.TableInFirstNS> refer_to_a1Offset = default(Offset<NamespaceA.TableInFirstNS>),
      Offset<NamespaceA.SecondTableInA> refer_to_a2Offset = default(Offset<NamespaceA.SecondTableInA>)) {
    builder.StartTable(2);
    TableInC.AddReferToA2(builder, refer_to_a2Offset);
    TableInC.AddReferToA1(builder, refer_to_a1Offset);
    return TableInC.EndTableInC(builder);
  }

  public static void StartTableInC(FlatBufferBuilder builder) { builder.StartTable(2); }
  public static void AddReferToA1(FlatBufferBuilder builder, Offset<NamespaceA.TableInFirstNS> referToA1Offset) { builder.AddOffset(0, referToA1Offset.Value, 0); }
  public static void AddReferToA2(FlatBufferBuilder builder, Offset<NamespaceA.SecondTableInA> referToA2Offset) { builder.AddOffset(1, referToA2Offset.Value, 0); }
  public static Offset<NamespaceC.TableInC> EndTableInC(FlatBufferBuilder builder) {
    int o = builder.EndTable();
    return new Offset<NamespaceC.TableInC>(o);
  }
  public TableInCT UnPack() {
    var _o = new TableInCT();
    this.UnPackTo(_o);
    return _o;
  }
  public void UnPackTo(TableInCT _o) {
    _o.ReferToA1 = this.ReferToA1.HasValue ? this.ReferToA1.Value.UnPack() : null;
    _o.ReferToA2 = this.ReferToA2.HasValue ? this.ReferToA2.Value.UnPack() : null;
  }
  public static Offset<NamespaceC.TableInC> Pack(FlatBufferBuilder builder, TableInCT _o) {
    if (_o == null) return default(Offset<NamespaceC.TableInC>);
    var _refer_to_a1 = _o.ReferToA1 == null ? default(Offset<NamespaceA.TableInFirstNS>) : NamespaceA.TableInFirstNS.Pack(builder, _o.ReferToA1);
    var _refer_to_a2 = _o.ReferToA2 == null ? default(Offset<NamespaceA.SecondTableInA>) : NamespaceA.SecondTableInA.Pack(builder, _o.ReferToA2);
    return CreateTableInC(
      builder,
      _refer_to_a1,
      _refer_to_a2);
  }
};

public class TableInCT
{
#if ENABLE_JSON_SERIALIZATION
  [Newtonsoft.Json.JsonProperty("refer_to_a1")]
#endif
  public NamespaceA.TableInFirstNST ReferToA1 { get; set; }
#if ENABLE_JSON_SERIALIZATION
  [Newtonsoft.Json.JsonProperty("refer_to_a2")]
#endif
  public NamespaceA.SecondTableInAT ReferToA2 { get; set; }

  public TableInCT() {
    this.ReferToA1 = null;
    this.ReferToA2 = null;
  }
}


}
