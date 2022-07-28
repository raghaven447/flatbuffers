import * as flatbuffers from 'flatbuffers';


export enum BaseType{
  None = 0,
  UType = 1,
  Bool = 2,
  Byte = 3,
  UByte = 4,
  Short = 5,
  UShort = 6,
  Int = 7,
  UInt = 8,
  Long = 9,
  ULong = 10,
  Float = 11,
  Double = 12,
  String = 13,
  Vector = 14,
  Obj = 15,
  Union = 16,
  Array = 17,
  MaxBaseType = 18
}

/**
 * New schema language features that are not supported by old code generators.
 */
export enum AdvancedFeatures{
  AdvancedArrayFeatures = '1',
  AdvancedUnionFeatures = '2',
  OptionalScalars = '4',
  DefaultVectorsAndStrings = '8'
}

export class Type {
  bb: flatbuffers.ByteBuffer|null = null;
  bb_pos = 0;
__init(i:number, bb:flatbuffers.ByteBuffer):Type {
  this.bb_pos = i;
  this.bb = bb;
  return this;
}

static getRootAsType(bb:flatbuffers.ByteBuffer, obj?:Type):Type {
  return (obj || new Type()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
}

static getSizePrefixedRootAsType(bb:flatbuffers.ByteBuffer, obj?:Type):Type {
  bb.setPosition(bb.position() + flatbuffers.SIZE_PREFIX_LENGTH);
  return (obj || new Type()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
}

baseType():BaseType {
  const offset = this.bb!.__offset(this.bb_pos, 4);
  return offset ? this.bb!.readInt8(this.bb_pos + offset) : BaseType.None;
}

mutate_base_type(value:BaseType):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 4);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeInt8(this.bb_pos + offset, value);
  return true;
}

element():BaseType {
  const offset = this.bb!.__offset(this.bb_pos, 6);
  return offset ? this.bb!.readInt8(this.bb_pos + offset) : BaseType.None;
}

mutate_element(value:BaseType):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 6);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeInt8(this.bb_pos + offset, value);
  return true;
}

index():number {
  const offset = this.bb!.__offset(this.bb_pos, 8);
  return offset ? this.bb!.readInt32(this.bb_pos + offset) : -1;
}

mutate_index(value:number):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 8);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeInt32(this.bb_pos + offset, value);
  return true;
}

fixedLength():number {
  const offset = this.bb!.__offset(this.bb_pos, 10);
  return offset ? this.bb!.readUint16(this.bb_pos + offset) : 0;
}

mutate_fixed_length(value:number):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 10);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeUint16(this.bb_pos + offset, value);
  return true;
}

/**
 * The size (octets) of the `base_type` field.
 */
baseSize():number {
  const offset = this.bb!.__offset(this.bb_pos, 12);
  return offset ? this.bb!.readUint32(this.bb_pos + offset) : 4;
}

mutate_base_size(value:number):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 12);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeUint32(this.bb_pos + offset, value);
  return true;
}

/**
 * The size (octets) of the `element` field, if present.
 */
elementSize():number {
  const offset = this.bb!.__offset(this.bb_pos, 14);
  return offset ? this.bb!.readUint32(this.bb_pos + offset) : 0;
}

mutate_element_size(value:number):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 14);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeUint32(this.bb_pos + offset, value);
  return true;
}

static getFullyQualifiedName():string {
  return 'reflection.Type';
}

static startType(builder:flatbuffers.Builder) {
  builder.startObject(6);
}

static addBaseType(builder:flatbuffers.Builder, baseType:BaseType) {
  builder.addFieldInt8(0, baseType, BaseType.None);
}

static addElement(builder:flatbuffers.Builder, element:BaseType) {
  builder.addFieldInt8(1, element, BaseType.None);
}

static addIndex(builder:flatbuffers.Builder, index:number) {
  builder.addFieldInt32(2, index, -1);
}

static addFixedLength(builder:flatbuffers.Builder, fixedLength:number) {
  builder.addFieldInt16(3, fixedLength, 0);
}

