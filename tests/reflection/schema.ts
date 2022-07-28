// automatically generated by the FlatBuffers compiler, do not modify

import * as flatbuffers from 'flatbuffers';

import { Enum, EnumT } from '../reflection/enum';
import { Object_, ObjectT } from '../reflection/object';
import { SchemaFile, SchemaFileT } from '../reflection/schema-file';
import { Service, ServiceT } from '../reflection/service';


export class Schema {
  bb: flatbuffers.ByteBuffer|null = null;
  bb_pos = 0;
__init(i:number, bb:flatbuffers.ByteBuffer):Schema {
  this.bb_pos = i;
  this.bb = bb;
  return this;
}

static getRootAsSchema(bb:flatbuffers.ByteBuffer, obj?:Schema):Schema {
  return (obj || new Schema()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
}

static getSizePrefixedRootAsSchema(bb:flatbuffers.ByteBuffer, obj?:Schema):Schema {
  bb.setPosition(bb.position() + flatbuffers.SIZE_PREFIX_LENGTH);
  return (obj || new Schema()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
}

static bufferHasIdentifier(bb:flatbuffers.ByteBuffer):boolean {
  return bb.__has_identifier('BFBS');
}

objects(index: number, obj?:Object_):Object_|null {
  const offset = this.bb!.__offset(this.bb_pos, 4);
  return offset ? (obj || new Object_()).__init(this.bb!.__indirect(this.bb!.__vector(this.bb_pos + offset) + index * 4), this.bb!) : null;
}

objectsLength():number {
  const offset = this.bb!.__offset(this.bb_pos, 4);
  return offset ? this.bb!.__vector_len(this.bb_pos + offset) : 0;
}

enums(index: number, obj?:Enum):Enum|null {
  const offset = this.bb!.__offset(this.bb_pos, 6);
  return offset ? (obj || new Enum()).__init(this.bb!.__indirect(this.bb!.__vector(this.bb_pos + offset) + index * 4), this.bb!) : null;
}

enumsLength():number {
  const offset = this.bb!.__offset(this.bb_pos, 6);
  return offset ? this.bb!.__vector_len(this.bb_pos + offset) : 0;
}

fileIdent():string|null
fileIdent(optionalEncoding:flatbuffers.Encoding):string|Uint8Array|null
fileIdent(optionalEncoding?:any):string|Uint8Array|null {
  const offset = this.bb!.__offset(this.bb_pos, 8);
  return offset ? this.bb!.__string(this.bb_pos + offset, optionalEncoding) : null;
}

fileExt():string|null
fileExt(optionalEncoding:flatbuffers.Encoding):string|Uint8Array|null
fileExt(optionalEncoding?:any):string|Uint8Array|null {
  const offset = this.bb!.__offset(this.bb_pos, 10);
  return offset ? this.bb!.__string(this.bb_pos + offset, optionalEncoding) : null;
}

rootTable(obj?:Object_):Object_|null {
  const offset = this.bb!.__offset(this.bb_pos, 12);
  return offset ? (obj || new Object_()).__init(this.bb!.__indirect(this.bb_pos + offset), this.bb!) : null;
}

services(index: number, obj?:Service):Service|null {
  const offset = this.bb!.__offset(this.bb_pos, 14);
  return offset ? (obj || new Service()).__init(this.bb!.__indirect(this.bb!.__vector(this.bb_pos + offset) + index * 4), this.bb!) : null;
}

servicesLength():number {
  const offset = this.bb!.__offset(this.bb_pos, 14);
  return offset ? this.bb!.__vector_len(this.bb_pos + offset) : 0;
}

advancedFeatures():bigint {
  const offset = this.bb!.__offset(this.bb_pos, 16);
  return offset ? this.bb!.readUint64(this.bb_pos + offset) : BigInt('0');
}

mutate_advanced_features(value:bigint):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 16);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeUint64(this.bb_pos + offset, value);
  return true;
}

/**
 * All the files used in this compilation. Files are relative to where
 * flatc was invoked.
 */
fbsFiles(index: number, obj?:SchemaFile):SchemaFile|null {
  const offset = this.bb!.__offset(this.bb_pos, 18);
  return offset ? (obj || new SchemaFile()).__init(this.bb!.__indirect(this.bb!.__vector(this.bb_pos + offset) + index * 4), this.bb!) : null;
}

fbsFilesLength():number {
  const offset = this.bb!.__offset(this.bb_pos, 18);
  return offset ? this.bb!.__vector_len(this.bb_pos + offset) : 0;
}

static getFullyQualifiedName():string {
  return 'reflection.Schema';
}

static startSchema(builder:flatbuffers.Builder) {
  builder.startObject(8);
}

static addObjects(builder:flatbuffers.Builder, objectsOffset:flatbuffers.Offset) {
  builder.addFieldOffset(0, objectsOffset, 0);
}

static createObjectsVector(builder:flatbuffers.Builder, data:flatbuffers.Offset[]):flatbuffers.Offset {
  builder.startVector(4, data.length, 4);
  for (let i = data.length - 1; i >= 0; i--) {
    builder.addOffset(data[i]!);
  }
  return builder.endVector();
}

static startObjectsVector(builder:flatbuffers.Builder, numElems:number) {
  builder.startVector(4, numElems, 4);
}

static addEnums(builder:flatbuffers.Builder, enumsOffset:flatbuffers.Offset) {
  builder.addFieldOffset(1, enumsOffset, 0);
}

static createEnumsVector(builder:flatbuffers.Builder, data:flatbuffers.Offset[]):flatbuffers.Offset {
  builder.startVector(4, data.length, 4);
  for (let i = data.length - 1; i >= 0; i--) {
    builder.addOffset(data[i]!);
  }
  return builder.endVector();
}

static startEnumsVector(builder:flatbuffers.Builder, numElems:number) {
  builder.startVector(4, numElems, 4);
}

static addFileIdent(builder:flatbuffers.Builder, fileIdentOffset:flatbuffers.Offset) {
  builder.addFieldOffset(2, fileIdentOffset, 0);
}

static addFileExt(builder:flatbuffers.Builder, fileExtOffset:flatbuffers.Offset) {
  builder.addFieldOffset(3, fileExtOffset, 0);
}

static addRootTable(builder:flatbuffers.Builder, rootTableOffset:flatbuffers.Offset) {
  builder.addFieldOffset(4, rootTableOffset, 0);
}

static addServices(builder:flatbuffers.Builder, servicesOffset:flatbuffers.Offset) {
  builder.addFieldOffset(5, servicesOffset, 0);
}

static createServicesVector(builder:flatbuffers.Builder, data:flatbuffers.Offset[]):flatbuffers.Offset {
  builder.startVector(4, data.length, 4);
  for (let i = data.length - 1; i >= 0; i--) {
    builder.addOffset(data[i]!);
  }
  return builder.endVector();
}

static startServicesVector(builder:flatbuffers.Builder, numElems:number) {
  builder.startVector(4, numElems, 4);
}

static addAdvancedFeatures(builder:flatbuffers.Builder, advancedFeatures:bigint) {
  builder.addFieldInt64(6, advancedFeatures, BigInt('0'));
}

static addFbsFiles(builder:flatbuffers.Builder, fbsFilesOffset:flatbuffers.Offset) {
  builder.addFieldOffset(7, fbsFilesOffset, 0);
}

static createFbsFilesVector(builder:flatbuffers.Builder, data:flatbuffers.Offset[]):flatbuffers.Offset {
  builder.startVector(4, data.length, 4);
  for (let i = data.length - 1; i >= 0; i--) {
    builder.addOffset(data[i]!);
  }
  return builder.endVector();
}

static startFbsFilesVector(builder:flatbuffers.Builder, numElems:number) {
  builder.startVector(4, numElems, 4);
}

static endSchema(builder:flatbuffers.Builder):flatbuffers.Offset {
  const offset = builder.endObject();
  builder.requiredField(offset, 4) // objects
  builder.requiredField(offset, 6) // enums
  return offset;
}

static finishSchemaBuffer(builder:flatbuffers.Builder, offset:flatbuffers.Offset) {
  builder.finish(offset, 'BFBS');
}

static finishSizePrefixedSchemaBuffer(builder:flatbuffers.Builder, offset:flatbuffers.Offset) {
  builder.finish(offset, 'BFBS', true);
}


unpack(): SchemaT {
  return new SchemaT(
    this.bb!.createObjList(this.objects.bind(this), this.objectsLength()),
    this.bb!.createObjList(this.enums.bind(this), this.enumsLength()),
    this.fileIdent(),
    this.fileExt(),
    (this.rootTable() !== null ? this.rootTable()!.unpack() : null),
    this.bb!.createObjList(this.services.bind(this), this.servicesLength()),
    this.advancedFeatures(),
    this.bb!.createObjList(this.fbsFiles.bind(this), this.fbsFilesLength())
  );
}


unpackTo(_o: SchemaT): void {
  _o.objects = this.bb!.createObjList(this.objects.bind(this), this.objectsLength());
  _o.enums = this.bb!.createObjList(this.enums.bind(this), this.enumsLength());
  _o.fileIdent = this.fileIdent();
  _o.fileExt = this.fileExt();
  _o.rootTable = (this.rootTable() !== null ? this.rootTable()!.unpack() : null);
  _o.services = this.bb!.createObjList(this.services.bind(this), this.servicesLength());
  _o.advancedFeatures = this.advancedFeatures();
  _o.fbsFiles = this.bb!.createObjList(this.fbsFiles.bind(this), this.fbsFilesLength());
}
}

