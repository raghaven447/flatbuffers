// automatically generated by the FlatBuffers compiler, do not modify

import * as flatbuffers from 'flatbuffers';

import { KeyValue, KeyValueT } from '../reflection/key-value';
import { Type, TypeT } from '../reflection/type';


export class Field {
  bb: flatbuffers.ByteBuffer|null = null;
  bb_pos = 0;
__init(i:number, bb:flatbuffers.ByteBuffer):Field {
  this.bb_pos = i;
  this.bb = bb;
  return this;
}

static getRootAsField(bb:flatbuffers.ByteBuffer, obj?:Field):Field {
  return (obj || new Field()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
}

static getSizePrefixedRootAsField(bb:flatbuffers.ByteBuffer, obj?:Field):Field {
  bb.setPosition(bb.position() + flatbuffers.SIZE_PREFIX_LENGTH);
  return (obj || new Field()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
}

name():string|null
name(optionalEncoding:flatbuffers.Encoding):string|Uint8Array|null
name(optionalEncoding?:any):string|Uint8Array|null {
  const offset = this.bb!.__offset(this.bb_pos, 4);
  return offset ? this.bb!.__string(this.bb_pos + offset, optionalEncoding) : null;
}

type(obj?:Type):Type|null {
  const offset = this.bb!.__offset(this.bb_pos, 6);
  return offset ? (obj || new Type()).__init(this.bb!.__indirect(this.bb_pos + offset), this.bb!) : null;
}

id():number {
  const offset = this.bb!.__offset(this.bb_pos, 8);
  return offset ? this.bb!.readUint16(this.bb_pos + offset) : 0;
}

mutate_id(value:number):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 8);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeUint16(this.bb_pos + offset, value);
  return true;
}

offset():number {
  const offset = this.bb!.__offset(this.bb_pos, 10);
  return offset ? this.bb!.readUint16(this.bb_pos + offset) : 0;
}

mutate_offset(value:number):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 10);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeUint16(this.bb_pos + offset, value);
  return true;
}

defaultInteger():bigint {
  const offset = this.bb!.__offset(this.bb_pos, 12);
  return offset ? this.bb!.readInt64(this.bb_pos + offset) : BigInt('0');
}

mutate_default_integer(value:bigint):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 12);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeInt64(this.bb_pos + offset, value);
  return true;
}

defaultReal():number {
  const offset = this.bb!.__offset(this.bb_pos, 14);
  return offset ? this.bb!.readFloat64(this.bb_pos + offset) : 0.0;
}

mutate_default_real(value:number):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 14);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeFloat64(this.bb_pos + offset, value);
  return true;
}

deprecated():boolean {
  const offset = this.bb!.__offset(this.bb_pos, 16);
  return offset ? !!this.bb!.readInt8(this.bb_pos + offset) : false;
}

mutate_deprecated(value:boolean):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 16);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeInt8(this.bb_pos + offset, +value);
  return true;
}

required():boolean {
  const offset = this.bb!.__offset(this.bb_pos, 18);
  return offset ? !!this.bb!.readInt8(this.bb_pos + offset) : false;
}

mutate_required(value:boolean):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 18);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeInt8(this.bb_pos + offset, +value);
  return true;
}

key():boolean {
  const offset = this.bb!.__offset(this.bb_pos, 20);
  return offset ? !!this.bb!.readInt8(this.bb_pos + offset) : false;
}

mutate_key(value:boolean):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 20);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeInt8(this.bb_pos + offset, +value);
  return true;
}

attributes(index: number, obj?:KeyValue):KeyValue|null {
  const offset = this.bb!.__offset(this.bb_pos, 22);
  return offset ? (obj || new KeyValue()).__init(this.bb!.__indirect(this.bb!.__vector(this.bb_pos + offset) + index * 4), this.bb!) : null;
}

attributesLength():number {
  const offset = this.bb!.__offset(this.bb_pos, 22);
  return offset ? this.bb!.__vector_len(this.bb_pos + offset) : 0;
}

documentation(index: number):string
documentation(index: number,optionalEncoding:flatbuffers.Encoding):string|Uint8Array
documentation(index: number,optionalEncoding?:any):string|Uint8Array|null {
  const offset = this.bb!.__offset(this.bb_pos, 24);
  return offset ? this.bb!.__string(this.bb!.__vector(this.bb_pos + offset) + index * 4, optionalEncoding) : null;
}

documentationLength():number {
  const offset = this.bb!.__offset(this.bb_pos, 24);
  return offset ? this.bb!.__vector_len(this.bb_pos + offset) : 0;
}

optional():boolean {
  const offset = this.bb!.__offset(this.bb_pos, 26);
  return offset ? !!this.bb!.readInt8(this.bb_pos + offset) : false;
}

mutate_optional(value:boolean):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 26);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeInt8(this.bb_pos + offset, +value);
  return true;
}

/**
 * Number of padding octets to always add after this field. Structs only.
 */
padding():number {
  const offset = this.bb!.__offset(this.bb_pos, 28);
  return offset ? this.bb!.readUint16(this.bb_pos + offset) : 0;
}

mutate_padding(value:number):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 28);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeUint16(this.bb_pos + offset, value);
  return true;
}

static getFullyQualifiedName():string {
  return 'reflection.Field';
}

static startField(builder:flatbuffers.Builder) {
  builder.startObject(13);
}

static addName(builder:flatbuffers.Builder, nameOffset:flatbuffers.Offset) {
  builder.addFieldOffset(0, nameOffset, 0);
}

