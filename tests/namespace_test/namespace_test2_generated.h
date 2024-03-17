// automatically generated by the FlatBuffers compiler, do not modify


#ifndef FLATBUFFERS_GENERATED_NAMESPACETEST2_NAMESPACEA_H_
#define FLATBUFFERS_GENERATED_NAMESPACETEST2_NAMESPACEA_H_

#include "flatbuffers/flatbuffers.h"

// Ensure the included flatbuffers.h is the same version as when this file was
// generated, otherwise it may not be compatible.
static_assert(FLATBUFFERS_VERSION_MAJOR == 24 &&
              FLATBUFFERS_VERSION_MINOR == 3 &&
              FLATBUFFERS_VERSION_REVISION == 7,
             "Non-compatible flatbuffers version included");

namespace NamespaceA {

struct TableInFirstNS;
struct TableInFirstNSBuilder;
struct TableInFirstNST;

}  // namespace NamespaceA

namespace NamespaceC {

struct TableInC;
struct TableInCBuilder;
struct TableInCT;

}  // namespace NamespaceC

namespace NamespaceA {

struct SecondTableInA;
struct SecondTableInABuilder;
struct SecondTableInAT;

bool operator==(const TableInFirstNST &lhs, const TableInFirstNST &rhs);
bool operator!=(const TableInFirstNST &lhs, const TableInFirstNST &rhs);
}  // namespace NamespaceA

namespace NamespaceC {

bool operator==(const TableInCT &lhs, const TableInCT &rhs);
bool operator!=(const TableInCT &lhs, const TableInCT &rhs);
}  // namespace NamespaceC

namespace NamespaceA {

bool operator==(const SecondTableInAT &lhs, const SecondTableInAT &rhs);
bool operator!=(const SecondTableInAT &lhs, const SecondTableInAT &rhs);

inline const ::flatbuffers::TypeTable *TableInFirstNSTypeTable();

}  // namespace NamespaceA

namespace NamespaceC {

inline const ::flatbuffers::TypeTable *TableInCTypeTable();

}  // namespace NamespaceC

