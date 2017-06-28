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

#include "flatbuffers/idl.h"
#include "flatbuffers/util.h"
#include "flatbuffers/code_generators.h"


namespace flatbuffers {
  static std::string GeneratedFileName(const std::string &path,
                                       const std::string &file_name) {
    return path + file_name + ".schema.json";
  }
  namespace jsons {
    std::string GenNativeType(BaseType type) {
      switch (type) {
      case BASE_TYPE_BOOL:    return "boolean";

      case BASE_TYPE_CHAR:
      case BASE_TYPE_UCHAR:
      case BASE_TYPE_SHORT:
      case BASE_TYPE_USHORT:
      case BASE_TYPE_INT:
      case BASE_TYPE_UINT:
      case BASE_TYPE_LONG:
      case BASE_TYPE_ULONG:
      case BASE_TYPE_FLOAT:
      case BASE_TYPE_DOUBLE:
        return "number";
      case BASE_TYPE_STRING:  return "string";
      default:
      {
        return "?";
      }
      }
    }

    template<class T>
    std::string GenFullName(const T* enum_def) {
      std::stringstream fullName;
      auto nameSpaces = enum_def->defined_namespace->components;
      for (auto const &ns : nameSpaces) {
        fullName << ns << "_";
      }

      fullName << enum_def->name;
      return fullName.str();
    }

    template<class T>
    std::string GenTypeRef(const T* enum_def) {
      return "\"$ref\" : \"#/definitions/" + GenFullName(enum_def) + "\"";
    }

    std::string GenType(const std::string &name) {
      return "\"type\" : \"" + name + "\"";
    }

    std::string GenType(const Type &type) {      
      switch (type.base_type) {
      case BASE_TYPE_VECTOR: {
        std::stringstream typeline;
        typeline << "\"type\" : \"array\", ";
        if (type.element == BASE_TYPE_STRUCT) {
          typeline << "\"items\" : { " << GenTypeRef(type.struct_def) << " }";
        }
        else {
          typeline << "\"items\" : { " << GenType(GenNativeType(type.element)) << " }";
        }
        
        return typeline.str();
      }
      case BASE_TYPE_STRUCT: {
        return GenTypeRef(type.struct_def);
      }
      case BASE_TYPE_UNION: {
        std::stringstream unionTypes;
        unionTypes << "\"anyOf\": [";
        for(auto const& ut : type.enum_def->vals.vec) {
          if (ut->union_type.base_type == BASE_TYPE_NONE) {
            continue;
          }
          if (ut->union_type.base_type == BASE_TYPE_STRUCT) {
            unionTypes << "{ " + GenTypeRef(ut->union_type.struct_def) + " }";
          }

          if (&ut != &type.enum_def->vals.vec.back()) {
            unionTypes << ",";
          }
        }
        unionTypes << "]";
        return unionTypes.str();
      }
      case BASE_TYPE_UTYPE:   
        return GenTypeRef(type.enum_def);      
      }
      
      if (type.base_type == BASE_TYPE_CHAR && type.enum_def != nullptr) {
        // it is a reference to an enum type
        return GenTypeRef(type.enum_def);
      }

      return GenType(GenNativeType(type.base_type));
    }

    class JsonSchemaGenerator : public BaseGenerator {
    private:
      CodeWriter code_;
    public:
      JsonSchemaGenerator(const Parser& parser, const std::string& path, const std::string& file_name)
        : BaseGenerator(parser, path, file_name, "", "") {
      }

      explicit JsonSchemaGenerator(const BaseGenerator& base_generator)
        : BaseGenerator(base_generator) {
      }

      

      bool generate() override {
        code_.Clear();
        code_ += "{";
        code_ += "\"$schema\": \"http://json-schema.org/draft-04/schema#\",";
        code_ += "\"definitions\": {";

        for (auto &e : parser_.enums_.vec) {
          code_ += "";
          code_ += "\"" + GenFullName(e) + "\" : {";
          code_ += GenType("string") + ",";
          std::stringstream enumdef;
          enumdef << "\"enum\": [";
          for (auto &enumval : e->vals.vec) {
            enumdef << "\"" + enumval->name + "\"";
            if (&enumval != &e->vals.vec.back()) {
              enumdef << ", ";
            }
          }
          enumdef << "]";
          code_ += enumdef.str();
          code_ += "},";  // close type
        }

        for (auto &s : parser_.structs_.vec) {
          code_ += "";
          code_ += "\"" + GenFullName(s) + "\" : {";
          code_ += GenType("object") + ",";
          std::stringstream comment;
          for (auto commentLine : s->doc_comment) {
            comment << commentLine;
          }
          code_ += "\"description\" : \"" + comment.str() + "\",";
          code_ += "\"properties\" : {";

          for (auto const &prop : s->fields.vec) {
            std::stringstream typeLine;
            typeLine << "  \"" + prop->name + "\" : { " + GenType(prop->value.type) + " }";
            
            if (&prop != &s->fields.vec.back()) {
              code_ += typeLine.str() + ",";
            }
            else {
              code_ += typeLine.str();
            }
          }
          

          

          auto props = s->fields.vec;
          std::vector<flatbuffers::FieldDef*> requiredProperties;
          std::copy_if(
            props.begin(),
            props.end(),
            std::back_inserter(requiredProperties),
            [](flatbuffers::FieldDef *prop) { return prop->required; });
          if (requiredProperties.size() > 0) {
            code_ += "  },";  // close properties
            std::stringstream requiredString;
            requiredString  << "\"required\" : [ ";
            for (const auto &reqProp : requiredProperties) {
              requiredString << "\"" << reqProp->name << "\"";
              if (&reqProp != &requiredProperties.back()) {
                requiredString << ", ";
              }
            }
            requiredString << "]";
            code_ += requiredString.str();
          } else {
            code_ += "  }";  // close properties
          }
          
          if (&s != &parser_.structs_.vec.back()) {
            code_ += "},";  // close type
          }
          else {
            code_ += "}";  // close type
          }
        }
        code_ += "},";  // close definitions

        // mark root type
        code_ += "\"$ref\" : \"#/definitions/" + GenFullName(parser_.root_struct_def_) + "\"";
        
        code_ += "}";  // close schema root
        const auto file_path = GeneratedFileName(path_, file_name_);
        const auto final_code = code_.ToString();
        return SaveFile(file_path.c_str(), final_code, false);
      }
    };
  }  // namespace jsons

  bool GenerateJsonSchema(const Parser &parser, const std::string &path, const std::string &file_name) {
    jsons::JsonSchemaGenerator generator(parser, path, file_name);
    return generator.generate();
  }
}  // namespace flatbuffers
