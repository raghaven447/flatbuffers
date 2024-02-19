// automatically generated by the FlatBuffers compiler, do not modify
// swiftlint:disable all
// swiftformat:disable all

public struct BytesCount: NativeStruct, Verifiable, FlatbuffersInitializable, NativeObject {

  static func validateVersion() { FlatBuffersVersion_23_5_26() }

  private var _x: Int64

  public init(_ bb: ByteBuffer, o: Int32) {
    let _accessor = Struct(bb: bb, position: o)
    _x = _accessor.readBuffer(of: Int64.self, at: 0)
  }

  public init(x: Int64) {
    _x = x
  }

  public init() {
    _x = 0
  }

  public init(_ _t: inout BytesCount_Mutable) {
    _x = _t.x
  }

  public var x: Int64 { _x }

  public static func verify<T>(_ verifier: inout Verifier, at position: Int, of type: T.Type) throws where T: Verifiable {
    try verifier.inBuffer(position: position, of: BytesCount.self)
  }
}

extension BytesCount: Encodable {

  enum CodingKeys: String, CodingKey {
    case x = "x"
  }
  public func encode(to encoder: Encoder) throws {
    var container = encoder.container(keyedBy: CodingKeys.self)
    if x != 0 {
      try container.encodeIfPresent(x, forKey: .x)
    }
  }
}

public struct BytesCount_Mutable: FlatBufferObject {

  static func validateVersion() { FlatBuffersVersion_23_5_26() }
  public var __buffer: ByteBuffer! { return _accessor.bb }
  private var _accessor: Struct

  public init(_ bb: ByteBuffer, o: Int32) { _accessor = Struct(bb: bb, position: o) }

  public var x: Int64 { return _accessor.readBuffer(of: Int64.self, at: 0) }
  @discardableResult public func mutate(x: Int64) -> Bool { return _accessor.mutate(x, index: 0) }
  

  public mutating func unpack() -> BytesCount {
    return BytesCount(&self)
  }
  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout BytesCount?) -> Offset {
    guard var obj = obj else { return Offset() }
    return pack(&builder, obj: &obj)
  }

  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout BytesCount) -> Offset {
    return builder.create(struct: obj)
  }
}

public struct InternalMessage: FlatBufferObject, Verifiable, ObjectAPIPacker {

  static func validateVersion() { FlatBuffersVersion_23_5_26() }
  public var __buffer: ByteBuffer! { return _accessor.bb }
  private var _accessor: Table

  private init(_ t: Table) { _accessor = t }
  public init(_ bb: ByteBuffer, o: Int32) { _accessor = Table(bb: bb, position: o) }

  private enum VTOFFSET: VOffset {
    case str = 4
    var v: Int32 { Int32(self.rawValue) }
    var p: VOffset { self.rawValue }
  }

  public var str: String? { let o = _accessor.offset(VTOFFSET.str.v); return o == 0 ? nil : _accessor.string(at: o) }
  public var strSegmentArray: [UInt8]? { return _accessor.getVector(at: VTOFFSET.str.v) }
  public static func startInternalMessage(_ fbb: inout FlatBufferBuilder) -> UOffset { fbb.startTable(with: 1) }
  public static func add(str: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: str, at: VTOFFSET.str.p) }
  public static func endInternalMessage(_ fbb: inout FlatBufferBuilder, start: UOffset) -> Offset { let end = Offset(offset: fbb.endTable(at: start)); return end }
  public static func createInternalMessage(
    _ fbb: inout FlatBufferBuilder,
    strOffset str: Offset = Offset()
  ) -> Offset {
    let __start = InternalMessage.startInternalMessage(&fbb)
    InternalMessage.add(str: str, &fbb)
    return InternalMessage.endInternalMessage(&fbb, start: __start)
  }
  

  public mutating func unpack() -> InternalMessageT {
    return InternalMessageT(&self)
  }
  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout InternalMessageT?) -> Offset {
    guard var obj = obj else { return Offset() }
    return pack(&builder, obj: &obj)
  }

  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout InternalMessageT) -> Offset {
    let __str: Offset
    if let s = obj.str {
      __str = builder.create(string: s)
    } else {
      __str = Offset()
    }

    let __root = InternalMessage.startInternalMessage(&builder)
    InternalMessage.add(str: __str, &builder)
    return InternalMessage.endInternalMessage(&builder, start: __root)
  }

  public static func verify<T>(_ verifier: inout Verifier, at position: Int, of type: T.Type) throws where T: Verifiable {
    var _v = try verifier.visitTable(at: position)
    try _v.visit(field: VTOFFSET.str.p, fieldName: "str", required: false, type: ForwardOffset<String>.self)
    _v.finish()
  }
}

extension InternalMessage: Encodable {

  enum CodingKeys: String, CodingKey {
    case str = "str"
  }
  public func encode(to encoder: Encoder) throws {
    var container = encoder.container(keyedBy: CodingKeys.self)
    try container.encodeIfPresent(str, forKey: .str)
  }
}

public class InternalMessageT: NativeObject {

  public var str: String?

