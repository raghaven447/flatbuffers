// automatically generated by the FlatBuffers compiler, do not modify

package MyGame.Example;

import java.nio.*;
import java.lang.*;
import java.util.*;
import com.google.flatbuffers.*;

@SuppressWarnings("unused")
public final class Referrable extends Table {
  public static void ValidateVersion() { Constants.FLATBUFFERS_1_12_0(); }
  public static Referrable getRootAsReferrable(ByteBuffer _bb) { return getRootAsReferrable(_bb, new Referrable()); }
  public static Referrable getRootAsReferrable(ByteBuffer _bb, Referrable obj) { _bb.order(ByteOrder.LITTLE_ENDIAN); return (obj.__assign(_bb.getInt(_bb.position()) + _bb.position(), _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __reset(_i, _bb); }
  public Referrable __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public long id() { int o = __offset(4); return o != 0 ? bb.getLong(o + bb_pos) : 0L; }
  public boolean mutateId(long id) { int o = __offset(4); if (o != 0) { bb.putLong(o + bb_pos, id); return true; } else { return false; } }

  public static int createReferrable(FlatBufferBuilder builder,
      long id) {
    builder.startTable(1);
    Referrable.addId(builder, id);
    return Referrable.endReferrable(builder);
  }

  public static void startReferrable(FlatBufferBuilder builder) { builder.startTable(1); }
  public static void addId(FlatBufferBuilder builder, long id) { builder.addLong(0, id, 0L); }
  public static int endReferrable(FlatBufferBuilder builder) {
    int o = builder.endTable();
    return o;
  }

  @Override
  protected int keysCompare(Integer o1, Integer o2, ByteBuffer _bb) {
    long val_1 = _bb.getLong(__offset(4, o1, _bb));
    long val_2 = _bb.getLong(__offset(4, o2, _bb));
    return val_1 > val_2 ? 1 : val_1 < val_2 ? -1 : 0;
  }

  public static Referrable __lookup_by_key(Referrable obj, int vectorLocation, long key, ByteBuffer bb) {
    int span = bb.getInt(vectorLocation - 4);
    int start = 0;
    while (span != 0) {
      int middle = span / 2;
      int tableOffset = __indirect(vectorLocation + 4 * (start + middle), bb);
      long val = bb.getLong(__offset(4, bb.capacity() - tableOffset, bb));
      int comp = val > key ? 1 : val < key ? -1 : 0;
      if (comp > 0) {
        span = middle;
      } else if (comp < 0) {
        middle++;
        start += middle;
        span -= middle;
      } else {
        return (obj == null ? new Referrable() : obj).__assign(tableOffset, bb);
      }
    }
    return null;
  }

  public static final class Vector extends BaseVector {
    public Vector __assign(int _vector, int _element_size, ByteBuffer _bb) { __reset(_vector, _element_size, _bb); return this; }

    public Referrable get(int j) { return get(new Referrable(), j); }
    public Referrable get(Referrable obj, int j) {  return obj.__assign(__indirect(__element(j), bb), bb); }
    public Referrable getByKey(long key) {  return __lookup_by_key(null, __vector(), key, bb); }
    public Referrable getByKey(Referrable obj, long key) {  return __lookup_by_key(obj, __vector(), key, bb); }
  }
  public ReferrableT unpack() {
    ReferrableT _o = new ReferrableT();
    this.unpackTo(_o);
    return _o;
  }
  public void unpackTo(ReferrableT _o) {
    long _oId = this.id();
    _o.setId(_oId);
  }
  public static int pack(FlatBufferBuilder builder, ReferrableT _o) {
    if (_o == null) return 0;
    return createReferrable(
      builder,
      _o.getId());
  }
}