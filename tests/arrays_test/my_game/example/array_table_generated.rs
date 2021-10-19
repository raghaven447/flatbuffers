// automatically generated by the FlatBuffers compiler, do not modify
extern crate alloc;
extern crate core;
extern crate flatbuffers;
use self::alloc::{boxed::Box, vec::Vec};
use self::alloc::string::{String, ToString as _};
use self::core::{cmp::Ordering, fmt, mem, ptr, slice};
use self::flatbuffers::{EndianScalar, Follow, Verifiable};
use super::*;
pub enum ArrayTableOffset {}
#[derive(Copy, Clone, PartialEq)]

pub struct ArrayTable<'a> {
  pub _tab: flatbuffers::Table<'a>,
}

impl<'a> flatbuffers::Follow<'a> for ArrayTable<'a> {
  type Inner = ArrayTable<'a>;
  #[inline]
  fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
    Self { _tab: flatbuffers::Table { buf, loc } }
  }
}

impl<'a> ArrayTable<'a> {
  pub const VT_A: flatbuffers::VOffsetT = 4;

  pub const fn get_fully_qualified_name() -> &'static str {
    "MyGame.Example.ArrayTable"
  }

  #[inline]
  pub fn init_from_table(table: flatbuffers::Table<'a>) -> Self {
    ArrayTable { _tab: table }
  }
  #[allow(unused_mut)]
  pub fn create<'bldr: 'args, 'args: 'mut_bldr, 'mut_bldr>(
    _fbb: &'mut_bldr mut flatbuffers::FlatBufferBuilder<'bldr>,
    args: &'args ArrayTableArgs<'args>
  ) -> flatbuffers::WIPOffset<ArrayTable<'bldr>> {
    let mut builder = ArrayTableBuilder::new(_fbb);
    if let Some(x) = args.a { builder.add_a(x); }
    builder.finish()
  }

  pub fn unpack(&self) -> ArrayTableT {
    let a = self.a().map(|x| {
      x.unpack()
    });
    ArrayTableT {
      a,
    }
  }

  #[inline]
  pub fn a(&self) -> Option<&'a ArrayStruct> {
    self._tab.get::<ArrayStruct>(ArrayTable::VT_A, None)
  }
}

impl flatbuffers::Verifiable for ArrayTable<'_> {
  #[inline]
  fn run_verifier(
    v: &mut flatbuffers::Verifier, pos: usize
  ) -> Result<(), flatbuffers::InvalidFlatbuffer> {
    v.visit_table(pos)?
     .visit_field::<ArrayStruct>("a", Self::VT_A, false)?
     .finish();
    Ok(())
  }
}
pub struct ArrayTableArgs<'a> {
    pub a: Option<&'a ArrayStruct>,
}
impl<'a> Default for ArrayTableArgs<'a> {
  #[inline]
  fn default() -> Self {
    ArrayTableArgs {
      a: None,
    }
  }
}
pub struct ArrayTableBuilder<'a: 'b, 'b> {
  fbb_: &'b mut flatbuffers::FlatBufferBuilder<'a>,
  start_: flatbuffers::WIPOffset<flatbuffers::TableUnfinishedWIPOffset>,
}
impl<'a: 'b, 'b> ArrayTableBuilder<'a, 'b> {
  #[inline]
  pub fn add_a(&mut self, a: &ArrayStruct) {
    self.fbb_.push_slot_always::<&ArrayStruct>(ArrayTable::VT_A, a);
  }
  #[inline]
  pub fn new(_fbb: &'b mut flatbuffers::FlatBufferBuilder<'a>) -> ArrayTableBuilder<'a, 'b> {
    let start = _fbb.start_table();
    ArrayTableBuilder {
      fbb_: _fbb,
      start_: start,
    }
  }
  #[inline]
  pub fn finish(self) -> flatbuffers::WIPOffset<ArrayTable<'a>> {
    let o = self.fbb_.end_table(self.start_);
    flatbuffers::WIPOffset::new(o.value())
  }
}

impl fmt::Debug for ArrayTable<'_> {
  fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
    let mut ds = f.debug_struct("ArrayTable");
      ds.field("a", &self.a());
      ds.finish()
  }
}
#[non_exhaustive]
#[derive(Debug, Clone, PartialEq)]
pub struct ArrayTableT {
  pub a: Option<ArrayStructT>,
}
impl Default for ArrayTableT {
  fn default() -> Self {
    Self {
      a: None,
    }
  }
}
impl ArrayTableT {
  pub fn pack<'b>(
    &self,
    _fbb: &mut flatbuffers::FlatBufferBuilder<'b>
  ) -> flatbuffers::WIPOffset<ArrayTable<'b>> {
    let a_tmp = self.a.as_ref().map(|x| x.pack());
    let a = a_tmp.as_ref();
    ArrayTable::create(_fbb, &ArrayTableArgs{
      a,
    })
  }
}
#[inline]
#[deprecated(since="2.0.0", note="Deprecated in favor of `root_as...` methods.")]
pub fn get_root_as_array_table<'a>(buf: &'a [u8]) -> ArrayTable<'a> {
  unsafe { flatbuffers::root_unchecked::<ArrayTable<'a>>(buf) }
}