  public init(_ _t: inout InternalMessage) {
    str = _t.str
  }

  public init() {
  }

  public func serialize() -> ByteBuffer { return serialize(type: InternalMessage.self) }

}
public struct Message: FlatBufferObject, Verifiable, ObjectAPIPacker {

  static func validateVersion() { FlatBuffersVersion_23_5_26() }
  public var __buffer: ByteBuffer! { return _accessor.bb }
  private var _accessor: Table

  private init(_ t: Table) { _accessor = t }
  public init(_ bb: ByteBuffer, o: Int32) { _accessor = Table(bb: bb, position: o) }

  private enum VTOFFSET: VOffset {
    case id = 4
    case position = 6
    case pointer = 8
    var v: Int32 { Int32(self.rawValue) }
    var p: VOffset { self.rawValue }
  }

  public var id: Int64 { let o = _accessor.offset(VTOFFSET.id.v); return o == 0 ? 0 : _accessor.readBuffer(of: Int64.self, at: o) }
  @discardableResult public func mutate(id: Int64) -> Bool {let o = _accessor.offset(VTOFFSET.id.v);  return _accessor.mutate(id, index: o) }
  public var position: BytesCount! { let o = _accessor.offset(VTOFFSET.position.v); return _accessor.readBuffer(of: BytesCount.self, at: o) }
  public var mutablePosition: BytesCount_Mutable! { let o = _accessor.offset(VTOFFSET.position.v); return BytesCount_Mutable(_accessor.bb, o: o + _accessor.position) }
  public var pointer: InternalMessage! { let o = _accessor.offset(VTOFFSET.pointer.v); return InternalMessage(_accessor.bb, o: _accessor.indirect(o + _accessor.position)) }
  public static func startMessage(_ fbb: inout FlatBufferBuilder) -> UOffset { fbb.startTable(with: 3) }
  public static func add(id: Int64, _ fbb: inout FlatBufferBuilder) { fbb.add(element: id, def: 0, at: VTOFFSET.id.p) }
  public static func add(position: BytesCount?, _ fbb: inout FlatBufferBuilder) { guard let position = position else { return }; fbb.create(struct: position, position: VTOFFSET.position.p) }
  public static func add(pointer: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: pointer, at: VTOFFSET.pointer.p) }
  public static func endMessage(_ fbb: inout FlatBufferBuilder, start: UOffset) -> Offset { let end = Offset(offset: fbb.endTable(at: start)); fbb.require(table: end, fields: [6, 8]); return end }
  public static func createMessage(
    _ fbb: inout FlatBufferBuilder,
    id: Int64 = 0,
    position: BytesCount,
    pointerOffset pointer: Offset
  ) -> Offset {
    let __start = Message.startMessage(&fbb)
    Message.add(id: id, &fbb)
    Message.add(position: position, &fbb)
    Message.add(pointer: pointer, &fbb)
    return Message.endMessage(&fbb, start: __start)
  }
  

  public mutating func unpack() -> MessageT {
    return MessageT(&self)
  }
  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout MessageT?) -> Offset {
    guard var obj = obj else { return Offset() }
    return pack(&builder, obj: &obj)
  }

  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout MessageT) -> Offset {
    let __pointer = InternalMessage.pack(&builder, obj: &obj.pointer)
    let __root = Message.startMessage(&builder)
    Message.add(id: obj.id, &builder)
    Message.add(position: obj.position, &builder)
    Message.add(pointer: __pointer, &builder)
    return Message.endMessage(&builder, start: __root)
  }

  public static func verify<T>(_ verifier: inout Verifier, at position: Int, of type: T.Type) throws where T: Verifiable {
    var _v = try verifier.visitTable(at: position)
    try _v.visit(field: VTOFFSET.id.p, fieldName: "id", required: false, type: Int64.self)
    try _v.visit(field: VTOFFSET.position.p, fieldName: "position", required: true, type: BytesCount.self)
    try _v.visit(field: VTOFFSET.pointer.p, fieldName: "pointer", required: true, type: ForwardOffset<InternalMessage>.self)
    _v.finish()
  }
}

extension Message: Encodable {

  enum CodingKeys: String, CodingKey {
    case id = "id"
    case position = "position"
    case pointer = "pointer"
  }
  public func encode(to encoder: Encoder) throws {
    var container = encoder.container(keyedBy: CodingKeys.self)
    if id != 0 {
      try container.encodeIfPresent(id, forKey: .id)
    }
    try container.encodeIfPresent(position, forKey: .position)
    try container.encodeIfPresent(pointer, forKey: .pointer)
  }
}

public class MessageT: NativeObject {

  public var id: Int64
  public var position: BytesCount
  public var pointer: InternalMessageT

  public init(_ _t: inout Message) {
    id = _t.id
    position = _t.position
    var __pointer = _t.pointer
    pointer = __pointer!.unpack()
  }

  public init() {
    id = 0
    position = BytesCount()
    pointer = InternalMessageT()
  }

  public func serialize() -> ByteBuffer { return serialize(type: Message.self) }

}