static addBaseSize(builder:flatbuffers.Builder, baseSize:number) {
  builder.addFieldInt32(4, baseSize, 4);
}

static addElementSize(builder:flatbuffers.Builder, elementSize:number) {
  builder.addFieldInt32(5, elementSize, 0);
}

static endType(builder:flatbuffers.Builder):flatbuffers.Offset {
  const offset = builder.endObject();
  return offset;
}

static createType(builder:flatbuffers.Builder, baseType:BaseType, element:BaseType, index:number, fixedLength:number, baseSize:number, elementSize:number):flatbuffers.Offset {
  Type.startType(builder);
  Type.addBaseType(builder, baseType);
  Type.addElement(builder, element);
  Type.addIndex(builder, index);
  Type.addFixedLength(builder, fixedLength);
  Type.addBaseSize(builder, baseSize);
  Type.addElementSize(builder, elementSize);
  return Type.endType(builder);
}

unpack(): TypeT {
  return new TypeT(
    this.baseType(),
    this.element(),
    this.index(),
    this.fixedLength(),
    this.baseSize(),
    this.elementSize()
  );
}


unpackTo(_o: TypeT): void {
  _o.baseType = this.baseType();
  _o.element = this.element();
  _o.index = this.index();
  _o.fixedLength = this.fixedLength();
  _o.baseSize = this.baseSize();
  _o.elementSize = this.elementSize();
}
}