namespace NamespaceA {

inline const ::flatbuffers::TypeTable *SecondTableInATypeTable();

struct TableInFirstNST : public ::flatbuffers::NativeTable {
  typedef TableInFirstNS TableType;
  static FLATBUFFERS_CONSTEXPR_CPP11 const char *GetFullyQualifiedName() {
    return "NamespaceA.TableInFirstNST";
  }
  std::unique_ptr<NamespaceA::NamespaceB::TableInNestedNST> foo_table{};
  NamespaceA::NamespaceB::EnumInNestedNS foo_enum = NamespaceA::NamespaceB::EnumInNestedNS_A;
  NamespaceA::NamespaceB::UnionInNestedNSUnion foo_union{};
  std::unique_ptr<NamespaceA::NamespaceB::StructInNestedNS> foo_struct{};
  TableInFirstNST() = default;
  TableInFirstNST(const TableInFirstNST &o);
  TableInFirstNST(TableInFirstNST&&) FLATBUFFERS_NOEXCEPT = default;
  TableInFirstNST &operator=(TableInFirstNST o) FLATBUFFERS_NOEXCEPT;
};

struct TableInFirstNS FLATBUFFERS_FINAL_CLASS : private ::flatbuffers::Table {
  typedef TableInFirstNST NativeTableType;
  typedef TableInFirstNSBuilder Builder;
  static const ::flatbuffers::TypeTable *MiniReflectTypeTable() {
    return TableInFirstNSTypeTable();
  }
  static FLATBUFFERS_CONSTEXPR_CPP11 const char *GetFullyQualifiedName() {
    return "NamespaceA.TableInFirstNS";
  }
  enum FlatBuffersVTableOffset FLATBUFFERS_VTABLE_UNDERLYING_TYPE {
    VT_FOO_TABLE = 4,
    VT_FOO_ENUM = 6,
    VT_FOO_UNION_TYPE = 8,
    VT_FOO_UNION = 10,
    VT_FOO_STRUCT = 12
  };
  const NamespaceA::NamespaceB::TableInNestedNS *foo_table() const {
    return GetPointer<const NamespaceA::NamespaceB::TableInNestedNS *>(VT_FOO_TABLE);
  }
  NamespaceA::NamespaceB::TableInNestedNS *mutable_foo_table() {
    return GetPointer<NamespaceA::NamespaceB::TableInNestedNS *>(VT_FOO_TABLE);
  }
  NamespaceA::NamespaceB::EnumInNestedNS foo_enum() const {
    return static_cast<NamespaceA::NamespaceB::EnumInNestedNS>(GetField<int8_t>(VT_FOO_ENUM, 0));
  }
  bool mutate_foo_enum(NamespaceA::NamespaceB::EnumInNestedNS _foo_enum = static_cast<NamespaceA::NamespaceB::EnumInNestedNS>(0)) {
    return SetField<int8_t>(VT_FOO_ENUM, static_cast<int8_t>(_foo_enum), 0);
  }
  NamespaceA::NamespaceB::UnionInNestedNS foo_union_type() const {
    return static_cast<NamespaceA::NamespaceB::UnionInNestedNS>(GetField<uint8_t>(VT_FOO_UNION_TYPE, 0));
  }
  const void *foo_union() const {
    return GetPointer<const void *>(VT_FOO_UNION);
  }
  template<typename T> const T *foo_union_as() const;
  const NamespaceA::NamespaceB::TableInNestedNS *foo_union_as_TableInNestedNS() const {
    return foo_union_type() == NamespaceA::NamespaceB::UnionInNestedNS_TableInNestedNS ? static_cast<const NamespaceA::NamespaceB::TableInNestedNS *>(foo_union()) : nullptr;
  }
  void *mutable_foo_union() {
    return GetPointer<void *>(VT_FOO_UNION);
  }
  const NamespaceA::NamespaceB::StructInNestedNS *foo_struct() const {
    return GetStruct<const NamespaceA::NamespaceB::StructInNestedNS *>(VT_FOO_STRUCT);
  }
  NamespaceA::NamespaceB::StructInNestedNS *mutable_foo_struct() {
    return GetStruct<NamespaceA::NamespaceB::StructInNestedNS *>(VT_FOO_STRUCT);
  }
  bool Verify(::flatbuffers::Verifier &verifier) const {
    return VerifyTableStart(verifier) &&
           VerifyOffset(verifier, VT_FOO_TABLE) &&
           verifier.VerifyTable(foo_table()) &&
           VerifyField<int8_t>(verifier, VT_FOO_ENUM, 1) &&
           VerifyField<uint8_t>(verifier, VT_FOO_UNION_TYPE, 1) &&
           VerifyOffset(verifier, VT_FOO_UNION) &&
           VerifyUnionInNestedNS(verifier, foo_union(), foo_union_type()) &&
           VerifyField<NamespaceA::NamespaceB::StructInNestedNS>(verifier, VT_FOO_STRUCT, 4) &&
           verifier.EndTable();
  }
  TableInFirstNST *UnPack(const ::flatbuffers::resolver_function_t *_resolver = nullptr) const;
  void UnPackTo(TableInFirstNST *_o, const ::flatbuffers::resolver_function_t *_resolver = nullptr) const;
  static ::flatbuffers::Offset<TableInFirstNS> Pack(::flatbuffers::FlatBufferBuilder &_fbb, const TableInFirstNST* _o, const ::flatbuffers::rehasher_function_t *_rehasher = nullptr);
};

template<> inline const NamespaceA::NamespaceB::TableInNestedNS *TableInFirstNS::foo_union_as<NamespaceA::NamespaceB::TableInNestedNS>() const {
  return foo_union_as_TableInNestedNS();
}

struct TableInFirstNSBuilder {
  typedef TableInFirstNS Table;
  ::flatbuffers::FlatBufferBuilder &fbb_;
  ::flatbuffers::uoffset_t start_;
  void add_foo_table(::flatbuffers::Offset<NamespaceA::NamespaceB::TableInNestedNS> foo_table) {
    fbb_.AddOffset(TableInFirstNS::VT_FOO_TABLE, foo_table);
  }
  void add_foo_enum(NamespaceA::NamespaceB::EnumInNestedNS foo_enum) {
    fbb_.AddElement<int8_t>(TableInFirstNS::VT_FOO_ENUM, static_cast<int8_t>(foo_enum), 0);
  }
  void add_foo_union_type(NamespaceA::NamespaceB::UnionInNestedNS foo_union_type) {
    fbb_.AddElement<uint8_t>(TableInFirstNS::VT_FOO_UNION_TYPE, static_cast<uint8_t>(foo_union_type), 0);
  }
  void add_foo_union(::flatbuffers::Offset<void> foo_union) {
    fbb_.AddOffset(TableInFirstNS::VT_FOO_UNION, foo_union);
  }
  void add_foo_struct(const NamespaceA::NamespaceB::StructInNestedNS *foo_struct) {
    fbb_.AddStruct(TableInFirstNS::VT_FOO_STRUCT, foo_struct);
  }
  explicit TableInFirstNSBuilder(::flatbuffers::FlatBufferBuilder &_fbb)
        : fbb_(_fbb) {
    start_ = fbb_.StartTable();
  }
  ::flatbuffers::Offset<TableInFirstNS> Finish() {
    const auto end = fbb_.EndTable(start_);
    auto o = ::flatbuffers::Offset<TableInFirstNS>(end);
    return o;
  }
};

inline ::flatbuffers::Offset<TableInFirstNS> CreateTableInFirstNS(
    ::flatbuffers::FlatBufferBuilder &_fbb,
    ::flatbuffers::Offset<NamespaceA::NamespaceB::TableInNestedNS> foo_table = 0,
    NamespaceA::NamespaceB::EnumInNestedNS foo_enum = NamespaceA::NamespaceB::EnumInNestedNS_A,
    NamespaceA::NamespaceB::UnionInNestedNS foo_union_type = NamespaceA::NamespaceB::UnionInNestedNS_NONE,
    ::flatbuffers::Offset<void> foo_union = 0,
    const NamespaceA::NamespaceB::StructInNestedNS *foo_struct = nullptr) {
  TableInFirstNSBuilder builder_(_fbb);
  builder_.add_foo_struct(foo_struct);
  builder_.add_foo_union(foo_union);
  builder_.add_foo_table(foo_table);
  builder_.add_foo_union_type(foo_union_type);
  builder_.add_foo_enum(foo_enum);
  return builder_.Finish();
}

::flatbuffers::Offset<TableInFirstNS> CreateTableInFirstNS(::flatbuffers::FlatBufferBuilder &_fbb, const TableInFirstNST *_o, const ::flatbuffers::rehasher_function_t *_rehasher = nullptr);

}  // namespace NamespaceA

