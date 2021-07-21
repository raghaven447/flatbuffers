// automatically generated by the FlatBuffers compiler, do not modify
use std::mem;
use std::cmp::Ordering;
use flatbuffers;
use self::flatbuffers::{EndianScalar, Follow};
use super::*;
#[deprecated(since = "2.0.0", note = "Use associated constants instead. This will no longer be generated in 2021.")]
pub const ENUM_MIN_ANY: u8 = 0;
#[deprecated(since = "2.0.0", note = "Use associated constants instead. This will no longer be generated in 2021.")]
pub const ENUM_MAX_ANY: u8 = 3;
#[deprecated(since = "2.0.0", note = "Use associated constants instead. This will no longer be generated in 2021.")]
#[allow(non_camel_case_types)]
pub const ENUM_VALUES_ANY: [Any; 4] = [
  Any::NONE,
  Any::Monster,
  Any::TestSimpleTableWithEnum,
  Any::MyGame_Example2_Monster,
];

#[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Default)]
#[repr(transparent)]
pub struct Any(pub u8);
#[allow(non_upper_case_globals)]
impl Any {
  pub const NONE: Self = Self(0);
  pub const Monster: Self = Self(1);
  pub const TestSimpleTableWithEnum: Self = Self(2);
  pub const MyGame_Example2_Monster: Self = Self(3);

  pub const ENUM_MIN: u8 = 0;
  pub const ENUM_MAX: u8 = 3;
  pub const ENUM_VALUES: &'static [Self] = &[
    Self::NONE,
    Self::Monster,
    Self::TestSimpleTableWithEnum,
    Self::MyGame_Example2_Monster,
  ];
  /// Returns the variant's name or "" if unknown.
  pub fn variant_name(self) -> Option<&'static str> {
    match self {
      Self::NONE => Some("NONE"),
      Self::Monster => Some("Monster"),
      Self::TestSimpleTableWithEnum => Some("TestSimpleTableWithEnum"),
      Self::MyGame_Example2_Monster => Some("MyGame_Example2_Monster"),
      _ => None,
    }
  }
}
impl std::fmt::Debug for Any {
  fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
    if let Some(name) = self.variant_name() {
      f.write_str(name)
    } else {
      f.write_fmt(format_args!("<UNKNOWN {:?}>", self.0))
    }
  }
}
impl<'a> flatbuffers::Follow<'a> for Any {
  type Inner = Self;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    let b = unsafe {
      flatbuffers::read_scalar_at::<u8>(buf, loc)
    };
    Self(b)
  }
}

impl flatbuffers::Push for Any {
    type Output = Any;
    #[inline]
    fn push(&self, dst: &mut [u8], _rest: &[u8]) {
        unsafe { flatbuffers::emplace_scalar::<u8>(dst, self.0); }
    }
}

impl flatbuffers::EndianScalar for Any {
  #[inline]
  fn to_little_endian(self) -> Self {
    let b = u8::to_le(self.0);
    Self(b)
  }
  #[inline]
  #[allow(clippy::wrong_self_convention)]
  fn from_little_endian(self) -> Self {
    let b = u8::from_le(self.0);
    Self(b)
  }
}

impl<'a> flatbuffers::Verifiable for Any {
  #[inline]
  fn run_verifier(
    v: &mut flatbuffers::Verifier, pos: usize
  ) -> Result<(), flatbuffers::InvalidFlatbuffer> {
    use self::flatbuffers::Verifiable;
    u8::run_verifier(v, pos)
  }
}

impl flatbuffers::SimpleToVerifyInSlice for Any {}
pub struct AnyUnionTableOffset {}

