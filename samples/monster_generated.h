// automatically generated by the FlatBuffers compiler, do not modify


#ifndef FLATBUFFERS_GENERATED_MONSTER_MYGAME_SAMPLE_H_
#define FLATBUFFERS_GENERATED_MONSTER_MYGAME_SAMPLE_H_

#include "flatbuffers/flatbuffers.h"

// Ensure the included flatbuffers.h is the same version as when this file was
// generated, otherwise it may not be compatible.
static_assert(FLATBUFFERS_VERSION_MAJOR == 22 &&
              FLATBUFFERS_VERSION_MINOR == 11 &&
              FLATBUFFERS_VERSION_REVISION == 23,
             "Non-compatible flatbuffers version included");

namespace MyGame {
namespace Sample {

struct Vec3;

struct Monster;
struct MonsterBuilder;
struct MonsterT;

struct Weapon;
struct WeaponBuilder;
struct WeaponT;

bool operator==(const Vec3 &lhs, const Vec3 &rhs);
bool operator!=(const Vec3 &lhs, const Vec3 &rhs);
bool operator==(const MonsterT &lhs, const MonsterT &rhs);
bool operator!=(const MonsterT &lhs, const MonsterT &rhs);
bool operator==(const WeaponT &lhs, const WeaponT &rhs);
bool operator!=(const WeaponT &lhs, const WeaponT &rhs);

inline const flatbuffers::TypeTable *Vec3TypeTable();

inline const flatbuffers::TypeTable *MonsterTypeTable();

inline const flatbuffers::TypeTable *WeaponTypeTable();

enum Color : int8_t {
  Color_Red = 0,
  Color_Green = 1,
  Color_Blue = 2,
  Color_MIN = Color_Red,
  Color_MAX = Color_Blue
};

inline const Color (&EnumValuesColor())[3] {
  static const Color values[] = {
    Color_Red,
    Color_Green,
    Color_Blue
  };
  return values;
}

inline const char * const *EnumNamesColor() {
  static const char * const names[4] = {
    "Red",
    "Green",
    "Blue",
    nullptr
  };
  return names;
}

inline const char *EnumNameColor(Color e) {
  if (flatbuffers::IsOutRange(e, Color_Red, Color_Blue)) return "";
  const size_t index = static_cast<size_t>(e);
  return EnumNamesColor()[index];
}

enum Equipment : uint8_t {
  Equipment_NONE = 0,
  Equipment_Weapon = 1,
  Equipment_MIN = Equipment_NONE,
  Equipment_MAX = Equipment_Weapon
};

inline const Equipment (&EnumValuesEquipment())[2] {
  static const Equipment values[] = {
    Equipment_NONE,
    Equipment_Weapon
  };
  return values;
}

inline const char * const *EnumNamesEquipment() {
  static const char * const names[3] = {
    "NONE",
    "Weapon",
    nullptr
  };
  return names;
}

inline const char *EnumNameEquipment(Equipment e) {
  if (flatbuffers::IsOutRange(e, Equipment_NONE, Equipment_Weapon)) return "";
  const size_t index = static_cast<size_t>(e);
  return EnumNamesEquipment()[index];
}

template<typename T> struct EquipmentTraits {
  static const Equipment enum_value = Equipment_NONE;
};

template<> struct EquipmentTraits<MyGame::Sample::Weapon> {
  static const Equipment enum_value = Equipment_Weapon;
};

template<typename T> struct EquipmentUnionTraits {
  static const Equipment enum_value = Equipment_NONE;
};

template<> struct EquipmentUnionTraits<MyGame::Sample::WeaponT> {
  static const Equipment enum_value = Equipment_Weapon;
};

struct EquipmentUnion {
  Equipment type;
  void *value;

  EquipmentUnion() : type(Equipment_NONE), value(nullptr) {}
  EquipmentUnion(EquipmentUnion&& u) FLATBUFFERS_NOEXCEPT :
    type(Equipment_NONE), value(nullptr)
    { std::swap(type, u.type); std::swap(value, u.value); }
  EquipmentUnion(const EquipmentUnion &);
  EquipmentUnion &operator=(const EquipmentUnion &u)
    { EquipmentUnion t(u); std::swap(type, t.type); std::swap(value, t.value); return *this; }
  EquipmentUnion &operator=(EquipmentUnion &&u) FLATBUFFERS_NOEXCEPT
    { std::swap(type, u.type); std::swap(value, u.value); return *this; }
  ~EquipmentUnion() { Reset(); }

  void Reset();

  template <typename T>
  void Set(T&& val) {
    typedef typename std::remove_reference<T>::type RT;
    Reset();
    type = EquipmentUnionTraits<RT>::enum_value;
    if (type != Equipment_NONE) {
      value = new RT(std::forward<T>(val));
    }
  }

  static void *UnPack(const void *obj, Equipment type, const flatbuffers::resolver_function_t *resolver);
  flatbuffers::Offset<void> Pack(flatbuffers::FlatBufferBuilder &_fbb, const flatbuffers::rehasher_function_t *_rehasher = nullptr) const;