#[inline]
#[deprecated(since="2.0.0", note="Deprecated in favor of `root_as...` methods.")]
pub fn get_size_prefixed_root_as_array_table<'a>(buf: &'a [u8]) -> ArrayTable<'a> {
  unsafe { flatbuffers::size_prefixed_root_unchecked::<ArrayTable<'a>>(buf) }
}

#[inline]
/// Verifies that a buffer of bytes contains a `ArrayTable`
/// and returns it.
/// Note that verification is still experimental and may not
/// catch every error, or be maximally performant. For the
/// previous, unchecked, behavior use
/// `root_as_array_table_unchecked`.
pub fn root_as_array_table(buf: &[u8]) -> Result<ArrayTable, flatbuffers::InvalidFlatbuffer> {
  flatbuffers::root::<ArrayTable>(buf)
}
#[inline]
/// Verifies that a buffer of bytes contains a size prefixed
/// `ArrayTable` and returns it.
/// Note that verification is still experimental and may not
/// catch every error, or be maximally performant. For the
/// previous, unchecked, behavior use
/// `size_prefixed_root_as_array_table_unchecked`.
pub fn size_prefixed_root_as_array_table(buf: &[u8]) -> Result<ArrayTable, flatbuffers::InvalidFlatbuffer> {
  flatbuffers::size_prefixed_root::<ArrayTable>(buf)
}
#[inline]
/// Verifies, with the given options, that a buffer of bytes
/// contains a `ArrayTable` and returns it.
/// Note that verification is still experimental and may not
/// catch every error, or be maximally performant. For the
/// previous, unchecked, behavior use
/// `root_as_array_table_unchecked`.
pub fn root_as_array_table_with_opts<'b, 'o>(
  opts: &'o flatbuffers::VerifierOptions,
  buf: &'b [u8],
) -> Result<ArrayTable<'b>, flatbuffers::InvalidFlatbuffer> {
  flatbuffers::root_with_opts::<ArrayTable<'b>>(opts, buf)
}
#[inline]
/// Verifies, with the given verifier options, that a buffer of
/// bytes contains a size prefixed `ArrayTable` and returns
/// it. Note that verification is still experimental and may not
/// catch every error, or be maximally performant. For the
/// previous, unchecked, behavior use
/// `root_as_array_table_unchecked`.
pub fn size_prefixed_root_as_array_table_with_opts<'b, 'o>(
  opts: &'o flatbuffers::VerifierOptions,
  buf: &'b [u8],
) -> Result<ArrayTable<'b>, flatbuffers::InvalidFlatbuffer> {
  flatbuffers::size_prefixed_root_with_opts::<ArrayTable<'b>>(opts, buf)
}
#[inline]
/// Assumes, without verification, that a buffer of bytes contains a ArrayTable and returns it.
/// # Safety
/// Callers must trust the given bytes do indeed contain a valid `ArrayTable`.
pub unsafe fn root_as_array_table_unchecked(buf: &[u8]) -> ArrayTable {
  flatbuffers::root_unchecked::<ArrayTable>(buf)
}
#[inline]
/// Assumes, without verification, that a buffer of bytes contains a size prefixed ArrayTable and returns it.
/// # Safety
/// Callers must trust the given bytes do indeed contain a valid size prefixed `ArrayTable`.
pub unsafe fn size_prefixed_root_as_array_table_unchecked(buf: &[u8]) -> ArrayTable {
  flatbuffers::size_prefixed_root_unchecked::<ArrayTable>(buf)
}
pub const ARRAY_TABLE_IDENTIFIER: &str = "ARRT";

#[inline]
pub fn array_table_buffer_has_identifier(buf: &[u8]) -> bool {
  flatbuffers::buffer_has_identifier(buf, ARRAY_TABLE_IDENTIFIER, false)
}

#[inline]
pub fn array_table_size_prefixed_buffer_has_identifier(buf: &[u8]) -> bool {
  flatbuffers::buffer_has_identifier(buf, ARRAY_TABLE_IDENTIFIER, true)
}

pub const ARRAY_TABLE_EXTENSION: &str = "mon";

#[inline]
pub fn finish_array_table_buffer<'a, 'b>(
    fbb: &'b mut flatbuffers::FlatBufferBuilder<'a>,
    root: flatbuffers::WIPOffset<ArrayTable<'a>>) {
  fbb.finish(root, Some(ARRAY_TABLE_IDENTIFIER));
}

#[inline]
pub fn finish_size_prefixed_array_table_buffer<'a, 'b>(fbb: &'b mut flatbuffers::FlatBufferBuilder<'a>, root: flatbuffers::WIPOffset<ArrayTable<'a>>) {
  fbb.finish_size_prefixed(root, Some(ARRAY_TABLE_IDENTIFIER));
}
