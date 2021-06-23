// automatically generated by the FlatBuffers compiler, do not modify
// ignore_for_file: unused_import, unused_field, unused_element, unused_local_variable

library my_game.example2;

import 'dart:typed_data' show Uint8List;
import 'package:flat_buffers/flat_buffers.dart' as fb;

import './monster_test_my_game_generated.dart' as my_game;
import './monster_test_my_game.example_generated.dart' as my_game_example;

class Monster {
  Monster._(this._bc, this._bcOffset);
  factory Monster(List<int> bytes) {
    fb.BufferContext rootRef = new fb.BufferContext.fromBytes(bytes);
    return reader.read(rootRef, 0);
  }

  static const fb.Reader<Monster> reader = const _MonsterReader();

  final fb.BufferContext _bc;
  final int _bcOffset;


  @override
  String toString() {
    return 'Monster{}';
  }

  MonsterT unpack() => MonsterT();

  static int pack(fb.Builder fbBuilder, MonsterT? object) {
    if (object == null) return 0;
    return object.pack(fbBuilder);
  }
}

class MonsterT {
  int pack(fb.Builder fbBuilder) {
    fbBuilder.startTable();
    return fbBuilder.endTable();
  }

  @override
  String toString() {
    return 'MonsterT{}';
  }
}

class _MonsterReader extends fb.TableReader<Monster> {
  const _MonsterReader();

  @override
  Monster createObject(fb.BufferContext bc, int offset) => 
    new Monster._(bc, offset);
}

class MonsterObjectBuilder extends fb.ObjectBuilder {

  MonsterObjectBuilder();

  /// Finish building, and store into the [fbBuilder].
  @override
  int finish(fb.Builder fbBuilder) {
    fbBuilder.startTable();
    return fbBuilder.endTable();
  }

  /// Convenience method to serialize to byte list.
  @override
  Uint8List toBytes([String? fileIdentifier]) {
    fb.Builder fbBuilder = new fb.Builder();
    int offset = finish(fbBuilder);
    return fbBuilder.finish(offset, fileIdentifier);
  }
}
