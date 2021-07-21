// automatically generated by the FlatBuffers compiler, do not modify
use std::mem;
use std::cmp::Ordering;
use flatbuffers;
use self::flatbuffers::{EndianScalar, Follow};
use super::*;
#[deprecated(since = "2.0.0", note = "Use associated constants instead. This will no longer be generated in 2021.")]
pub const ENUM_MIN_ANY_AMBIGUOUS_ALIASES: u8 = 0;
#[deprecated(since = "2.0.0", note = "Use associated constants instead. This will no longer be generated in 2021.")]
pub const ENUM_MAX_ANY_AMBIGUOUS_ALIASES: u8 = 3;
#[deprecated(since = "2.0.0", note = "Use associated constants instead. This will no longer be generated in 2021.")]
#[allow(non_camel_case_types)]
pub const ENUM_VALUES_ANY_AMBIGUOUS_ALIASES: [AnyAmbiguousAliases; 4] = [
  AnyAmbiguousAliases::NONE,
  AnyAmbiguousAliases::M1,
  AnyAmbiguousAliases::M2,
  AnyAmbiguousAliases::M3,
];

#[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Default)]
#[repr(transparent)]
pub struct AnyAmbiguousAliases(pub u8);
#[allow(non_upper_case_globals)]
impl AnyAmbiguousAliases {
  pub const NONE: Self = Self(0);
  pub const M1: Self = Self(1);
  pub const M2: Self = Self(2);
  pub const M3: Self = Self(3);

  pub const ENUM_MIN: u8 = 0;
  pub const ENUM_MAX: u8 = 3;
  pub const ENUM_VALUES: &'static [Self] = &[
    Self::NONE,
    Self::M1,
    Self::M2,
    Self::M3,
  ];
  /// Returns the variant's name or "" if unknown.
  pub fn variant_name(self) -> Option<&'static str> {
    match self {
      Self::NONE => Some("NONE"),
      Self::M1 => Some("M1"),
      Self::M2 => Some("M2"),
      Self::M3 => Some("M3"),
      _ => None,
    }
  }
}
impl std::fmt::Debug for AnyAmbiguousAliases {
  fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
    if let Some(name) = self.variant_name() {
      f.write_str(name)
    } else {
      f.write_fmt(format_args!("<UNKNOWN {:?}>", self.0))
    }
  }
}
impl<'a> flatbuffers::Follow<'a> for AnyAmbiguousAliases {
  type Inner = Self;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    let b = unsafe {
      flatbuffers::read_scalar_at::<u8>(buf, loc)
    };
    Self(b)
  }
}

impl flatbuffers::Push for AnyAmbiguousAliases {
    type Output = AnyAmbiguousAliases;
    #[inline]
    fn push(&self, dst: &mut [u8], _rest: &[u8]) {
        unsafe { flatbuffers::emplace_scalar::<u8>(dst, self.0); }
    }
}

impl flatbuffers::EndianScalar for AnyAmbiguousAliases {
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

impl<'a> flatbuffers::Verifiable for AnyAmbiguousAliases {
  #[inline]
  fn run_verifier(
    v: &mut flatbuffers::Verifier, pos: usize
  ) -> Result<(), flatbuffers::InvalidFlatbuffer> {
    use self::flatbuffers::Verifiable;
    u8::run_verifier(v, pos)
  }
}

impl flatbuffers::SimpleToVerifyInSlice for AnyAmbiguousAliases {}
pub struct AnyAmbiguousAliasesUnionTableOffset {}

#[allow(clippy::upper_case_acronyms)]
#[non_exhaustive]
#[derive(Debug, Clone, PartialEq)]
pub enum AnyAmbiguousAliasesT {
  NONE,
  M1(Box<MonsterT>),
  M2(Box<MonsterT>),
  M3(Box<MonsterT>),
}
impl Default for AnyAmbiguousAliasesT {
  fn default() -> Self {
    Self::NONE
  }
}
impl AnyAmbiguousAliasesT {
  pub fn any_ambiguous_aliases_type(&self) -> AnyAmbiguousAliases {
    match self {
      Self::NONE => AnyAmbiguousAliases::NONE,
      Self::M1(_) => AnyAmbiguousAliases::M1,
      Self::M2(_) => AnyAmbiguousAliases::M2,
      Self::M3(_) => AnyAmbiguousAliases::M3,
    }
  }
  pub fn pack(&self, fbb: &mut flatbuffers::FlatBufferBuilder) -> Option<flatbuffers::WIPOffset<flatbuffers::UnionWIPOffset>> {
    match self {
      Self::NONE => None,
      Self::M1(v) => Some(v.pack(fbb).as_union_value()),
      Self::M2(v) => Some(v.pack(fbb).as_union_value()),
      Self::M3(v) => Some(v.pack(fbb).as_union_value()),
    }
  }
  /// If the union variant matches, return the owned MonsterT, setting the union to NONE.
  pub fn take_m1(&mut self) -> Option<Box<MonsterT>> {
    if let Self::M1(_) = self {
      let v = std::mem::replace(self, Self::NONE);
      if let Self::M1(w) = v {
        Some(w)
      } else {
        unreachable!()
      }
    } else {
      None
    }
  }
  /// If the union variant matches, return a reference to the MonsterT.
  pub fn as_m1(&self) -> Option<&MonsterT> {
    if let Self::M1(v) = self { Some(v.as_ref()) } else { None }
  }
  /// If the union variant matches, return a mutable reference to the MonsterT.
  pub fn as_m1_mut(&mut self) -> Option<&mut MonsterT> {
    if let Self::M1(v) = self { Some(v.as_mut()) } else { None }
  }
  /// If the union variant matches, return the owned MonsterT, setting the union to NONE.
  pub fn take_m2(&mut self) -> Option<Box<MonsterT>> {
    if let Self::M2(_) = self {
      let v = std::mem::replace(self, Self::NONE);
      if let Self::M2(w) = v {
        Some(w)
      } else {
        unreachable!()
      }
    } else {
      None
    }
  }
  /// If the union variant matches, return a reference to the MonsterT.
  pub fn as_m2(&self) -> Option<&MonsterT> {
    if let Self::M2(v) = self { Some(v.as_ref()) } else { None }
  }
  /// If the union variant matches, return a mutable reference to the MonsterT.
  pub fn as_m2_mut(&mut self) -> Option<&mut MonsterT> {
    if let Self::M2(v) = self { Some(v.as_mut()) } else { None }
  }
  /// If the union variant matches, return the owned MonsterT, setting the union to NONE.
  pub fn take_m3(&mut self) -> Option<Box<MonsterT>> {
    if let Self::M3(_) = self {
      let v = std::mem::replace(self, Self::NONE);
      if let Self::M3(w) = v {
        Some(w)
      } else {
        unreachable!()
      }
    } else {
      None
    }
  }
  /// If the union variant matches, return a reference to the MonsterT.
  pub fn as_m3(&self) -> Option<&MonsterT> {
    if let Self::M3(v) = self { Some(v.as_ref()) } else { None }
  }
  /// If the union variant matches, return a mutable reference to the MonsterT.
  pub fn as_m3_mut(&mut self) -> Option<&mut MonsterT> {
    if let Self::M3(v) = self { Some(v.as_mut()) } else { None }
  }
}
