// automatically generated by the FlatBuffers compiler, do not modify
// @generated
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
pub enum TableAOffset {}
#[derive(Copy, Clone, PartialEq)]

pub struct TableA<'a> {
  pub _tab: flatbuffers::Table<'a>,
}

impl<'a> flatbuffers::Follow<'a> for TableA<'a> {
  type Inner = TableA<'a>;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    Self { _tab: flatbuffers::Table { buf, loc } }
  }
}

impl<'a> TableA<'a> {
  pub const VT_B: flatbuffers::VOffsetT = 4;

  pub const fn get_fully_qualified_name() -> &'static str {
    "TableA"
  }

  #[inline]
  pub fn init_from_table(table: flatbuffers::Table<'a>) -> Self {
    TableA { _tab: table }
  }
  #[allow(unused_mut)]
  pub fn create<'bldr: 'args, 'args: 'mut_bldr, 'mut_bldr>(
    _fbb: &'mut_bldr mut flatbuffers::FlatBufferBuilder<'bldr>,
    args: &'args TableAArgs<'args>
  ) -> flatbuffers::WIPOffset<TableA<'bldr>> {
    let mut builder = TableABuilder::new(_fbb);
    if let Some(x) = args.b { builder.add_b(x); }
    builder.finish()
  }

  pub fn unpack(&self) -> TableAT {
    let b = self.b().map(|x| {
      Box::new(x.unpack())
    });
    TableAT {
      b,
    }
  }

  #[inline]
  pub fn b(&self) -> Option<my_game::other_name_space::TableB<'a>> {
    self._tab.get::<flatbuffers::ForwardsUOffset<my_game::other_name_space::TableB>>(TableA::VT_B, None)
  }
}

impl flatbuffers::FullyQualifiedName for TableA<'_> {
  fn get_fully_qualified_name() -> &'static str {
    "TableA"
  }
}

impl flatbuffers::Verifiable for TableA<'_> {
  #[inline]
  fn run_verifier(
    v: &mut flatbuffers::Verifier, pos: usize
  ) -> Result<(), flatbuffers::InvalidFlatbuffer> {
    use self::flatbuffers::Verifiable;
    v.visit_table(pos)?
     .visit_field::<flatbuffers::ForwardsUOffset<my_game::other_name_space::TableB>>("b", Self::VT_B, false)?
     .finish();
    Ok(())
  }
}
pub struct TableAArgs<'a> {
    pub b: Option<flatbuffers::WIPOffset<my_game::other_name_space::TableB<'a>>>,
}
impl<'a> Default for TableAArgs<'a> {
  #[inline]
  fn default() -> Self {
    TableAArgs {
      b: None,
    }
  }
}

impl Serialize for TableA<'_> {
  fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
  where
    S: Serializer,
  {
    let mut s = serializer.serialize_struct("TableA", 1)?;
      if let Some(f) = self.b() {
        s.serialize_field("b", &f)?;
      } else {
        s.skip_field("b")?;
      }
    s.end()
  }
}

pub struct TableABuilder<'a: 'b, 'b> {
  fbb_: &'b mut flatbuffers::FlatBufferBuilder<'a>,
  start_: flatbuffers::WIPOffset<flatbuffers::TableUnfinishedWIPOffset>,
}
impl<'a: 'b, 'b> TableABuilder<'a, 'b> {
  #[inline]
  pub fn add_b(&mut self, b: flatbuffers::WIPOffset<my_game::other_name_space::TableB<'b >>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<my_game::other_name_space::TableB>>(TableA::VT_B, b);
  }
  #[inline]
  pub fn new(_fbb: &'b mut flatbuffers::FlatBufferBuilder<'a>) -> TableABuilder<'a, 'b> {
    let start = _fbb.start_table();
    TableABuilder {
      fbb_: _fbb,
      start_: start,
    }
  }
  #[inline]
  pub fn finish(self) -> flatbuffers::WIPOffset<TableA<'a>> {
    let o = self.fbb_.end_table(self.start_);
    flatbuffers::WIPOffset::new(o.value())
  }
}

impl core::fmt::Debug for TableA<'_> {
  fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
    let mut ds = f.debug_struct("TableA");
      ds.field("b", &self.b());
      ds.finish()
  }
}
#[non_exhaustive]
#[derive(Debug, Clone, PartialEq)]
pub struct TableAT {
  pub b: Option<Box<my_game::other_name_space::TableBT>>,
}
impl Default for TableAT {
  fn default() -> Self {
    Self {
      b: None,
    }
  }
}
impl TableAT {
  pub fn pack<'b>(
    &self,
    _fbb: &mut flatbuffers::FlatBufferBuilder<'b>
  ) -> flatbuffers::WIPOffset<TableA<'b>> {
    let b = self.b.as_ref().map(|x|{
      x.pack(_fbb)
    });
    TableA::create(_fbb, &TableAArgs{
      b,
    })
  }
}
