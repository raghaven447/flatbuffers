// automatically generated by the FlatBuffers compiler, do not modify
extern crate alloc;
extern crate core;
extern crate flatbuffers;
use self::alloc::{boxed::Box, vec::Vec};
use self::alloc::string::{String, ToString as _};
use self::core::{cmp::Ordering, fmt, mem, ptr, slice};
use self::flatbuffers::{EndianScalar, Follow, Verifiable};
use super::*;
pub enum ReferrableOffset {}
#[derive(Copy, Clone, PartialEq)]

pub struct Referrable<'a> {
  pub _tab: flatbuffers::Table<'a>,
}

impl<'a> flatbuffers::Follow<'a> for Referrable<'a> {
  type Inner = Referrable<'a>;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    Self { _tab: flatbuffers::Table { buf, loc } }
  }
}

impl<'a> Referrable<'a> {
  pub const VT_ID: flatbuffers::VOffsetT = 4;

  pub const fn get_fully_qualified_name() -> &'static str {
    "MyGame.Example.Referrable"
  }

  #[inline]
  pub fn init_from_table(table: flatbuffers::Table<'a>) -> Self {
    Referrable { _tab: table }
  }
  #[allow(unused_mut)]
  pub fn create<'bldr: 'args, 'args: 'mut_bldr, 'mut_bldr>(
    _fbb: &'mut_bldr mut flatbuffers::FlatBufferBuilder<'bldr>,
    args: &'args ReferrableArgs
  ) -> flatbuffers::WIPOffset<Referrable<'bldr>> {
    let mut builder = ReferrableBuilder::new(_fbb);
    builder.add_id(args.id);
    builder.finish()
  }

  pub fn unpack(&self) -> ReferrableT {
    let id = self.id();
    ReferrableT {
      id,
    }
  }

  #[inline]
  pub fn id(&self) -> u64 {
    self._tab.get::<u64>(Referrable::VT_ID, Some(0)).unwrap()
  }
  #[inline]
  pub fn key_compare_less_than(&self, o: &Referrable) -> bool {
    self.id() < o.id()
  }

  #[inline]
  pub fn key_compare_with_value(&self, val: u64) ->  Ordering {
    let key = self.id();
    key.cmp(&val)
  }
}

impl flatbuffers::Verifiable for Referrable<'_> {
  #[inline]
  fn run_verifier(
    v: &mut flatbuffers::Verifier, pos: usize
  ) -> Result<(), flatbuffers::InvalidFlatbuffer> {
    v.visit_table(pos)?
     .visit_field::<u64>("id", Self::VT_ID, false)?
     .finish();
    Ok(())
  }
}
pub struct ReferrableArgs {
    pub id: u64,
}
impl<'a> Default for ReferrableArgs {
  #[inline]
  fn default() -> Self {
    ReferrableArgs {
      id: 0,
    }
  }
}
pub struct ReferrableBuilder<'a: 'b, 'b> {
  fbb_: &'b mut flatbuffers::FlatBufferBuilder<'a>,
  start_: flatbuffers::WIPOffset<flatbuffers::TableUnfinishedWIPOffset>,
}
impl<'a: 'b, 'b> ReferrableBuilder<'a, 'b> {
  #[inline]
  pub fn add_id(&mut self, id: u64) {
    self.fbb_.push_slot::<u64>(Referrable::VT_ID, id, 0);
  }
  #[inline]
  pub fn new(_fbb: &'b mut flatbuffers::FlatBufferBuilder<'a>) -> ReferrableBuilder<'a, 'b> {
    let start = _fbb.start_table();
    ReferrableBuilder {
      fbb_: _fbb,
      start_: start,
    }
  }
  #[inline]
  pub fn finish(self) -> flatbuffers::WIPOffset<Referrable<'a>> {
    let o = self.fbb_.end_table(self.start_);
    flatbuffers::WIPOffset::new(o.value())
  }
}

impl fmt::Debug for Referrable<'_> {
  fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
    let mut ds = f.debug_struct("Referrable");
      ds.field("id", &self.id());
      ds.finish()
  }
}
#[non_exhaustive]
#[derive(Debug, Clone, PartialEq)]
pub struct ReferrableT {
  pub id: u64,
}
impl Default for ReferrableT {
  fn default() -> Self {
    Self {
      id: 0,
    }
  }
}
impl ReferrableT {
  pub fn pack<'b>(
    &self,
    _fbb: &mut flatbuffers::FlatBufferBuilder<'b>
  ) -> flatbuffers::WIPOffset<Referrable<'b>> {
    let id = self.id;
    Referrable::create(_fbb, &ReferrableArgs{
      id,
    })
  }
}
