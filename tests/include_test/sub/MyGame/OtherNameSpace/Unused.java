// automatically generated by the FlatBuffers compiler, do not modify

package MyGame.OtherNameSpace;

import java.nio.*;
import java.lang.*;
import java.util.*;
import com.google.flatbuffers.*;

@SuppressWarnings("unused")
public final class Unused extends Struct {
  public void __init(int _i, ByteBuffer _bb) { __reset(_i, _bb); }
  public Unused __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public int a() { return bb.getInt(bb_pos + 0); }
  public void mutateA(int a) { bb.putInt(bb_pos + 0, a); }

  public static int createUnused(FlatBufferBuilder builder, int a) {
    builder.prep(4, 4);
    builder.putInt(a);
    return builder.offset();
  }

  public static final class Vector extends BaseVector {
    public Vector __assign(int _vector, int _element_size, ByteBuffer _bb) { __reset(_vector, _element_size, _bb); return this; }

    public Unused get(int j) { return get(new Unused(), j); }
    public Unused get(Unused obj, int j) {  return obj.__assign(__element(j), bb); }
  }
}

