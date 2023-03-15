// <auto-generated>
//  automatically generated by the FlatBuffers compiler, do not modify
// </auto-generated>

namespace type_field_collsion
{

using global::System;
using global::System.Collections.Generic;
using global::Google.FlatBuffers;

public struct Collision : IFlatbufferObject
{
  private Table __p;
  public ByteBuffer ByteBuffer { get { return __p.bb; } }
  public static void ValidateVersion() { FlatBufferConstants.FLATBUFFERS_23_3_3(); }
  public static Collision GetRootAsCollision(ByteBuffer _bb) { return GetRootAsCollision(_bb, new Collision()); }
  public static Collision GetRootAsCollision(ByteBuffer _bb, Collision obj) { return (obj.__assign(_bb.GetInt(_bb.Position) + _bb.Position, _bb)); }
  public static bool VerifyCollision(ByteBuffer _bb) {Google.FlatBuffers.Verifier verifier = new Google.FlatBuffers.Verifier(_bb); return verifier.VerifyBuffer("", false, CollisionVerify.Verify); }
  public void __init(int _i, ByteBuffer _bb) { __p = new Table(_i, _bb); }
  public Collision __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public int Collision_ { get { int o = __p.__offset(4); return o != 0 ? __p.bb.GetInt(o + __p.bb_pos) : (int)0; } }

  public static Offset<type_field_collsion.Collision> CreateCollision(FlatBufferBuilder builder,
      int collision = 0) {
    builder.StartTable(1);
    Collision.AddCollision(builder, collision);
    return Collision.EndCollision(builder);
  }

  public static void StartCollision(FlatBufferBuilder builder) { builder.StartTable(1); }
  public static void AddCollision(FlatBufferBuilder builder, int collision) { builder.AddInt(0, collision, 0); }
  public static Offset<type_field_collsion.Collision> EndCollision(FlatBufferBuilder builder) {
    int o = builder.EndTable();
    return new Offset<type_field_collsion.Collision>(o);
  }
  public static void FinishCollisionBuffer(FlatBufferBuilder builder, Offset<type_field_collsion.Collision> offset) { builder.Finish(offset.Value); }
  public static void FinishSizePrefixedCollisionBuffer(FlatBufferBuilder builder, Offset<type_field_collsion.Collision> offset) { builder.FinishSizePrefixed(offset.Value); }
  public CollisionT UnPack() {
    var _o = new CollisionT();
    this.UnPackTo(_o);
    return _o;
  }
  public void UnPackTo(CollisionT _o) {
    _o.Collision_ = this.Collision_;
  }
  public static Offset<type_field_collsion.Collision> Pack(FlatBufferBuilder builder, CollisionT _o) {
    if (_o == null) return default(Offset<type_field_collsion.Collision>);
    return CreateCollision(
      builder,
      _o.Collision_);
  }
}

public class CollisionT
{
  public int Collision_ { get; set; }

  public CollisionT() {
    this.Collision_ = 0;
  }
  public static CollisionT DeserializeFromBinary(byte[] fbBuffer) {
    return Collision.GetRootAsCollision(new ByteBuffer(fbBuffer)).UnPack();
  }
  public byte[] SerializeToBinary() {
    var fbb = new FlatBufferBuilder(0x10000);
    Collision.FinishCollisionBuffer(fbb, Collision.Pack(fbb, this));
    return fbb.DataBuffer.ToSizedArray();
  }
}


// Verification function for 'Collision' table.
static public class CollisionVerify
{
  static public bool Verify(Google.FlatBuffers.Verifier verifier, uint tablePos)
  {
    bool result = true;
    result = result && verifier.VerifyTableStart(tablePos);
    result = result && verifier.VerifyField(tablePos, 4 /*Collision*/, 4 /*int*/, 4, false);
    result = result && verifier.VerifyTableEnd(tablePos);
    return result;
  }
}

}
