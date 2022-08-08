//@generated
// automatically generated by the FlatBuffers compiler, do not modify
extern crate alloc;
extern crate flatbuffers;
use alloc::boxed::Box;
use alloc::string::{String, ToString};
use alloc::vec::Vec;
use core::mem;
use core::cmp::Ordering;
use self::flatbuffers::{EndianScalar, Follow};
use super::*;
#[deprecated(since = "2.0.0", note = "Use associated constants instead. This will no longer be generated in 2021.")]
pub const ENUM_MIN_OPTIONAL_BYTE: i8 = 0;
#[deprecated(since = "2.0.0", note = "Use associated constants instead. This will no longer be generated in 2021.")]
pub const ENUM_MAX_OPTIONAL_BYTE: i8 = 2;
#[deprecated(since = "2.0.0", note = "Use associated constants instead. This will no longer be generated in 2021.")]
#[allow(non_camel_case_types)]
pub const ENUM_VALUES_OPTIONAL_BYTE: [OptionalByte; 3] = [
  OptionalByte::None,
  OptionalByte::One,
  OptionalByte::Two,
];

#[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Default)]
#[repr(transparent)]
pub struct OptionalByte(pub i8);
#[allow(non_upper_case_globals)]
impl OptionalByte {
  pub const None: Self = Self(0);
  pub const One: Self = Self(1);
  pub const Two: Self = Self(2);

  pub const ENUM_MIN: i8 = 0;
  pub const ENUM_MAX: i8 = 2;
  pub const ENUM_VALUES: &'static [Self] = &[
    Self::None,
    Self::One,
    Self::Two,
  ];
  /// Returns the variant's name or "" if unknown.
  pub fn variant_name(self) -> Option<&'static str> {
    match self {
      Self::None => Some("None"),
      Self::One => Some("One"),
      Self::Two => Some("Two"),
      _ => None,
    }
  }
}
impl core::fmt::Debug for OptionalByte {
  fn fmt(&self, f: &mut core::fmt::Formatter) -> core::fmt::Result {
    if let Some(name) = self.variant_name() {
      f.write_str(name)
    } else {
      f.write_fmt(format_args!("<UNKNOWN {:?}>", self.0))
    }
  }
}
impl<'a> flatbuffers::Follow<'a> for OptionalByte {
  type Inner = Self;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    let b = unsafe {
      flatbuffers::read_scalar_at::<i8>(buf, loc)
    };
    Self(b)
  }
}

impl flatbuffers::Push for OptionalByte {
    type Output = OptionalByte;
    #[inline]
    fn push(&self, dst: &mut [u8], _rest: &[u8]) {
        unsafe { flatbuffers::emplace_scalar::<i8>(dst, self.0); }
    }
}

impl flatbuffers::EndianScalar for OptionalByte {
  #[inline]
  fn to_little_endian(self) -> Self {
    let b = i8::to_le(self.0);
    Self(b)
  }
  #[inline]
  #[allow(clippy::wrong_self_convention)]
  fn from_little_endian(self) -> Self {
    let b = i8::from_le(self.0);
    Self(b)
  }
}

impl<'a> flatbuffers::Verifiable for OptionalByte {
  #[inline]
  fn run_verifier(
    v: &mut flatbuffers::Verifier, pos: usize
  ) -> Result<(), flatbuffers::InvalidFlatbuffer> {
    use self::flatbuffers::Verifiable;
    i8::run_verifier(v, pos)
  }
}

impl flatbuffers::SimpleToVerifyInSlice for OptionalByte {}
