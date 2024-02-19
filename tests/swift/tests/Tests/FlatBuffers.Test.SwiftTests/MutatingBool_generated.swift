// automatically generated by the FlatBuffers compiler, do not modify
// swiftlint:disable all
// swiftformat:disable all

import FlatBuffers

public struct Property: NativeStruct, Verifiable, FlatbuffersInitializable, NativeObject {

  static func validateVersion() { FlatBuffersVersion_23_5_26() }

  private var _property: Bool

  public init(_ bb: ByteBuffer, o: Int32) {
    let _accessor = Struct(bb: bb, position: o)
    _property = _accessor.readBuffer(of: Bool.self, at: 0)
  }

  public init(property: Bool) {
    _property = property
  }

  public init() {
    _property = false
  }

  public init(_ _t: inout Property_Mutable) {
    _property = _t.property
  }

  public var property: Bool { _property }

  public static func verify<T>(_ verifier: inout Verifier, at position: Int, of type: T.Type) throws where T: Verifiable {
    try verifier.inBuffer(position: position, of: Property.self)
  }
}

extension Property: Encodable {

  enum CodingKeys: String, CodingKey {
    case property = "property"
  }
  public func encode(to encoder: Encoder) throws {
    var container = encoder.container(keyedBy: CodingKeys.self)
    if property != false {
      try container.encodeIfPresent(property, forKey: .property)
    }
  }
}

public struct Property_Mutable: FlatBufferObject {

  static func validateVersion() { FlatBuffersVersion_23_5_26() }
  public var __buffer: ByteBuffer! { return _accessor.bb }
  private var _accessor: Struct

  public init(_ bb: ByteBuffer, o: Int32) { _accessor = Struct(bb: bb, position: o) }

  public var property: Bool { return _accessor.readBuffer(of: Bool.self, at: 0) }
  @discardableResult public func mutate(property: Bool) -> Bool { return _accessor.mutate(property, index: 0) }
  

  public mutating func unpack() -> Property {
    return Property(&self)
  }
  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout Property?) -> Offset {
    guard var obj = obj else { return Offset() }
    return pack(&builder, obj: &obj)
  }

  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout Property) -> Offset {
    return builder.create(struct: obj)
  }
}

public struct TestMutatingBool: FlatBufferObject, Verifiable, ObjectAPIPacker {

  static func validateVersion() { FlatBuffersVersion_23_5_26() }
  public var __buffer: ByteBuffer! { return _accessor.bb }
  private var _accessor: Table

  private init(_ t: Table) { _accessor = t }
  public init(_ bb: ByteBuffer, o: Int32) { _accessor = Table(bb: bb, position: o) }

  private enum VTOFFSET: VOffset {
    case b = 4
    var v: Int32 { Int32(self.rawValue) }
    var p: VOffset { self.rawValue }
  }

  public var b: Property? { let o = _accessor.offset(VTOFFSET.b.v); return o == 0 ? nil : _accessor.readBuffer(of: Property.self, at: o) }
  public var mutableB: Property_Mutable? { let o = _accessor.offset(VTOFFSET.b.v); return o == 0 ? nil : Property_Mutable(_accessor.bb, o: o + _accessor.position) }
  public static func startTestMutatingBool(_ fbb: inout FlatBufferBuilder) -> UOffset { fbb.startTable(with: 1) }
  public static func add(b: Property?, _ fbb: inout FlatBufferBuilder) { guard let b = b else { return }; fbb.create(struct: b, position: VTOFFSET.b.p) }
  public static func endTestMutatingBool(_ fbb: inout FlatBufferBuilder, start: UOffset) -> Offset { let end = Offset(offset: fbb.endTable(at: start)); return end }
  public static func createTestMutatingBool(
    _ fbb: inout FlatBufferBuilder,
    b: Property? = nil
  ) -> Offset {
    let __start = TestMutatingBool.startTestMutatingBool(&fbb)
    TestMutatingBool.add(b: b, &fbb)
    return TestMutatingBool.endTestMutatingBool(&fbb, start: __start)
  }
  

  public mutating func unpack() -> TestMutatingBoolT {
    return TestMutatingBoolT(&self)
  }
  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout TestMutatingBoolT?) -> Offset {
    guard var obj = obj else { return Offset() }
    return pack(&builder, obj: &obj)
  }

  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout TestMutatingBoolT) -> Offset {
    let __root = TestMutatingBool.startTestMutatingBool(&builder)
    TestMutatingBool.add(b: obj.b, &builder)
    return TestMutatingBool.endTestMutatingBool(&builder, start: __root)
  }

  public static func verify<T>(_ verifier: inout Verifier, at position: Int, of type: T.Type) throws where T: Verifiable {
    var _v = try verifier.visitTable(at: position)
    try _v.visit(field: VTOFFSET.b.p, fieldName: "b", required: false, type: Property.self)
    _v.finish()
  }
}

extension TestMutatingBool: Encodable {

  enum CodingKeys: String, CodingKey {
    case b = "b"
  }
  public func encode(to encoder: Encoder) throws {
    var container = encoder.container(keyedBy: CodingKeys.self)
    try container.encodeIfPresent(b, forKey: .b)
  }
}

public class TestMutatingBoolT: NativeObject {

  public var b: Property?

  public init(_ _t: inout TestMutatingBool) {
    b = _t.b
  }

  public init() {
    b = Property()
  }

  public func serialize() -> ByteBuffer { return serialize(type: TestMutatingBool.self) }

}
