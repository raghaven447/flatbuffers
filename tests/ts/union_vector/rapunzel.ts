// automatically generated by the FlatBuffers compiler, do not modify

/* eslint-disable @typescript-eslint/no-unused-vars, @typescript-eslint/no-explicit-any, @typescript-eslint/no-non-null-assertion */

import * as flatbuffers from 'flatbuffers';



export class Rapunzel implements flatbuffers.IUnpackableObject<RapunzelT> {
  bb: flatbuffers.ByteBuffer|null = null;
  bb_pos = 0;
  __init(i:number, bb:flatbuffers.ByteBuffer):Rapunzel {
  this.bb_pos = i;
  this.bb = bb;
  return this;
}

hairLength():number {
  return this.bb!.readInt32(this.bb_pos);
}

mutate_hair_length(value:number):boolean {
  this.bb!.writeInt32(this.bb_pos + 0, value);
  return true;
}

static getFullyQualifiedName():string {
  return 'Rapunzel';
}

static sizeOf():number {
  return 4;
}

static createRapunzel(builder:flatbuffers.Builder, hair_length: number):flatbuffers.Offset {
  builder.prep(4, 4);
  builder.writeInt32(hair_length);
  return builder.offset();
}


unpack(): RapunzelT {
  return new RapunzelT(
    this.hairLength()
  );
}


unpackTo(_o: RapunzelT): void {
  _o.hairLength = this.hairLength();
}
}

export class RapunzelT implements flatbuffers.IGeneratedObject {
constructor(
  public hairLength: number = 0
){}


pack(builder:flatbuffers.Builder): flatbuffers.Offset {
  return Rapunzel.createRapunzel(builder,
    this.hairLength
  );
}
}
