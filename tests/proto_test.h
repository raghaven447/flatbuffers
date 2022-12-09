#ifndef TESTS_PROTO_TEST_H
#define TESTS_PROTO_TEST_H

#include <string>

#include "flatbuffers/idl.h"
namespace flatbuffers {
namespace tests {

void RunTest(const flatbuffers::IDLOptions &opts, const std::string &proto_path, const std::string &proto_file,
        const std::string &golden_file, const std::string import_proto_file = {});
void proto_test(const std::string &proto_path, const std::string &proto_file);
void proto_test_union(const std::string &proto_path, const std::string &proto_file);
void proto_test_union_suffix(const std::string &proto_path, const std::string &proto_file);
void proto_test_include(const std::string &proto_path, const std::string &proto_file, const std::string &import_proto_file);
void proto_test_include_union(const std::string &proto_path, const std::string &proto_file, const std::string &import_proto_file);

void proto_test_id(const std::string &proto_path, const std::string &proto_file);
void proto_test_union_id(const std::string &proto_path, const std::string &proto_file);
void proto_test_union_suffix_id(const std::string &proto_path, const std::string &proto_file);
void proto_test_include_id(const std::string &proto_path, const std::string &proto_file, const std::string &import_proto_file);
void proto_test_include_union_id(const std::string &proto_path, const std::string &proto_file, const std::string &import_proto_file);

void ParseProtoTest(const std::string& tests_data_path);
void ParseProtoBufAsciiTest();

}  // namespace tests
}  // namespace flatbuffers

#endif
