// automatically generated by the FlatBuffers compiler, do not modify
// @generated
extern crate alloc;
extern crate flatbuffers;
use alloc::boxed::Box;
use alloc::string::{String, ToString};
use alloc::vec::Vec;
use core::mem;
use core::cmp::Ordering;
use self::flatbuffers::{EndianScalar, Follow};
use super::*;
// struct PossiblyReservedWords, aligned to 4
#[repr(transparent)]
#[derive(Clone, Copy, PartialEq)]
pub struct PossiblyReservedWords(pub [u8; 16]);
impl Default for PossiblyReservedWords { 
  fn default() -> Self { 
    Self([0; 16])
  }
}
impl core::fmt::Debug for PossiblyReservedWords {
  fn fmt(&self, f: &mut core::fmt::Formatter) -> core::fmt::Result {
    f.debug_struct("PossiblyReservedWords")
      .field("follow_", &self.follow_())
      .field("push_", &self.push_())
      .field("size_", &self.size_())
      .field("alignment_", &self.alignment_())
      .finish()
  }
}

impl flatbuffers::SimpleToVerifyInSlice for PossiblyReservedWords {}
impl<'a> flatbuffers::Follow<'a> for PossiblyReservedWords {
  type Inner = &'a PossiblyReservedWords;
  #[inline]
  unsafe fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    <&'a PossiblyReservedWords>::follow(buf, loc)
  }
}
impl<'a> flatbuffers::Follow<'a> for &'a PossiblyReservedWords {
  type Inner = &'a PossiblyReservedWords;
  #[inline]
  unsafe fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    flatbuffers::follow_cast_ref::<PossiblyReservedWords>(buf, loc)
  }
}
impl<'b> flatbuffers::Push for PossiblyReservedWords {
    type Output = PossiblyReservedWords;
    #[inline]
    unsafe fn push(&self, dst: &mut [u8], _written_len: usize) {
        let src = ::core::slice::from_raw_parts(self as *const PossiblyReservedWords as *const u8, Self::size());
        dst.copy_from_slice(src);
    }
}

impl<'a> flatbuffers::Verifiable for PossiblyReservedWords {
  #[inline]
  fn run_verifier(
    v: &mut flatbuffers::Verifier, pos: usize
  ) -> Result<(), flatbuffers::InvalidFlatbuffer> {
    use self::flatbuffers::Verifiable;
    v.in_buffer::<Self>(pos)
  }
}

