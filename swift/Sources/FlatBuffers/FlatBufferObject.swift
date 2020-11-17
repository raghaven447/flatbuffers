/*
 * Copyright 2020 Google Inc. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import Foundation

/// FlatbufferObject structures all the Flatbuffers objects
public protocol FlatBufferObject {
  var __buffer: ByteBuffer! { get }
  init(_ bb: ByteBuffer, o: Int32)
}

public protocol ObjectAPI {
  associatedtype T
  static func pack(_ builder: inout FlatBufferBuilder, obj: inout T) -> Offset<UOffset>
  mutating func unpack() -> T
}

/// Readable is structures all the Flatbuffers structs
///
/// Readable is a procotol that each Flatbuffer struct should confirm to since
/// FlatBufferBuilder would require a Type to both create(struct:) and createVector(structs:) functions
public protocol Readable: FlatBufferObject {
  static var size: Int { get }
  static var alignment: Int { get }
}

public protocol Enum {
  associatedtype T: Scalar
  static var byteSize: Int { get }
  var value: T { get }
}
