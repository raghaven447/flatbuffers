// automatically generated by the FlatBuffers compiler, do not modify
extern crate alloc;
extern crate core;
extern crate flatbuffers;
use self::alloc::{boxed::Box, vec::Vec};
use self::alloc::string::{String, ToString as _};
use self::core::{cmp::Ordering, fmt, mem, ptr, slice};
use self::flatbuffers::{EndianScalar, Follow, Verifiable};
use super::*;
// struct Test, aligned to 2
#[repr(transparent)]
#[derive(Clone, Copy, PartialEq)]
pub struct Test(pub [u8; 4]);
impl Default for Test { 
  fn default() -> Self { 
    Self([0; 4])
  }
}
impl fmt::Debug for Test {
  fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
    f.debug_struct("Test")
      .field("a", &self.a())
      .field("b", &self.b())
      .finish()
  }
}

impl flatbuffers::SimpleToVerifyInSlice for Test {}
impl flatbuffers::SafeSliceAccess for Test {}
impl<'a> flatbuffers::Follow<'a> for Test {
  type Inner = &'a Test;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    <&'a Test>::follow(buf, loc)
  }
}
impl<'a> flatbuffers::Follow<'a> for &'a Test {
  type Inner = &'a Test;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    flatbuffers::follow_cast_ref::<Test>(buf, loc)
  }
}
impl<'b> flatbuffers::Push for Test {
    type Output = Test;
    #[inline]
    fn push(&self, dst: &mut [u8], _rest: &[u8]) {
        let src = unsafe {
            slice::from_raw_parts(self as *const Test as *const u8, Self::size())
        };
        dst.copy_from_slice(src);
    }
}
impl<'b> flatbuffers::Push for &'b Test {
    type Output = Test;

    #[inline]
    fn push(&self, dst: &mut [u8], _rest: &[u8]) {
        let src = unsafe {
            slice::from_raw_parts(*self as *const Test as *const u8, Self::size())
        };
        dst.copy_from_slice(src);
    }
}

impl<'a> flatbuffers::Verifiable for Test {
  #[inline]
  fn run_verifier(
    v: &mut flatbuffers::Verifier, pos: usize
  ) -> Result<(), flatbuffers::InvalidFlatbuffer> {
    v.in_buffer::<Self>(pos)
  }
}
impl<'a> Test {
  #[allow(clippy::too_many_arguments)]
  pub fn new(
    a: i16,
    b: i8,
  ) -> Self {
    let mut s = Self([0; 4]);
    s.set_a(a);
    s.set_b(b);
    s
  }

  pub const fn get_fully_qualified_name() -> &'static str {
    "MyGame.Example.Test"
  }

  pub fn a(&self) -> i16 {
    let mut uninit = mem::MaybeUninit::<i16>::uninit();
    unsafe {
      ptr::copy_nonoverlapping(
        self.0[0..].as_ptr(),
        uninit.as_mut_ptr() as *mut u8,
        mem::size_of::<i16>(),
      );
      uninit.assume_init()
    }.from_little_endian()
  }

  pub fn set_a(&mut self, x: i16) {
    let x_le = x.to_little_endian();
    unsafe {
      ptr::copy_nonoverlapping(
        &x_le as *const i16 as *const u8,
        self.0[0..].as_mut_ptr(),
        mem::size_of::<i16>(),
      );
    }
  }

  pub fn b(&self) -> i8 {
    let mut uninit = mem::MaybeUninit::<i8>::uninit();
    unsafe {
      ptr::copy_nonoverlapping(
        self.0[2..].as_ptr(),
        uninit.as_mut_ptr() as *mut u8,
        mem::size_of::<i8>(),
      );
      uninit.assume_init()
    }.from_little_endian()
  }

  pub fn set_b(&mut self, x: i8) {
    let x_le = x.to_little_endian();
    unsafe {
      ptr::copy_nonoverlapping(
        &x_le as *const i8 as *const u8,
        self.0[2..].as_mut_ptr(),
        mem::size_of::<i8>(),
      );
    }
  }

  pub fn unpack(&self) -> TestT {
    TestT {
      a: self.a(),
      b: self.b(),
    }
  }
}

#[derive(Debug, Clone, PartialEq, Default)]
pub struct TestT {
  pub a: i16,
  pub b: i8,
}
impl TestT {
  pub fn pack(&self) -> Test {
    Test::new(
      self.a,
      self.b,
    )
  }
}