static addType(builder:flatbuffers.Builder, typeOffset:flatbuffers.Offset) {
  builder.addFieldOffset(1, typeOffset, 0);
}

static addId(builder:flatbuffers.Builder, id:number) {
  builder.addFieldInt16(2, id, 0);
}

static addOffset(builder:flatbuffers.Builder, offset:number) {
  builder.addFieldInt16(3, offset, 0);
}

static addDefaultInteger(builder:flatbuffers.Builder, defaultInteger:bigint) {
  builder.addFieldInt64(4, defaultInteger, BigInt('0'));
}

static addDefaultReal(builder:flatbuffers.Builder, defaultReal:number) {
  builder.addFieldFloat64(5, defaultReal, 0.0);
}

static addDeprecated(builder:flatbuffers.Builder, deprecated:boolean) {
  builder.addFieldInt8(6, +deprecated, +false);
}

static addRequired(builder:flatbuffers.Builder, required:boolean) {
  builder.addFieldInt8(7, +required, +false);
}

static addKey(builder:flatbuffers.Builder, key:boolean) {
  builder.addFieldInt8(8, +key, +false);
}

static addAttributes(builder:flatbuffers.Builder, attributesOffset:flatbuffers.Offset) {
  builder.addFieldOffset(9, attributesOffset, 0);
}

static createAttributesVector(builder:flatbuffers.Builder, data:flatbuffers.Offset[]):flatbuffers.Offset {
  builder.startVector(4, data.length, 4);
  for (let i = data.length - 1; i >= 0; i--) {
    builder.addOffset(data[i]!);
  }
  return builder.endVector();
}

static startAttributesVector(builder:flatbuffers.Builder, numElems:number) {
  builder.startVector(4, numElems, 4);
}

static addDocumentation(builder:flatbuffers.Builder, documentationOffset:flatbuffers.Offset) {
  builder.addFieldOffset(10, documentationOffset, 0);
}

static createDocumentationVector(builder:flatbuffers.Builder, data:flatbuffers.Offset[]):flatbuffers.Offset {
  builder.startVector(4, data.length, 4);
  for (let i = data.length - 1; i >= 0; i--) {
    builder.addOffset(data[i]!);
  }
  return builder.endVector();
}

static startDocumentationVector(builder:flatbuffers.Builder, numElems:number) {
  builder.startVector(4, numElems, 4);
}

static addOptional(builder:flatbuffers.Builder, optional:boolean) {
  builder.addFieldInt8(11, +optional, +false);
}

static addPadding(builder:flatbuffers.Builder, padding:number) {
  builder.addFieldInt16(12, padding, 0);
}

static endField(builder:flatbuffers.Builder):flatbuffers.Offset {
  const offset = builder.endObject();
  builder.requiredField(offset, 4) // name
  builder.requiredField(offset, 6) // type
  return offset;
}


unpack(): FieldT {
  return new FieldT(
    this.name(),
    (this.type() !== null ? this.type()!.unpack() : null),
    this.id(),
    this.offset(),
    this.defaultInteger(),
    this.defaultReal(),
    this.deprecated(),
    this.required(),
    this.key(),
    this.bb!.createObjList(this.attributes.bind(this), this.attributesLength()),
    this.bb!.createScalarList(this.documentation.bind(this), this.documentationLength()),
    this.optional(),
    this.padding()
  );
}


unpackTo(_o: FieldT): void {
  _o.name = this.name();
  _o.type = (this.type() !== null ? this.type()!.unpack() : null);
  _o.id = this.id();
  _o.offset = this.offset();
  _o.defaultInteger = this.defaultInteger();
  _o.defaultReal = this.defaultReal();
  _o.deprecated = this.deprecated();
  _o.required = this.required();
  _o.key = this.key();
  _o.attributes = this.bb!.createObjList(this.attributes.bind(this), this.attributesLength());
  _o.documentation = this.bb!.createScalarList(this.documentation.bind(this), this.documentationLength());
  _o.optional = this.optional();
  _o.padding = this.padding();
}
}

export class FieldT {
constructor(
  public name: string|Uint8Array|null = null,
  public type: TypeT|null = null,
  public id: number = 0,
  public offset: number = 0,
  public defaultInteger: bigint = BigInt('0'),
  public defaultReal: number = 0.0,
  public deprecated: boolean = false,
  public required: boolean = false,
  public key: boolean = false,
  public attributes: (KeyValueT)[] = [],
  public documentation: (string)[] = [],
  public optional: boolean = false,
  public padding: number = 0
){}


pack(builder:flatbuffers.Builder): flatbuffers.Offset {
  const name = (this.name !== null ? builder.createString(this.name!) : 0);
  const type = (this.type !== null ? this.type!.pack(builder) : 0);
  const attributes = Field.createAttributesVector(builder, builder.createObjectOffsetList(this.attributes));
  const documentation = Field.createDocumentationVector(builder, builder.createObjectOffsetList(this.documentation));

  Field.startField(builder);
  Field.addName(builder, name);
  Field.addType(builder, type);
  Field.addId(builder, this.id);
  Field.addOffset(builder, this.offset);
  Field.addDefaultInteger(builder, this.defaultInteger);
  Field.addDefaultReal(builder, this.defaultReal);
  Field.addDeprecated(builder, this.deprecated);
  Field.addRequired(builder, this.required);
  Field.addKey(builder, this.key);
  Field.addAttributes(builder, attributes);
  Field.addDocumentation(builder, documentation);
  Field.addOptional(builder, this.optional);
  Field.addPadding(builder, this.padding);

  return Field.endField(builder);
}
}
