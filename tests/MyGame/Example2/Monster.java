// automatically generated by the FlatBuffers compiler, do not modify

package MyGame.Example2;

import com.google.flatbuffers.Table;
import com.google.flatbuffers.Struct;
import com.google.flatbuffers.FlatBufferBuilder;
import com.google.flatbuffers.BaseVector;
import java.nio.ByteBuffer;

@SuppressWarnings("unused")
public final class Monster extends Table {
  public static void ValidateVersion() { Constants.FLATBUFFERS_22_11_23(); }
  public static Monster getRootAsMonster(ByteBuffer _bb) { return getRootAsMonster(_bb, new Monster()); }
  public static Monster getRootAsMonster(ByteBuffer _bb, Monster obj) { _bb.order(ByteOrder.LITTLE_ENDIAN); return (obj.__assign(_bb.getInt(_bb.position()) + _bb.position(), _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __reset(_i, _bb); }
  public Monster __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }


  public static void startMonster(FlatBufferBuilder builder) { builder.startTable(0); }
  public static int endMonster(FlatBufferBuilder builder) {
    int o = builder.endTable();
    return o;
  }

  public static final class Vector extends BaseVector {
    public Vector __assign(int _vector, int _element_size, ByteBuffer _bb) { __reset(_vector, _element_size, _bb); return this; }

    public Monster get(int j) { return get(new Monster(), j); }
    public Monster get(Monster obj, int j) {  return obj.__assign(__indirect(__element(j), bb), bb); }
  }
  public MonsterT unpack() {
    MonsterT _o = new MonsterT();
    unpackTo(_o);
    return _o;
  }
  public void unpackTo(MonsterT _o) {
  }
  public static int pack(FlatBufferBuilder builder, MonsterT _o) {
    if (_o == null) return 0;
    startMonster(builder);
    return endMonster(builder);
  }
}