namespace NamespaceC {

struct TableInCT : public ::flatbuffers::NativeTable {
  typedef TableInC TableType;
  static FLATBUFFERS_CONSTEXPR_CPP11 const char *GetFullyQualifiedName() {
    return "NamespaceC.TableInCT";
  }
  std::unique_ptr<NamespaceA::TableInFirstNST> refer_to_a1{};
  std::unique_ptr<NamespaceA::SecondTableInAT> refer_to_a2{};
  TableInCT() = default;
  TableInCT(const TableInCT &o);
  TableInCT(TableInCT&&) FLATBUFFERS_NOEXCEPT = default;
  TableInCT &operator=(TableInCT o) FLATBUFFERS_NOEXCEPT;
};

struct TableInC FLATBUFFERS_FINAL_CLASS : private ::flatbuffers::Table {
  typedef TableInCT NativeTableType;
  typedef TableInCBuilder Builder;
  static const ::flatbuffers::TypeTable *MiniReflectTypeTable() {
    return TableInCTypeTable();
  }
  static FLATBUFFERS_CONSTEXPR_CPP11 const char *GetFullyQualifiedName() {
    return "NamespaceC.TableInC";
  }
  enum FlatBuffersVTableOffset FLATBUFFERS_VTABLE_UNDERLYING_TYPE {
    VT_REFER_TO_A1 = 4,
    VT_REFER_TO_A2 = 6
  };
  const NamespaceA::TableInFirstNS *refer_to_a1() const {
    return GetPointer<const NamespaceA::TableInFirstNS *>(VT_REFER_TO_A1);
  }
  NamespaceA::TableInFirstNS *mutable_refer_to_a1() {
    return GetPointer<NamespaceA::TableInFirstNS *>(VT_REFER_TO_A1);
  }
  const NamespaceA::SecondTableInA *refer_to_a2() const {
    return GetPointer<const NamespaceA::SecondTableInA *>(VT_REFER_TO_A2);
  }
  NamespaceA::SecondTableInA *mutable_refer_to_a2() {
    return GetPointer<NamespaceA::SecondTableInA *>(VT_REFER_TO_A2);
  }
  bool Verify(::flatbuffers::Verifier &verifier) const {
    return VerifyTableStart(verifier) &&
           VerifyOffset(verifier, VT_REFER_TO_A1) &&
           verifier.VerifyTable(refer_to_a1()) &&
           VerifyOffset(verifier, VT_REFER_TO_A2) &&
           verifier.VerifyTable(refer_to_a2()) &&
           verifier.EndTable();
  }
  TableInCT *UnPack(const ::flatbuffers::resolver_function_t *_resolver = nullptr) const;
  void UnPackTo(TableInCT *_o, const ::flatbuffers::resolver_function_t *_resolver = nullptr) const;
  static ::flatbuffers::Offset<TableInC> Pack(::flatbuffers::FlatBufferBuilder &_fbb, const TableInCT* _o, const ::flatbuffers::rehasher_function_t *_rehasher = nullptr);
};

struct TableInCBuilder {
  typedef TableInC Table;
  ::flatbuffers::FlatBufferBuilder &fbb_;
  ::flatbuffers::uoffset_t start_;
  void add_refer_to_a1(::flatbuffers::Offset<NamespaceA::TableInFirstNS> refer_to_a1) {
    fbb_.AddOffset(TableInC::VT_REFER_TO_A1, refer_to_a1);
  }
  void add_refer_to_a2(::flatbuffers::Offset<NamespaceA::SecondTableInA> refer_to_a2) {
    fbb_.AddOffset(TableInC::VT_REFER_TO_A2, refer_to_a2);
  }
  explicit TableInCBuilder(::flatbuffers::FlatBufferBuilder &_fbb)
        : fbb_(_fbb) {
    start_ = fbb_.StartTable();
  }
  ::flatbuffers::Offset<TableInC> Finish() {
    const auto end = fbb_.EndTable(start_);
    auto o = ::flatbuffers::Offset<TableInC>(end);
    return o;
  }
};

inline ::flatbuffers::Offset<TableInC> CreateTableInC(
    ::flatbuffers::FlatBufferBuilder &_fbb,
    ::flatbuffers::Offset<NamespaceA::TableInFirstNS> refer_to_a1 = 0,
    ::flatbuffers::Offset<NamespaceA::SecondTableInA> refer_to_a2 = 0) {
  TableInCBuilder builder_(_fbb);
  builder_.add_refer_to_a2(refer_to_a2);
  builder_.add_refer_to_a1(refer_to_a1);
  return builder_.Finish();
}

::flatbuffers::Offset<TableInC> CreateTableInC(::flatbuffers::FlatBufferBuilder &_fbb, const TableInCT *_o, const ::flatbuffers::rehasher_function_t *_rehasher = nullptr);

}  // namespace NamespaceC

