// automatically generated by the FlatBuffers compiler, do not modify

import * as flatbuffers from 'flatbuffers';

import { Abc } from '../foobar/abc.js';
import { class_ } from '../foobar/class.js';


export class Tab implements flatbuffers.IUnpackableObject<TabT> {
  bb: flatbuffers.ByteBuffer|null = null;
  bb_pos = 0;
  __init(i:number, bb:flatbuffers.ByteBuffer):Tab {
  this.bb_pos = i;
  this.bb = bb;
  return this;
}

static getRootAsTab(bb:flatbuffers.ByteBuffer, obj?:Tab):Tab {
  return (obj || new Tab()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
}

static getSizePrefixedRootAsTab(bb:flatbuffers.ByteBuffer, obj?:Tab):Tab {
  bb.setPosition(bb.position() + flatbuffers.SIZE_PREFIX_LENGTH);
  return (obj || new Tab()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
}

abc():Abc {
  const offset = this.bb!.__offset(this.bb_pos, 4);
  return offset ? this.bb!.readInt32(this.bb_pos + offset) : Abc.a;
}

mutate_abc(value:Abc):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 4);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeInt32(this.bb_pos + offset, value);
  return true;
}

arg():class_ {
  const offset = this.bb!.__offset(this.bb_pos, 6);
  return offset ? this.bb!.readInt32(this.bb_pos + offset) : class_.arguments_;
}

mutate_arg(value:class_):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 6);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeInt32(this.bb_pos + offset, value);
  return true;
}

name():string|null
name(optionalEncoding:flatbuffers.Encoding):string|Uint8Array|null
name(optionalEncoding?:any):string|Uint8Array|null {
  const offset = this.bb!.__offset(this.bb_pos, 8);
  return offset ? this.bb!.__string(this.bb_pos + offset, optionalEncoding) : null;
}

static getFullyQualifiedName():string {
  return 'foobar.Tab';
}

static startTab(builder:flatbuffers.Builder) {
  builder.startObject(3);
}

static addAbc(builder:flatbuffers.Builder, abc:Abc) {
  builder.addFieldInt32(0, abc, Abc.a);
}

static addArg(builder:flatbuffers.Builder, arg:class_) {
  builder.addFieldInt32(1, arg, class_.arguments_);
}

static addName(builder:flatbuffers.Builder, nameOffset:flatbuffers.Offset) {
  builder.addFieldOffset(2, nameOffset, 0);
}

static endTab(builder:flatbuffers.Builder):flatbuffers.Offset {
  const offset = builder.endObject();
  return offset;
}

static createTab(builder:flatbuffers.Builder, abc:Abc, arg:class_, nameOffset:flatbuffers.Offset):flatbuffers.Offset {
  Tab.startTab(builder);
  Tab.addAbc(builder, abc);
  Tab.addArg(builder, arg);
  Tab.addName(builder, nameOffset);
  return Tab.endTab(builder);
}

unpack(): TabT {
  return new TabT(
    this.abc(),
    this.arg(),
    this.name()
  );
}


unpackTo(_o: TabT): void {
  _o.abc = this.abc();
  _o.arg = this.arg();
  _o.name = this.name();
}
}

export class TabT implements flatbuffers.IGeneratedObject {
constructor(
  public abc: Abc = Abc.a,
  public arg: class_ = class_.arguments_,
  public name: string|Uint8Array|null = null
){}


pack(builder:flatbuffers.Builder): flatbuffers.Offset {
  const name = (this.name !== null ? builder.createString(this.name!) : 0);

  return Tab.createTab(builder,
    this.abc,
    this.arg,
    name
  );
}
}

// Verification function for 'Tab' table.
export function tabVerify(verifier: flatbuffers.Verifier, tablePos: flatbuffers.UOffset): boolean {
  let result = true;
  result = result && verifier.verifyTableStart(tablePos);
  result = result && verifier.verifyField(tablePos, 4 /*Abc*/, 4 /*Int32*/, 4, false);
  result = result && verifier.verifyField(tablePos, 6 /*Arg*/, 4 /*Int32*/, 4, false);
  result = result && verifier.verifyString(tablePos, 8 /*Name*/, false);
  result = result && verifier.verifyTableEnd(tablePos);
  return result;
}
