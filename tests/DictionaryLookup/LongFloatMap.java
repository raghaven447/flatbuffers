// automatically generated by the FlatBuffers compiler, do not modify

package DictionaryLookup;

import java.nio.*;
import java.lang.*;
import java.util.*;
import com.google.flatbuffers.*;

@SuppressWarnings("unused")
public final class LongFloatMap extends Table {
  public static void ValidateVersion() { Constants.FLATBUFFERS_22_9_24(); }
  public static LongFloatMap getRootAsLongFloatMap(ByteBuffer _bb) { return getRootAsLongFloatMap(_bb, new LongFloatMap()); }
  public static LongFloatMap getRootAsLongFloatMap(ByteBuffer _bb, LongFloatMap obj) { _bb.order(ByteOrder.LITTLE_ENDIAN); return (obj.__assign(_bb.getInt(_bb.position()) + _bb.position(), _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __reset(_i, _bb); }
  public LongFloatMap __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public DictionaryLookup.LongFloatEntry entries(int j) { return entries(new DictionaryLookup.LongFloatEntry(), j); }
  public DictionaryLookup.LongFloatEntry entries(DictionaryLookup.LongFloatEntry obj, int j) { int o = __offset(4); return o != 0 ? obj.__assign(__indirect(__vector(o) + j * 4), bb) : null; }
  public int entriesLength() { int o = __offset(4); return o != 0 ? __vector_len(o) : 0; }
  public DictionaryLookup.LongFloatEntry entriesByKey(long key) { int o = __offset(4); return o != 0 ? DictionaryLookup.LongFloatEntry.__lookup_by_key(null, __vector(o), key, bb) : null; }
  public DictionaryLookup.LongFloatEntry entriesByKey(DictionaryLookup.LongFloatEntry obj, long key) { int o = __offset(4); return o != 0 ? DictionaryLookup.LongFloatEntry.__lookup_by_key(obj, __vector(o), key, bb) : null; }
  public DictionaryLookup.LongFloatEntry.Vector entriesVector() { return entriesVector(new DictionaryLookup.LongFloatEntry.Vector()); }
  public DictionaryLookup.LongFloatEntry.Vector entriesVector(DictionaryLookup.LongFloatEntry.Vector obj) { int o = __offset(4); return o != 0 ? obj.__assign(__vector(o), 4, bb) : null; }

  public static int createLongFloatMap(FlatBufferBuilder builder,
      int entriesOffset) {
    builder.startTable(1);
    LongFloatMap.addEntries(builder, entriesOffset);
    return LongFloatMap.endLongFloatMap(builder);
  }

  public static void startLongFloatMap(FlatBufferBuilder builder) { builder.startTable(1); }
  public static void addEntries(FlatBufferBuilder builder, int entriesOffset) { builder.addOffset(0, entriesOffset, 0); }
  public static int createEntriesVector(FlatBufferBuilder builder, int[] data) { builder.startVector(4, data.length, 4); for (int i = data.length - 1; i >= 0; i--) builder.addOffset(data[i]); return builder.endVector(); }
  public static void startEntriesVector(FlatBufferBuilder builder, int numElems) { builder.startVector(4, numElems, 4); }
  public static int endLongFloatMap(FlatBufferBuilder builder) {
    int o = builder.endTable();
    return o;
  }
  public static void finishLongFloatMapBuffer(FlatBufferBuilder builder, int offset) { builder.finish(offset); }
  public static void finishSizePrefixedLongFloatMapBuffer(FlatBufferBuilder builder, int offset) { builder.finishSizePrefixed(offset); }

  public static final class Vector extends BaseVector {
    public Vector __assign(int _vector, int _element_size, ByteBuffer _bb) { __reset(_vector, _element_size, _bb); return this; }

    public LongFloatMap get(int j) { return get(new LongFloatMap(), j); }
    public LongFloatMap get(LongFloatMap obj, int j) {  return obj.__assign(__indirect(__element(j), bb), bb); }
  }
}