namespace NamespaceA {

struct SecondTableInAT : public ::flatbuffers::NativeTable {
  typedef SecondTableInA TableType;
  static FLATBUFFERS_CONSTEXPR_CPP11 const char *GetFullyQualifiedName() {
    return "NamespaceA.SecondTableInAT";
  }
  std::unique_ptr<NamespaceC::TableInCT> refer_to_c{};
  SecondTableInAT() = default;
  SecondTableInAT(const SecondTableInAT &o);
  SecondTableInAT(SecondTableInAT&&) FLATBUFFERS_NOEXCEPT = default;
  SecondTableInAT &operator=(SecondTableInAT o) FLATBUFFERS_NOEXCEPT;
};

struct SecondTableInA FLATBUFFERS_FINAL_CLASS : private ::flatbuffers::Table {
  typedef SecondTableInAT NativeTableType;
  typedef SecondTableInABuilder Builder;
  static const ::flatbuffers::TypeTable *MiniReflectTypeTable() {
    return SecondTableInATypeTable();
  }
  static FLATBUFFERS_CONSTEXPR_CPP11 const char *GetFullyQualifiedName() {
    return "NamespaceA.SecondTableInA";
  }
  enum FlatBuffersVTableOffset FLATBUFFERS_VTABLE_UNDERLYING_TYPE {
    VT_REFER_TO_C = 4
  };
  const NamespaceC::TableInC *refer_to_c() const {
    return GetPointer<const NamespaceC::TableInC *>(VT_REFER_TO_C);
  }
  NamespaceC::TableInC *mutable_refer_to_c() {
    return GetPointer<NamespaceC::TableInC *>(VT_REFER_TO_C);
  }
  bool Verify(::flatbuffers::Verifier &verifier) const {
    return VerifyTableStart(verifier) &&
           VerifyOffset(verifier, VT_REFER_TO_C) &&
           verifier.VerifyTable(refer_to_c()) &&
           verifier.EndTable();
  }
  SecondTableInAT *UnPack(const ::flatbuffers::resolver_function_t *_resolver = nullptr) const;
  void UnPackTo(SecondTableInAT *_o, const ::flatbuffers::resolver_function_t *_resolver = nullptr) const;
  static ::flatbuffers::Offset<SecondTableInA> Pack(::flatbuffers::FlatBufferBuilder &_fbb, const SecondTableInAT* _o, const ::flatbuffers::rehasher_function_t *_rehasher = nullptr);
};

struct SecondTableInABuilder {
  typedef SecondTableInA Table;
  ::flatbuffers::FlatBufferBuilder &fbb_;
  ::flatbuffers::uoffset_t start_;
  void add_refer_to_c(::flatbuffers::Offset<NamespaceC::TableInC> refer_to_c) {
    fbb_.AddOffset(SecondTableInA::VT_REFER_TO_C, refer_to_c);
  }
  explicit SecondTableInABuilder(::flatbuffers::FlatBufferBuilder &_fbb)
        : fbb_(_fbb) {
    start_ = fbb_.StartTable();
  }
  ::flatbuffers::Offset<SecondTableInA> Finish() {
    const auto end = fbb_.EndTable(start_);
    auto o = ::flatbuffers::Offset<SecondTableInA>(end);
    return o;
  }
};

inline ::flatbuffers::Offset<SecondTableInA> CreateSecondTableInA(
    ::flatbuffers::FlatBufferBuilder &_fbb,
    ::flatbuffers::Offset<NamespaceC::TableInC> refer_to_c = 0) {
  SecondTableInABuilder builder_(_fbb);
  builder_.add_refer_to_c(refer_to_c);
  return builder_.Finish();
}

::flatbuffers::Offset<SecondTableInA> CreateSecondTableInA(::flatbuffers::FlatBufferBuilder &_fbb, const SecondTableInAT *_o, const ::flatbuffers::rehasher_function_t *_rehasher = nullptr);


inline bool operator==(const TableInFirstNST &lhs, const TableInFirstNST &rhs) {
  return
      ((lhs.foo_table == rhs.foo_table) || (lhs.foo_table && rhs.foo_table && *lhs.foo_table == *rhs.foo_table)) &&
      (lhs.foo_enum == rhs.foo_enum) &&
      (lhs.foo_union == rhs.foo_union) &&
      ((lhs.foo_struct == rhs.foo_struct) || (lhs.foo_struct && rhs.foo_struct && *lhs.foo_struct == *rhs.foo_struct));
}

inline bool operator!=(const TableInFirstNST &lhs, const TableInFirstNST &rhs) {
    return !(lhs == rhs);
}


inline TableInFirstNST::TableInFirstNST(const TableInFirstNST &o)
      : foo_table((o.foo_table) ? new NamespaceA::NamespaceB::TableInNestedNST(*o.foo_table) : nullptr),
        foo_enum(o.foo_enum),
        foo_union(o.foo_union),
        foo_struct((o.foo_struct) ? new NamespaceA::NamespaceB::StructInNestedNS(*o.foo_struct) : nullptr) {
}

inline TableInFirstNST &TableInFirstNST::operator=(TableInFirstNST o) FLATBUFFERS_NOEXCEPT {
  std::swap(foo_table, o.foo_table);
  std::swap(foo_enum, o.foo_enum);
  std::swap(foo_union, o.foo_union);
  std::swap(foo_struct, o.foo_struct);
  return *this;
}

inline TableInFirstNST *TableInFirstNS::UnPack(const ::flatbuffers::resolver_function_t *_resolver) const {
  auto _o = std::unique_ptr<TableInFirstNST>(new TableInFirstNST());
  UnPackTo(_o.get(), _resolver);
  return _o.release();
}

inline void TableInFirstNS::UnPackTo(TableInFirstNST *_o, const ::flatbuffers::resolver_function_t *_resolver) const {
  (void)_o;
  (void)_resolver;
  { auto _e = foo_table(); if (_e) { if(_o->foo_table) { _e->UnPackTo(_o->foo_table.get(), _resolver); } else { _o->foo_table = std::unique_ptr<NamespaceA::NamespaceB::TableInNestedNST>(_e->UnPack(_resolver)); } } else if (_o->foo_table) { _o->foo_table.reset(); } }
  { auto _e = foo_enum(); _o->foo_enum = _e; }
  { auto _e = foo_union_type(); _o->foo_union.type = _e; }
  { auto _e = foo_union(); if (_e) _o->foo_union.value = NamespaceA::NamespaceB::UnionInNestedNSUnion::UnPack(_e, foo_union_type(), _resolver); }
  { auto _e = foo_struct(); if (_e) _o->foo_struct = std::unique_ptr<NamespaceA::NamespaceB::StructInNestedNS>(new NamespaceA::NamespaceB::StructInNestedNS(*_e)); }
}

inline ::flatbuffers::Offset<TableInFirstNS> TableInFirstNS::Pack(::flatbuffers::FlatBufferBuilder &_fbb, const TableInFirstNST* _o, const ::flatbuffers::rehasher_function_t *_rehasher) {
  return CreateTableInFirstNS(_fbb, _o, _rehasher);
}

inline ::flatbuffers::Offset<TableInFirstNS> CreateTableInFirstNS(::flatbuffers::FlatBufferBuilder &_fbb, const TableInFirstNST *_o, const ::flatbuffers::rehasher_function_t *_rehasher) {
  (void)_rehasher;
  (void)_o;
  struct _VectorArgs { ::flatbuffers::FlatBufferBuilder *__fbb; const TableInFirstNST* __o; const ::flatbuffers::rehasher_function_t *__rehasher; } _va = { &_fbb, _o, _rehasher}; (void)_va;
  auto _foo_table = _o->foo_table ? CreateTableInNestedNS(_fbb, _o->foo_table.get(), _rehasher) : 0;
  auto _foo_enum = _o->foo_enum;
  auto _foo_union_type = _o->foo_union.type;
  auto _foo_union = _o->foo_union.Pack(_fbb);
  auto _foo_struct = _o->foo_struct ? _o->foo_struct.get() : nullptr;
  return NamespaceA::CreateTableInFirstNS(
      _fbb,
      _foo_table,
      _foo_enum,
      _foo_union_type,
      _foo_union,
      _foo_struct);
}

}  // namespace NamespaceA