  MyGame::Sample::WeaponT *AsWeapon() {
    return type == Equipment_Weapon ?
      reinterpret_cast<MyGame::Sample::WeaponT *>(value) : nullptr;
  }
  const MyGame::Sample::WeaponT *AsWeapon() const {
    return type == Equipment_Weapon ?
      reinterpret_cast<const MyGame::Sample::WeaponT *>(value) : nullptr;
  }
};


inline bool operator==(const EquipmentUnion &lhs, const EquipmentUnion &rhs) {
  if (lhs.type != rhs.type) return false;
  switch (lhs.type) {
    case Equipment_NONE: {
      return true;
    }
    case Equipment_Weapon: {
      return *(reinterpret_cast<const MyGame::Sample::WeaponT *>(lhs.value)) ==
             *(reinterpret_cast<const MyGame::Sample::WeaponT *>(rhs.value));
    }
    default: {
      return false;
    }
  }
}

inline bool operator!=(const EquipmentUnion &lhs, const EquipmentUnion &rhs) {
    return !(lhs == rhs);
}

bool VerifyEquipment(flatbuffers::Verifier &verifier, const void *obj, Equipment type);
bool VerifyEquipmentVector(flatbuffers::Verifier &verifier, const flatbuffers::Vector<flatbuffers::Offset<void>> *values, const flatbuffers::Vector<uint8_t> *types);

FLATBUFFERS_MANUALLY_ALIGNED_STRUCT(4) Vec3 FLATBUFFERS_FINAL_CLASS {
 private:
  float x_;
  float y_;
  float z_;

 public:
  static const flatbuffers::TypeTable *MiniReflectTypeTable() {
    return Vec3TypeTable();
  }
  Vec3()
      : x_(0),
        y_(0),
        z_(0) {
  }
  Vec3(float _x, float _y, float _z)
      : x_(flatbuffers::EndianScalar(_x)),
        y_(flatbuffers::EndianScalar(_y)),
        z_(flatbuffers::EndianScalar(_z)) {
  }
  float x() const {
    return flatbuffers::EndianScalar(x_);
  }
  void mutate_x(float _x) {
    flatbuffers::WriteScalar(&x_, _x);
  }
  float y() const {
    return flatbuffers::EndianScalar(y_);
  }
  void mutate_y(float _y) {
    flatbuffers::WriteScalar(&y_, _y);
  }
  float z() const {
    return flatbuffers::EndianScalar(z_);
  }
  void mutate_z(float _z) {
    flatbuffers::WriteScalar(&z_, _z);
  }
};
FLATBUFFERS_STRUCT_END(Vec3, 12);

inline bool operator==(const Vec3 &lhs, const Vec3 &rhs) {
  return
      (lhs.x() == rhs.x()) &&
      (lhs.y() == rhs.y()) &&
      (lhs.z() == rhs.z());
}

inline bool operator!=(const Vec3 &lhs, const Vec3 &rhs) {
    return !(lhs == rhs);
}


struct MonsterT : public flatbuffers::NativeTable {
  typedef Monster TableType;
  flatbuffers::unique_ptr<MyGame::Sample::Vec3> pos{};
  int16_t mana = 150;
  int16_t hp = 100;
  std::string name{};
  std::vector<uint8_t> inventory{};
  MyGame::Sample::Color color = MyGame::Sample::Color_Blue;
  std::vector<flatbuffers::unique_ptr<MyGame::Sample::WeaponT>> weapons{};
  MyGame::Sample::EquipmentUnion equipped{};
  std::vector<MyGame::Sample::Vec3> path{};
  MonsterT() = default;
  MonsterT(const MonsterT &o);
  MonsterT(MonsterT&&) FLATBUFFERS_NOEXCEPT = default;
  MonsterT &operator=(MonsterT o) FLATBUFFERS_NOEXCEPT;
};

struct Monster FLATBUFFERS_FINAL_CLASS : private flatbuffers::Table {
  typedef MonsterT NativeTableType;
  typedef MonsterBuilder Builder;
  static const flatbuffers::TypeTable *MiniReflectTypeTable() {
    return MonsterTypeTable();
  }
  enum FlatBuffersVTableOffset FLATBUFFERS_VTABLE_UNDERLYING_TYPE {
    VT_POS = 4,
    VT_MANA = 6,
    VT_HP = 8,
    VT_NAME = 10,
    VT_INVENTORY = 14,
    VT_COLOR = 16,
    VT_WEAPONS = 18,
    VT_EQUIPPED_TYPE = 20,
    VT_EQUIPPED = 22,
    VT_PATH = 24
  };
  const MyGame::Sample::Vec3 *pos() const {
    return GetStruct<const MyGame::Sample::Vec3 *>(VT_POS);
  }
  MyGame::Sample::Vec3 *mutable_pos() {
    return GetStruct<MyGame::Sample::Vec3 *>(VT_POS);
  }
  int16_t mana() const {
    return GetField<int16_t>(VT_MANA, 150);
  }
  bool mutate_mana(int16_t _mana = 150) {
    return SetField<int16_t>(VT_MANA, _mana, 150);
  }
  int16_t hp() const {
    return GetField<int16_t>(VT_HP, 100);
  }
  bool mutate_hp(int16_t _hp = 100) {
    return SetField<int16_t>(VT_HP, _hp, 100);
  }
  const flatbuffers::String *name() const {
    return GetPointer<const flatbuffers::String *>(VT_NAME);
  }
  flatbuffers::String *mutable_name() {
    return GetPointer<flatbuffers::String *>(VT_NAME);
  }
  const flatbuffers::Vector<uint8_t> *inventory() const {
    return GetPointer<const flatbuffers::Vector<uint8_t> *>(VT_INVENTORY);
  }
  flatbuffers::Vector<uint8_t> *mutable_inventory() {
    return GetPointer<flatbuffers::Vector<uint8_t> *>(VT_INVENTORY);
  }
  MyGame::Sample::Color color() const {
    return static_cast<MyGame::Sample::Color>(GetField<int8_t>(VT_COLOR, 2));
  }
  bool mutate_color(MyGame::Sample::Color _color = static_cast<MyGame::Sample::Color>(2)) {
    return SetField<int8_t>(VT_COLOR, static_cast<int8_t>(_color), 2);
  }
  const flatbuffers::Vector<flatbuffers::Offset<MyGame::Sample::Weapon>> *weapons() const {
    return GetPointer<const flatbuffers::Vector<flatbuffers::Offset<MyGame::Sample::Weapon>> *>(VT_WEAPONS);
  }
  flatbuffers::Vector<flatbuffers::Offset<MyGame::Sample::Weapon>> *mutable_weapons() {
    return GetPointer<flatbuffers::Vector<flatbuffers::Offset<MyGame::Sample::Weapon>> *>(VT_WEAPONS);
  }
  MyGame::Sample::Equipment equipped_type() const {
    return static_cast<MyGame::Sample::Equipment>(GetField<uint8_t>(VT_EQUIPPED_TYPE, 0));
  }
  const void *equipped() const {
    return GetPointer<const void *>(VT_EQUIPPED);
  }
  template<typename T> const T *equipped_as() const;
  const MyGame::Sample::Weapon *equipped_as_Weapon() const {
    return equipped_type() == MyGame::Sample::Equipment_Weapon ? static_cast<const MyGame::Sample::Weapon *>(equipped()) : nullptr;
  }
  void *mutable_equipped() {
    return GetPointer<void *>(VT_EQUIPPED);
  }
  const flatbuffers::Vector<const MyGame::Sample::Vec3 *> *path() const {
    return GetPointer<const flatbuffers::Vector<const MyGame::Sample::Vec3 *> *>(VT_PATH);
  }
  flatbuffers::Vector<const MyGame::Sample::Vec3 *> *mutable_path() {
    return GetPointer<flatbuffers::Vector<const MyGame::Sample::Vec3 *> *>(VT_PATH);
  }
  bool Verify(flatbuffers::Verifier &verifier) const {
    return VerifyTableStart(verifier) &&
           VerifyField<MyGame::Sample::Vec3>(verifier, VT_POS, 4) &&
           VerifyField<int16_t>(verifier, VT_MANA, 2) &&
           VerifyField<int16_t>(verifier, VT_HP, 2) &&
           VerifyOffset(verifier, VT_NAME) &&
           verifier.VerifyString(name()) &&
           VerifyOffset(verifier, VT_INVENTORY) &&
           verifier.VerifyVector(inventory()) &&
           VerifyField<int8_t>(verifier, VT_COLOR, 1) &&
           VerifyOffset(verifier, VT_WEAPONS) &&
           verifier.VerifyVector(weapons()) &&
           verifier.VerifyVectorOfTables(weapons()) &&
           VerifyField<uint8_t>(verifier, VT_EQUIPPED_TYPE, 1) &&
           VerifyOffset(verifier, VT_EQUIPPED) &&
           VerifyEquipment(verifier, equipped(), equipped_type()) &&
           VerifyOffset(verifier, VT_PATH) &&
           verifier.VerifyVector(path()) &&
           verifier.EndTable();
  }
  MonsterT *UnPack(const flatbuffers::resolver_function_t *_resolver = nullptr) const;
  void UnPackTo(MonsterT *_o, const flatbuffers::resolver_function_t *_resolver = nullptr) const;
  static flatbuffers::Offset<Monster> Pack(flatbuffers::FlatBufferBuilder &_fbb, const MonsterT* _o, const flatbuffers::rehasher_function_t *_rehasher = nullptr);
};

template<> inline const MyGame::Sample::Weapon *Monster::equipped_as<MyGame::Sample::Weapon>() const {
  return equipped_as_Weapon();
}

struct MonsterBuilder {
  typedef Monster Table;
  flatbuffers::FlatBufferBuilder &fbb_;
  flatbuffers::uoffset_t start_;
  void add_pos(const MyGame::Sample::Vec3 *pos) {
    fbb_.AddStruct(Monster::VT_POS, pos);
  }
  void add_mana(int16_t mana) {
    fbb_.AddElement<int16_t>(Monster::VT_MANA, mana, 150);
  }
  void add_hp(int16_t hp) {
    fbb_.AddElement<int16_t>(Monster::VT_HP, hp, 100);
  }
  void add_name(flatbuffers::Offset<flatbuffers::String> name) {
    fbb_.AddOffset(Monster::VT_NAME, name);
  }
  void add_inventory(flatbuffers::Offset<flatbuffers::Vector<uint8_t>> inventory) {
    fbb_.AddOffset(Monster::VT_INVENTORY, inventory);
  }
  void add_color(MyGame::Sample::Color color) {
    fbb_.AddElement<int8_t>(Monster::VT_COLOR, static_cast<int8_t>(color), 2);
  }
  void add_weapons(flatbuffers::Offset<flatbuffers::Vector<flatbuffers::Offset<MyGame::Sample::Weapon>>> weapons) {
    fbb_.AddOffset(Monster::VT_WEAPONS, weapons);
  }
  void add_equipped_type(MyGame::Sample::Equipment equipped_type) {
    fbb_.AddElement<uint8_t>(Monster::VT_EQUIPPED_TYPE, static_cast<uint8_t>(equipped_type), 0);
  }
  void add_equipped(flatbuffers::Offset<void> equipped) {
    fbb_.AddOffset(Monster::VT_EQUIPPED, equipped);
  }
  void add_path(flatbuffers::Offset<flatbuffers::Vector<const MyGame::Sample::Vec3 *>> path) {
    fbb_.AddOffset(Monster::VT_PATH, path);
  }
  explicit MonsterBuilder(flatbuffers::FlatBufferBuilder &_fbb)
        : fbb_(_fbb) {
    start_ = fbb_.StartTable();
  }
  flatbuffers::Offset<Monster> Finish() {
    const auto end = fbb_.EndTable(start_);
    auto o = flatbuffers::Offset<Monster>(end);
    return o;
  }
};

inline flatbuffers::Offset<Monster> CreateMonster(
    flatbuffers::FlatBufferBuilder &_fbb,
    const MyGame::Sample::Vec3 *pos = nullptr,
    int16_t mana = 150,
    int16_t hp = 100,
    flatbuffers::Offset<flatbuffers::String> name = 0,
    flatbuffers::Offset<flatbuffers::Vector<uint8_t>> inventory = 0,
    MyGame::Sample::Color color = MyGame::Sample::Color_Blue,
    flatbuffers::Offset<flatbuffers::Vector<flatbuffers::Offset<MyGame::Sample::Weapon>>> weapons = 0,
    MyGame::Sample::Equipment equipped_type = MyGame::Sample::Equipment_NONE,
    flatbuffers::Offset<void> equipped = 0,
    flatbuffers::Offset<flatbuffers::Vector<const MyGame::Sample::Vec3 *>> path = 0) {
  MonsterBuilder builder_(_fbb);
  builder_.add_path(path);
  builder_.add_equipped(equipped);
  builder_.add_weapons(weapons);
  builder_.add_inventory(inventory);
  builder_.add_name(name);
  builder_.add_pos(pos);
  builder_.add_hp(hp);
  builder_.add_mana(mana);
  builder_.add_equipped_type(equipped_type);
  builder_.add_color(color);
  return builder_.Finish();
}

inline flatbuffers::Offset<Monster> CreateMonsterDirect(
    flatbuffers::FlatBufferBuilder &_fbb,
    const MyGame::Sample::Vec3 *pos = nullptr,
    int16_t mana = 150,
    int16_t hp = 100,
    const char *name = nullptr,
    const std::vector<uint8_t> *inventory = nullptr,
    MyGame::Sample::Color color = MyGame::Sample::Color_Blue,
    const std::vector<flatbuffers::Offset<MyGame::Sample::Weapon>> *weapons = nullptr,
    MyGame::Sample::Equipment equipped_type = MyGame::Sample::Equipment_NONE,
    flatbuffers::Offset<void> equipped = 0,
    const std::vector<MyGame::Sample::Vec3> *path = nullptr) {
  auto name__ = name ? _fbb.CreateString(name) : 0;
  auto inventory__ = inventory ? _fbb.CreateVector<uint8_t>(*inventory) : 0;
  auto weapons__ = weapons ? _fbb.CreateVector<flatbuffers::Offset<MyGame::Sample::Weapon>>(*weapons) : 0;
  auto path__ = path ? _fbb.CreateVectorOfStructs<MyGame::Sample::Vec3>(*path) : 0;
  return MyGame::Sample::CreateMonster(
      _fbb,
      pos,
      mana,
      hp,
      name__,
      inventory__,
      color,
      weapons__,
      equipped_type,
      equipped,
      path__);
}

flatbuffers::Offset<Monster> CreateMonster(flatbuffers::FlatBufferBuilder &_fbb, const MonsterT *_o, const flatbuffers::rehasher_function_t *_rehasher = nullptr);

struct WeaponT : public flatbuffers::NativeTable {
  typedef Weapon TableType;
  std::string name{};
  int16_t damage = 0;
};

struct Weapon FLATBUFFERS_FINAL_CLASS : private flatbuffers::Table {
  typedef WeaponT NativeTableType;
  typedef WeaponBuilder Builder;
  static const flatbuffers::TypeTable *MiniReflectTypeTable() {
    return WeaponTypeTable();
  }
  enum FlatBuffersVTableOffset FLATBUFFERS_VTABLE_UNDERLYING_TYPE {
    VT_NAME = 4,
    VT_DAMAGE = 6
  };
  const flatbuffers::String *name() const {
    return GetPointer<const flatbuffers::String *>(VT_NAME);
  }
  flatbuffers::String *mutable_name() {
    return GetPointer<flatbuffers::String *>(VT_NAME);
  }
  int16_t damage() const {
    return GetField<int16_t>(VT_DAMAGE, 0);
  }
  bool mutate_damage(int16_t _damage = 0) {
    return SetField<int16_t>(VT_DAMAGE, _damage, 0);
  }
  bool Verify(flatbuffers::Verifier &verifier) const {
    return VerifyTableStart(verifier) &&
           VerifyOffset(verifier, VT_NAME) &&
           verifier.VerifyString(name()) &&
           VerifyField<int16_t>(verifier, VT_DAMAGE, 2) &&
           verifier.EndTable();
  }
  WeaponT *UnPack(const flatbuffers::resolver_function_t *_resolver = nullptr) const;
  void UnPackTo(WeaponT *_o, const flatbuffers::resolver_function_t *_resolver = nullptr) const;
  static flatbuffers::Offset<Weapon> Pack(flatbuffers::FlatBufferBuilder &_fbb, const WeaponT* _o, const flatbuffers::rehasher_function_t *_rehasher = nullptr);
};

struct WeaponBuilder {
  typedef Weapon Table;
  flatbuffers::FlatBufferBuilder &fbb_;
  flatbuffers::uoffset_t start_;
  void add_name(flatbuffers::Offset<flatbuffers::String> name) {
    fbb_.AddOffset(Weapon::VT_NAME, name);
  }
  void add_damage(int16_t damage) {
    fbb_.AddElement<int16_t>(Weapon::VT_DAMAGE, damage, 0);
  }
  explicit WeaponBuilder(flatbuffers::FlatBufferBuilder &_fbb)
        : fbb_(_fbb) {
    start_ = fbb_.StartTable();
  }
  flatbuffers::Offset<Weapon> Finish() {
    const auto end = fbb_.EndTable(start_);
    auto o = flatbuffers::Offset<Weapon>(end);
    return o;
  }
};

inline flatbuffers::Offset<Weapon> CreateWeapon(
    flatbuffers::FlatBufferBuilder &_fbb,
    flatbuffers::Offset<flatbuffers::String> name = 0,
    int16_t damage = 0) {
  WeaponBuilder builder_(_fbb);
  builder_.add_name(name);
  builder_.add_damage(damage);
  return builder_.Finish();
}

inline flatbuffers::Offset<Weapon> CreateWeaponDirect(
    flatbuffers::FlatBufferBuilder &_fbb,
    const char *name = nullptr,
    int16_t damage = 0) {
  auto name__ = name ? _fbb.CreateString(name) : 0;
  return MyGame::Sample::CreateWeapon(
      _fbb,
      name__,
      damage);
}

flatbuffers::Offset<Weapon> CreateWeapon(flatbuffers::FlatBufferBuilder &_fbb, const WeaponT *_o, const flatbuffers::rehasher_function_t *_rehasher = nullptr);


inline bool operator==(const MonsterT &lhs, const MonsterT &rhs) {
  return
      ((lhs.pos == rhs.pos) || (lhs.pos && rhs.pos && *lhs.pos == *rhs.pos)) &&
      (lhs.mana == rhs.mana) &&
      (lhs.hp == rhs.hp) &&
      (lhs.name == rhs.name) &&
      (lhs.inventory == rhs.inventory) &&
      (lhs.color == rhs.color) &&
      (lhs.weapons.size() == rhs.weapons.size() && std::equal(lhs.weapons.cbegin(), lhs.weapons.cend(), rhs.weapons.cbegin(), [](flatbuffers::unique_ptr<MyGame::Sample::WeaponT> const &a, flatbuffers::unique_ptr<MyGame::Sample::WeaponT> const &b) { return (a == b) || (a && b && *a == *b); })) &&
      (lhs.equipped == rhs.equipped) &&
      (lhs.path == rhs.path);
}

inline bool operator!=(const MonsterT &lhs, const MonsterT &rhs) {
    return !(lhs == rhs);
}


inline MonsterT::MonsterT(const MonsterT &o)
      : pos((o.pos) ? new MyGame::Sample::Vec3(*o.pos) : nullptr),
        mana(o.mana),
        hp(o.hp),
        name(o.name),
        inventory(o.inventory),
        color(o.color),
        equipped(o.equipped),
        path(o.path) {
  weapons.reserve(o.weapons.size());
  for (const auto &weapons_ : o.weapons) { weapons.emplace_back((weapons_) ? new MyGame::Sample::WeaponT(*weapons_) : nullptr); }
}

inline MonsterT &MonsterT::operator=(MonsterT o) FLATBUFFERS_NOEXCEPT {
  std::swap(pos, o.pos);
  std::swap(mana, o.mana);
  std::swap(hp, o.hp);
  std::swap(name, o.name);
  std::swap(inventory, o.inventory);
  std::swap(color, o.color);
  std::swap(weapons, o.weapons);
  std::swap(equipped, o.equipped);
  std::swap(path, o.path);
  return *this;
}

inline MonsterT *Monster::UnPack(const flatbuffers::resolver_function_t *_resolver) const {
  auto _o = std::unique_ptr<MonsterT>(new MonsterT());
  UnPackTo(_o.get(), _resolver);
  return _o.release();
}

inline void Monster::UnPackTo(MonsterT *_o, const flatbuffers::resolver_function_t *_resolver) const {
  (void)_o;
  (void)_resolver;
  { auto _e = pos(); if (_e) _o->pos = flatbuffers::unique_ptr<MyGame::Sample::Vec3>(new MyGame::Sample::Vec3(*_e)); }
  { auto _e = mana(); _o->mana = _e; }
  { auto _e = hp(); _o->hp = _e; }
  { auto _e = name(); if (_e) _o->name = _e->str(); }
  { auto _e = inventory(); if (_e) { _o->inventory.resize(_e->size()); std::copy(_e->begin(), _e->end(), _o->inventory.begin()); } }
  { auto _e = color(); _o->color = _e; }
  { auto _e = weapons(); if (_e) { _o->weapons.resize(_e->size()); for (flatbuffers::uoffset_t _i = 0; _i < _e->size(); _i++) { if(_o->weapons[_i]) { _e->Get(_i)->UnPackTo(_o->weapons[_i].get(), _resolver); } else { _o->weapons[_i] = flatbuffers::unique_ptr<MyGame::Sample::WeaponT>(_e->Get(_i)->UnPack(_resolver)); }; } } else { _o->weapons.resize(0); } }
  { auto _e = equipped_type(); _o->equipped.type = _e; }
  { auto _e = equipped(); if (_e) _o->equipped.value = MyGame::Sample::EquipmentUnion::UnPack(_e, equipped_type(), _resolver); }
  { auto _e = path(); if (_e) { _o->path.resize(_e->size()); for (flatbuffers::uoffset_t _i = 0; _i < _e->size(); _i++) { _o->path[_i] = *_e->Get(_i); } } else { _o->path.resize(0); } }
}

inline flatbuffers::Offset<Monster> Monster::Pack(flatbuffers::FlatBufferBuilder &_fbb, const MonsterT* _o, const flatbuffers::rehasher_function_t *_rehasher) {
  return CreateMonster(_fbb, _o, _rehasher);
}

inline flatbuffers::Offset<Monster> CreateMonster(flatbuffers::FlatBufferBuilder &_fbb, const MonsterT *_o, const flatbuffers::rehasher_function_t *_rehasher) {
  (void)_rehasher;
  (void)_o;
  struct _VectorArgs { flatbuffers::FlatBufferBuilder *__fbb; const MonsterT* __o; const flatbuffers::rehasher_function_t *__rehasher; } _va = { &_fbb, _o, _rehasher}; (void)_va;
  auto _pos = _o->pos ? _o->pos.get() : nullptr;
  auto _mana = _o->mana;
  auto _hp = _o->hp;
  auto _name = _o->name.empty() ? 0 : _fbb.CreateString(_o->name);
  auto _inventory = _o->inventory.size() ? _fbb.CreateVector(_o->inventory) : 0;
  auto _color = _o->color;
  auto _weapons = _o->weapons.size() ? _fbb.CreateVector<flatbuffers::Offset<MyGame::Sample::Weapon>> (_o->weapons.size(), [](size_t i, _VectorArgs *__va) { return CreateWeapon(*__va->__fbb, __va->__o->weapons[i].get(), __va->__rehasher); }, &_va ) : 0;
  auto _equipped_type = _o->equipped.type;
  auto _equipped = _o->equipped.Pack(_fbb);
  auto _path = _o->path.size() ? _fbb.CreateVectorOfStructs(_o->path) : 0;
  return MyGame::Sample::CreateMonster(
      _fbb,
      _pos,
      _mana,
      _hp,
      _name,
      _inventory,
      _color,
      _weapons,
      _equipped_type,
      _equipped,
      _path);
}


inline bool operator==(const WeaponT &lhs, const WeaponT &rhs) {
  return
      (lhs.name == rhs.name) &&
      (lhs.damage == rhs.damage);
}

inline bool operator!=(const WeaponT &lhs, const WeaponT &rhs) {
    return !(lhs == rhs);
}


inline WeaponT *Weapon::UnPack(const flatbuffers::resolver_function_t *_resolver) const {
  auto _o = std::unique_ptr<WeaponT>(new WeaponT());
  UnPackTo(_o.get(), _resolver);
  return _o.release();
}

inline void Weapon::UnPackTo(WeaponT *_o, const flatbuffers::resolver_function_t *_resolver) const {
  (void)_o;
  (void)_resolver;
  { auto _e = name(); if (_e) _o->name = _e->str(); }
  { auto _e = damage(); _o->damage = _e; }
}

inline flatbuffers::Offset<Weapon> Weapon::Pack(flatbuffers::FlatBufferBuilder &_fbb, const WeaponT* _o, const flatbuffers::rehasher_function_t *_rehasher) {
  return CreateWeapon(_fbb, _o, _rehasher);
}

inline flatbuffers::Offset<Weapon> CreateWeapon(flatbuffers::FlatBufferBuilder &_fbb, const WeaponT *_o, const flatbuffers::rehasher_function_t *_rehasher) {
  (void)_rehasher;
  (void)_o;
  struct _VectorArgs { flatbuffers::FlatBufferBuilder *__fbb; const WeaponT* __o; const flatbuffers::rehasher_function_t *__rehasher; } _va = { &_fbb, _o, _rehasher}; (void)_va;
  auto _name = _o->name.empty() ? 0 : _fbb.CreateString(_o->name);
  auto _damage = _o->damage;
  return MyGame::Sample::CreateWeapon(
      _fbb,
      _name,
      _damage);
}

inline bool VerifyEquipment(flatbuffers::Verifier &verifier, const void *obj, Equipment type) {
  switch (type) {
    case Equipment_NONE: {
      return true;
    }
    case Equipment_Weapon: {
      auto ptr = reinterpret_cast<const MyGame::Sample::Weapon *>(obj);
      return verifier.VerifyTable(ptr);
    }
    default: return true;
  }
}

inline bool VerifyEquipmentVector(flatbuffers::Verifier &verifier, const flatbuffers::Vector<flatbuffers::Offset<void>> *values, const flatbuffers::Vector<uint8_t> *types) {
  if (!values || !types) return !values && !types;
  if (values->size() != types->size()) return false;
  for (flatbuffers::uoffset_t i = 0; i < values->size(); ++i) {
    if (!VerifyEquipment(
        verifier,  values->Get(i), types->GetEnum<Equipment>(i))) {
      return false;
    }
  }
  return true;
}

inline void *EquipmentUnion::UnPack(const void *obj, Equipment type, const flatbuffers::resolver_function_t *resolver) {
  (void)resolver;
  switch (type) {
    case Equipment_Weapon: {
      auto ptr = reinterpret_cast<const MyGame::Sample::Weapon *>(obj);
      return ptr->UnPack(resolver);
    }
    default: return nullptr;
  }
}

inline flatbuffers::Offset<void> EquipmentUnion::Pack(flatbuffers::FlatBufferBuilder &_fbb, const flatbuffers::rehasher_function_t *_rehasher) const {
  (void)_rehasher;
  switch (type) {
    case Equipment_Weapon: {
      auto ptr = reinterpret_cast<const MyGame::Sample::WeaponT *>(value);
      return CreateWeapon(_fbb, ptr, _rehasher).Union();
    }
    default: return 0;
  }
}

inline EquipmentUnion::EquipmentUnion(const EquipmentUnion &u) : type(u.type), value(nullptr) {
  switch (type) {
    case Equipment_Weapon: {
      value = new MyGame::Sample::WeaponT(*reinterpret_cast<MyGame::Sample::WeaponT *>(u.value));
      break;
    }
    default:
      break;
  }
}

inline void EquipmentUnion::Reset() {
  switch (type) {
    case Equipment_Weapon: {
      auto ptr = reinterpret_cast<MyGame::Sample::WeaponT *>(value);
      delete ptr;
      break;
    }
    default: break;
  }
  value = nullptr;
  type = Equipment_NONE;
}

inline const flatbuffers::TypeTable *ColorTypeTable() {
  static const flatbuffers::TypeCode type_codes[] = {
    { flatbuffers::ET_CHAR, 0, 0 },
    { flatbuffers::ET_CHAR, 0, 0 },
    { flatbuffers::ET_CHAR, 0, 0 }
  };
  static const flatbuffers::TypeFunction type_refs[] = {
    MyGame::Sample::ColorTypeTable
  };
  static const char * const names[] = {
    "Red",
    "Green",
    "Blue"
  };
  static const flatbuffers::TypeTable tt = {
    flatbuffers::ST_ENUM, 3, type_codes, type_refs, nullptr, nullptr, names
  };
  return &tt;
}

inline const flatbuffers::TypeTable *EquipmentTypeTable() {
  static const flatbuffers::TypeCode type_codes[] = {
    { flatbuffers::ET_SEQUENCE, 0, -1 },
    { flatbuffers::ET_SEQUENCE, 0, 0 }
  };
  static const flatbuffers::TypeFunction type_refs[] = {
    MyGame::Sample::WeaponTypeTable
  };
  static const char * const names[] = {
    "NONE",
    "Weapon"
  };
  static const flatbuffers::TypeTable tt = {
    flatbuffers::ST_UNION, 2, type_codes, type_refs, nullptr, nullptr, names
  };
  return &tt;
}

inline const flatbuffers::TypeTable *Vec3TypeTable() {
  static const flatbuffers::TypeCode type_codes[] = {
    { flatbuffers::ET_FLOAT, 0, -1 },
    { flatbuffers::ET_FLOAT, 0, -1 },
    { flatbuffers::ET_FLOAT, 0, -1 }
  };
  static const int64_t values[] = { 0, 4, 8, 12 };
  static const char * const names[] = {
    "x",
    "y",
    "z"
  };
  static const flatbuffers::TypeTable tt = {
    flatbuffers::ST_STRUCT, 3, type_codes, nullptr, nullptr, values, names
  };
  return &tt;
}

inline const flatbuffers::TypeTable *MonsterTypeTable() {
  static const flatbuffers::TypeCode type_codes[] = {
    { flatbuffers::ET_SEQUENCE, 0, 0 },
    { flatbuffers::ET_SHORT, 0, -1 },
    { flatbuffers::ET_SHORT, 0, -1 },
    { flatbuffers::ET_STRING, 0, -1 },
    { flatbuffers::ET_BOOL, 0, -1 },
    { flatbuffers::ET_UCHAR, 1, -1 },
    { flatbuffers::ET_CHAR, 0, 1 },
    { flatbuffers::ET_SEQUENCE, 1, 2 },
    { flatbuffers::ET_UTYPE, 0, 3 },
    { flatbuffers::ET_SEQUENCE, 0, 3 },
    { flatbuffers::ET_SEQUENCE, 1, 0 }
  };
  static const flatbuffers::TypeFunction type_refs[] = {
    MyGame::Sample::Vec3TypeTable,
    MyGame::Sample::ColorTypeTable,
    MyGame::Sample::WeaponTypeTable,
    MyGame::Sample::EquipmentTypeTable
  };
  static const char * const names[] = {
    "pos",
    "mana",
    "hp",
    "name",
    "friendly",
    "inventory",
    "color",
    "weapons",
    "equipped_type",
    "equipped",
    "path"
  };
  static const flatbuffers::TypeTable tt = {
    flatbuffers::ST_TABLE, 11, type_codes, type_refs, nullptr, nullptr, names
  };
  return &tt;
}

inline const flatbuffers::TypeTable *WeaponTypeTable() {
  static const flatbuffers::TypeCode type_codes[] = {
    { flatbuffers::ET_STRING, 0, -1 },
    { flatbuffers::ET_SHORT, 0, -1 }
  };
  static const char * const names[] = {
    "name",
    "damage"
  };
  static const flatbuffers::TypeTable tt = {
    flatbuffers::ST_TABLE, 2, type_codes, nullptr, nullptr, nullptr, names
  };
  return &tt;
}

inline const MyGame::Sample::Monster *GetMonster(const void *buf) {
  return flatbuffers::GetRoot<MyGame::Sample::Monster>(buf);
}

inline const MyGame::Sample::Monster *GetSizePrefixedMonster(const void *buf) {
  return flatbuffers::GetSizePrefixedRoot<MyGame::Sample::Monster>(buf);
}

inline Monster *GetMutableMonster(void *buf) {
  return flatbuffers::GetMutableRoot<Monster>(buf);
}

inline MyGame::Sample::Monster *GetMutableSizePrefixedMonster(void *buf) {
  return flatbuffers::GetMutableSizePrefixedRoot<MyGame::Sample::Monster>(buf);
}

inline bool VerifyMonsterBuffer(
    flatbuffers::Verifier &verifier) {
  return verifier.VerifyBuffer<MyGame::Sample::Monster>(nullptr);
}

inline bool VerifySizePrefixedMonsterBuffer(
    flatbuffers::Verifier &verifier) {
  return verifier.VerifySizePrefixedBuffer<MyGame::Sample::Monster>(nullptr);
}

inline void FinishMonsterBuffer(
    flatbuffers::FlatBufferBuilder &fbb,
    flatbuffers::Offset<MyGame::Sample::Monster> root) {
  fbb.Finish(root);
}

inline void FinishSizePrefixedMonsterBuffer(
    flatbuffers::FlatBufferBuilder &fbb,
    flatbuffers::Offset<MyGame::Sample::Monster> root) {
  fbb.FinishSizePrefixed(root);
}

inline flatbuffers::unique_ptr<MyGame::Sample::MonsterT> UnPackMonster(
    const void *buf,
    const flatbuffers::resolver_function_t *res = nullptr) {
  return flatbuffers::unique_ptr<MyGame::Sample::MonsterT>(GetMonster(buf)->UnPack(res));
}

inline flatbuffers::unique_ptr<MyGame::Sample::MonsterT> UnPackSizePrefixedMonster(
    const void *buf,
    const flatbuffers::resolver_function_t *res = nullptr) {
  return flatbuffers::unique_ptr<MyGame::Sample::MonsterT>(GetSizePrefixedMonster(buf)->UnPack(res));
}

}  // namespace Sample
}  // namespace MyGame

#endif  // FLATBUFFERS_GENERATED_MONSTER_MYGAME_SAMPLE_H_
