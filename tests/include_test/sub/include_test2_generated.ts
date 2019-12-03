// automatically generated by the FlatBuffers compiler, do not modify

import * as NS16326118448017516856 from "./include_test1_generated";
/**
 * @enum {number}
 */
export namespace MyGame.OtherNameSpace{
export enum FromInclude{
  IncludeVal= 0
}};

/**
 * @constructor
 */
export namespace MyGame.OtherNameSpace{
export class Unused {
  bb: flatbuffers.ByteBuffer|null = null;

  bb_pos:number = 0;
/**
 * @param number i
 * @param flatbuffers.ByteBuffer bb
 * @returns Unused
 */
__init(i:number, bb:flatbuffers.ByteBuffer):Unused {
  this.bb_pos = i;
  this.bb = bb;
  return this;
};

/**
 * @returns number
 */
a():number {
  return this.bb!.readInt32(this.bb_pos);
};

/**
 * @param number value
 * @returns boolean
 */
mutate_a(value:number):boolean {
  var offset = this.bb!.__offset(this.bb_pos, 0);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeInt32(this.bb_pos + offset, value);
  return true;
};

/**
 * @param flatbuffers.Builder builder
 * @param number a
 * @returns flatbuffers.Offset
 */
static createUnused(builder:flatbuffers.Builder, a: number):flatbuffers.Offset {
  builder.prep(4, 4);
  builder.writeInt32(a);
  return builder.offset();
};

}
}
/**
 * @constructor
 */
export namespace MyGame.OtherNameSpace{
export class TableB {
  bb: flatbuffers.ByteBuffer|null = null;

  bb_pos:number = 0;
/**
 * @param number i
 * @param flatbuffers.ByteBuffer bb
 * @returns TableB
 */
__init(i:number, bb:flatbuffers.ByteBuffer):TableB {
  this.bb_pos = i;
  this.bb = bb;
  return this;
};

/**
 * @param flatbuffers.ByteBuffer bb
 * @param TableB= obj
 * @returns TableB
 */
static getRootAsTableB(bb:flatbuffers.ByteBuffer, obj?:TableB):TableB {
  return (obj || new TableB).__init(bb.readInt32(bb.position()) + bb.position(), bb);
};

/**
 * @param flatbuffers.ByteBuffer bb
 * @param TableB= obj
 * @returns TableB
 */
static getSizePrefixedRootAsTableB(bb:flatbuffers.ByteBuffer, obj?:TableB):TableB {
  return (obj || new TableB).__init(bb.readInt32(bb.position()) + bb.position(), bb);
};

/**
 * @param TableA= obj
 * @returns TableA|null
 */
a(obj?:NS16326118448017516856.TableA):NS16326118448017516856.TableA|null {
  var offset = this.bb!.__offset(this.bb_pos, 4);
  return offset ? (obj || new NS16326118448017516856.TableA).__init(this.bb!.__indirect(this.bb_pos + offset), this.bb!) : null;
};

/**
 * @param flatbuffers.Builder builder
 */
static startTableB(builder:flatbuffers.Builder) {
  builder.startObject(1);
};

/**
 * @param flatbuffers.Builder builder
 * @param flatbuffers.Offset aOffset
 */
static addA(builder:flatbuffers.Builder, aOffset:flatbuffers.Offset) {
  builder.addFieldOffset(0, aOffset, 0);
};

/**
 * @param flatbuffers.Builder builder
 * @returns flatbuffers.Offset
 */
static endTableB(builder:flatbuffers.Builder):flatbuffers.Offset {
  var offset = builder.endObject();
  return offset;
};

static createTableB(builder:flatbuffers.Builder, aOffset:flatbuffers.Offset):flatbuffers.Offset {
  TableB.startTableB(builder);
  TableB.addA(builder, aOffset);
  return TableB.endTableB(builder);
}
}
}
