// automatically generated by the FlatBuffers compiler, do not modify

import FlatBuffers

public enum Character: UInt8, Enum { 
	public typealias T = UInt8
	public static var byteSize: Int { return MemoryLayout<UInt8>.size }
	public var value: UInt8 { return self.rawValue }
	case none = 0, mulan = 1, rapunzel = 2, belle = 3, bookfan = 4, other = 5, unused = 6
}

public struct Rapunzel: Readable {
	private var _accessor: Struct
	public static var size = 4
	public static var alignment = 4	
	public init(_ bb: ByteBuffer, o: Int32) { _accessor = Struct(bb: bb, position: o) }

	public var hairLength: Int32 { return _accessor.readBuffer(of: Int32.self, at: 0) }
	public func mutate(hairLength: Int32) -> Bool { return _accessor.mutate(hairLength, index: 0) }
}

public struct BookReader: Readable {
	private var _accessor: Struct
	public static var size = 4
	public static var alignment = 4	
	public init(_ bb: ByteBuffer, o: Int32) { _accessor = Struct(bb: bb, position: o) }

	public var booksRead: Int32 { return _accessor.readBuffer(of: Int32.self, at: 0) }
	public func mutate(booksRead: Int32) -> Bool { return _accessor.mutate(booksRead, index: 0) }
}

public func createRapunzel(hairLength: Int32) -> UnsafeMutableRawPointer {
	let memory = UnsafeMutableRawPointer.allocate(byteCount: Rapunzel.size, alignment: Rapunzel.alignment)
	memory.initializeMemory(as: UInt8.self, repeating: 0, count: Rapunzel.size)
	memory.storeBytes(of: hairLength, toByteOffset: 0, as: Int32.self)
	return memory
}

public func createBookReader(booksRead: Int32) -> UnsafeMutableRawPointer {
	let memory = UnsafeMutableRawPointer.allocate(byteCount: BookReader.size, alignment: BookReader.alignment)
	memory.initializeMemory(as: UInt8.self, repeating: 0, count: BookReader.size)
	memory.storeBytes(of: booksRead, toByteOffset: 0, as: Int32.self)
	return memory
}

public struct Attacker: FlatBufferObject {
	private var _accessor: Table
	public static func finish(_ fbb: FlatBufferBuilder, end: Offset<UOffset>, prefix: Bool = false) { fbb.finish(offset: end, fileId: "MOVI", addPrefix: prefix) }
	public static func getRootAsAttacker(bb: ByteBuffer) -> Attacker { return Attacker(Table(bb: bb, position: Int32(bb.read(def: UOffset.self, position: bb.reader)) + Int32(bb.reader))) }

	private init(_ t: Table) { _accessor = t }
	public init(_ bb: ByteBuffer, o: Int32) { _accessor = Table(bb: bb, position: o) }

	public var swordAttackDamage: Int32 { let o = _accessor.offset(4); return o == 0 ? 0 : _accessor.readBuffer(of: Int32.self, at: o) }
	public func mutate(swordAttackDamage: Int32) -> Bool {let o = _accessor.offset(4);  return _accessor.mutate(swordAttackDamage, index: o) }
	public static func startAttacker(_ fbb: FlatBufferBuilder) -> UOffset { fbb.startTable(with: 1) }
	public static func add(swordAttackDamage: Int32, _ fbb: FlatBufferBuilder) { fbb.add(element: swordAttackDamage, def: 0, at: 0) }
	public static func endAttacker(_ fbb: FlatBufferBuilder, start: UOffset) -> Offset<UOffset> { let end = Offset<UOffset>(offset: fbb.endTable(at: start)); return end }
}

public struct Movie: FlatBufferObject {
	private var _accessor: Table
	public static func finish(_ fbb: FlatBufferBuilder, end: Offset<UOffset>, prefix: Bool = false) { fbb.finish(offset: end, fileId: "MOVI", addPrefix: prefix) }
	public static func getRootAsMovie(bb: ByteBuffer) -> Movie { return Movie(Table(bb: bb, position: Int32(bb.read(def: UOffset.self, position: bb.reader)) + Int32(bb.reader))) }

	private init(_ t: Table) { _accessor = t }
	public init(_ bb: ByteBuffer, o: Int32) { _accessor = Table(bb: bb, position: o) }

	public var mainCharacterType: Character { let o = _accessor.offset(4); return o == 0 ? Character(rawValue: 0)! : Character(rawValue: _accessor.readBuffer(of: UInt8.self, at: o)) ?? Character(rawValue: 0)! }
	public func mutate(mainCharacterType: Character) -> Bool {let o = _accessor.offset(4);  return _accessor.mutate(mainCharacterType.rawValue, index: o) }
	public func mainCharacter<T: FlatBufferObject>(type: T.Type) -> T? { let o = _accessor.offset(6); return o == 0 ? nil : _accessor.union(o) }
	public var charactersTypeCount: Int32 { let o = _accessor.offset(8); return o == 0 ? 0 : _accessor.vector(count: o) }
	public func charactersType(at index: Int32) -> Character? { let o = _accessor.offset(8); return o == 0 ? Character(rawValue: 0)! : Character(rawValue: _accessor.directRead(of: UInt8.self, offset: _accessor.vector(at: o) + index * 1)) }
	public var charactersCount: Int32 { let o = _accessor.offset(10); return o == 0 ? 0 : _accessor.vector(count: o) }
	public func characters<T: FlatBufferObject>(at index: Int32, type: T.Type) -> T? { let o = _accessor.offset(10); return o == 0 ? nil : _accessor.directUnion(_accessor.vector(at: o) + index * 4) }
	public static func startMovie(_ fbb: FlatBufferBuilder) -> UOffset { fbb.startTable(with: 4) }
	public static func add(mainCharacterType: Character, _ fbb: FlatBufferBuilder) { fbb.add(element: mainCharacterType.rawValue, def: 0, at: 0) }
	public static func add(mainCharacter: Offset<UOffset>, _ fbb: FlatBufferBuilder) { fbb.add(offset: mainCharacter, at: 1)  }
	public static func add(charactersType: Offset<UOffset>, _ fbb: FlatBufferBuilder) { fbb.add(offset: charactersType, at: 2)  }
	public static func add(characters: Offset<UOffset>, _ fbb: FlatBufferBuilder) { fbb.add(offset: characters, at: 3)  }
	public static func endMovie(_ fbb: FlatBufferBuilder, start: UOffset) -> Offset<UOffset> { let end = Offset<UOffset>(offset: fbb.endTable(at: start)); return end }
}