impl<'a> PossiblyReservedWords {
  #[allow(clippy::too_many_arguments)]
  pub fn new(
    follow_: f32,
    push_: f32,
    size_: f32,
    alignment_: f32,
  ) -> Self {
    let mut s = Self([0; 16]);
    s.set_follow_(follow_);
    s.set_push_(push_);
    s.set_size_(size_);
    s.set_alignment_(alignment_);
    s
  }

  pub const fn get_fully_qualified_name() -> &'static str {
    "RustNamerTest.PossiblyReservedWords"
  }

  pub fn follow_(&self) -> f32 {
    let mut mem = core::mem::MaybeUninit::<<f32 as EndianScalar>::Scalar>::uninit();
    // Safety:
    // Created from a valid Table for this object
    // Which contains a valid value in this slot
    EndianScalar::from_little_endian(unsafe {
      core::ptr::copy_nonoverlapping(
        self.0[0..].as_ptr(),
        mem.as_mut_ptr() as *mut u8,
        core::mem::size_of::<<f32 as EndianScalar>::Scalar>(),
      );
      mem.assume_init()
    })
  }

  pub fn set_follow_(&mut self, x: f32) {
    let x_le = x.to_little_endian();
    // Safety:
    // Created from a valid Table for this object
    // Which contains a valid value in this slot
    unsafe {
      core::ptr::copy_nonoverlapping(
        &x_le as *const _ as *const u8,
        self.0[0..].as_mut_ptr(),
        core::mem::size_of::<<f32 as EndianScalar>::Scalar>(),
      );
    }
  }

  pub fn push_(&self) -> f32 {
    let mut mem = core::mem::MaybeUninit::<<f32 as EndianScalar>::Scalar>::uninit();
    // Safety:
    // Created from a valid Table for this object
    // Which contains a valid value in this slot
    EndianScalar::from_little_endian(unsafe {
      core::ptr::copy_nonoverlapping(
        self.0[4..].as_ptr(),
        mem.as_mut_ptr() as *mut u8,
        core::mem::size_of::<<f32 as EndianScalar>::Scalar>(),
      );
      mem.assume_init()
    })
  }

  pub fn set_push_(&mut self, x: f32) {
    let x_le = x.to_little_endian();
    // Safety:
    // Created from a valid Table for this object
    // Which contains a valid value in this slot
    unsafe {
      core::ptr::copy_nonoverlapping(
        &x_le as *const _ as *const u8,
        self.0[4..].as_mut_ptr(),
        core::mem::size_of::<<f32 as EndianScalar>::Scalar>(),
      );
    }
  }

  pub fn size_(&self) -> f32 {
    let mut mem = core::mem::MaybeUninit::<<f32 as EndianScalar>::Scalar>::uninit();
    // Safety:
    // Created from a valid Table for this object
    // Which contains a valid value in this slot
    EndianScalar::from_little_endian(unsafe {
      core::ptr::copy_nonoverlapping(
        self.0[8..].as_ptr(),
        mem.as_mut_ptr() as *mut u8,
        core::mem::size_of::<<f32 as EndianScalar>::Scalar>(),
      );
      mem.assume_init()
    })
  }

  pub fn set_size_(&mut self, x: f32) {
    let x_le = x.to_little_endian();
    // Safety:
    // Created from a valid Table for this object
    // Which contains a valid value in this slot
    unsafe {
      core::ptr::copy_nonoverlapping(
        &x_le as *const _ as *const u8,
        self.0[8..].as_mut_ptr(),
        core::mem::size_of::<<f32 as EndianScalar>::Scalar>(),
      );
    }
  }

  pub fn alignment_(&self) -> f32 {
    let mut mem = core::mem::MaybeUninit::<<f32 as EndianScalar>::Scalar>::uninit();
    // Safety:
    // Created from a valid Table for this object
    // Which contains a valid value in this slot
    EndianScalar::from_little_endian(unsafe {
      core::ptr::copy_nonoverlapping(
        self.0[12..].as_ptr(),
        mem.as_mut_ptr() as *mut u8,
        core::mem::size_of::<<f32 as EndianScalar>::Scalar>(),
      );
      mem.assume_init()
    })
  }

  pub fn set_alignment_(&mut self, x: f32) {
    let x_le = x.to_little_endian();
    // Safety:
    // Created from a valid Table for this object
    // Which contains a valid value in this slot
    unsafe {
      core::ptr::copy_nonoverlapping(
        &x_le as *const _ as *const u8,
        self.0[12..].as_mut_ptr(),
        core::mem::size_of::<<f32 as EndianScalar>::Scalar>(),
      );
    }
  }

  pub fn unpack(&self) -> PossiblyReservedWordsT {
    PossiblyReservedWordsT {
      follow_: self.follow_(),
      push_: self.push_(),
      size_: self.size_(),
      alignment_: self.alignment_(),
    }
  }
}

#[derive(Debug, Clone, PartialEq, Default)]
pub struct PossiblyReservedWordsT {
  pub follow_: f32,
  pub push_: f32,
  pub size_: f32,
  pub alignment_: f32,
}
impl PossiblyReservedWordsT {
  pub fn pack(&self) -> PossiblyReservedWords {
    PossiblyReservedWords::new(
      self.follow_,
      self.push_,
      self.size_,
      self.alignment_,
    )
  }
}