#[non_exhaustive]
#[derive(Debug, Clone, PartialEq)]
pub enum AnyT {
  NONE,
  Monster(Box<MonsterT>),
  TestSimpleTableWithEnum(Box<TestSimpleTableWithEnumT>),
  MyGameExample2Monster(Box<super::example_2::MonsterT>),
}
impl Default for AnyT {
  fn default() -> Self {
    Self::NONE
  }
}
impl AnyT {
  pub fn any_type(&self) -> Any {
    match self {
      Self::NONE => Any::NONE,
      Self::Monster(_) => Any::Monster,
      Self::TestSimpleTableWithEnum(_) => Any::TestSimpleTableWithEnum,
      Self::MyGameExample2Monster(_) => Any::MyGame_Example2_Monster,
    }
  }
  pub fn pack(&self, fbb: &mut flatbuffers::FlatBufferBuilder) -> Option<flatbuffers::WIPOffset<flatbuffers::UnionWIPOffset>> {
    match self {
      Self::NONE => None,
      Self::Monster(v) => Some(v.pack(fbb).as_union_value()),
      Self::TestSimpleTableWithEnum(v) => Some(v.pack(fbb).as_union_value()),
      Self::MyGameExample2Monster(v) => Some(v.pack(fbb).as_union_value()),
    }
  }
  /// If the union variant matches, return the owned MonsterT, setting the union to NONE.
  pub fn take_monster(&mut self) -> Option<Box<MonsterT>> {
    if let Self::Monster(_) = self {
      let v = std::mem::replace(self, Self::NONE);
      if let Self::Monster(w) = v {
        Some(w)
      } else {
        unreachable!()
      }
    } else {
      None
    }
  }
  /// If the union variant matches, return a reference to the MonsterT.
  pub fn as_monster(&self) -> Option<&MonsterT> {
    if let Self::Monster(v) = self { Some(v.as_ref()) } else { None }
  }
  /// If the union variant matches, return a mutable reference to the MonsterT.
  pub fn as_monster_mut(&mut self) -> Option<&mut MonsterT> {
    if let Self::Monster(v) = self { Some(v.as_mut()) } else { None }
  }
  /// If the union variant matches, return the owned TestSimpleTableWithEnumT, setting the union to NONE.
  pub fn take_test_simple_table_with_enum(&mut self) -> Option<Box<TestSimpleTableWithEnumT>> {
    if let Self::TestSimpleTableWithEnum(_) = self {
      let v = std::mem::replace(self, Self::NONE);
      if let Self::TestSimpleTableWithEnum(w) = v {
        Some(w)
      } else {
        unreachable!()
      }
    } else {
      None
    }
  }
  /// If the union variant matches, return a reference to the TestSimpleTableWithEnumT.
  pub fn as_test_simple_table_with_enum(&self) -> Option<&TestSimpleTableWithEnumT> {
    if let Self::TestSimpleTableWithEnum(v) = self { Some(v.as_ref()) } else { None }
  }
  /// If the union variant matches, return a mutable reference to the TestSimpleTableWithEnumT.
  pub fn as_test_simple_table_with_enum_mut(&mut self) -> Option<&mut TestSimpleTableWithEnumT> {
    if let Self::TestSimpleTableWithEnum(v) = self { Some(v.as_mut()) } else { None }
  }
  /// If the union variant matches, return the owned super::example_2::MonsterT, setting the union to NONE.
  pub fn take_my_game_example_2_monster(&mut self) -> Option<Box<super::example_2::MonsterT>> {
    if let Self::MyGameExample2Monster(_) = self {
      let v = std::mem::replace(self, Self::NONE);
      if let Self::MyGameExample2Monster(w) = v {
        Some(w)
      } else {
        unreachable!()
      }
    } else {
      None
    }
  }
  /// If the union variant matches, return a reference to the super::example_2::MonsterT.
  pub fn as_my_game_example_2_monster(&self) -> Option<&super::example_2::MonsterT> {
    if let Self::MyGameExample2Monster(v) = self { Some(v.as_ref()) } else { None }
  }
  /// If the union variant matches, return a mutable reference to the super::example_2::MonsterT.
  pub fn as_my_game_example_2_monster_mut(&mut self) -> Option<&mut super::example_2::MonsterT> {
    if let Self::MyGameExample2Monster(v) = self { Some(v.as_mut()) } else { None }
  }
}
