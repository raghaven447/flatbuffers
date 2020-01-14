// <auto-generated>
//  automatically generated by the FlatBuffers compiler, do not modify
// </auto-generated>

namespace NamespaceA
{

using global::System;
using global::System.Collections.Generic;
using global::System.Linq;
using global::FlatBuffers;

public struct TableInFirstNS : IFlatbufferObject
{
  private Table __p;
  public ByteBuffer ByteBuffer { get { return __p.bb; } }
  public static void ValidateVersion() { FlatBufferConstants.FLATBUFFERS_1_11_1(); }
  public static TableInFirstNS GetRootAsTableInFirstNS(ByteBuffer _bb) { return GetRootAsTableInFirstNS(_bb, new TableInFirstNS()); }
  public static TableInFirstNS GetRootAsTableInFirstNS(ByteBuffer _bb, TableInFirstNS obj) { return (obj.__assign(_bb.GetInt(_bb.Position) + _bb.Position, _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __p = new Table(_i, _bb); }
  public TableInFirstNS __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public NamespaceA.NamespaceB.TableInNestedNS? FooTable { get { int o = __p.__offset(4); return o != 0 ? (NamespaceA.NamespaceB.TableInNestedNS?)(new NamespaceA.NamespaceB.TableInNestedNS()).__assign(__p.__indirect(o + __p.bb_pos), __p.bb) : null; } }
  public NamespaceA.NamespaceB.EnumInNestedNS FooEnum { get { int o = __p.__offset(6); return o != 0 ? (NamespaceA.NamespaceB.EnumInNestedNS)__p.bb.GetSbyte(o + __p.bb_pos) : NamespaceA.NamespaceB.EnumInNestedNS.A; } }
  public bool MutateFooEnum(NamespaceA.NamespaceB.EnumInNestedNS foo_enum) { int o = __p.__offset(6); if (o != 0) { __p.bb.PutSbyte(o + __p.bb_pos, (sbyte)foo_enum); return true; } else { return false; } }
  public NamespaceA.NamespaceB.StructInNestedNS? FooStruct { get { int o = __p.__offset(8); return o != 0 ? (NamespaceA.NamespaceB.StructInNestedNS?)(new NamespaceA.NamespaceB.StructInNestedNS()).__assign(o + __p.bb_pos, __p.bb) : null; } }

  public static void StartTableInFirstNS(FlatBufferBuilder builder) { builder.StartTable(3); }
  public static void AddFooTable(FlatBufferBuilder builder, Offset<NamespaceA.NamespaceB.TableInNestedNS> fooTableOffset) { builder.AddOffset(0, fooTableOffset.Value, 0); }
  public static void AddFooEnum(FlatBufferBuilder builder, NamespaceA.NamespaceB.EnumInNestedNS fooEnum) { builder.AddSbyte(1, (sbyte)fooEnum, 0); }
  public static void AddFooStruct(FlatBufferBuilder builder, Offset<NamespaceA.NamespaceB.StructInNestedNS> fooStructOffset) { builder.AddStruct(2, fooStructOffset.Value, 0); }
  public static Offset<NamespaceA.TableInFirstNS> EndTableInFirstNS(FlatBufferBuilder builder) {
    int o = builder.EndTable();
    return new Offset<NamespaceA.TableInFirstNS>(o);
  }
  public TableInFirstNST UnPack() {
    var _o = new TableInFirstNST();
    this.UnPackTo(_o);
    return _o;
  }
  public void UnPackTo(TableInFirstNST _o) {
    _o.FooTable = this.FooTable?.UnPack();
    _o.FooEnum = this.FooEnum;
    _o.FooStruct = this.FooStruct?.UnPack();
  }
  public static Offset<NamespaceA.TableInFirstNS> Pack(FlatBufferBuilder builder, TableInFirstNST _o) {
    if (_o == null) return default(Offset<NamespaceA.TableInFirstNS>);
    var _foo_table = _o.FooTable == null ? default(Offset<NamespaceA.NamespaceB.TableInNestedNS>) : NamespaceA.NamespaceB.TableInNestedNS.Pack(builder, _o.FooTable);
    StartTableInFirstNS(builder);
    AddFooTable(builder, _foo_table);
    AddFooEnum(builder, _o.FooEnum);
    AddFooStruct(builder, NamespaceA.NamespaceB.StructInNestedNS.Pack(builder, _o.FooStruct));
    return EndTableInFirstNS(builder);
  }
};

public class TableInFirstNST
{
  public NamespaceA.NamespaceB.TableInNestedNST FooTable { get; set; } 
  public NamespaceA.NamespaceB.EnumInNestedNS FooEnum { get; set; } = NamespaceA.NamespaceB.EnumInNestedNS.A;
  public NamespaceA.NamespaceB.StructInNestedNST FooStruct { get; set; } = new NamespaceA.NamespaceB.StructInNestedNST();
};


}
