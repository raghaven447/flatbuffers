/*
 * Copyright 2014 Google Inc. All rights reserved.
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

// independent from idl_parser, since this code is not needed for most clients

#include "flatbuffers/code_generators.h"
#include "flatbuffers/flatbuffers.h"
#include "flatbuffers/idl.h"
#include "flatbuffers/util.h"

#include <unordered_set>

namespace flatbuffers {

// Pedantic warning free version of toupper().
inline char ToUpper(char c) { return static_cast<char>(::toupper(c)); }

static std::string GeneratedFileName(const std::string &path,
                                     const std::string &file_name,
                                     const std::string &postfix) {
  return path + file_name + "_" + postfix + ".h";
}

namespace cpp {
class CppNativeGenerator : public BaseGenerator {
 public:
   CppNativeGenerator(const Parser &parser, const std::string &path,
               const std::string &file_name)
      : BaseGenerator(parser, path, file_name, "", "::"),
        cur_name_space_(nullptr),
        float_const_gen_("std::numeric_limits<double>::",
                         "std::numeric_limits<float>::", "quiet_NaN()",
                         "infinity()") {
    static const char * const keywords[] = {
                               "alignas",
                               "alignof",
                               "and",
                               "and_eq",
                               "asm",
                               "atomic_cancel",
                               "atomic_commit",
                               "atomic_noexcept",
                               "auto",
                               "bitand",
                               "bitor",
                               "bool",
                               "break",
                               "case",
                               "catch",
                               "char",
                               "char16_t",
                               "char32_t",
                               "class",
                               "compl",
                               "concept",
                               "const",
                               "constexpr",
                               "const_cast",
                               "continue",
                               "co_await",
                               "co_return",
                               "co_yield",
                               "decltype",
                               "default",
                               "delete",
                               "do",
                               "double",
                               "dynamic_cast",
                               "else",
                               "enum",
                               "explicit",
                               "export",
                               "extern",
                               "false",
                               "float",
                               "for",
                               "friend",
                               "goto",
                               "if",
                               "import",
                               "inline",
                               "int",
                               "long",
                               "module",
                               "mutable",
                               "namespace",
                               "new",
                               "noexcept",
                               "not",
                               "not_eq",
                               "nullptr",
                               "operator",
                               "or",
                               "or_eq",
                               "private",
                               "protected",
                               "public",
                               "register",
                               "reinterpret_cast",
                               "requires",
                               "return",
                               "short",
                               "signed",
                               "sizeof",
                               "static",
                               "static_assert",
                               "static_cast",
                               "struct",
                               "switch",
                               "synchronized",
                               "template",
                               "this",
                               "thread_local",
                               "throw",
                               "true",
                               "try",
                               "typedef",
                               "typeid",
                               "typename",
                               "union",
                               "unsigned",
                               "using",
                               "virtual",
                               "void",
                               "volatile",
                               "wchar_t",
                               "while",
                               "xor",
                               "xor_eq",
                               nullptr };
    for (auto kw = keywords; *kw; kw++) keywords_.insert(*kw);
  }

  std::string GenIncludeGuard() const {
    // Generate include guard.
    std::string guard = file_name_;
    // Remove any non-alpha-numeric characters that may appear in a filename.
    struct IsAlnum {
      bool operator()(char c) const { return !is_alnum(c); }
    };
    guard.erase(std::remove_if(guard.begin(), guard.end(), IsAlnum()),
                guard.end());
    guard = "FLATBUFFERS_NATIVE_" + guard;
    guard += "_";
    // For further uniqueness, also add the namespace.
    auto name_space = parser_.current_namespace_;
    for (auto it = name_space->components.begin();
         it != name_space->components.end(); ++it) {
      guard += *it + "_";
    }
    guard += "H_";
    std::transform(guard.begin(), guard.end(), guard.begin(), ToUpper);
    return guard;
  }

  std::string EscapeKeyword(const std::string &name) const {
    return keywords_.find(name) == keywords_.end() ? name : name + "_";
  }

  std::string Name(const Definition &def) const {
    return EscapeKeyword(def.name);
  }

  std::string Name(const EnumVal &ev) const { return EscapeKeyword(ev.name); }

  bool hasNative(const StructDef &struct_def)
  {
    return struct_def.attributes.Lookup("native_type") != nullptr;
  }

  // Iterate through all definitions we haven't generate code for (enums,
  // structs, and tables) and output them to a single file.
  bool generate() {
    code_.Clear();
    code_ += "// " + std::string(FlatBuffersGeneratedWarning()) + "\n\n";

    const auto include_guard = GenIncludeGuard();
    code_ += "#ifndef " + include_guard;
    code_ += "#define " + include_guard;
    code_ += "";

    if (parser_.opts.gen_nullable) {
      code_ += "#pragma clang system_header\n\n";
    }

    code_ += "#include \"flatbuffers/flatbuffers.h\"";
    code_ += "#include \"" + GeneratedFileName(path_, file_name_, "generated") + "\"";

    code_ += "";

    FLATBUFFERS_ASSERT(!cur_name_space_);

    // Generate forward declarations for all structs/tables, since they may
    // have circular references.
    for (auto it = parser_.structs_.vec.begin();
         it != parser_.structs_.vec.end(); ++it) {
      const auto &struct_def = **it;
      if (!struct_def.generated && !hasNative(struct_def)) {
        SetNameSpace(struct_def.defined_namespace);
        auto nativeName = NativeName(struct_def);
        if (!struct_def.fixed) { code_ += "struct " + nativeName + ";"; }
      }
    }
    code_ += "";

    // Generate forward declarations for all equal operators
    if (parser_.opts.gen_compare) {
      for (auto it = parser_.structs_.vec.begin();
          it != parser_.structs_.vec.end(); ++it) {
        const auto &struct_def = **it;
        if (!struct_def.fixed && !struct_def.generated) {
          SetNameSpace(struct_def.defined_namespace);
          auto nativeName = NativeName(struct_def);
          code_ += "bool operator==(const " + nativeName + " &lhs, const " + nativeName + " &rhs);";
        }
      }
      code_ += "";
    }

    // Generate code for all the enum declarations.
    for (auto it = parser_.enums_.vec.begin(); it != parser_.enums_.vec.end();
         ++it) {
      const auto &enum_def = **it;
      if (enum_def.is_union && !enum_def.generated) {
        SetNameSpace(enum_def.defined_namespace);
        // unions are not supported right now
        FLATBUFFERS_ASSERT(false);
      }
    }

    // Generate code for all tables.
    for (auto it = parser_.structs_.vec.begin();
         it != parser_.structs_.vec.end(); ++it) {
      const auto &struct_def = **it;
      if (!struct_def.fixed && !struct_def.generated && !hasNative(struct_def)) {
        SetNameSpace(struct_def.defined_namespace);
        GenNativeTable(struct_def);
      }
    }

    // Generate Pack Unpack
    for (auto it = parser_.enums_.vec.begin(); it != parser_.enums_.vec.end();
         ++it) {
      const auto &enum_def = **it;
      if (enum_def.is_union && !enum_def.generated) {
        SetNameSpace(enum_def.defined_namespace);
        // unions are not supported right now
        FLATBUFFERS_ASSERT(false);
      }
    }
    for (auto it = parser_.structs_.vec.begin();
         it != parser_.structs_.vec.end(); ++it) {
      const auto &struct_def = **it;
      if (!struct_def.fixed && !struct_def.generated) {
        SetNameSpace(struct_def.defined_namespace);
        GenTablePackUnpack(struct_def);
      }
    }

    if (cur_name_space_) SetNameSpace(nullptr);

    // Close the include guard.
    code_ += "#endif  // " + include_guard;

    const auto file_path = GeneratedFileName(path_, file_name_, "native");
    const auto final_code = code_.ToString();
    return SaveFile(file_path.c_str(), final_code, false);
  }

 private:
  CodeWriter code_;

  std::unordered_set<std::string> keywords_;

  // This tracks the current namespace so we can insert namespace declarations.
  const Namespace *cur_name_space_;

  const Namespace *CurrentNameSpace() const { return cur_name_space_; }

  // Translates a qualified name in flatbuffer text format to the same name in
  // the equivalent C++ namespace.
  static std::string TranslateNameSpace(const std::string &qualified_name) {
    std::string cpp_qualified_name = qualified_name;
    size_t start_pos = 0;
    while ((start_pos = cpp_qualified_name.find(".", start_pos)) !=
           std::string::npos) {
      cpp_qualified_name.replace(start_pos, 1, "::");
    }
    return cpp_qualified_name;
  }

  void GenComment(const std::vector<std::string> &dc, const char *prefix = "") {
    std::string text;
    ::flatbuffers::GenComment(dc, &text, nullptr, prefix);
    code_ += text + "\\";
  }

  // Return a C++ type from the table in idl.h
  std::string GenTypeBasic(const Type &type, bool user_facing_type) const {
    static const char * const ctypename[] = {
    // clang-format off
    #define FLATBUFFERS_TD(ENUM, IDLTYPE, CTYPE, JTYPE, GTYPE, NTYPE, PTYPE, \
                           RTYPE) \
            #CTYPE,
        FLATBUFFERS_GEN_TYPES(FLATBUFFERS_TD)
    #undef FLATBUFFERS_TD
      // clang-format on
    };
    if (user_facing_type) {
      if (type.enum_def) return WrapInNameSpace(*type.enum_def);
      if (type.base_type == BASE_TYPE_BOOL) return "bool";
    }
    return ctypename[type.base_type];
  }

  // Return a C++ pointer type, specialized to the actual struct/table types,
  // and vector element types.
  std::string GenTypePointer(const Type &type) const {
    switch (type.base_type) {
      case BASE_TYPE_STRING: {
        return "flatbuffers::String";
      }
      case BASE_TYPE_VECTOR: {
        const auto type_name = GenTypeWire(type.VectorType(), "", false);
        return "flatbuffers::Vector<" + type_name + ">";
      }
      case BASE_TYPE_STRUCT: {
        return WrapInNameSpace(*type.struct_def);
      }
      case BASE_TYPE_UNION:
      // fall through
      default: { return "void"; }
    }
  }

  // Return a C++ type for any type (scalar/pointer) specifically for
  // building a flatbuffer.
  std::string GenTypeWire(const Type &type, const char *postfix,
                          bool user_facing_type) const {
    if (IsScalar(type.base_type)) {
      return GenTypeBasic(type, user_facing_type) + postfix;
    } else if (IsStruct(type)) {
      return "const " + GenTypePointer(type) + " *";
    } else {
      return "flatbuffers::Offset<" + GenTypePointer(type) + ">" + postfix;
    }
  }

  std::string NullableExtension() {
    return parser_.opts.gen_nullable ? " _Nullable " : "";
  }

  std::string NativeName(const StructDef &sd) {
    auto nativeName = sd.fixed ? Name(sd) : parser_.opts.object_prefix + Name(sd) + parser_.opts.object_suffix;
    return WrapInNameSpace(sd.defined_namespace, nativeName);
  }

  std::string NameNameSpace(const StructDef &sd) {
    return WrapInNameSpace(sd.defined_namespace, Name(sd));
  }

  std::string NativeName(const EnumDef &ed) {
    return ed.name + "Union";
  }

  const std::string &PtrType() {
    return parser_.opts.cpp_object_api_pointer_type;
  }

  std::string GenTypeNativePtr(const std::string &type, bool is_constructor) {
    auto &ptr_type = parser_.opts.cpp_object_api_pointer_type;
    if (ptr_type != "naked")
      return ptr_type + "<" + type + ">";
    else if (is_constructor)
      return "";
    else
      return type + "*";
  }

  std::string GenPtrGet(const FieldDef &field) {
    auto cpp_ptr_type_get = field.attributes.Lookup("cpp_ptr_type_get");
    if (cpp_ptr_type_get)
      return cpp_ptr_type_get->constant;
    auto &ptr_type = PtrType();
    return ptr_type == "naked" ? "" : ".get()";
  }

  std::string GenTypeNative(const StructDef &struct_def) {
    auto type_name = NativeName(struct_def);
    auto native_type = struct_def.attributes.Lookup("native_type");
    if (native_type)
      return native_type->constant;
    else
      return GenTypeNativePtr(type_name, false);
  }

  std::string GenTypeNative(const Type &type) {
    if (type.base_type == BASE_TYPE_STRING) {
      auto &ret = parser_.opts.cpp_object_api_string_type;
      return ret.empty() ? "std::string" : ret;
    } else if (type.base_type == BASE_TYPE_VECTOR) {
      const auto type_name = GenTypeNative(type.VectorType());
      if (type.struct_def && type.struct_def->attributes.Lookup("native_custom_alloc")) {
        auto native_custom_alloc = type.struct_def->attributes.Lookup("native_custom_alloc");
        return "std::vector<" + type_name + "," +
               native_custom_alloc->constant + "<" + type_name + ">>";
      } else
        return "std::vector<" + type_name + ">";
    } else if (type.base_type == BASE_TYPE_STRUCT) {
      return GenTypeNative(*type.struct_def);
    } else if (type.base_type == BASE_TYPE_UNION) {
      return NativeName(*type.enum_def);
    } else {
      return GenTypeBasic(type, true);
    }
  }

  std::string GetEnumValUse(const EnumDef &enum_def,
                            const EnumVal &enum_val) const {
    const IDLOptions &opts = parser_.opts;
    if (opts.scoped_enums) {
      return Name(enum_def) + "::" + Name(enum_val);
    } else if (opts.prefixed_enums) {
      return Name(enum_def) + "_" + Name(enum_val);
    } else {
      return Name(enum_val);
    }
  }

  std::string StripUnionType(const std::string &name) {
    return name.substr(0, name.size() - strlen(UnionTypeFieldSuffix()));
  }

  std::string TablePackSignature(const StructDef &struct_def, bool predecl) {
    return "flatbuffers::Offset<" + NameNameSpace(struct_def) + "> " + 
           "Pack(flatbuffers::FlatBufferBuilder &_fbb, const " +
           NativeName(struct_def) + " &_o," +
           " const flatbuffers::rehasher_function_t *_rehasher" +
           (predecl ? " = nullptr" : "") + ")";
  }

  std::string TableUnPackSignature(const StructDef &struct_def, bool predecl) {
    return NativeName(struct_def) + " UnPack(" + NameNameSpace(struct_def) + " &_i, "
           + "const flatbuffers::resolver_function_t *_resolver" +
           (predecl ? " = nullptr" : "") + ") const";
  }

  // Generates a value with optionally a cast applied if the field has a
  // different underlying type from its interface type (currently only the
  // case for enums. "from" specify the direction, true meaning from the
  // underlying type to the interface type.
  std::string GenUnderlyingCast(const FieldDef &field, bool from,
                                const std::string &val) {
    if (from && field.value.type.base_type == BASE_TYPE_BOOL) {
      return val + " != 0";
    } else if ((field.value.type.enum_def &&
                IsScalar(field.value.type.base_type)) ||
               field.value.type.base_type == BASE_TYPE_BOOL) {
      return "static_cast<" + GenTypeBasic(field.value.type, from) + ">(" +
             val + ")";
    } else {
      return val;
    }
  }

  std::string GenFieldOffsetName(const FieldDef &field) {
    std::string uname = Name(field);
    std::transform(uname.begin(), uname.end(), uname.begin(), ToUpper);
    return "VT_" + uname;
  }

  void GenFullyQualifiedNameGetter(const StructDef &struct_def) {
    if (!parser_.opts.generate_name_strings) { return; }
    auto fullname = struct_def.defined_namespace->GetFullyQualifiedName(NativeName(struct_def));
    code_.SetValue("NAME", fullname);
    code_.SetValue("CONSTEXPR", "FLATBUFFERS_CONSTEXPR");
    code_ += "  static {{CONSTEXPR}} const char *GetFullyQualifiedName() {";
    code_ += "    return \"{{NAME}}\";";
    code_ += "  }";
  }

  std::string GenDefaultConstant(const FieldDef &field) {
    if(IsFloat(field.value.type.base_type))
      return float_const_gen_.GenFloatConstant(field);
    else
      return field.value.constant;
  }

  std::string GetDefaultScalarValue(const FieldDef &field, bool is_ctor) {
    if (field.value.type.enum_def && IsScalar(field.value.type.base_type)) {
      auto ev = field.value.type.enum_def->ReverseLookup(
          StringToInt(field.value.constant.c_str()), false);
      if (ev) {
        return WrapInNameSpace(field.value.type.enum_def->defined_namespace,
                               GetEnumValUse(*field.value.type.enum_def, *ev));
      } else {
        return GenUnderlyingCast(field, true, field.value.constant);
      }
    } else if (field.value.type.base_type == BASE_TYPE_BOOL) {
      return field.value.constant == "0" ? "false" : "true";
    } else if (field.attributes.Lookup("cpp_type")) {
      if (is_ctor) {
        if (PtrType() == "naked") {
          return "nullptr";
        } else {
          return "";
        }
      } else {
        return "0";
      }
    } else {
      return GenDefaultConstant(field);
    }
  }

  void GenParam(const FieldDef &field, bool direct, const char *prefix) {
    code_.SetValue("PRE", prefix);
    code_.SetValue("PARAM_NAME", Name(field));
    if (direct && field.value.type.base_type == BASE_TYPE_STRING) {
      code_.SetValue("PARAM_TYPE", "const char *");
      code_.SetValue("PARAM_VALUE", "nullptr");
    } else if (direct && field.value.type.base_type == BASE_TYPE_VECTOR) {
      const auto vtype = field.value.type.VectorType();
      std::string type;
      if (IsStruct(vtype)) {
        type = WrapInNameSpace(*vtype.struct_def);
      } else {
        type = GenTypeWire(vtype, "", false);
      }
      code_.SetValue("PARAM_TYPE", "const std::vector<" + type + "> *");
      code_.SetValue("PARAM_VALUE", "nullptr");
    } else {
      code_.SetValue("PARAM_TYPE", GenTypeWire(field.value.type, " ", true));
      code_.SetValue("PARAM_VALUE", GetDefaultScalarValue(field, false));
    }
    code_ += "{{PRE}}{{PARAM_TYPE}}{{PARAM_NAME}} = {{PARAM_VALUE}}\\";
  }

  // Generate a member, including a default value for scalars and raw pointers.
  void GenMember(const FieldDef &field) {
    if (!field.deprecated &&  // Deprecated fields won't be accessible.
        field.value.type.base_type != BASE_TYPE_UTYPE &&
        (field.value.type.base_type != BASE_TYPE_VECTOR ||
         field.value.type.element != BASE_TYPE_UTYPE)) {
      auto type = GenTypeNative(field.value.type);
      code_.SetValue("FIELD_TYPE", type);
      code_.SetValue("FIELD_NAME", Name(field));
      code_ += "  {{FIELD_TYPE}} {{FIELD_NAME}};";
    }
  }

  // Generate the default constructor for this struct. Properly initialize all
  // scalar members with default values.
  void GenDefaultConstructor(const StructDef &struct_def) {
    std::string initializer_list;
    for (auto it = struct_def.fields.vec.begin();
         it != struct_def.fields.vec.end(); ++it) {
      const auto &field = **it;
      if (!field.deprecated &&  // Deprecated fields won't be accessible.
          field.value.type.base_type != BASE_TYPE_UTYPE) {
        auto native_default = field.attributes.Lookup("native_default");
        // Scalar types get parsed defaults, raw pointers get nullptrs.
        if (IsScalar(field.value.type.base_type)) {
          if (!initializer_list.empty()) { initializer_list += ",\n        "; }
          initializer_list += Name(field);
          initializer_list += "(" + (native_default ? std::string(native_default->constant) : GetDefaultScalarValue(field, true)) + ")";
        } else if (field.value.type.base_type == BASE_TYPE_STRUCT) {
          if (IsStruct(field.value.type)) {
            if (native_default) {
              if (!initializer_list.empty()) {
                initializer_list += ",\n        ";
              }
              initializer_list +=
                  Name(field) + "(" + native_default->constant + ")";
            }
          }
        }
      }
    }
    if (!initializer_list.empty()) {
      initializer_list = "\n      : " + initializer_list;
    }

    code_.SetValue("NATIVE_NAME", NativeName(struct_def));
    code_.SetValue("INIT_LIST", initializer_list);

    code_ += "  {{NATIVE_NAME}}(){{INIT_LIST}} {";
    code_ += "  }";
  }

  void GenCompareOperator(const StructDef &struct_def, std::string accessSuffix = "") {
    std::string compare_op;
    for (auto it = struct_def.fields.vec.begin();
         it != struct_def.fields.vec.end(); ++it) {
      const auto &field = **it;
      if (!field.deprecated &&  // Deprecated fields won't be accessible.
        field.value.type.base_type != BASE_TYPE_UTYPE &&
        (field.value.type.base_type != BASE_TYPE_VECTOR ||
         field.value.type.element != BASE_TYPE_UTYPE)) {
        if (!compare_op.empty()) {
          compare_op += " &&\n      ";
        }
        auto accessor = Name(field) + accessSuffix;
        compare_op += "(lhs." + accessor + " == rhs." + accessor + ")";
      }
    }

    std::string cmp_lhs;
    std::string cmp_rhs;
    if (compare_op.empty()) {
      cmp_lhs = "";
      cmp_rhs = "";
      compare_op = "  return true;";
    } else {
      cmp_lhs = "lhs";
      cmp_rhs = "rhs";
      compare_op = "  return\n      " + compare_op + ";";
    }

    code_.SetValue("CMP_OP", compare_op);
    code_.SetValue("CMP_LHS", cmp_lhs);
    code_.SetValue("CMP_RHS", cmp_rhs);
    code_ += "";
    code_ += "inline bool operator==(const {{NATIVE_NAME}} &{{CMP_LHS}}, const {{NATIVE_NAME}} &{{CMP_RHS}}) {";
    code_ += "{{CMP_OP}}";
    code_ += "}";
  }

  void GenOperatorNewDelete(const StructDef &struct_def) {
    if (auto native_custom_alloc =
            struct_def.attributes.Lookup("native_custom_alloc")) {
      code_ += "  inline void *operator new (std::size_t count) {";
      code_ += "    return " + native_custom_alloc->constant +
               "<{{NATIVE_NAME}}>().allocate(count / sizeof({{NATIVE_NAME}}));";
      code_ += "  }";
      code_ += "  inline void operator delete (void *ptr) {";
      code_ += "    return " + native_custom_alloc->constant +
               "<{{NATIVE_NAME}}>().deallocate(static_cast<{{NATIVE_NAME}}*>("
               "ptr),1);";
      code_ += "  }";
    }
  }

  void GenNativeTable(const StructDef &struct_def) {
    code_.SetValue("STRUCT_NAME", Name(struct_def));
    code_.SetValue("NATIVE_NAME", NativeName(struct_def));

    // Generate a C++ object that can hold an unpacked version of this table.
    code_ += "struct {{NATIVE_NAME}} : public flatbuffers::NativeTable {";
    code_ += "  typedef {{STRUCT_NAME}} TableType;";
    GenFullyQualifiedNameGetter(struct_def);
    for (auto it = struct_def.fields.vec.begin();
         it != struct_def.fields.vec.end(); ++it) {
      GenMember(**it);
    }
    GenOperatorNewDelete(struct_def);
    GenDefaultConstructor(struct_def);
    code_ += "};";
    if (parser_.opts.gen_compare) GenCompareOperator(struct_def);
    code_ += "";
  }

  std::string GenUnionUnpackVal(const FieldDef &afield,
                                const char *vec_elem_access,
                                const char *vec_type_access) {
    return afield.value.type.enum_def->name +
           "Union::UnPack(" + "_e" + vec_elem_access + ", " +
           EscapeKeyword(afield.name + UnionTypeFieldSuffix()) +
           "()" + vec_type_access + ", _resolver)";
  }

  std::string GenUnpackVal(const Type &type, const std::string &val,
                           bool invector, const FieldDef &afield) {
    switch (type.base_type) {
      case BASE_TYPE_STRING: {
        return val + "->str()";
      }
      case BASE_TYPE_STRUCT: {
        std::string unpacker;
        if (IsStruct(type)) {
          unpacker = "*" + val;
        } else if (hasNative(*type.struct_def)) {
          unpacker = "flatbuffers::UnPack(*" + val + ")";
        } else {
          unpacker = "flatbuffers::UnPack(*" + val + ", _resolver)";
        }

        if (invector || afield.native_inline) {
          return unpacker;
        } else {
          const auto nativeName = NativeName(*type.struct_def);
          const auto ptype = GenTypeNativePtr( nativeName, true);
          return ptype + "(new " + nativeName + "(" + unpacker + ")";
        }
      }
      case BASE_TYPE_UNION: {
        return GenUnionUnpackVal(
            afield, invector ? "->Get(_i)" : "",
            invector ? ("->GetEnum<" + type.enum_def->name + ">(_i)").c_str()
                     : "");
      }
      default: {
        return val;
        break;
      }
    }
  };

  std::string GenUnpackFieldStatement(const FieldDef &field,
                                      const FieldDef *union_field) {
    std::string code;
    switch (field.value.type.base_type) {
      case BASE_TYPE_VECTOR: {
        std::string indexing;
        if (field.value.type.enum_def) {
          indexing += "static_cast<" +
                      WrapInNameSpace(*field.value.type.enum_def) + ">(";
        }
        indexing += "_e->Get(_i)";
        if (field.value.type.enum_def) { indexing += ")"; }
        if (field.value.type.element == BASE_TYPE_BOOL) { indexing += " != 0"; }

        // Generate code that pushes data from _e to _o in the form:
        //   for (uoffset_t i = 0; i < _e->size(); ++i) {
        //     _o->field.push_back(_e->Get(_i));
        //   }
        auto name = Name(field);
        if (field.value.type.element == BASE_TYPE_UTYPE) {
          name = StripUnionType(Name(field));
        }
        auto access =
            field.value.type.element == BASE_TYPE_UTYPE
                ? ".type"
                : (field.value.type.element == BASE_TYPE_UNION ? ".value" : "");
        code += "{ _o." + name + ".resize(_e->size()); ";
        code += "for (flatbuffers::uoffset_t _i = 0;";
        code += " _i < _e->size(); _i++) { ";

        code += "_o." + name + "[_i]" + access + " = ";
        code +=
            GenUnpackVal(field.value.type.VectorType(), indexing, true, field);
        code += "; } }";
        break;
      }
      case BASE_TYPE_UTYPE: {
        FLATBUFFERS_ASSERT(union_field->value.type.base_type == BASE_TYPE_UNION);
        // Generate code that sets the union type, of the form:
        //   _o->field.type = _e;
        code += "_o." + union_field->name + ".type = _e;";
        break;
      }
      case BASE_TYPE_UNION: {
        // Generate code that sets the union value, of the form:
        //   _o->field.value = Union::Unpack(_e, field_type(), resolver);
        code += "_o." + Name(field) + ".value = ";
        code += GenUnionUnpackVal(field, "", "");
        code += ";";
        break;
      }
      default: {
        // Generate code for assigning the value, of the form:
        //  _o->field = value;
        code += "_o." + Name(field) + " = ";
        code += GenUnpackVal(field.value.type, "_e", false, field) + ";";
        break;
      }
    }
    return code;
  }

  std::string GenCreateParam(const FieldDef &field) {
    const IDLOptions &opts = parser_.opts;

    std::string value = "_o->";
    if (field.value.type.base_type == BASE_TYPE_UTYPE) {
      value += StripUnionType(Name(field));
      value += ".type";
    } else {
      value += Name(field);
    }
    if (field.value.type.base_type != BASE_TYPE_VECTOR && field.attributes.Lookup("cpp_type")) {
      auto type = GenTypeBasic(field.value.type, false);
      value =
          "_rehasher ? "
          "static_cast<" +
          type + ">((*_rehasher)(" + value + GenPtrGet(field) + ")) : 0";
    }


    std::string code;
    switch (field.value.type.base_type) {
      // String fields are of the form:
      //   _fbb.CreateString(_o->field)
      case BASE_TYPE_STRING: {
        code += "_fbb.CreateString(" + value + ")";

        // For optional fields, check to see if there actually is any data
        // in _o->field before attempting to access it. If there isn't,
        // depending on set_empty_to_null either set it to 0 or an empty string.
        if (!field.required) {
          auto empty_value =
              opts.set_empty_to_null ? "0" : "_fbb.CreateSharedString(\"\")";
          code = value + ".empty() ? " + empty_value + " : " + code;
        }
        break;
      }
      // Vector fields come in several flavours, of the forms:
      //   _fbb.CreateVector(_o->field);
      //   _fbb.CreateVector((const utype*)_o->field.data(), _o->field.size());
      //   _fbb.CreateVectorOfStrings(_o->field)
      //   _fbb.CreateVectorOfStructs(_o->field)
      //   _fbb.CreateVector<Offset<T>>(_o->field.size() [&](size_t i) {
      //     return CreateT(_fbb, _o->Get(i), rehasher);
      //   });
      case BASE_TYPE_VECTOR: {
        auto vector_type = field.value.type.VectorType();
        switch (vector_type.base_type) {
          case BASE_TYPE_STRING: {
            code += "_fbb.CreateVectorOfStrings(" + value + ")";
            break;
          }
          case BASE_TYPE_STRUCT: {
            if (IsStruct(vector_type)) {
              auto native_type =
                  field.value.type.struct_def->attributes.Lookup("native_type");
              if (native_type) {
                code += "_fbb.CreateVectorOfNativeStructs<";
                code += WrapInNameSpace(*vector_type.struct_def) + ">";
              } else {
                code += "_fbb.CreateVectorOfStructs";
              }
              code += "(" + value + ")";
            } else {
              code += "_fbb.CreateVector<flatbuffers::Offset<";
              code += WrapInNameSpace(*vector_type.struct_def) + ">> ";
              code += "(" + value + ".size(), ";
              code += "[](size_t i, _VectorArgs *__va) { ";
              code += "return Create" + vector_type.struct_def->name;
              code += "(*__va->__fbb, __va->_" + value + "[i]" +
                      GenPtrGet(field) + ", ";
              code += "__va->__rehasher); }, &_va )";
            }
            break;
          }
          case BASE_TYPE_BOOL: {
            code += "_fbb.CreateVector(" + value + ")";
            break;
          }
          case BASE_TYPE_UNION: {
            code +=
                "_fbb.CreateVector<flatbuffers::"
                "Offset<void>>(" +
                value +
                ".size(), [](size_t i, _VectorArgs *__va) { "
                "return __va->_" +
                value + "[i].Pack(*__va->__fbb, __va->__rehasher); }, &_va)";
            break;
          }
          case BASE_TYPE_UTYPE: {
            value = StripUnionType(value);
            code += "_fbb.CreateVector<uint8_t>(" + value +
                    ".size(), [](size_t i, _VectorArgs *__va) { "
                    "return static_cast<uint8_t>(__va->_" +
                    value + "[i].type); }, &_va)";
            break;
          }
          default: {
            if (field.value.type.enum_def) {
              // For enumerations, we need to get access to the array data for
              // the underlying storage type (eg. uint8_t).
              const auto basetype = GenTypeBasic(
                  field.value.type.enum_def->underlying_type, false);
              code += "_fbb.CreateVectorScalarCast<" + basetype +
                      ">(flatbuffers::data(" + value + "), " + value +
                      ".size())";
            } else if (field.attributes.Lookup("cpp_type")) {
              auto type = GenTypeBasic(vector_type, false);
              code += "_fbb.CreateVector<" + type + ">(" + value + ".size(), ";
              code += "[](size_t i, _VectorArgs *__va) { ";
              code += "return __va->__rehasher ? ";
              code += "static_cast<" + type + ">((*__va->__rehasher)";
              code += "(__va->_" + value + "[i]" + GenPtrGet(field) + ")) : 0";
              code += "; }, &_va )";
            } else {
              code += "_fbb.CreateVector(" + value + ")";
            }
            break;
          }
        }

        // If set_empty_to_null option is enabled, for optional fields, check to
        // see if there actually is any data in _o->field before attempting to
        // access it.
        if (opts.set_empty_to_null && !field.required) {
          code = value + ".size() ? " + code + " : 0";
        }
        break;
      }
      case BASE_TYPE_UNION: {
        // _o->field.Pack(_fbb);
        code += value + ".Pack(_fbb)";
        break;
      }
      case BASE_TYPE_STRUCT: {
        if (IsStruct(field.value.type)) {
          auto native_type =
              field.value.type.struct_def->attributes.Lookup("native_type");
          if (native_type) {
            code += "flatbuffers::Pack(" + value + ")";
          } else if (field.native_inline) {
            code += "&" + value;
          } else {
            code += value + " ? " + value + GenPtrGet(field) + " : 0";
          }
        } else {
          // _o->field ? CreateT(_fbb, _o->field.get(), _rehasher);
          const auto type = field.value.type.struct_def->name;
          code += value + " ? Create" + type;
          code += "(_fbb, " + value + GenPtrGet(field) + ", _rehasher)";
          code += " : 0";
        }
        break;
      }
      default: {
        code += value;
        break;
      }
    }
    return code;
  }

  // Generate code for tables that needs to come after the regular definition.
  void GenTablePackUnpack(const StructDef &struct_def) {
    code_.SetValue("STRUCT_NAME", Name(struct_def));
    code_.SetValue("NATIVE_NAME", NativeName(struct_def));
    code_.SetValue("NATIVE_TYPE", GenTypeNative(struct_def));

    code_ += "inline " +
              TableUnPackSignature(struct_def, false) + " {";
    code_ += "  (void)_i;";
    code_ += "  (void)_resolver;";
    code_ += "  auto _o = {{NATIVE_NAME}}();";

    for (auto it = struct_def.fields.vec.begin();
          it != struct_def.fields.vec.end(); ++it) {
      const auto &field = **it;
      if (field.deprecated) { continue; }

      // Assign a value from |this| to |_o|.   Values from |this| are stored
      // in a variable |_e| by calling this->field_type().  The value is then
      // assigned to |_o| using the GenUnpackFieldStatement.
      const bool is_union = field.value.type.base_type == BASE_TYPE_UTYPE;
      const auto statement =
          GenUnpackFieldStatement(field, is_union ? *(it + 1) : nullptr);

      code_.SetValue("FIELD_NAME", Name(field));
      auto prefix = "  { auto _e = _i.{{FIELD_NAME}}(); ";
      auto check = IsScalar(field.value.type.base_type) ? "" : "if (_e) ";
      auto postfix = " };";
      code_ += std::string(prefix) + check + statement + postfix;
    }
    code_ += "}";
    code_ += "";

    // Generate a CreateX method that works with an unpacked C++ object.
    code_ += "inline " + TablePackSignature(struct_def, false) + " {";
    code_ += "  (void)_rehasher;";
    code_ += "  (void)_i;";
    code_ += "  {{STRUCT_NAME}}Builder builder_(_fbb);";

    code_ +=
        "  struct _VectorArgs "
        "{ flatbuffers::FlatBufferBuilder *__fbb; "
        "const " + Name(struct_def) +
        "& __i; "
        "const flatbuffers::rehasher_function_t *__rehasher; } _va = { "
        "&_fbb, _i, _rehasher}; (void)_va;";

    for (size_t size = struct_def.sortbysize ? sizeof(largest_scalar_t) : 1;
         size; size /= 2) {
      for (auto it = struct_def.fields.vec.rbegin();
           it != struct_def.fields.vec.rend(); ++it) {
        const auto &field = **it;
        if (!field.deprecated && (!struct_def.sortbysize ||
                                  size == SizeOf(field.value.type.base_type))) {
          code_.SetValue("FIELD_NAME", Name(field));
          code_ += "  builder_.add_{{FIELD_NAME}}(" + GenCreateParam(field) + ");";
        }
      }
    }
    code_ += "  return builder_.Finish();";
    code_ += "}";
    code_ += "";
  }


  // Set up the correct namespace. Only open a namespace if the existing one is
  // different (closing/opening only what is necessary).
  //
  // The file must start and end with an empty (or null) namespace so that
  // namespaces are properly opened and closed.
  void SetNameSpace(const Namespace *ns) {
    if (cur_name_space_ == ns) { return; }

    // Compute the size of the longest common namespace prefix.
    // If cur_name_space is A::B::C::D and ns is A::B::E::F::G,
    // the common prefix is A::B:: and we have old_size = 4, new_size = 5
    // and common_prefix_size = 2
    size_t old_size = cur_name_space_ ? cur_name_space_->components.size() : 0;
    size_t new_size = ns ? ns->components.size() : 0;

    size_t common_prefix_size = 0;
    while (common_prefix_size < old_size && common_prefix_size < new_size &&
           ns->components[common_prefix_size] ==
               cur_name_space_->components[common_prefix_size]) {
      common_prefix_size++;
    }

    // Close cur_name_space in reverse order to reach the common prefix.
    // In the previous example, D then C are closed.
    for (size_t j = old_size; j > common_prefix_size; --j) {
      code_ += "}  // namespace " + cur_name_space_->components[j - 1];
    }
    if (old_size != common_prefix_size) { code_ += ""; }

    // open namespace parts to reach the ns namespace
    // in the previous example, E, then F, then G are opened
    for (auto j = common_prefix_size; j != new_size; ++j) {
      code_ += "namespace " + ns->components[j] + " {";
    }
    if (new_size != common_prefix_size) { code_ += ""; }

    cur_name_space_ = ns;
  }

  const TypedFloatConstantGenerator float_const_gen_;
};

}  // namespace cpp

bool GenerateCPPNative(const Parser &parser, const std::string &path,
                 const std::string &file_name) {
  cpp::CppNativeGenerator generator(parser, path, file_name);
  return generator.generate();
}

}  // namespace flatbuffers
