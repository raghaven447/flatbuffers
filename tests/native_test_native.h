// automatically generated by the FlatBuffers compiler, do not modify


#ifndef FLATBUFFERS_NATIVE_NATIVETEST_H_
#define FLATBUFFERS_NATIVE_NATIVETEST_H_

#include "flatbuffers/flatbuffers.h"
#include "native_test_generated.h"
#include "custom_native.h"


namespace Native {

struct Foo;

bool operator==(const Foo &lhs, const Foo &rhs);
flatbuffers::Offset<::Foo> Pack(flatbuffers::FlatBufferBuilder &_fbb, const Foo &_o, const flatbuffers::rehasher_function_t *_rehasher = nullptr);
Foo UnPack(const ::Foo &_f, const flatbuffers::resolver_function_t *_resolver = nullptr);

struct Foo : public flatbuffers::NativeTable {
  typedef ::Foo TableType;
  ::BundleSize enumData;
  MyMat bitData;
  std::vector<std::complex<double>> iqData;
  std::complex<double> iqSample;
  Comp iqSample2;
  int32_t newInt;
  Foo()
      : enumData(::BundleSize_Size2),
        newInt(0) {
  }
};

inline bool operator==(const Foo &lhs, const Foo &rhs) {
  return
      (lhs.enumData == rhs.enumData) &&
      (lhs.bitData == rhs.bitData) &&
      (lhs.iqData == rhs.iqData) &&
      (lhs.iqSample == rhs.iqSample) &&
      (lhs.iqSample2 == rhs.iqSample2) &&
      (lhs.newInt == rhs.newInt);
}

inline Foo UnPack(const ::Foo &_f, const flatbuffers::resolver_function_t *_resolver) {
  (void)_f;
  (void)_resolver;
  auto _o = Foo();
  { auto _e = _f.enumData(); _o.enumData = _e; };
  { auto _e = _f.bitData(); if (_e) _o.bitData = Native::UnPack(*_e, _resolver); };
  { auto _e = _f.iqData(); if (_e) { _o.iqData.resize(_e->size()); for (flatbuffers::uoffset_t _i = 0; _i < _e->size(); _i++) { _o.iqData[_i] = Native::UnPack(*_e->Get(_i)); } } };
  { auto _e = _f.iqSample(); if (_e) _o.iqSample = Native::UnPack(*_e); };
  { auto _e = _f.iqSample2(); if (_e) _o.iqSample2 = *_e; };
  { auto _e = _f.newInt(); _o.newInt = _e; };
  return _o;
}

inline flatbuffers::Offset<::Foo> Pack(flatbuffers::FlatBufferBuilder &_fbb, const Foo &_o, const flatbuffers::rehasher_function_t *_rehasher) {
  (void)_rehasher;
  (void)_o;
  struct _VectorArgs { flatbuffers::FlatBufferBuilder *__fbb; const Foo& __o; const flatbuffers::rehasher_function_t *__rehasher; } _va = { &_fbb, _o, _rehasher}; (void)_va;
  auto newInt__ = _o.newInt;
  auto iqSample2__ = &_o.iqSample2;
  auto iqSample__ = & static_cast<const Complex &>(Native::Pack(_o.iqSample));
  auto iqData__ = _o.iqData.size() ? _fbb.CreateVectorOfStructs<::Complex>(_o.iqData.size(),[&](size_t i, ::Complex *r) {*r = Native::Pack(_o.iqData[i]);}) : 0;
  auto bitData__ = Native::Pack(_fbb, _o.bitData, _rehasher);
  auto enumData__ = _o.enumData;
  FooBuilder builder_(_fbb);
  builder_.add_newInt(newInt__);
  builder_.add_iqSample2(iqSample2__);
  builder_.add_iqSample(iqSample__);
  builder_.add_iqData(iqData__);
  builder_.add_bitData(bitData__);
  builder_.add_enumData(enumData__);
  return builder_.Finish();
}

}  // namespace Native

#endif  // FLATBUFFERS_NATIVE_NATIVETEST_H_
