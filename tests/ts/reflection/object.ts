// automatically generated by the FlatBuffers compiler, do not modify

import * as flatbuffers from 'flatbuffers';

import { Field, FieldT } from '../reflection/field.js';
import { KeyValue, KeyValueT } from '../reflection/key-value.js';


export class Object_ implements flatbuffers.IUnpackableObject<Object_T> {
  bb: flatbuffers.ByteBuffer|null = null;
  bb_pos = 0;
  __init(i:number, bb:flatbuffers.ByteBuffer):Object_ {
  this.bb_pos = i;
  this.bb = bb;
  return this;
}

static getRootAsObject(bb:flatbuffers.ByteBuffer, obj?:Object_):Object_ {
  return (obj || new Object_()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
}

static getSizePrefixedRootAsObject(bb:flatbuffers.ByteBuffer, obj?:Object_):Object_ {
  bb.setPosition(bb.position() + flatbuffers.SIZE_PREFIX_LENGTH);
  return (obj || new Object_()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
}

name():string|null
name(optionalEncoding:flatbuffers.Encoding):string|Uint8Array|null
name(optionalEncoding?:any):string|Uint8Array|null {
  const offset = this.bb!.__offset(this.bb_pos, 4);
  return offset ? this.bb!.__string(this.bb_pos + offset, optionalEncoding) : null;
}

fields(index: number, obj?:Field):Field|null {
  const offset = this.bb!.__offset(this.bb_pos, 6);
  return offset ? (obj || new Field()).__init(this.bb!.__indirect(this.bb!.__vector(this.bb_pos + offset) + index * 4), this.bb!) : null;
}

fieldsLength():number {
  const offset = this.bb!.__offset(this.bb_pos, 6);
  return offset ? this.bb!.__vector_len(this.bb_pos + offset) : 0;
}

isStruct():boolean {
  const offset = this.bb!.__offset(this.bb_pos, 8);
  return offset ? !!this.bb!.readInt8(this.bb_pos + offset) : false;
}

mutate_is_struct(value:boolean):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 8);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeInt8(this.bb_pos + offset, +value);
  return true;
}

minalign():number {
  const offset = this.bb!.__offset(this.bb_pos, 10);
  return offset ? this.bb!.readInt32(this.bb_pos + offset) : 0;
}

mutate_minalign(value:number):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 10);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeInt32(this.bb_pos + offset, value);
  return true;
}

bytesize():number {
  const offset = this.bb!.__offset(this.bb_pos, 12);
  return offset ? this.bb!.readInt32(this.bb_pos + offset) : 0;
}

mutate_bytesize(value:number):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 12);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeInt32(this.bb_pos + offset, value);
  return true;
}

attributes(index: number, obj?:KeyValue):KeyValue|null {
  const offset = this.bb!.__offset(this.bb_pos, 14);
  return offset ? (obj || new KeyValue()).__init(this.bb!.__indirect(this.bb!.__vector(this.bb_pos + offset) + index * 4), this.bb!) : null;
}

attributesLength():number {
  const offset = this.bb!.__offset(this.bb_pos, 14);
  return offset ? this.bb!.__vector_len(this.bb_pos + offset) : 0;
}

documentation(index: number):string
documentation(index: number,optionalEncoding:flatbuffers.Encoding):string|Uint8Array
documentation(index: number,optionalEncoding?:any):string|Uint8Array|null {
  const offset = this.bb!.__offset(this.bb_pos, 16);
  return offset ? this.bb!.__string(this.bb!.__vector(this.bb_pos + offset) + index * 4, optionalEncoding) : null;
}

documentationLength():number {
  const offset = this.bb!.__offset(this.bb_pos, 16);
  return offset ? this.bb!.__vector_len(this.bb_pos + offset) : 0;
}

/**
 * File that this Object is declared in.
 */
declarationFile():string|null
declarationFile(optionalEncoding:flatbuffers.Encoding):string|Uint8Array|null
declarationFile(optionalEncoding?:any):string|Uint8Array|null {
  const offset = this.bb!.__offset(this.bb_pos, 18);
  return offset ? this.bb!.__string(this.bb_pos + offset, optionalEncoding) : null;
}

static getFullyQualifiedName():string {
  return 'reflection_Object';
}

static startObject(builder:flatbuffers.Builder) {
  builder.startObject(8);
}

static addName(builder:flatbuffers.Builder, nameOffset:flatbuffers.Offset) {
  builder.addFieldOffset(0, nameOffset, 0);
}

static addFields(builder:flatbuffers.Builder, fieldsOffset:flatbuffers.Offset) {
  builder.addFieldOffset(1, fieldsOffset, 0);
}

