// automatically generated by the FlatBuffers compiler, do not modify

package MyGame.Example;

import java.nio.*;
import java.lang.*;
import java.util.*;
import com.google.flatbuffers.*;

@SuppressWarnings("unused")
public final class ArrayTable extends Table {
  public static void ValidateVersion() { Constants.FLATBUFFERS_1_12_0(); }
  public static ArrayTable getRootAsArrayTable(ByteBuffer _bb) { return getRootAsArrayTable(_bb, new ArrayTable()); }
  public static ArrayTable getRootAsArrayTable(ByteBuffer _bb, ArrayTable obj) { _bb.order(ByteOrder.LITTLE_ENDIAN); return (obj.__assign(_bb.getInt(_bb.position()) + _bb.position(), _bb)); }
  public static boolean ArrayTableBufferHasIdentifier(ByteBuffer _bb) { return __has_identifier(_bb, "ARRT"); }
  public void __init(int _i, ByteBuffer _bb) { __reset(_i, _bb); }
  public ArrayTable __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public MyGame.Example.ArrayStruct a() { return a(new MyGame.Example.ArrayStruct()); }
  public MyGame.Example.ArrayStruct a(MyGame.Example.ArrayStruct obj) { int o = __offset(4); return o != 0 ? obj.__assign(o + bb_pos, bb) : null; }

  public static void startArrayTable(FlatBufferBuilder builder) { builder.startTable(1); }
  public static void addA(FlatBufferBuilder builder, int aOffset) { builder.addStruct(0, aOffset, 0); }
  public static int endArrayTable(FlatBufferBuilder builder) {
    int o = builder.endTable();
    return o;
  }
  public static void finishArrayTableBuffer(FlatBufferBuilder builder, int offset) { builder.finish(offset, "ARRT"); }
  public static void finishSizePrefixedArrayTableBuffer(FlatBufferBuilder builder, int offset) { builder.finishSizePrefixed(offset, "ARRT"); }

  public static final class Vector extends BaseVector {
    public Vector __assign(int _vector, int _element_size, ByteBuffer _bb) { __reset(_vector, _element_size, _bb); return this; }

    public ArrayTable get(int j) { return get(new ArrayTable(), j); }
    public ArrayTable get(ArrayTable obj, int j) {  return obj.__assign(__indirect(__element(j), bb), bb); }
  }
  public ArrayTableT unpack() {
    ArrayTableT _o = new ArrayTableT();
    this.unpackTo(_o);
    return _o;
  }
  public void unpackTo(ArrayTableT _o) {
    MyGame.Example.ArrayStructT _oA = this.a() != null ? this.a().unpack() : null;
    _o.setA(_oA);
  }
  public static int pack(FlatBufferBuilder builder, ArrayTableT _o) {
    if (_o == null) return 0;
    startArrayTable(builder);
    addA(builder, MyGame.Example.ArrayStruct.pack(builder, _o.getA()));
    return endArrayTable(builder);
  }
}