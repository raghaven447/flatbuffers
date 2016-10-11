// automatically generated by the FlatBuffers compiler, do not modify

package Testing.KeySearch;

import java.nio.*;
import java.lang.*;
import java.util.*;
import com.google.flatbuffers.*;

@SuppressWarnings("unused")
public final class MasterDict extends Table {
  public static MasterDict getRootAsMasterDict(ByteBuffer _bb) { return getRootAsMasterDict(_bb, new MasterDict()); }
  public static MasterDict getRootAsMasterDict(ByteBuffer _bb, MasterDict obj) { _bb.order(ByteOrder.LITTLE_ENDIAN); return (obj.__assign(_bb.getInt(_bb.position()) + _bb.position(), _bb)); }
  public static boolean MasterDictBufferHasIdentifier(ByteBuffer _bb) { return __has_identifier(_bb, "FBMD"); }
  public void __init(int _i, ByteBuffer _bb) { bb_pos = _i; bb = _bb; }
  public MasterDict __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public UByteEntry ubyteEntries(int j) { return ubyteEntries(new UByteEntry(), j); }
  public UByteEntry ubyteEntries(UByteEntry obj, int j) { int o = __offset(4); return o != 0 ? obj.__assign(__indirect(__vector(o) + j * 4), bb) : null; }
  public int ubyteEntriesLength() { int o = __offset(4); return o != 0 ? __vector_len(o) : 0; }
  public ByteEntry byteEntries(int j) { return byteEntries(new ByteEntry(), j); }
  public ByteEntry byteEntries(ByteEntry obj, int j) { int o = __offset(6); return o != 0 ? obj.__assign(__indirect(__vector(o) + j * 4), bb) : null; }
  public int byteEntriesLength() { int o = __offset(6); return o != 0 ? __vector_len(o) : 0; }
  public ByteEntry bytesEntriesByKey( byte key ) { int vectorOffset = __vector(__offset(6)) - 4; return vectorOffset != 0 ? ByteEntry.lookupByKey(bb.array().length - vectorOffset, key, bb) : null;  }
  public BoolEntry boolEntries(int j) { return boolEntries(new BoolEntry(), j); }
  public BoolEntry boolEntries(BoolEntry obj, int j) { int o = __offset(8); return o != 0 ? obj.__assign(__indirect(__vector(o) + j * 4), bb) : null; }
  public int boolEntriesLength() { int o = __offset(8); return o != 0 ? __vector_len(o) : 0; }
  public BoolEntry boolEntriesByKey( boolean key ) { int vectorOffset = __vector(__offset(8)) - 4; return vectorOffset != 0 ? BoolEntry.lookupByKey(bb.array().length - vectorOffset, key, bb) : null;  }
  public ShortEntry shortEntries(int j) { return shortEntries(new ShortEntry(), j); }
  public ShortEntry shortEntries(ShortEntry obj, int j) { int o = __offset(10); return o != 0 ? obj.__assign(__indirect(__vector(o) + j * 4), bb) : null; }
  public int shortEntriesLength() { int o = __offset(10); return o != 0 ? __vector_len(o) : 0; }
  public ShortEntry shortEntriesByKey( short key ) { int vectorOffset = __vector(__offset(10)) - 4; return vectorOffset != 0 ? ShortEntry.lookupByKey(bb.array().length - vectorOffset, key, bb) : null;  }
  public UShortEntry ushortEntries(int j) { return ushortEntries(new UShortEntry(), j); }
  public UShortEntry ushortEntries(UShortEntry obj, int j) { int o = __offset(12); return o != 0 ? obj.__assign(__indirect(__vector(o) + j * 4), bb) : null; }
  public int ushortEntriesLength() { int o = __offset(12); return o != 0 ? __vector_len(o) : 0; }
  public UShortEntry ushortEntriesByKey( short key ) { int vectorOffset = __vector(__offset(12)) - 4; return vectorOffset != 0 ? UShortEntry.lookupByKey(bb.array().length - vectorOffset, key, bb) : null;  }
  public IntEntry intEntries(int j) { return intEntries(new IntEntry(), j); }
  public IntEntry intEntries(IntEntry obj, int j) { int o = __offset(14); return o != 0 ? obj.__assign(__indirect(__vector(o) + j * 4), bb) : null; }
  public int intEntriesLength() { int o = __offset(14); return o != 0 ? __vector_len(o) : 0; }
  public IntEntry intEntriesByKey( int key ) { int vectorOffset = __vector(__offset(14)) - 4; return vectorOffset != 0 ? IntEntry.lookupByKey(bb.array().length - vectorOffset, key, bb) : null;  }
  public UIntEntry uintEntries(int j) { return uintEntries(new UIntEntry(), j); }
  public UIntEntry uintEntries(UIntEntry obj, int j) { int o = __offset(16); return o != 0 ? obj.__assign(__indirect(__vector(o) + j * 4), bb) : null; }
  public int uintEntriesLength() { int o = __offset(16); return o != 0 ? __vector_len(o) : 0; }
  public UIntEntry uintEntriesByKey( int key ) { int vectorOffset = __vector(__offset(16)) - 4; return vectorOffset != 0 ? UIntEntry.lookupByKey(bb.array().length - vectorOffset, key, bb) : null;  }
  public FloatEntry floatEntries(int j) { return floatEntries(new FloatEntry(), j); }
  public FloatEntry floatEntries(FloatEntry obj, int j) { int o = __offset(18); return o != 0 ? obj.__assign(__indirect(__vector(o) + j * 4), bb) : null; }
  public int floatEntriesLength() { int o = __offset(18); return o != 0 ? __vector_len(o) : 0; }
  public FloatEntry floatEntriesByKey( float key ) { int vectorOffset = __vector(__offset(18)) - 4; return vectorOffset != 0 ? FloatEntry.lookupByKey(bb.array().length - vectorOffset, key, bb) : null;  }
  public LongEntry longEntries(int j) { return longEntries(new LongEntry(), j); }
  public LongEntry longEntries(LongEntry obj, int j) { int o = __offset(20); return o != 0 ? obj.__assign(__indirect(__vector(o) + j * 4), bb) : null; }
  public int longEntriesLength() { int o = __offset(20); return o != 0 ? __vector_len(o) : 0; }
  public LongEntry longEntriesByKey( long key ) { int vectorOffset = __vector(__offset(20)) - 4; return vectorOffset != 0 ? LongEntry.lookupByKey(bb.array().length - vectorOffset, key, bb) : null;  }
  public ULongEntry ulongEntries(int j) { return ulongEntries(new ULongEntry(), j); }
  public ULongEntry ulongEntries(ULongEntry obj, int j) { int o = __offset(22); return o != 0 ? obj.__assign(__indirect(__vector(o) + j * 4), bb) : null; }
  public int ulongEntriesLength() { int o = __offset(22); return o != 0 ? __vector_len(o) : 0; }
  public ULongEntry ulongEntriesByKey( long key ) { int vectorOffset = __vector(__offset(22)) - 4; return vectorOffset != 0 ? ULongEntry.lookupByKey(bb.array().length - vectorOffset, key, bb) : null;  }
  public DoubleEntry doubleEntries(int j) { return doubleEntries(new DoubleEntry(), j); }
  public DoubleEntry doubleEntries(DoubleEntry obj, int j) { int o = __offset(24); return o != 0 ? obj.__assign(__indirect(__vector(o) + j * 4), bb) : null; }
  public int doubleEntriesLength() { int o = __offset(24); return o != 0 ? __vector_len(o) : 0; }
  public DoubleEntry doubleEntriesByKey( double key ) { int vectorOffset = __vector(__offset(24)) - 4; return vectorOffset != 0 ? DoubleEntry.lookupByKey(bb.array().length - vectorOffset, key, bb) : null;  }
  public StringEntry stringEntries(int j) { return stringEntries(new StringEntry(), j); }
  public StringEntry stringEntries(StringEntry obj, int j) { int o = __offset(26); return o != 0 ? obj.__assign(__indirect(__vector(o) + j * 4), bb) : null; }
  public int stringEntriesLength() { int o = __offset(26); return o != 0 ? __vector_len(o) : 0; }
  public StringEntry stringEntriesByKey( String key ) { int vectorOffset = __vector(__offset(26)) - 4; return vectorOffset != 0 ? StringEntry.lookupByKey(bb.array().length - vectorOffset, key, bb) : null;  }

