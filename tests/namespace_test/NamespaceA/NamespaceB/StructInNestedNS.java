// automatically generated by the FlatBuffers compiler, do not modify

package NamespaceA.NamespaceB;

import java.nio.*;
import java.lang.*;
import java.util.*;
import com.google.flatbuffers.*;

@SuppressWarnings("unused")
public final class StructInNestedNS extends Struct {
  public void __init(int _i, ByteBuffer _bb) { __reset(_i, _bb); }
  public StructInNestedNS __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public int a() { return bb.getInt(bb_pos + 0); }
  public void mutateA(int a) { bb.putInt(bb_pos + 0, a); }
  public int b() { return bb.getInt(bb_pos + 4); }
  public void mutateB(int b) { bb.putInt(bb_pos + 4, b); }

  public static int createStructInNestedNS(FlatBufferBuilder builder, int a, int b) {
    builder.prep(4, 8);
    builder.putInt(b);
    builder.putInt(a);
    return builder.offset();
  }

  public static final class Vector extends BaseVector {
    public Vector __assign(int _vector, int _element_size, ByteBuffer _bb) { __reset(_vector, _element_size, _bb); return this; }

    public StructInNestedNS get(int j) { return get(new StructInNestedNS(), j); }
    public StructInNestedNS get(StructInNestedNS obj, int j) {  return obj.__assign(__element(j), bb); }
  }
  public StructInNestedNST unpack() {
    StructInNestedNST _o = new StructInNestedNST();
    this.unpackTo(_o);
    return _o;
  }
  public void unpackTo(StructInNestedNST _o) {
    int _oA = this.a();
    _o.setA(_oA);
    int _oB = this.b();
    _o.setB(_oB);
  }
  public static int pack(FlatBufferBuilder builder, StructInNestedNST _o) {
    if (_o == null) return 0;
    return createStructInNestedNS(
      builder,
      _o.getA(),
      _o.getB());
  }
}