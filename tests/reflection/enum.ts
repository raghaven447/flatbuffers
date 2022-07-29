// automatically generated by the FlatBuffers compiler, do not modify

import * as flatbuffers from 'flatbuffers';

import { EnumVal, EnumValT } from '../reflection/enum-val.js';
import { KeyValue, KeyValueT } from '../reflection/key-value.js';
import { Type, TypeT } from '../reflection/type.js';


export class Enum {
  bb: flatbuffers.ByteBuffer|null = null;
  bb_pos = 0;
__init(i:number, bb:flatbuffers.ByteBuffer):Enum {
  this.bb_pos = i;
  this.bb = bb;
  return this;
}

static getRootAsEnum(bb:flatbuffers.ByteBuffer, obj?:Enum):Enum {
  return (obj || new Enum()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
}

static getSizePrefixedRootAsEnum(bb:flatbuffers.ByteBuffer, obj?:Enum):Enum {
  bb.setPosition(bb.position() + flatbuffers.SIZE_PREFIX_LENGTH);
  return (obj || new Enum()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
}

name():string|null
name(optionalEncoding:flatbuffers.Encoding):string|Uint8Array|null
name(optionalEncoding?:any):string|Uint8Array|null {
  const offset = this.bb!.__offset(this.bb_pos, 4);
  return offset ? this.bb!.__string(this.bb_pos + offset, optionalEncoding) : null;
}

values(index: number, obj?:EnumVal):EnumVal|null {
  const offset = this.bb!.__offset(this.bb_pos, 6);
  return offset ? (obj || new EnumVal()).__init(this.bb!.__indirect(this.bb!.__vector(this.bb_pos + offset) + index * 4), this.bb!) : null;
}

valuesLength():number {
  const offset = this.bb!.__offset(this.bb_pos, 6);
  return offset ? this.bb!.__vector_len(this.bb_pos + offset) : 0;
}

isUnion():boolean {
  const offset = this.bb!.__offset(this.bb_pos, 8);
  return offset ? !!this.bb!.readInt8(this.bb_pos + offset) : false;
}

mutate_is_union(value:boolean):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 8);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeInt8(this.bb_pos + offset, +value);
  return true;
}

underlyingType(obj?:Type):Type|null {
  const offset = this.bb!.__offset(this.bb_pos, 10);
  return offset ? (obj || new Type()).__init(this.bb!.__indirect(this.bb_pos + offset), this.bb!) : null;
}

attributes(index: number, obj?:KeyValue):KeyValue|null {
  const offset = this.bb!.__offset(this.bb_pos, 12);
  return offset ? (obj || new KeyValue()).__init(this.bb!.__indirect(this.bb!.__vector(this.bb_pos + offset) + index * 4), this.bb!) : null;
}

attributesLength():number {
  const offset = this.bb!.__offset(this.bb_pos, 12);
  return offset ? this.bb!.__vector_len(this.bb_pos + offset) : 0;
}

documentation(index: number):string
documentation(index: number,optionalEncoding:flatbuffers.Encoding):string|Uint8Array
documentation(index: number,optionalEncoding?:any):string|Uint8Array|null {
  const offset = this.bb!.__offset(this.bb_pos, 14);
  return offset ? this.bb!.__string(this.bb!.__vector(this.bb_pos + offset) + index * 4, optionalEncoding) : null;
}

documentationLength():number {
  const offset = this.bb!.__offset(this.bb_pos, 14);
  return offset ? this.bb!.__vector_len(this.bb_pos + offset) : 0;
}

/**
 * File that this Enum is declared in.
 */
declarationFile():string|null
declarationFile(optionalEncoding:flatbuffers.Encoding):string|Uint8Array|null
declarationFile(optionalEncoding?:any):string|Uint8Array|null {
  const offset = this.bb!.__offset(this.bb_pos, 16);
  return offset ? this.bb!.__string(this.bb_pos + offset, optionalEncoding) : null;
}

static getFullyQualifiedName():string {
  return 'reflection.Enum';
}

static startEnum(builder:flatbuffers.Builder) {
  builder.startObject(7);
}

static addName(builder:flatbuffers.Builder, nameOffset:flatbuffers.Offset) {
  builder.addFieldOffset(0, nameOffset, 0);
}

static addValues(builder:flatbuffers.Builder, valuesOffset:flatbuffers.Offset) {
  builder.addFieldOffset(1, valuesOffset, 0);
}

static createValuesVector(builder:flatbuffers.Builder, data:flatbuffers.Offset[]):flatbuffers.Offset {
  builder.startVector(4, data.length, 4);
  for (let i = data.length - 1; i >= 0; i--) {
    builder.addOffset(data[i]!);
  }
  return builder.endVector();
}

static startValuesVector(builder:flatbuffers.Builder, numElems:number) {
  builder.startVector(4, numElems, 4);
}

static addIsUnion(builder:flatbuffers.Builder, isUnion:boolean) {
  builder.addFieldInt8(2, +isUnion, +false);
}

static addUnderlyingType(builder:flatbuffers.Builder, underlyingTypeOffset:flatbuffers.Offset) {
  builder.addFieldOffset(3, underlyingTypeOffset, 0);
}

static addAttributes(builder:flatbuffers.Builder, attributesOffset:flatbuffers.Offset) {
  builder.addFieldOffset(4, attributesOffset, 0);
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
  builder.addFieldOffset(5, documentationOffset, 0);
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

static addDeclarationFile(builder:flatbuffers.Builder, declarationFileOffset:flatbuffers.Offset) {
  builder.addFieldOffset(6, declarationFileOffset, 0);
}

static endEnum(builder:flatbuffers.Builder):flatbuffers.Offset {
  const offset = builder.endObject();
  builder.requiredField(offset, 4) // name
  builder.requiredField(offset, 6) // values
  builder.requiredField(offset, 10) // underlying_type
  return offset;
}


unpack(): EnumT {
  return new EnumT(
    this.name(),
    this.bb!.createObjList(this.values.bind(this), this.valuesLength()),
    this.isUnion(),
    (this.underlyingType() !== null ? this.underlyingType()!.unpack() : null),
    this.bb!.createObjList(this.attributes.bind(this), this.attributesLength()),
    this.bb!.createScalarList(this.documentation.bind(this), this.documentationLength()),
    this.declarationFile()
  );
}


unpackTo(_o: EnumT): void {
  _o.name = this.name();
  _o.values = this.bb!.createObjList(this.values.bind(this), this.valuesLength());
  _o.isUnion = this.isUnion();
  _o.underlyingType = (this.underlyingType() !== null ? this.underlyingType()!.unpack() : null);
  _o.attributes = this.bb!.createObjList(this.attributes.bind(this), this.attributesLength());
  _o.documentation = this.bb!.createScalarList(this.documentation.bind(this), this.documentationLength());
  _o.declarationFile = this.declarationFile();
}
}

export class EnumT {
constructor(
  public name: string|Uint8Array|null = null,
  public values: (EnumValT)[] = [],
  public isUnion: boolean = false,
  public underlyingType: TypeT|null = null,
  public attributes: (KeyValueT)[] = [],
  public documentation: (string)[] = [],
  public declarationFile: string|Uint8Array|null = null
){}


pack(builder:flatbuffers.Builder): flatbuffers.Offset {
  const name = (this.name !== null ? builder.createString(this.name!) : 0);
  const values = Enum.createValuesVector(builder, builder.createObjectOffsetList(this.values));
  const underlyingType = (this.underlyingType !== null ? this.underlyingType!.pack(builder) : 0);
  const attributes = Enum.createAttributesVector(builder, builder.createObjectOffsetList(this.attributes));
  const documentation = Enum.createDocumentationVector(builder, builder.createObjectOffsetList(this.documentation));
  const declarationFile = (this.declarationFile !== null ? builder.createString(this.declarationFile!) : 0);

  Enum.startEnum(builder);
  Enum.addName(builder, name);
  Enum.addValues(builder, values);
  Enum.addIsUnion(builder, this.isUnion);
  Enum.addUnderlyingType(builder, underlyingType);
  Enum.addAttributes(builder, attributes);
  Enum.addDocumentation(builder, documentation);
  Enum.addDeclarationFile(builder, declarationFile);

  return Enum.endEnum(builder);
}
}