export class SchemaT {
constructor(
  public objects: (ObjectT)[] = [],
  public enums: (EnumT)[] = [],
  public fileIdent: string|Uint8Array|null = null,
  public fileExt: string|Uint8Array|null = null,
  public rootTable: ObjectT|null = null,
  public services: (ServiceT)[] = [],
  public advancedFeatures: bigint = BigInt('0'),
  public fbsFiles: (SchemaFileT)[] = []
){}


pack(builder:flatbuffers.Builder): flatbuffers.Offset {
  const objects = Schema.createObjectsVector(builder, builder.createObjectOffsetList(this.objects));
  const enums = Schema.createEnumsVector(builder, builder.createObjectOffsetList(this.enums));
  const fileIdent = (this.fileIdent !== null ? builder.createString(this.fileIdent!) : 0);
  const fileExt = (this.fileExt !== null ? builder.createString(this.fileExt!) : 0);
  const rootTable = (this.rootTable !== null ? this.rootTable!.pack(builder) : 0);
  const services = Schema.createServicesVector(builder, builder.createObjectOffsetList(this.services));
  const fbsFiles = Schema.createFbsFilesVector(builder, builder.createObjectOffsetList(this.fbsFiles));

  Schema.startSchema(builder);
  Schema.addObjects(builder, objects);
  Schema.addEnums(builder, enums);
  Schema.addFileIdent(builder, fileIdent);
  Schema.addFileExt(builder, fileExt);
  Schema.addRootTable(builder, rootTable);
  Schema.addServices(builder, services);
  Schema.addAdvancedFeatures(builder, this.advancedFeatures);
  Schema.addFbsFiles(builder, fbsFiles);

  return Schema.endSchema(builder);
}
}
