// <auto-generated>
//  automatically generated by the FlatBuffers compiler, do not modify
// </auto-generated>

using global::System;
using global::FlatBuffers;

public struct TableA : IFlatbufferObject
{
  private Table __p;
  public ByteBuffer ByteBuffer { get { return __p.bb; } }
  public static void ValidateVersion() { FlatBufferConstants.FLATBUFFERS_1_11_1(); }
  public static TableA GetRootAsTableA(ByteBuffer _bb) { return GetRootAsTableA(_bb, new TableA()); }
  public static TableA GetRootAsTableA(ByteBuffer _bb, TableA obj) { return (obj.__assign(_bb.GetInt(_bb.Position) + _bb.Position, _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __p = new Table(_i, _bb); }
  public TableA __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public MyGame.OtherNameSpace.TableB? B { get { int o = __p.__offset(4); return o != 0 ? (MyGame.OtherNameSpace.TableB?)(new MyGame.OtherNameSpace.TableB()).__assign(__p.__indirect(o + __p.bb_pos), __p.bb) : null; } }

  public static Offset<TableA> CreateTableA(FlatBufferBuilder builder,
      Offset<MyGame.OtherNameSpace.TableB> bOffset = default(Offset<MyGame.OtherNameSpace.TableB>)) {
    builder.StartTable(1);
    TableA.AddB(builder, bOffset);
    return TableA.EndTableA(builder);
  }

  public static void StartTableA(FlatBufferBuilder builder) { builder.StartTable(1); }
  public static void AddB(FlatBufferBuilder builder, Offset<MyGame.OtherNameSpace.TableB> bOffset) { builder.AddOffset(0, bOffset.Value, 0); }
  public static Offset<TableA> EndTableA(FlatBufferBuilder builder) {
    int o = builder.EndTable();
    return new Offset<TableA>(o);
  }
};

