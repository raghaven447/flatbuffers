// automatically generated by the FlatBuffers compiler, do not modify
// ignore_for_file: unused_import, unused_field, unused_element, unused_local_variable

library keyword_test;

import 'dart:typed_data' show Uint8List;
import 'package:flat_buffers/flat_buffers.dart' as fb;


class Abc {
  final int value;
  const Abc._(this.value);

  factory Abc.fromValue(int value) {
    final result = values[value];
    if (result == null) {
        throw StateError('Invalid value $value for bit flag enum Abc');
    }
    return result;
  }

  static Abc? _createOrNull(int? value) => 
      value == null ? null : Abc.fromValue(value);

  static const int minValue = 0;
  static const int maxValue = 2;
  static bool containsValue(int value) => values.containsKey(value);

  static const Abc Void = Abc._(0);
  static const Abc Where = Abc._(1);
  static const Abc Stackalloc = Abc._(2);
  static const Map<int, Abc> values = {
    0: Void,
    1: Where,
    2: Stackalloc};

  static const fb.Reader<Abc> reader = _AbcReader();

  @override
  String toString() {
    return 'Abc{value: $value}';
  }
}

class _AbcReader extends fb.Reader<Abc> {
  const _AbcReader();

  @override
  int get size => 4;

  @override
  Abc read(fb.BufferContext bc, int offset) =>
      Abc.fromValue(const fb.Int32Reader().read(bc, offset));
}

class Public {
  final int value;
  const Public._(this.value);

  factory Public.fromValue(int value) {
    final result = values[value];
    if (result == null) {
        throw StateError('Invalid value $value for bit flag enum Public');
    }
    return result;
  }

  static Public? _createOrNull(int? value) => 
      value == null ? null : Public.fromValue(value);

  static const int minValue = 0;
  static const int maxValue = 0;
  static bool containsValue(int value) => values.containsKey(value);

  static const Public None = Public._(0);
  static const Map<int, Public> values = {
    0: None};

  static const fb.Reader<Public> reader = _PublicReader();

  @override
  String toString() {
    return 'Public{value: $value}';
  }
}

class _PublicReader extends fb.Reader<Public> {
  const _PublicReader();

  @override
  int get size => 4;

  @override
  Public read(fb.BufferContext bc, int offset) =>
      Public.fromValue(const fb.Int32Reader().read(bc, offset));
}

class KeywordsInUnionTypeId {
  final int value;
  const KeywordsInUnionTypeId._(this.value);

  factory KeywordsInUnionTypeId.fromValue(int value) {
    final result = values[value];
    if (result == null) {
        throw StateError('Invalid value $value for bit flag enum KeywordsInUnionTypeId');
    }
    return result;
  }

  static KeywordsInUnionTypeId? _createOrNull(int? value) => 
      value == null ? null : KeywordsInUnionTypeId.fromValue(value);

  static const int minValue = 0;
  static const int maxValue = 2;
  static bool containsValue(int value) => values.containsKey(value);

  static const KeywordsInUnionTypeId None = KeywordsInUnionTypeId._(0);
  static const KeywordsInUnionTypeId Static = KeywordsInUnionTypeId._(1);
  static const KeywordsInUnionTypeId Internal = KeywordsInUnionTypeId._(2);
  static const Map<int, KeywordsInUnionTypeId> values = {
    0: None,
    1: Static,
    2: Internal};

  static const fb.Reader<KeywordsInUnionTypeId> reader = _KeywordsInUnionTypeIdReader();

  @override
  String toString() {
    return 'KeywordsInUnionTypeId{value: $value}';
  }
}

class _KeywordsInUnionTypeIdReader extends fb.Reader<KeywordsInUnionTypeId> {
  const _KeywordsInUnionTypeIdReader();

  @override
  int get size => 1;

  @override
  KeywordsInUnionTypeId read(fb.BufferContext bc, int offset) =>
      KeywordsInUnionTypeId.fromValue(const fb.Uint8Reader().read(bc, offset));
}

