//@generated
// automatically generated by the FlatBuffers compiler, do not modify
extern crate alloc;
extern crate flatbuffers;
use alloc::boxed::Box;
use alloc::string::{String, ToString};
use alloc::vec::Vec;
use core::mem;
use core::cmp::Ordering;
extern crate serde;
use self::serde::ser::{Serialize, Serializer, SerializeStruct};
use self::flatbuffers::{EndianScalar, Follow};
use super::*;
#[deprecated(since = "2.0.0", note = "Use associated constants instead. This will no longer be generated in 2021.")]
pub const ENUM_MIN_FROM_INCLUDE: i64 = 0;
#[deprecated(since = "2.0.0", note = "Use associated constants instead. This will no longer be generated in 2021.")]
pub const ENUM_MAX_FROM_INCLUDE: i64 = 0;
#[deprecated(since = "2.0.0", note = "Use associated constants instead. This will no longer be generated in 2021.")]
#[allow(non_camel_case_types)]
pub const ENUM_VALUES_FROM_INCLUDE: [FromInclude; 1] = [
  FromInclude::IncludeVal,
];

#[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Default)]
#[repr(transparent)]
pub struct FromInclude(pub i64);
#[allow(non_upper_case_globals)]
impl FromInclude {
  pub const IncludeVal: Self = Self(0);

  pub const ENUM_MIN: i64 = 0;
  pub const ENUM_MAX: i64 = 0;
  pub const ENUM_VALUES: &'static [Self] = &[
    Self::IncludeVal,
  ];
  /// Returns the variant's name or "" if unknown.
  pub fn variant_name(self) -> Option<&'static str> {
    match self {
      Self::IncludeVal => Some("IncludeVal"),
      _ => None,
    }
  }
}
impl core::fmt::Debug for FromInclude {
  fn fmt(&self, f: &mut core::fmt::Formatter) -> core::fmt::Result {
    if let Some(name) = self.variant_name() {
      f.write_str(name)
    } else {
      f.write_fmt(format_args!("<UNKNOWN {:?}>", self.0))
    }
  }
}
impl Serialize for FromInclude {
  fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
  where
    S: Serializer,
  {
    serializer.serialize_unit_variant("FromInclude", self.0 as u32, self.variant_name().unwrap())
  }
}

impl<'a> flatbuffers::Follow<'a> for FromInclude {
  type Inner = Self;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    let b = unsafe {
      flatbuffers::read_scalar_at::<i64>(buf, loc)
    };
    Self(b)
  }
}

impl flatbuffers::Push for FromInclude {
    type Output = FromInclude;
    #[inline]
    fn push(&self, dst: &mut [u8], _rest: &[u8]) {
        unsafe { flatbuffers::emplace_scalar::<i64>(dst, self.0); }
    }
}

impl flatbuffers::EndianScalar for FromInclude {
  #[inline]
  fn to_little_endian(self) -> Self {
    let b = i64::to_le(self.0);
    Self(b)
  }
  #[inline]
  #[allow(clippy::wrong_self_convention)]
  fn from_little_endian(self) -> Self {
    let b = i64::from_le(self.0);
    Self(b)
  }
}

impl<'a> flatbuffers::Verifiable for FromInclude {
  #[inline]
  fn run_verifier(
    v: &mut flatbuffers::Verifier, pos: usize
  ) -> Result<(), flatbuffers::InvalidFlatbuffer> {
    use self::flatbuffers::Verifiable;
    i64::run_verifier(v, pos)
  }
}

impl flatbuffers::SimpleToVerifyInSlice for FromInclude {}