  public static int createMasterDict(FlatBufferBuilder builder,
      int ubyteEntriesOffset,
      int byteEntriesOffset,
      int boolEntriesOffset,
      int shortEntriesOffset,
      int ushortEntriesOffset,
      int intEntriesOffset,
      int uintEntriesOffset,
      int floatEntriesOffset,
      int longEntriesOffset,
      int ulongEntriesOffset,
      int doubleEntriesOffset,
      int stringEntriesOffset) {
    builder.startObject(12);
    MasterDict.addStringEntries(builder, stringEntriesOffset);
    MasterDict.addDoubleEntries(builder, doubleEntriesOffset);
    MasterDict.addUlongEntries(builder, ulongEntriesOffset);
    MasterDict.addLongEntries(builder, longEntriesOffset);
    MasterDict.addFloatEntries(builder, floatEntriesOffset);
    MasterDict.addUintEntries(builder, uintEntriesOffset);
    MasterDict.addIntEntries(builder, intEntriesOffset);
    MasterDict.addUshortEntries(builder, ushortEntriesOffset);
    MasterDict.addShortEntries(builder, shortEntriesOffset);
    MasterDict.addBoolEntries(builder, boolEntriesOffset);
    MasterDict.addByteEntries(builder, byteEntriesOffset);
    MasterDict.addUbyteEntries(builder, ubyteEntriesOffset);
    return MasterDict.endMasterDict(builder);
  }