namespace NamespaceC {


inline bool operator==(const TableInCT &lhs, const TableInCT &rhs) {
  return
      ((lhs.refer_to_a1 == rhs.refer_to_a1) || (lhs.refer_to_a1 && rhs.refer_to_a1 && *lhs.refer_to_a1 == *rhs.refer_to_a1)) &&
      ((lhs.refer_to_a2 == rhs.refer_to_a2) || (lhs.refer_to_a2 && rhs.refer_to_a2 && *lhs.refer_to_a2 == *rhs.refer_to_a2));
}

inline bool operator!=(const TableInCT &lhs, const TableInCT &rhs) {
    return !(lhs == rhs);
}


inline TableInCT::TableInCT(const TableInCT &o)
      : refer_to_a1((o.refer_to_a1) ? new NamespaceA::TableInFirstNST(*o.refer_to_a1) : nullptr),
        refer_to_a2((o.refer_to_a2) ? new NamespaceA::SecondTableInAT(*o.refer_to_a2) : nullptr) {
}

inline TableInCT &TableInCT::operator=(TableInCT o) FLATBUFFERS_NOEXCEPT {
  std::swap(refer_to_a1, o.refer_to_a1);
  std::swap(refer_to_a2, o.refer_to_a2);
  return *this;
}

inline TableInCT *TableInC::UnPack(const ::flatbuffers::resolver_function_t *_resolver) const {
  auto _o = std::unique_ptr<TableInCT>(new TableInCT());
  UnPackTo(_o.get(), _resolver);
  return _o.release();
}

inline void TableInC::UnPackTo(TableInCT *_o, const ::flatbuffers::resolver_function_t *_resolver) const {
  (void)_o;
  (void)_resolver;
  { auto _e = refer_to_a1(); if (_e) { if(_o->refer_to_a1) { _e->UnPackTo(_o->refer_to_a1.get(), _resolver); } else { _o->refer_to_a1 = std::unique_ptr<NamespaceA::TableInFirstNST>(_e->UnPack(_resolver)); } } else if (_o->refer_to_a1) { _o->refer_to_a1.reset(); } }
  { auto _e = refer_to_a2(); if (_e) { if(_o->refer_to_a2) { _e->UnPackTo(_o->refer_to_a2.get(), _resolver); } else { _o->refer_to_a2 = std::unique_ptr<NamespaceA::SecondTableInAT>(_e->UnPack(_resolver)); } } else if (_o->refer_to_a2) { _o->refer_to_a2.reset(); } }
}

inline ::flatbuffers::Offset<TableInC> TableInC::Pack(::flatbuffers::FlatBufferBuilder &_fbb, const TableInCT* _o, const ::flatbuffers::rehasher_function_t *_rehasher) {
  return CreateTableInC(_fbb, _o, _rehasher);
}

inline ::flatbuffers::Offset<TableInC> CreateTableInC(::flatbuffers::FlatBufferBuilder &_fbb, const TableInCT *_o, const ::flatbuffers::rehasher_function_t *_rehasher) {
  (void)_rehasher;
  (void)_o;
  struct _VectorArgs { ::flatbuffers::FlatBufferBuilder *__fbb; const TableInCT* __o; const ::flatbuffers::rehasher_function_t *__rehasher; } _va = { &_fbb, _o, _rehasher}; (void)_va;
  auto _refer_to_a1 = _o->refer_to_a1 ? CreateTableInFirstNS(_fbb, _o->refer_to_a1.get(), _rehasher) : 0;
  auto _refer_to_a2 = _o->refer_to_a2 ? CreateSecondTableInA(_fbb, _o->refer_to_a2.get(), _rehasher) : 0;
  return NamespaceC::CreateTableInC(
      _fbb,
      _refer_to_a1,
      _refer_to_a2);
}

}  // namespace NamespaceC