export class TypeT {
constructor(
  public baseType: BaseType = BaseType.None,
  public element: BaseType = BaseType.None,
  public index: number = -1,
  public fixedLength: number = 0,
  public baseSize: number = 4,
  public elementSize: number = 0
){}


pack(builder:flatbuffers.Builder): flatbuffers.Offset {
  return Type.createType(builder,
    this.baseType,
    this.element,
    this.index,
    this.fixedLength,
    this.baseSize,
    this.elementSize
  );
}
}
export class KeyValue {
  bb: flatbuffers.ByteBuffer|null = null;
  bb_pos = 0;
__init(i:number, bb:flatbuffers.ByteBuffer):KeyValue {
  this.bb_pos = i;
  this.bb = bb;
  return this;
}

static getRootAsKeyValue(bb:flatbuffers.ByteBuffer, obj?:KeyValue):KeyValue {
  return (obj || new KeyValue()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
}

static getSizePrefixedRootAsKeyValue(bb:flatbuffers.ByteBuffer, obj?:KeyValue):KeyValue {
  bb.setPosition(bb.position() + flatbuffers.SIZE_PREFIX_LENGTH);
  return (obj || new KeyValue()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
}

key():string|null
key(optionalEncoding:flatbuffers.Encoding):string|Uint8Array|null
key(optionalEncoding?:any):string|Uint8Array|null {
  const offset = this.bb!.__offset(this.bb_pos, 4);
  return offset ? this.bb!.__string(this.bb_pos + offset, optionalEncoding) : null;
}

value():string|null
value(optionalEncoding:flatbuffers.Encoding):string|Uint8Array|null
value(optionalEncoding?:any):string|Uint8Array|null {
  const offset = this.bb!.__offset(this.bb_pos, 6);
  return offset ? this.bb!.__string(this.bb_pos + offset, optionalEncoding) : null;
}

static getFullyQualifiedName():string {
  return 'reflection.KeyValue';
}

static startKeyValue(builder:flatbuffers.Builder) {
  builder.startObject(2);
}

static addKey(builder:flatbuffers.Builder, keyOffset:flatbuffers.Offset) {
  builder.addFieldOffset(0, keyOffset, 0);
}

static addValue(builder:flatbuffers.Builder, valueOffset:flatbuffers.Offset) {
  builder.addFieldOffset(1, valueOffset, 0);
}

static endKeyValue(builder:flatbuffers.Builder):flatbuffers.Offset {
  const offset = builder.endObject();
  builder.requiredField(offset, 4) // key
  return offset;
}

static createKeyValue(builder:flatbuffers.Builder, keyOffset:flatbuffers.Offset, valueOffset:flatbuffers.Offset):flatbuffers.Offset {
  KeyValue.startKeyValue(builder);
  KeyValue.addKey(builder, keyOffset);
  KeyValue.addValue(builder, valueOffset);
  return KeyValue.endKeyValue(builder);
}

unpack(): KeyValueT {
  return new KeyValueT(
    this.key(),
    this.value()
  );
}


unpackTo(_o: KeyValueT): void {
  _o.key = this.key();
  _o.value = this.value();
}
}

export class KeyValueT {
constructor(
  public key: string|Uint8Array|null = null,
  public value: string|Uint8Array|null = null
){}


pack(builder:flatbuffers.Builder): flatbuffers.Offset {
  const key = (this.key !== null ? builder.createString(this.key!) : 0);
  const value = (this.value !== null ? builder.createString(this.value!) : 0);

  return KeyValue.createKeyValue(builder,
    key,
    value
  );
}
}
export class EnumVal {
  bb: flatbuffers.ByteBuffer|null = null;
  bb_pos = 0;
__init(i:number, bb:flatbuffers.ByteBuffer):EnumVal {
  this.bb_pos = i;
  this.bb = bb;
  return this;
}

static getRootAsEnumVal(bb:flatbuffers.ByteBuffer, obj?:EnumVal):EnumVal {
  return (obj || new EnumVal()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
}

static getSizePrefixedRootAsEnumVal(bb:flatbuffers.ByteBuffer, obj?:EnumVal):EnumVal {
  bb.setPosition(bb.position() + flatbuffers.SIZE_PREFIX_LENGTH);
  return (obj || new EnumVal()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
}

name():string|null
name(optionalEncoding:flatbuffers.Encoding):string|Uint8Array|null
name(optionalEncoding?:any):string|Uint8Array|null {
  const offset = this.bb!.__offset(this.bb_pos, 4);
  return offset ? this.bb!.__string(this.bb_pos + offset, optionalEncoding) : null;
}

value():bigint {
  const offset = this.bb!.__offset(this.bb_pos, 6);
  return offset ? this.bb!.readInt64(this.bb_pos + offset) : BigInt('0');
}

mutate_value(value:bigint):boolean {
  const offset = this.bb!.__offset(this.bb_pos, 6);

  if (offset === 0) {
    return false;
  }

  this.bb!.writeInt64(this.bb_pos + offset, value);
  return true;
}

unionType(obj?:Type):Type|null {
  const offset = this.bb!.__offset(this.bb_pos, 10);
  return offset ? (obj || new Type()).__init(this.bb!.__indirect(this.bb_pos + offset), this.bb!) : null;
}

documentation(index: number):string
documentation(index: number,optionalEncoding:flatbuffers.Encoding):string|Uint8Array
documentation(index: number,optionalEncoding?:any):string|Uint8Array|null {
  const offset = this.bb!.__offset(this.bb_pos, 12);
  return offset ? this.bb!.__string(this.bb!.__vector(this.bb_pos + offset) + index * 4, optionalEncoding) : null;
}

documentationLength():number {
  const offset = this.bb!.__offset(this.bb_pos, 12);
  return offset ? this.bb!.__vector_len(this.bb_pos + offset) : 0;
}

static getFullyQualifiedName():string {
  return 'reflection.EnumVal';
}

static startEnumVal(builder:flatbuffers.Builder) {
  builder.startObject(5);
}

static addName(builder:flatbuffers.Builder, nameOffset:flatbuffers.Offset) {
  builder.addFieldOffset(0, nameOffset, 0);
}

static addValue(builder:flatbuffers.Builder, value:bigint) {
  builder.addFieldInt64(1, value, BigInt('0'));
}

static addUnionType(builder:flatbuffers.Builder, unionTypeOffset:flatbuffers.Offset) {
  builder.addFieldOffset(3, unionTypeOffset, 0);
}

static addDocumentation(builder:flatbuffers.Builder, documentationOffset:flatbuffers.Offset) {
  builder.addFieldOffset(4, documentationOffset, 0);
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

static endEnumVal(builder:flatbuffers.Builder):flatbuffers.Offset {
  const offset = builder.endObject();
  builder.requiredField(offset, 4) // name
  return offset;
}


unpack(): EnumValT {
  return new EnumValT(
    this.name(),
    this.value(),
    (this.unionType() !== null ? this.unionType()!.unpack() : null),
    this.bb!.createScalarList(this.documentation.bind(this), this.documentationLength())
  );
}


unpackTo(_o: EnumValT): void {
  _o.name = this.name();
  _o.value = this.value();
  _o.unionType = (this.unionType() !== null ? this.unionType()!.unpack() : null);
  _o.documentation = this.bb!.createScalarList(this.documentation.bind(this), this.documentationLength());
}
}

export class EnumValT {
constructor(
  public name: string|Uint8Array|null = null,
  public value: bigint = BigInt('0'),
  public unionType: TypeT|null = null,
  public documentation: (string)[] = []
){}


pack(builder:flatbuffers.Builder): flatbuffers.Offset {
  const name = (this.name !== null ? builder.createString(this.name!) : 0);
  const unionType = (this.unionType !== null ? this.unionType!.pack(builder) : 0);
  const documentation = EnumVal.createDocumentationVector(builder, builder.createObjectOffsetList(this.documentation));

  EnumVal.startEnumVal(builder);
  EnumVal.addName(builder, name);
  EnumVal.addValue(builder, this.value);
  EnumVal.addUnionType(builder, unionType);
  EnumVal.addDocumentation(builder, documentation);

  return EnumVal.endEnumVal(builder);
}
}
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
export class Object_ {
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
  return 'reflection.Object';
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

unpack(): ObjectT {
  return new ObjectT(
    this.name(),
    this.bb!.createObjList(this.fields.bind(this), this.fieldsLength()),
    this.isStruct(),
    this.minalign(),
    this.bytesize(),
    this.bb!.createObjList(this.attributes.bind(this), this.attributesLength()),
    this.bb!.createScalarList(this.documentation.bind(this), this.documentationLength()),
    this.declarationFile()
  );
}


unpackTo(_o: ObjectT): void {
  _o.name = this.name();
  _o.fields = this.bb!.createObjList(this.fields.bind(this), this.fieldsLength());
  _o.isStruct = this.isStruct();
  _o.minalign = this.minalign();
  _o.bytesize = this.bytesize();
  _o.attributes = this.bb!.createObjList(this.attributes.bind(this), this.attributesLength());
  _o.documentation = this.bb!.createScalarList(this.documentation.bind(this), this.documentationLength());
  _o.declarationFile = this.declarationFile();
}
}

export class ObjectT {
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
export class RPCCall {
  bb: flatbuffers.ByteBuffer|null = null;
  bb_pos = 0;
__init(i:number, bb:flatbuffers.ByteBuffer):RPCCall {
  this.bb_pos = i;
  this.bb = bb;
  return this;
}

static getRootAsRPCCall(bb:flatbuffers.ByteBuffer, obj?:RPCCall):RPCCall {
  return (obj || new RPCCall()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
}

static getSizePrefixedRootAsRPCCall(bb:flatbuffers.ByteBuffer, obj?:RPCCall):RPCCall {
  bb.setPosition(bb.position() + flatbuffers.SIZE_PREFIX_LENGTH);
  return (obj || new RPCCall()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
}

name():string|null
name(optionalEncoding:flatbuffers.Encoding):string|Uint8Array|null
name(optionalEncoding?:any):string|Uint8Array|null {
  const offset = this.bb!.__offset(this.bb_pos, 4);
  return offset ? this.bb!.__string(this.bb_pos + offset, optionalEncoding) : null;
}

request(obj?:Object_):Object_|null {
  const offset = this.bb!.__offset(this.bb_pos, 6);
  return offset ? (obj || new Object_()).__init(this.bb!.__indirect(this.bb_pos + offset), this.bb!) : null;
}

response(obj?:Object_):Object_|null {
  const offset = this.bb!.__offset(this.bb_pos, 8);
  return offset ? (obj || new Object_()).__init(this.bb!.__indirect(this.bb_pos + offset), this.bb!) : null;
}

attributes(index: number, obj?:KeyValue):KeyValue|null {
  const offset = this.bb!.__offset(this.bb_pos, 10);
  return offset ? (obj || new KeyValue()).__init(this.bb!.__indirect(this.bb!.__vector(this.bb_pos + offset) + index * 4), this.bb!) : null;
}

attributesLength():number {
  const offset = this.bb!.__offset(this.bb_pos, 10);
  return offset ? this.bb!.__vector_len(this.bb_pos + offset) : 0;
}

documentation(index: number):string
documentation(index: number,optionalEncoding:flatbuffers.Encoding):string|Uint8Array
documentation(index: number,optionalEncoding?:any):string|Uint8Array|null {
  const offset = this.bb!.__offset(this.bb_pos, 12);
  return offset ? this.bb!.__string(this.bb!.__vector(this.bb_pos + offset) + index * 4, optionalEncoding) : null;
}

documentationLength():number {
  const offset = this.bb!.__offset(this.bb_pos, 12);
  return offset ? this.bb!.__vector_len(this.bb_pos + offset) : 0;
}

static getFullyQualifiedName():string {
  return 'reflection.RPCCall';
}

static startRPCCall(builder:flatbuffers.Builder) {
  builder.startObject(5);
}

static addName(builder:flatbuffers.Builder, nameOffset:flatbuffers.Offset) {
  builder.addFieldOffset(0, nameOffset, 0);
}

static addRequest(builder:flatbuffers.Builder, requestOffset:flatbuffers.Offset) {
  builder.addFieldOffset(1, requestOffset, 0);
}

static addResponse(builder:flatbuffers.Builder, responseOffset:flatbuffers.Offset) {
  builder.addFieldOffset(2, responseOffset, 0);
}

static addAttributes(builder:flatbuffers.Builder, attributesOffset:flatbuffers.Offset) {
  builder.addFieldOffset(3, attributesOffset, 0);
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
  builder.addFieldOffset(4, documentationOffset, 0);
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

static endRPCCall(builder:flatbuffers.Builder):flatbuffers.Offset {
  const offset = builder.endObject();
  builder.requiredField(offset, 4) // name
  builder.requiredField(offset, 6) // request
  builder.requiredField(offset, 8) // response
  return offset;
}


unpack(): RPCCallT {
  return new RPCCallT(
    this.name(),
    (this.request() !== null ? this.request()!.unpack() : null),
    (this.response() !== null ? this.response()!.unpack() : null),
    this.bb!.createObjList(this.attributes.bind(this), this.attributesLength()),
    this.bb!.createScalarList(this.documentation.bind(this), this.documentationLength())
  );
}


unpackTo(_o: RPCCallT): void {
  _o.name = this.name();
  _o.request = (this.request() !== null ? this.request()!.unpack() : null);
  _o.response = (this.response() !== null ? this.response()!.unpack() : null);
  _o.attributes = this.bb!.createObjList(this.attributes.bind(this), this.attributesLength());
  _o.documentation = this.bb!.createScalarList(this.documentation.bind(this), this.documentationLength());
}
}

export class RPCCallT {
constructor(
  public name: string|Uint8Array|null = null,
  public request: ObjectT|null = null,
  public response: ObjectT|null = null,
  public attributes: (KeyValueT)[] = [],
  public documentation: (string)[] = []
){}


pack(builder:flatbuffers.Builder): flatbuffers.Offset {
  const name = (this.name !== null ? builder.createString(this.name!) : 0);
  const request = (this.request !== null ? this.request!.pack(builder) : 0);
  const response = (this.response !== null ? this.response!.pack(builder) : 0);
  const attributes = RPCCall.createAttributesVector(builder, builder.createObjectOffsetList(this.attributes));
  const documentation = RPCCall.createDocumentationVector(builder, builder.createObjectOffsetList(this.documentation));

  RPCCall.startRPCCall(builder);
  RPCCall.addName(builder, name);
  RPCCall.addRequest(builder, request);
  RPCCall.addResponse(builder, response);
  RPCCall.addAttributes(builder, attributes);
  RPCCall.addDocumentation(builder, documentation);

  return RPCCall.endRPCCall(builder);
}
}
export class Service {
  bb: flatbuffers.ByteBuffer|null = null;
  bb_pos = 0;
__init(i:number, bb:flatbuffers.ByteBuffer):Service {
  this.bb_pos = i;
  this.bb = bb;
  return this;
}

static getRootAsService(bb:flatbuffers.ByteBuffer, obj?:Service):Service {
  return (obj || new Service()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
}

static getSizePrefixedRootAsService(bb:flatbuffers.ByteBuffer, obj?:Service):Service {
  bb.setPosition(bb.position() + flatbuffers.SIZE_PREFIX_LENGTH);
  return (obj || new Service()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
}

name():string|null
name(optionalEncoding:flatbuffers.Encoding):string|Uint8Array|null
name(optionalEncoding?:any):string|Uint8Array|null {
  const offset = this.bb!.__offset(this.bb_pos, 4);
  return offset ? this.bb!.__string(this.bb_pos + offset, optionalEncoding) : null;
}

calls(index: number, obj?:RPCCall):RPCCall|null {
  const offset = this.bb!.__offset(this.bb_pos, 6);
  return offset ? (obj || new RPCCall()).__init(this.bb!.__indirect(this.bb!.__vector(this.bb_pos + offset) + index * 4), this.bb!) : null;
}

callsLength():number {
  const offset = this.bb!.__offset(this.bb_pos, 6);
  return offset ? this.bb!.__vector_len(this.bb_pos + offset) : 0;
}

attributes(index: number, obj?:KeyValue):KeyValue|null {
  const offset = this.bb!.__offset(this.bb_pos, 8);
  return offset ? (obj || new KeyValue()).__init(this.bb!.__indirect(this.bb!.__vector(this.bb_pos + offset) + index * 4), this.bb!) : null;
}

attributesLength():number {
  const offset = this.bb!.__offset(this.bb_pos, 8);
  return offset ? this.bb!.__vector_len(this.bb_pos + offset) : 0;
}

documentation(index: number):string
documentation(index: number,optionalEncoding:flatbuffers.Encoding):string|Uint8Array
documentation(index: number,optionalEncoding?:any):string|Uint8Array|null {
  const offset = this.bb!.__offset(this.bb_pos, 10);
  return offset ? this.bb!.__string(this.bb!.__vector(this.bb_pos + offset) + index * 4, optionalEncoding) : null;
}

documentationLength():number {
  const offset = this.bb!.__offset(this.bb_pos, 10);
  return offset ? this.bb!.__vector_len(this.bb_pos + offset) : 0;
}

/**
 * File that this Service is declared in.
 */
declarationFile():string|null
declarationFile(optionalEncoding:flatbuffers.Encoding):string|Uint8Array|null
declarationFile(optionalEncoding?:any):string|Uint8Array|null {
  const offset = this.bb!.__offset(this.bb_pos, 12);
  return offset ? this.bb!.__string(this.bb_pos + offset, optionalEncoding) : null;
}

static getFullyQualifiedName():string {
  return 'reflection.Service';
}

static startService(builder:flatbuffers.Builder) {
  builder.startObject(5);
}

static addName(builder:flatbuffers.Builder, nameOffset:flatbuffers.Offset) {
  builder.addFieldOffset(0, nameOffset, 0);
}

static addCalls(builder:flatbuffers.Builder, callsOffset:flatbuffers.Offset) {
  builder.addFieldOffset(1, callsOffset, 0);
}

static createCallsVector(builder:flatbuffers.Builder, data:flatbuffers.Offset[]):flatbuffers.Offset {
  builder.startVector(4, data.length, 4);
  for (let i = data.length - 1; i >= 0; i--) {
    builder.addOffset(data[i]!);
  }
  return builder.endVector();
}

static startCallsVector(builder:flatbuffers.Builder, numElems:number) {
  builder.startVector(4, numElems, 4);
}

static addAttributes(builder:flatbuffers.Builder, attributesOffset:flatbuffers.Offset) {
  builder.addFieldOffset(2, attributesOffset, 0);
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
  builder.addFieldOffset(3, documentationOffset, 0);
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
  builder.addFieldOffset(4, declarationFileOffset, 0);
}

static endService(builder:flatbuffers.Builder):flatbuffers.Offset {
  const offset = builder.endObject();
  builder.requiredField(offset, 4) // name
  return offset;
}

static createService(builder:flatbuffers.Builder, nameOffset:flatbuffers.Offset, callsOffset:flatbuffers.Offset, attributesOffset:flatbuffers.Offset, documentationOffset:flatbuffers.Offset, declarationFileOffset:flatbuffers.Offset):flatbuffers.Offset {
  Service.startService(builder);
  Service.addName(builder, nameOffset);
  Service.addCalls(builder, callsOffset);
  Service.addAttributes(builder, attributesOffset);
  Service.addDocumentation(builder, documentationOffset);
  Service.addDeclarationFile(builder, declarationFileOffset);
  return Service.endService(builder);
}

unpack(): ServiceT {
  return new ServiceT(
    this.name(),
    this.bb!.createObjList(this.calls.bind(this), this.callsLength()),
    this.bb!.createObjList(this.attributes.bind(this), this.attributesLength()),
    this.bb!.createScalarList(this.documentation.bind(this), this.documentationLength()),
    this.declarationFile()
  );
}


unpackTo(_o: ServiceT): void {
  _o.name = this.name();
  _o.calls = this.bb!.createObjList(this.calls.bind(this), this.callsLength());
  _o.attributes = this.bb!.createObjList(this.attributes.bind(this), this.attributesLength());
  _o.documentation = this.bb!.createScalarList(this.documentation.bind(this), this.documentationLength());
  _o.declarationFile = this.declarationFile();
}
}

export class ServiceT {
constructor(
  public name: string|Uint8Array|null = null,
  public calls: (RPCCallT)[] = [],
  public attributes: (KeyValueT)[] = [],
  public documentation: (string)[] = [],
  public declarationFile: string|Uint8Array|null = null
){}


pack(builder:flatbuffers.Builder): flatbuffers.Offset {
  const name = (this.name !== null ? builder.createString(this.name!) : 0);
  const calls = Service.createCallsVector(builder, builder.createObjectOffsetList(this.calls));
  const attributes = Service.createAttributesVector(builder, builder.createObjectOffsetList(this.attributes));
  const documentation = Service.createDocumentationVector(builder, builder.createObjectOffsetList(this.documentation));
  const declarationFile = (this.declarationFile !== null ? builder.createString(this.declarationFile!) : 0);

  return Service.createService(builder,
    name,
    calls,
    attributes,
    documentation,
    declarationFile
  );
}
}
/**
 * File specific information.
 * Symbols declared within a file may be recovered by iterating over all
 * symbols and examining the `declaration_file` field.
 */
export class SchemaFile {
  bb: flatbuffers.ByteBuffer|null = null;
  bb_pos = 0;
__init(i:number, bb:flatbuffers.ByteBuffer):SchemaFile {
  this.bb_pos = i;
  this.bb = bb;
  return this;
}

static getRootAsSchemaFile(bb:flatbuffers.ByteBuffer, obj?:SchemaFile):SchemaFile {
  return (obj || new SchemaFile()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
}

static getSizePrefixedRootAsSchemaFile(bb:flatbuffers.ByteBuffer, obj?:SchemaFile):SchemaFile {
  bb.setPosition(bb.position() + flatbuffers.SIZE_PREFIX_LENGTH);
  return (obj || new SchemaFile()).__init(bb.readInt32(bb.position()) + bb.position(), bb);
}

/**
 * Filename, relative to project root.
 */
filename():string|null
filename(optionalEncoding:flatbuffers.Encoding):string|Uint8Array|null
filename(optionalEncoding?:any):string|Uint8Array|null {
  const offset = this.bb!.__offset(this.bb_pos, 4);
  return offset ? this.bb!.__string(this.bb_pos + offset, optionalEncoding) : null;
}

/**
 * Names of included files, relative to project root.
 */
includedFilenames(index: number):string
includedFilenames(index: number,optionalEncoding:flatbuffers.Encoding):string|Uint8Array
includedFilenames(index: number,optionalEncoding?:any):string|Uint8Array|null {
  const offset = this.bb!.__offset(this.bb_pos, 6);
  return offset ? this.bb!.__string(this.bb!.__vector(this.bb_pos + offset) + index * 4, optionalEncoding) : null;
}

includedFilenamesLength():number {
  const offset = this.bb!.__offset(this.bb_pos, 6);
  return offset ? this.bb!.__vector_len(this.bb_pos + offset) : 0;
}

static getFullyQualifiedName():string {
  return 'reflection.SchemaFile';
}

static startSchemaFile(builder:flatbuffers.Builder) {
  builder.startObject(2);
}

static addFilename(builder:flatbuffers.Builder, filenameOffset:flatbuffers.Offset) {
  builder.addFieldOffset(0, filenameOffset, 0);
}

static addIncludedFilenames(builder:flatbuffers.Builder, includedFilenamesOffset:flatbuffers.Offset) {
  builder.addFieldOffset(1, includedFilenamesOffset, 0);
}

static createIncludedFilenamesVector(builder:flatbuffers.Builder, data:flatbuffers.Offset[]):flatbuffers.Offset {
  builder.startVector(4, data.length, 4);
  for (let i = data.length - 1; i >= 0; i--) {
    builder.addOffset(data[i]!);
  }
  return builder.endVector();
}

static startIncludedFilenamesVector(builder:flatbuffers.Builder, numElems:number) {
  builder.startVector(4, numElems, 4);
}

static endSchemaFile(builder:flatbuffers.Builder):flatbuffers.Offset {
  const offset = builder.endObject();
  builder.requiredField(offset, 4) // filename
  return offset;
}

static createSchemaFile(builder:flatbuffers.Builder, filenameOffset:flatbuffers.Offset, includedFilenamesOffset:flatbuffers.Offset):flatbuffers.Offset {
  SchemaFile.startSchemaFile(builder);
  SchemaFile.addFilename(builder, filenameOffset);
  SchemaFile.addIncludedFilenames(builder, includedFilenamesOffset);
  return SchemaFile.endSchemaFile(builder);
}

unpack(): SchemaFileT {
  return new SchemaFileT(
    this.filename(),
    this.bb!.createScalarList(this.includedFilenames.bind(this), this.includedFilenamesLength())
  );
}


unpackTo(_o: SchemaFileT): void {
  _o.filename = this.filename();
  _o.includedFilenames = this.bb!.createScalarList(this.includedFilenames.bind(this), this.includedFilenamesLength());
}
}

export class SchemaFileT {
constructor(
  public filename: string|Uint8Array|null = null,
  public includedFilenames: (string)[] = []
){}


pack(builder:flatbuffers.Builder): flatbuffers.Offset {
  const filename = (this.filename !== null ? builder.createString(this.filename!) : 0);
  const includedFilenames = SchemaFile.createIncludedFilenamesVector(builder, builder.createObjectOffsetList(this.includedFilenames));

  return SchemaFile.createSchemaFile(builder,
    filename,
    includedFilenames
  );
}
}
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
