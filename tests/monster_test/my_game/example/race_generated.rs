// automatically generated by the FlatBuffers compiler, do not modify
extern crate alloc;
extern crate core;
extern crate flatbuffers;
use self::alloc::{boxed::Box, vec::Vec};
use self::alloc::string::{String, ToString as _};
use self::core::{cmp::Ordering, fmt, mem, ptr, slice};
use self::flatbuffers::{EndianScalar, Follow, Verifiable};
use super::*;
#[deprecated(since = "2.0.0", note = "Use associated constants instead. This will no longer be generated in 2021.")]
pub const ENUM_MIN_RACE: i8 = -1;
#[deprecated(since = "2.0.0", note = "Use associated constants instead. This will no longer be generated in 2021.")]
pub const ENUM_MAX_RACE: i8 = 2;
#[deprecated(since = "2.0.0", note = "Use associated constants instead. This will no longer be generated in 2021.")]
#[allow(non_camel_case_types)]
pub const ENUM_VALUES_RACE: [Race; 4] = [
  Race::None,
  Race::Human,
  Race::Dwarf,
  Race::Elf,
];

#[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Default)]
#[repr(transparent)]
pub struct Race(pub i8);
#[allow(non_upper_case_globals)]
impl Race {
  pub const None: Self = Self(-1);
  pub const Human: Self = Self(0);
  pub const Dwarf: Self = Self(1);
  pub const Elf: Self = Self(2);

  pub const ENUM_MIN: i8 = -1;
  pub const ENUM_MAX: i8 = 2;
  pub const ENUM_VALUES: &'static [Self] = &[
    Self::None,
    Self::Human,
    Self::Dwarf,
    Self::Elf,
  ];
  /// Returns the variant's name or "" if unknown.
  pub fn variant_name(self) -> Option<&'static str> {
    match self {
      Self::None => Some("None"),
      Self::Human => Some("Human"),
      Self::Dwarf => Some("Dwarf"),
      Self::Elf => Some("Elf"),
      _ => None,
    }
  }
}
impl fmt::Debug for Race {
  fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
    if let Some(name) = self.variant_name() {
      f.write_str(name)
    } else {
      f.write_fmt(format_args!("<UNKNOWN {:?}>", self.0))
    }
  }
}
impl<'a> flatbuffers::Follow<'a> for Race {
  type Inner = Self;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    let b = unsafe {
      flatbuffers::read_scalar_at::<i8>(buf, loc)
    };
    Self(b)
  }
}

impl flatbuffers::Push for Race {
    type Output = Race;
    #[inline]
    fn push(&self, dst: &mut [u8], _rest: &[u8]) {
        unsafe { flatbuffers::emplace_scalar::<i8>(dst, self.0); }
    }
}

impl flatbuffers::EndianScalar for Race {
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

impl<'a> flatbuffers::Verifiable for Race {
  #[inline]
  fn run_verifier(
    v: &mut flatbuffers::Verifier, pos: usize
  ) -> Result<(), flatbuffers::InvalidFlatbuffer> {
    i8::run_verifier(v, pos)
  }
}

impl flatbuffers::SimpleToVerifyInSlice for Race {}