namespace NamespaceA {


inline bool operator==(const SecondTableInAT &lhs, const SecondTableInAT &rhs) {
  return
      ((lhs.refer_to_c == rhs.refer_to_c) || (lhs.refer_to_c && rhs.refer_to_c && *lhs.refer_to_c == *rhs.refer_to_c));
}

inline bool operator!=(const SecondTableInAT &lhs, const SecondTableInAT &rhs) {
    return !(lhs == rhs);
}


inline SecondTableInAT::SecondTableInAT(const SecondTableInAT &o)
      : refer_to_c((o.refer_to_c) ? new NamespaceC::TableInCT(*o.refer_to_c) : nullptr) {
}

inline SecondTableInAT &SecondTableInAT::operator=(SecondTableInAT o) FLATBUFFERS_NOEXCEPT {
  std::swap(refer_to_c, o.refer_to_c);
  return *this;
}

inline SecondTableInAT *SecondTableInA::UnPack(const ::flatbuffers::resolver_function_t *_resolver) const {
  auto _o = std::unique_ptr<SecondTableInAT>(new SecondTableInAT());
  UnPackTo(_o.get(), _resolver);
  return _o.release();
}

inline void SecondTableInA::UnPackTo(SecondTableInAT *_o, const ::flatbuffers::resolver_function_t *_resolver) const {
  (void)_o;
  (void)_resolver;
  { auto _e = refer_to_c(); if (_e) { if(_o->refer_to_c) { _e->UnPackTo(_o->refer_to_c.get(), _resolver); } else { _o->refer_to_c = std::unique_ptr<NamespaceC::TableInCT>(_e->UnPack(_resolver)); } } else if (_o->refer_to_c) { _o->refer_to_c.reset(); } }
}

inline ::flatbuffers::Offset<SecondTableInA> SecondTableInA::Pack(::flatbuffers::FlatBufferBuilder &_fbb, const SecondTableInAT* _o, const ::flatbuffers::rehasher_function_t *_rehasher) {
  return CreateSecondTableInA(_fbb, _o, _rehasher);
}

inline ::flatbuffers::Offset<SecondTableInA> CreateSecondTableInA(::flatbuffers::FlatBufferBuilder &_fbb, const SecondTableInAT *_o, const ::flatbuffers::rehasher_function_t *_rehasher) {
  (void)_rehasher;
  (void)_o;
  struct _VectorArgs { ::flatbuffers::FlatBufferBuilder *__fbb; const SecondTableInAT* __o; const ::flatbuffers::rehasher_function_t *__rehasher; } _va = { &_fbb, _o, _rehasher}; (void)_va;
  auto _refer_to_c = _o->refer_to_c ? CreateTableInC(_fbb, _o->refer_to_c.get(), _rehasher) : 0;
  return NamespaceA::CreateSecondTableInA(
      _fbb,
      _refer_to_c);
}

inline const ::flatbuffers::TypeTable *TableInFirstNSTypeTable() {
  static const ::flatbuffers::TypeCode type_codes[] = {
    { ::flatbuffers::ET_SEQUENCE, 0, 0 },
    { ::flatbuffers::ET_CHAR, 0, 1 },
    { ::flatbuffers::ET_UTYPE, 0, 2 },
    { ::flatbuffers::ET_SEQUENCE, 0, 2 },
    { ::flatbuffers::ET_SEQUENCE, 0, 3 }
  };
  static const ::flatbuffers::TypeFunction type_refs[] = {
    NamespaceA::NamespaceB::TableInNestedNSTypeTable,
    NamespaceA::NamespaceB::EnumInNestedNSTypeTable,
    NamespaceA::NamespaceB::UnionInNestedNSTypeTable,
    NamespaceA::NamespaceB::StructInNestedNSTypeTable
  };
  static const char * const names[] = {
    "foo_table",
    "foo_enum",
    "foo_union_type",
    "foo_union",
    "foo_struct"
  };
  static const ::flatbuffers::TypeTable tt = {
    ::flatbuffers::ST_TABLE, 5, type_codes, type_refs, nullptr, nullptr, names
  };
  return &tt;
}

}  // namespace NamespaceA

