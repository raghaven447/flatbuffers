// automatically generated by the FlatBuffers compiler, do not modify


#ifndef FLATBUFFERS_GENERATED_NAMESPACETEST1_NAMESPACEA_NAMESPACEB_H_
#define FLATBUFFERS_GENERATED_NAMESPACETEST1_NAMESPACEA_NAMESPACEB_H_

#include "flatbuffers/flatbuffers.h"

namespace NamespaceA {
namespace NamespaceB {

struct TableInNestedNS;

struct StructInNestedNS;

inline const flatbuffers::TypeTable *TableInNestedNSTypeTable();

inline const flatbuffers::TypeTable *StructInNestedNSTypeTable();

enum EnumInNestedNS {
  EnumInNestedNS_A = 0,
  EnumInNestedNS_B = 1,
  EnumInNestedNS_C = 2,
  EnumInNestedNS_MIN = EnumInNestedNS_A,
  EnumInNestedNS_MAX = EnumInNestedNS_C
};

inline const EnumInNestedNS (&EnumValuesEnumInNestedNS())[3] {
  static const EnumInNestedNS values[] = {
    EnumInNestedNS_A,
    EnumInNestedNS_B,
    EnumInNestedNS_C
  };
  return values;
}

inline const char * const *EnumNamesEnumInNestedNS() {
  static const char * const names[] = {
    "A",
    "B",
    "C",
    nullptr
  };
  return names;
}

inline const char *EnumNameEnumInNestedNS(EnumInNestedNS e) {
  if (e < EnumInNestedNS_A || e > EnumInNestedNS_C) return "";
  const size_t index = static_cast<int>(e);
  return EnumNamesEnumInNestedNS()[index];
}

FLATBUFFERS_MANUALLY_ALIGNED_STRUCT(4) StructInNestedNS FLATBUFFERS_FINAL_CLASS {
 private:
  int32_t a_;
  int32_t b_;

 public:
  StructInNestedNS() {
    memset(this, 0, sizeof(StructInNestedNS));
  }
  StructInNestedNS(int32_t _a, int32_t _b)
      : a_(flatbuffers::EndianScalar(_a)),
        b_(flatbuffers::EndianScalar(_b)) {
  }
  int32_t a() const {
    return flatbuffers::EndianScalar(a_);
  }
  void mutate_a(int32_t _a) {
    flatbuffers::WriteScalar(&a_, _a);
  }
  int32_t b() const {
    return flatbuffers::EndianScalar(b_);
  }
  void mutate_b(int32_t _b) {
    flatbuffers::WriteScalar(&b_, _b);
  }
};
FLATBUFFERS_STRUCT_END(StructInNestedNS, 8);

struct TableInNestedNS FLATBUFFERS_FINAL_CLASS : private flatbuffers::Table {
  static const flatbuffers::TypeTable *MiniReflectTypeTable() {
    return TableInNestedNSTypeTable();
  }
  enum {
    VT_FOO = 4
  };
  int32_t foo() const {
    return GetField<int32_t>(VT_FOO, 0);
  }
  bool mutate_foo(int32_t _foo) {
    return SetField<int32_t>(VT_FOO, _foo, 0);
  }
  bool Verify(flatbuffers::Verifier &verifier) const {
    return VerifyTableStart(verifier) &&
           VerifyField<int32_t>(verifier, VT_FOO) &&
           verifier.EndTable();
  }
};

struct TableInNestedNSBuilder {
  flatbuffers::FlatBufferBuilder &fbb_;
  flatbuffers::uoffset_t start_;
  void add_foo(int32_t foo) {
    fbb_.AddElement<int32_t>(TableInNestedNS::VT_FOO, foo, 0);
  }
  explicit TableInNestedNSBuilder(flatbuffers::FlatBufferBuilder &_fbb)
        : fbb_(_fbb) {
    start_ = fbb_.StartTable();
  }
  TableInNestedNSBuilder &operator=(const TableInNestedNSBuilder &);
  flatbuffers::Offset<TableInNestedNS> Finish() {
    const auto end = fbb_.EndTable(start_);
    auto o = flatbuffers::Offset<TableInNestedNS>(end);
    return o;
  }
};

inline flatbuffers::Offset<TableInNestedNS> CreateTableInNestedNS(
    flatbuffers::FlatBufferBuilder &_fbb,
    int32_t foo = 0) {
  TableInNestedNSBuilder builder_(_fbb);
  builder_.add_foo(foo);
  return builder_.Finish();
}

inline const flatbuffers::TypeTable *EnumInNestedNSTypeTable() {
  static const flatbuffers::TypeCode type_codes[] = {
    { flatbuffers::ET_CHAR, 0, 0 },
    { flatbuffers::ET_CHAR, 0, 0 },
    { flatbuffers::ET_CHAR, 0, 0 }
  };
  static const flatbuffers::TypeFunction type_refs[] = {
    EnumInNestedNSTypeTable
  };
  static const char * const names[] = {
    "A",
    "B",
    "C"
  };
  static const flatbuffers::TypeTable tt = {
    flatbuffers::ST_ENUM, 3, type_codes, type_refs, nullptr, names
  };
  return &tt;
}

inline const flatbuffers::TypeTable *TableInNestedNSTypeTable() {
  static const flatbuffers::TypeCode type_codes[] = {
    { flatbuffers::ET_INT, 0, -1 }
  };
  static const char * const names[] = {
    "foo"
  };
  static const flatbuffers::TypeTable tt = {
    flatbuffers::ST_TABLE, 1, type_codes, nullptr, nullptr, names
  };
  return &tt;
}

inline const flatbuffers::TypeTable *StructInNestedNSTypeTable() {
  static const flatbuffers::TypeCode type_codes[] = {
    { flatbuffers::ET_INT, 0, -1 },
    { flatbuffers::ET_INT, 0, -1 }
  };
  static const int32_t values[] = { 0, 4, 8 };
  static const char * const names[] = {
    "a",
    "b"
  };
  static const flatbuffers::TypeTable tt = {
    flatbuffers::ST_STRUCT, 2, type_codes, nullptr, values, names
  };
  return &tt;
}

}  // namespace NamespaceB
}  // namespace NamespaceA

#endif  // FLATBUFFERS_GENERATED_NAMESPACETEST1_NAMESPACEA_NAMESPACEB_H_
