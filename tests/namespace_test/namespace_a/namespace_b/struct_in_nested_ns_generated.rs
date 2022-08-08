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
// struct StructInNestedNS, aligned to 4
#[repr(transparent)]
#[derive(Clone, Copy, PartialEq)]
pub struct StructInNestedNS(pub [u8; 8]);
impl Default for StructInNestedNS { 
  fn default() -> Self { 
    Self([0; 8])
  }
}
impl core::fmt::Debug for StructInNestedNS {
  fn fmt(&self, f: &mut core::fmt::Formatter) -> core::fmt::Result {
    f.debug_struct("StructInNestedNS")
      .field("a", &self.a())
      .field("b", &self.b())
      .finish()
  }
}

impl flatbuffers::SimpleToVerifyInSlice for StructInNestedNS {}
impl flatbuffers::SafeSliceAccess for StructInNestedNS {}
impl<'a> flatbuffers::Follow<'a> for StructInNestedNS {
  type Inner = &'a StructInNestedNS;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    <&'a StructInNestedNS>::follow(buf, loc)
  }
}
impl<'a> flatbuffers::Follow<'a> for &'a StructInNestedNS {
  type Inner = &'a StructInNestedNS;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    flatbuffers::follow_cast_ref::<StructInNestedNS>(buf, loc)
  }
}
impl<'b> flatbuffers::Push for StructInNestedNS {
    type Output = StructInNestedNS;
    #[inline]
    fn push(&self, dst: &mut [u8], _rest: &[u8]) {
        let src = unsafe {
            ::core::slice::from_raw_parts(self as *const StructInNestedNS as *const u8, Self::size())
        };
        dst.copy_from_slice(src);
    }
}
impl<'b> flatbuffers::Push for &'b StructInNestedNS {
    type Output = StructInNestedNS;

    #[inline]
    fn push(&self, dst: &mut [u8], _rest: &[u8]) {
        let src = unsafe {
            ::core::slice::from_raw_parts(*self as *const StructInNestedNS as *const u8, Self::size())
        };
        dst.copy_from_slice(src);
    }
}

impl<'a> flatbuffers::Verifiable for StructInNestedNS {
  #[inline]
  fn run_verifier(
    v: &mut flatbuffers::Verifier, pos: usize
  ) -> Result<(), flatbuffers::InvalidFlatbuffer> {
    use self::flatbuffers::Verifiable;
    v.in_buffer::<Self>(pos)
  }
}

impl<'a> StructInNestedNS {
  #[allow(clippy::too_many_arguments)]
  pub fn new(
    a: i32,
    b: i32,
  ) -> Self {
    let mut s = Self([0; 8]);
    s.set_a(a);
    s.set_b(b);
    s
  }

  pub const fn get_fully_qualified_name() -> &'static str {
    "NamespaceA.NamespaceB.StructInNestedNS"
  }

  pub fn a(&self) -> i32 {
    let mut mem = core::mem::MaybeUninit::<i32>::uninit();
    unsafe {
      core::ptr::copy_nonoverlapping(
        self.0[0..].as_ptr(),
        mem.as_mut_ptr() as *mut u8,
        core::mem::size_of::<i32>(),
      );
      mem.assume_init()
    }.from_little_endian()
  }

  pub fn set_a(&mut self, x: i32) {
    let x_le = x.to_little_endian();
    unsafe {
      core::ptr::copy_nonoverlapping(
        &x_le as *const i32 as *const u8,
        self.0[0..].as_mut_ptr(),
        core::mem::size_of::<i32>(),
      );
    }
  }

  pub fn b(&self) -> i32 {
    let mut mem = core::mem::MaybeUninit::<i32>::uninit();
    unsafe {
      core::ptr::copy_nonoverlapping(
        self.0[4..].as_ptr(),
        mem.as_mut_ptr() as *mut u8,
        core::mem::size_of::<i32>(),
      );
      mem.assume_init()
    }.from_little_endian()
  }

  pub fn set_b(&mut self, x: i32) {
    let x_le = x.to_little_endian();
    unsafe {
      core::ptr::copy_nonoverlapping(
        &x_le as *const i32 as *const u8,
        self.0[4..].as_mut_ptr(),
        core::mem::size_of::<i32>(),
      );
    }
  }

  pub fn unpack(&self) -> StructInNestedNST {
    StructInNestedNST {
      a: self.a(),
      b: self.b(),
    }
  }
}

#[derive(Debug, Clone, PartialEq, Default)]
pub struct StructInNestedNST {
  pub a: i32,
  pub b: i32,
}
impl StructInNestedNST {
  pub fn pack(&self) -> StructInNestedNS {
    StructInNestedNS::new(
      self.a,
      self.b,
    )
  }
}