class KeywordsInTable {
  KeywordsInTable._(this._bc, this._bcOffset);
  factory KeywordsInTable(List<int> bytes) {
    final rootRef = fb.BufferContext.fromBytes(bytes);
    return reader.read(rootRef, 0);
  }

  static const fb.Reader<KeywordsInTable> reader = _KeywordsInTableReader();

  final fb.BufferContext _bc;
  final int _bcOffset;

  ABC get $is => ABC.fromValue(const fb.Int32Reader().vTableGet(_bc, _bcOffset, 4, 0));
  public get private => public.fromValue(const fb.Int32Reader().vTableGet(_bc, _bcOffset, 6, 0));
  int get type => const fb.Int32Reader().vTableGet(_bc, _bcOffset, 8, 0);
  bool get $default => const fb.BoolReader().vTableGet(_bc, _bcOffset, 10, false);

  @override
  String toString() {
    return 'KeywordsInTable{\$is: $$is, private: $private, type: $type, \$default: $$default}';
  }

  KeywordsInTableT unpack() => KeywordsInTableT(
      $is: $is,
      private: private,
      type: type,
      $default: $default);

  static int pack(fb.Builder fbBuilder, KeywordsInTableT? object) {
    if (object == null) return 0;
    return object.pack(fbBuilder);
  }
}

class KeywordsInTableT implements fb.Packable {
  ABC $is;
  public private;
  int type;
  bool $default;

  KeywordsInTableT({
      this.$is = Abc.Void,
      this.private = Public.None,
      this.type = 0,
      this.$default = false});

  @override
  int pack(fb.Builder fbBuilder) {
    fbBuilder.startTable(4);
    fbBuilder.addInt32(0, $is.value);
    fbBuilder.addInt32(1, private.value);
    fbBuilder.addInt32(2, type);
    fbBuilder.addBool(3, $default);
    return fbBuilder.endTable();
  }

  @override
  String toString() {
    return 'KeywordsInTableT{\$is: $$is, private: $private, type: $type, \$default: $$default}';
  }
}

class _KeywordsInTableReader extends fb.TableReader<KeywordsInTable> {
  const _KeywordsInTableReader();

  @override
  KeywordsInTable createObject(fb.BufferContext bc, int offset) => 
    KeywordsInTable._(bc, offset);
}

class KeywordsInTableBuilder {
  KeywordsInTableBuilder(this.fbBuilder);

  final fb.Builder fbBuilder;

  void begin() {
    fbBuilder.startTable(4);
  }

  int addIs(ABC? $is) {
    fbBuilder.addInt32(0, $is?.value);
    return fbBuilder.offset;
  }
  int addPrivate(public? private) {
    fbBuilder.addInt32(1, private?.value);
    return fbBuilder.offset;
  }
  int addType(int? type) {
    fbBuilder.addInt32(2, type);
    return fbBuilder.offset;
  }
  int addDefault(bool? $default) {
    fbBuilder.addBool(3, $default);
    return fbBuilder.offset;
  }

  int finish() {
    return fbBuilder.endTable();
  }
}

class KeywordsInTableObjectBuilder extends fb.ObjectBuilder {
  final ABC? _$is;
  final public? _private;
  final int? _type;
  final bool? _$default;

  KeywordsInTableObjectBuilder({
    ABC? $is,
    public? private,
    int? type,
    bool? $default,
  })
      : _$is = $is,
        _private = private,
        _type = type,
        _$default = $default;

  /// Finish building, and store into the [fbBuilder].
  @override
  int finish(fb.Builder fbBuilder) {
    fbBuilder.startTable(4);
    fbBuilder.addInt32(0, _$is?.value);
    fbBuilder.addInt32(1, _private?.value);
    fbBuilder.addInt32(2, _type);
    fbBuilder.addBool(3, _$default);
    return fbBuilder.endTable();
  }

  /// Convenience method to serialize to byte list.
  @override
  Uint8List toBytes([String? fileIdentifier]) {
    final fbBuilder = fb.Builder(deduplicateTables: false);
    fbBuilder.finish(finish(fbBuilder), fileIdentifier);
    return fbBuilder.buffer;
  }
}
