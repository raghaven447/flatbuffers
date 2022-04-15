// automatically generated by the FlatBuffers compiler, do not modify

package MyGame.Example;

import java.nio.*;
import java.lang.*;
import java.util.*;
import com.google.flatbuffers.*;

@SuppressWarnings("unused")
public final class ArrayStruct extends Struct {
  public void __init(int _i, ByteBuffer _bb) { __reset(_i, _bb); }
  public ArrayStruct __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public float a() { return bb.getFloat(bb_pos + 0); }
  public void mutateA(float a) { bb.putFloat(bb_pos + 0, a); }
  public int b(int j) { return bb.getInt(bb_pos + 4 + j * 4); }
  public void mutateB(int j, int b) { bb.putInt(bb_pos + 4 + j * 4, b); }
  public byte c() { return bb.get(bb_pos + 64); }
  public void mutateC(byte c) { bb.put(bb_pos + 64, c); }
  public MyGame.Example.NestedStruct d(int j) { return d(new MyGame.Example.NestedStruct(), j); }
  public MyGame.Example.NestedStruct d(MyGame.Example.NestedStruct obj, int j) { return obj.__assign(bb_pos + 72 + j * 32, bb); }
  public int e() { return bb.getInt(bb_pos + 136); }
  public void mutateE(int e) { bb.putInt(bb_pos + 136, e); }
  public long f(int j) { return bb.getLong(bb_pos + 144 + j * 8); }
  public void mutateF(int j, long f) { bb.putLong(bb_pos + 144 + j * 8, f); }

  public static int createArrayStruct(FlatBufferBuilder builder, float a, int[] b, byte c, int[][] d_a, byte[] d_b, byte[][] d_c, long[][] d_d, int e, long[] f) {
    builder.prep(8, 160);
    for (int _idx0 = 2; _idx0 > 0; _idx0--) {
      builder.putLong(f[_idx0-1]);
    }
    builder.pad(4);
    builder.putInt(e);
    for (int _idx0 = 2; _idx0 > 0; _idx0--) {
      builder.prep(8, 32);
      for (int _idx1 = 2; _idx1 > 0; _idx1--) {
        builder.putLong(d_d[_idx0-1][_idx1-1]);
      }
      builder.pad(5);
      for (int _idx1 = 2; _idx1 > 0; _idx1--) {
        builder.putByte(d_c[_idx0-1][_idx1-1]);
      }
      builder.putByte(d_b[_idx0-1]);
      for (int _idx1 = 2; _idx1 > 0; _idx1--) {
        builder.putInt(d_a[_idx0-1][_idx1-1]);
      }
    }
    builder.pad(7);
    builder.putByte(c);
    for (int _idx0 = 15; _idx0 > 0; _idx0--) {
      builder.putInt(b[_idx0-1]);
    }
    builder.putFloat(a);
    return builder.offset();
  }

  public static final class Vector extends BaseVector {
    public Vector __assign(int _vector, int _element_size, ByteBuffer _bb) { __reset(_vector, _element_size, _bb); return this; }

    public ArrayStruct get(int j) { return get(new ArrayStruct(), j); }
    public ArrayStruct get(ArrayStruct obj, int j) {  return obj.__assign(__element(j), bb); }
  }
  public ArrayStructT unpack() {
    ArrayStructT _o = new ArrayStructT();
    unpackTo(_o);
    return _o;
  }
  public void unpackTo(ArrayStructT _o) {
    float _o_a = a();
    _o.setA(_o_a);
    int[] _o_b = _o.getB();
    for (int _j = 0; _j < 15; ++_j) { _o_b[_j] = b(_j); }
    byte _o_c = c();
    _o.setC(_o_c);
    MyGame.Example.NestedStructT[] _o_d = _o.getD();
    for (int _j = 0; _j < 2; ++_j) { _o_d[_j] = d(_j).unpack(); }
    int _o_e = e();
    _o.setE(_o_e);
    long[] _o_f = _o.getF();
    for (int _j = 0; _j < 2; ++_j) { _o_f[_j] = f(_j); }
  }
  public static int pack(FlatBufferBuilder builder, ArrayStructT _o) {
    if (_o == null) return 0;
    int[] _b = _o.getB();
    int[][] _d_a = new int[2][2];
    for (int idx0 = 0; idx0 < 2; ++idx0) {for (int idx1 = 0; idx1 < 2; ++idx1) {_d_a[idx0][idx1] = _o.getD()[idx0].getA()[idx1];}}
    byte[] _d_b = new byte[2];
    for (int idx0 = 0; idx0 < 2; ++idx0) {_d_b[idx0] = _o.getD()[idx0].getB();}
    byte[][] _d_c = new byte[2][2];
    for (int idx0 = 0; idx0 < 2; ++idx0) {for (int idx1 = 0; idx1 < 2; ++idx1) {_d_c[idx0][idx1] = _o.getD()[idx0].getC()[idx1];}}
    long[][] _d_d = new long[2][2];
    for (int idx0 = 0; idx0 < 2; ++idx0) {for (int idx1 = 0; idx1 < 2; ++idx1) {_d_d[idx0][idx1] = _o.getD()[idx0].getD()[idx1];}}
    long[] _f = _o.getF();
    return createArrayStruct(
      builder,
      _o.getA(),
      _b,
      _o.getC(),
      _d_a,
      _d_b,
      _d_c,
      _d_d,
      _o.getE(),
      _f);
  }
}