static createFieldsVector(builder:flatbuffers.Builder, data:flatbuffers.Offset[]):flatbuffers.Offset {
  builder.startVector(4, data.length, 4);
  for (let i = data.length - 1; i >= 0; i--) {
    builder.addOffset(data[i]!);
  }
  return builder.endVector();
}

static startFieldsVector(builder:flatbuffers.Builder, numElems:number) {
  builder.startVector(4, numElems, 4);
}

static addIsStruct(builder:flatbuffers.Builder, isStruct:boolean) {
  builder.addFieldInt8(2, +isStruct, +false);
}

static addMinalign(builder:flatbuffers.Builder, minalign:number) {
  builder.addFieldInt32(3, minalign, 0);
}

static addBytesize(builder:flatbuffers.Builder, bytesize:number) {
  builder.addFieldInt32(4, bytesize, 0);
}

static addAttributes(builder:flatbuffers.Builder, attributesOffset:flatbuffers.Offset) {
  builder.addFieldOffset(5, attributesOffset, 0);
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
  builder.addFieldOffset(6, documentationOffset, 0);
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
  builder.addFieldOffset(7, declarationFileOffset, 0);
}

static endObject(builder:flatbuffers.Builder):flatbuffers.Offset {
  const offset = builder.endObject();
  builder.requiredField(offset, 4) // name
  builder.requiredField(offset, 6) // fields
  return offset;
}

static createObject(builder:flatbuffers.Builder, nameOffset:flatbuffers.Offset, fieldsOffset:flatbuffers.Offset, isStruct:boolean, minalign:number, bytesize:number, attributesOffset:flatbuffers.Offset, documentationOffset:flatbuffers.Offset, declarationFileOffset:flatbuffers.Offset):flatbuffers.Offset {
  Object_.startObject(builder);
  Object_.addName(builder, nameOffset);
  Object_.addFields(builder, fieldsOffset);
  Object_.addIsStruct(builder, isStruct);
  Object_.addMinalign(builder, minalign);
  Object_.addBytesize(builder, bytesize);
  Object_.addAttributes(builder, attributesOffset);
  Object_.addDocumentation(builder, documentationOffset);
  Object_.addDeclarationFile(builder, declarationFileOffset);
  return Object_.endObject(builder);
}

unpack(): Object_T {
  return new Object_T(
    this.name(),
    this.bb!.createObjList<Field, FieldT>(this.fields.bind(this), this.fieldsLength()),
    this.isStruct(),
    this.minalign(),
    this.bytesize(),
    this.bb!.createObjList<KeyValue, KeyValueT>(this.attributes.bind(this), this.attributesLength()),
    this.bb!.createScalarList<string>(this.documentation.bind(this), this.documentationLength()),
    this.declarationFile()
  );
}


unpackTo(_o: Object_T): void {
  _o.name = this.name();
  _o.fields = this.bb!.createObjList<Field, FieldT>(this.fields.bind(this), this.fieldsLength());
  _o.isStruct = this.isStruct();
  _o.minalign = this.minalign();
  _o.bytesize = this.bytesize();
  _o.attributes = this.bb!.createObjList<KeyValue, KeyValueT>(this.attributes.bind(this), this.attributesLength());
  _o.documentation = this.bb!.createScalarList<string>(this.documentation.bind(this), this.documentationLength());
  _o.declarationFile = this.declarationFile();
}
}

export class Object_T implements flatbuffers.IGeneratedObject {
constructor(
  public name: string|Uint8Array|null = null,
  public fields: (FieldT)[] = [],
  public isStruct: boolean = false,
  public minalign: number = 0,
  public bytesize: number = 0,
  public attributes: (KeyValueT)[] = [],
  public documentation: (string)[] = [],
  public declarationFile: string|Uint8Array|null = null
){}


pack(builder:flatbuffers.Builder): flatbuffers.Offset {
  const name = (this.name !== null ? builder.createString(this.name!) : 0);
  const fields = Object_.createFieldsVector(builder, builder.createObjectOffsetList(this.fields));
  const attributes = Object_.createAttributesVector(builder, builder.createObjectOffsetList(this.attributes));
  const documentation = Object_.createDocumentationVector(builder, builder.createObjectOffsetList(this.documentation));
  const declarationFile = (this.declarationFile !== null ? builder.createString(this.declarationFile!) : 0);

  return Object_.createObject(builder,
    name,
    fields,
    this.isStruct,
    this.minalign,
    this.bytesize,
    attributes,
    documentation,
    declarationFile
  );
}
}