  public static void startMasterDict(FlatBufferBuilder builder) { builder.startObject(12); }
  public static void addUbyteEntries(FlatBufferBuilder builder, int ubyteEntriesOffset) { builder.addOffset(0, ubyteEntriesOffset, 0); }
  public static int createUbyteEntriesVector(FlatBufferBuilder builder, int[] data) { builder.startVector(4, data.length, 4); for (int i = data.length - 1; i >= 0; i--) builder.addOffset(data[i]); return builder.endVector(); }
  public static void startUbyteEntriesVector(FlatBufferBuilder builder, int numElems) { builder.startVector(4, numElems, 4); }
  public static void addByteEntries(FlatBufferBuilder builder, int byteEntriesOffset) { builder.addOffset(1, byteEntriesOffset, 0); }
  public static int createByteEntriesVector(FlatBufferBuilder builder, int[] data) { builder.startVector(4, data.length, 4); for (int i = data.length - 1; i >= 0; i--) builder.addOffset(data[i]); return builder.endVector(); }
  public static void startByteEntriesVector(FlatBufferBuilder builder, int numElems) { builder.startVector(4, numElems, 4); }
  public static void addBoolEntries(FlatBufferBuilder builder, int boolEntriesOffset) { builder.addOffset(2, boolEntriesOffset, 0); }
  public static int createBoolEntriesVector(FlatBufferBuilder builder, int[] data) { builder.startVector(4, data.length, 4); for (int i = data.length - 1; i >= 0; i--) builder.addOffset(data[i]); return builder.endVector(); }
  public static void startBoolEntriesVector(FlatBufferBuilder builder, int numElems) { builder.startVector(4, numElems, 4); }
  public static void addShortEntries(FlatBufferBuilder builder, int shortEntriesOffset) { builder.addOffset(3, shortEntriesOffset, 0); }
  public static int createShortEntriesVector(FlatBufferBuilder builder, int[] data) { builder.startVector(4, data.length, 4); for (int i = data.length - 1; i >= 0; i--) builder.addOffset(data[i]); return builder.endVector(); }
  public static void startShortEntriesVector(FlatBufferBuilder builder, int numElems) { builder.startVector(4, numElems, 4); }
  public static void addUshortEntries(FlatBufferBuilder builder, int ushortEntriesOffset) { builder.addOffset(4, ushortEntriesOffset, 0); }
  public static int createUshortEntriesVector(FlatBufferBuilder builder, int[] data) { builder.startVector(4, data.length, 4); for (int i = data.length - 1; i >= 0; i--) builder.addOffset(data[i]); return builder.endVector(); }
  public static void startUshortEntriesVector(FlatBufferBuilder builder, int numElems) { builder.startVector(4, numElems, 4); }
  public static void addIntEntries(FlatBufferBuilder builder, int intEntriesOffset) { builder.addOffset(5, intEntriesOffset, 0); }
  public static int createIntEntriesVector(FlatBufferBuilder builder, int[] data) { builder.startVector(4, data.length, 4); for (int i = data.length - 1; i >= 0; i--) builder.addOffset(data[i]); return builder.endVector(); }
  public static void startIntEntriesVector(FlatBufferBuilder builder, int numElems) { builder.startVector(4, numElems, 4); }
  public static void addUintEntries(FlatBufferBuilder builder, int uintEntriesOffset) { builder.addOffset(6, uintEntriesOffset, 0); }
  public static int createUintEntriesVector(FlatBufferBuilder builder, int[] data) { builder.startVector(4, data.length, 4); for (int i = data.length - 1; i >= 0; i--) builder.addOffset(data[i]); return builder.endVector(); }
  public static void startUintEntriesVector(FlatBufferBuilder builder, int numElems) { builder.startVector(4, numElems, 4); }
  public static void addFloatEntries(FlatBufferBuilder builder, int floatEntriesOffset) { builder.addOffset(7, floatEntriesOffset, 0); }
  public static int createFloatEntriesVector(FlatBufferBuilder builder, int[] data) { builder.startVector(4, data.length, 4); for (int i = data.length - 1; i >= 0; i--) builder.addOffset(data[i]); return builder.endVector(); }
  public static void startFloatEntriesVector(FlatBufferBuilder builder, int numElems) { builder.startVector(4, numElems, 4); }
  public static void addLongEntries(FlatBufferBuilder builder, int longEntriesOffset) { builder.addOffset(8, longEntriesOffset, 0); }
  public static int createLongEntriesVector(FlatBufferBuilder builder, int[] data) { builder.startVector(4, data.length, 4); for (int i = data.length - 1; i >= 0; i--) builder.addOffset(data[i]); return builder.endVector(); }
  public static void startLongEntriesVector(FlatBufferBuilder builder, int numElems) { builder.startVector(4, numElems, 4); }
  public static void addUlongEntries(FlatBufferBuilder builder, int ulongEntriesOffset) { builder.addOffset(9, ulongEntriesOffset, 0); }
  public static int createUlongEntriesVector(FlatBufferBuilder builder, int[] data) { builder.startVector(4, data.length, 4); for (int i = data.length - 1; i >= 0; i--) builder.addOffset(data[i]); return builder.endVector(); }
  public static void startUlongEntriesVector(FlatBufferBuilder builder, int numElems) { builder.startVector(4, numElems, 4); }
  public static void addDoubleEntries(FlatBufferBuilder builder, int doubleEntriesOffset) { builder.addOffset(10, doubleEntriesOffset, 0); }
  public static int createDoubleEntriesVector(FlatBufferBuilder builder, int[] data) { builder.startVector(4, data.length, 4); for (int i = data.length - 1; i >= 0; i--) builder.addOffset(data[i]); return builder.endVector(); }
  public static void startDoubleEntriesVector(FlatBufferBuilder builder, int numElems) { builder.startVector(4, numElems, 4); }
  public static void addStringEntries(FlatBufferBuilder builder, int stringEntriesOffset) { builder.addOffset(11, stringEntriesOffset, 0); }
  public static int createStringEntriesVector(FlatBufferBuilder builder, int[] data) { builder.startVector(4, data.length, 4); for (int i = data.length - 1; i >= 0; i--) builder.addOffset(data[i]); return builder.endVector(); }
  public static void startStringEntriesVector(FlatBufferBuilder builder, int numElems) { builder.startVector(4, numElems, 4); }
  public static int endMasterDict(FlatBufferBuilder builder) {
    int o = builder.endObject();
    return o;
  }
  public static void finishMasterDictBuffer(FlatBufferBuilder builder, int offset) { builder.finish(offset, "FBMD"); }
}