namespace NamespaceC {

inline const ::flatbuffers::TypeTable *TableInCTypeTable() {
  static const ::flatbuffers::TypeCode type_codes[] = {
    { ::flatbuffers::ET_SEQUENCE, 0, 0 },
    { ::flatbuffers::ET_SEQUENCE, 0, 1 }
  };
  static const ::flatbuffers::TypeFunction type_refs[] = {
    NamespaceA::TableInFirstNSTypeTable,
    NamespaceA::SecondTableInATypeTable
  };
  static const char * const names[] = {
    "refer_to_a1",
    "refer_to_a2"
  };
  static const ::flatbuffers::TypeTable tt = {
    ::flatbuffers::ST_TABLE, 2, type_codes, type_refs, nullptr, nullptr, names
  };
  return &tt;
}

}  // namespace NamespaceC

namespace NamespaceA {

inline const ::flatbuffers::TypeTable *SecondTableInATypeTable() {
  static const ::flatbuffers::TypeCode type_codes[] = {
    { ::flatbuffers::ET_SEQUENCE, 0, 0 }
  };
  static const ::flatbuffers::TypeFunction type_refs[] = {
    NamespaceC::TableInCTypeTable
  };
  static const char * const names[] = {
    "refer_to_c"
  };
  static const ::flatbuffers::TypeTable tt = {
    ::flatbuffers::ST_TABLE, 1, type_codes, type_refs, nullptr, nullptr, names
  };
  return &tt;
}

}  // namespace NamespaceA

#endif  // FLATBUFFERS_GENERATED_NAMESPACETEST2_NAMESPACEA_H_
