// automatically generated by the FlatBuffers compiler, do not modify

package NamespaceA;

import java.nio.*;
import java.lang.*;
import java.util.*;
import com.google.flatbuffers.*;

@SuppressWarnings("unused")
public final class TableInFirstNS extends Table {
  public static TableInFirstNS getRootAsTableInFirstNS(ByteBuffer _bb) { return getRootAsTableInFirstNS(_bb, new TableInFirstNS()); }
  public static TableInFirstNS getRootAsTableInFirstNS(ByteBuffer _bb, TableInFirstNS obj) { Constants.FLATBUFFERS_1_11_1(); _bb.order(ByteOrder.LITTLE_ENDIAN); return (obj.__assign(_bb.getInt(_bb.position()) + _bb.position(), _bb)); }
  public void __init(int _i, ByteBuffer _bb) { bb_pos = _i; bb = _bb; vtable_start = bb_pos - bb.getInt(bb_pos); vtable_size = bb.getShort(vtable_start); }
  public TableInFirstNS __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public int x() { int o = __offset(4); return o != 0 ? bb.getInt(o + bb_pos) : 0; }
  public boolean mutateX(int x) { int o = __offset(4); if (o != 0) { bb.putInt(o + bb_pos, x); return true; } else { return false; } }
  public NamespaceA.NamespaceB.TableInNestedNS fooTable() { return fooTable(new NamespaceA.NamespaceB.TableInNestedNS()); }
  public NamespaceA.NamespaceB.TableInNestedNS fooTable(NamespaceA.NamespaceB.TableInNestedNS obj) { int o = __offset(6); return o != 0 ? obj.__assign(__indirect(o + bb_pos), bb) : null; }
  public byte fooEnum() { int o = __offset(8); return o != 0 ? bb.get(o + bb_pos) : 0; }
  public boolean mutateFooEnum(byte foo_enum) { int o = __offset(8); if (o != 0) { bb.put(o + bb_pos, foo_enum); return true; } else { return false; } }
  public NamespaceA.NamespaceB.StructInNestedNS fooStruct() { return fooStruct(new NamespaceA.NamespaceB.StructInNestedNS()); }
  public NamespaceA.NamespaceB.StructInNestedNS fooStruct(NamespaceA.NamespaceB.StructInNestedNS obj) { int o = __offset(10); return o != 0 ? obj.__assign(o + bb_pos, bb) : null; }

  public static void startTableInFirstNS(FlatBufferBuilder builder) { builder.startTable(4); }
  public static void addX(FlatBufferBuilder builder, int x) { builder.addInt(0, x, 0); }
  public static void addFooTable(FlatBufferBuilder builder, int fooTableOffset) { builder.addOffset(1, fooTableOffset, 0); }
  public static void addFooEnum(FlatBufferBuilder builder, byte fooEnum) { builder.addByte(2, fooEnum, 0); }
  public static void addFooStruct(FlatBufferBuilder builder, int fooStructOffset) { builder.addStruct(3, fooStructOffset, 0); }
  public static int endTableInFirstNS(FlatBufferBuilder builder) {
    int o = builder.endTable();
    return o;
  }
}

