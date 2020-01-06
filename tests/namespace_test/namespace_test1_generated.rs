// automatically generated by the FlatBuffers compiler, do not modify


pub mod namespace_a {
    pub mod namespace_b {
        #![allow(unused_imports, irrefutable_let_patterns, dead_code, unused_mut)]
        use flatbuffers::{
            deserialize::{FromStructField, FromTableField, FromTableFieldUnion, Str, Table, Vector},
            errors::{InvalidFlatbuffer, OutOfBufferSpace, TryFromEnumError},
            serialize::{
                builder::FlatbufferWriter, FlatbufferPrimitive, FlatbufferTable, Offset, RawOffset,
            },
        };
        use core::{
            convert::{TryFrom, TryInto},
            fmt, ptr,
        };

        /// Enum for the flatbuffer `EnumInNestedNS` enum
        ///
        #[derive(Copy, Clone, Debug, PartialEq, Eq, PartialOrd, Ord, Hash)]
        pub enum EnumInNestedNS {
            A = 0,
            B = 1,
            C = 2,
        }

        impl From<EnumInNestedNS> for i8 {
            #[inline]
            fn from(value: EnumInNestedNS) -> i8 {
                value as i8
            }
        }

        impl TryFrom<i8> for EnumInNestedNS {
            type Error = TryFromEnumError;
            #[inline]
            fn try_from(value: i8) -> Result<EnumInNestedNS, TryFromEnumError> {
                match value {
                    0 => Ok(EnumInNestedNS::A),
                    1 => Ok(EnumInNestedNS::B),
                    2 => Ok(EnumInNestedNS::C),
                    _ => Err(TryFromEnumError),
                }
            }
        }

        #[doc(hidden)]
        impl<'a> FromTableField<'a> for EnumInNestedNS {
            const INLINE_SIZE: usize = 1;

            #[inline]
            fn from_field(buf: &'a [u8], offset: usize) -> Result<EnumInNestedNS, InvalidFlatbuffer> {
                i8::from_field(buf, offset)?
                    .try_into()
                    .or(Err(InvalidFlatbuffer))
            }
        }

        #[doc(hidden)]
        unsafe impl<'a> FromStructField<'a> for EnumInNestedNS {
            type Input = [u8; 1];

            #[inline]
            fn from_struct_field(buf: &'a Self::Input) -> Result<EnumInNestedNS, InvalidFlatbuffer> {
                i8::from_struct_field(buf)?
                    .try_into()
                    .or(Err(InvalidFlatbuffer))
            }
        }

        unsafe impl FlatbufferPrimitive for EnumInNestedNS {
            const SIZE: usize = 1;
            const ALIGNMENT: usize = 1;

            #[inline]
            unsafe fn serialize(&self, buffer: *mut u8, offset: RawOffset) {
                FlatbufferPrimitive::serialize(&(*self as i8), buffer, offset)
            }
        }

        /// View of a flatbuffer `TableInNestedNS` object
        ///
        /// This struct is used for deserializing. For serializing see [`TableInNestedNS`](struct.TableInNestedNS.html).
        ///
        #[derive(Copy, Clone)]
        pub struct TableInNestedNSView<'a> {
            table: Table<'a>,
        }

        #[doc(hidden)]
        impl<'a> FromTableField<'a> for TableInNestedNSView<'a> {
            const INLINE_SIZE: usize = Table::INLINE_SIZE;

            #[inline]
            fn from_field(buf: &'a [u8], offset: usize) -> Result<Self, InvalidFlatbuffer> {
                FromTableField::from_field(buf, offset).map(|table| Self { table })
            }
        }

        impl<'a> TableInNestedNSView<'a> {
            /// Getter for the `foo` field.
            ///
            ///
            /// # Panics
            ///
            /// If the value cannot be deserialized.
            #[inline]
            pub fn foo(&self) -> i32 {
                self.try_get_foo().unwrap()
            }

            /// Getter for the `foo` field.
            ///
            #[inline]
            pub fn try_get_foo(&self) -> Result<i32, InvalidFlatbuffer> {
                self.table.get_field(4).map(|value| value.unwrap_or(0))
            }

            /// Begin parsing a flatbuffer with a `Weapon` as the root object
            #[inline]
            pub fn from_buffer_as_root(buffer: &'a [u8]) -> Result<Self, InvalidFlatbuffer> {
                FromTableField::from_field(buffer, 0)
            }
        }

        impl<'a> fmt::Debug for TableInNestedNSView<'a> {
            fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
                formatter.debug_struct("TableInNestedNSView")
                    .field("foo", &self.try_get_foo())
                    .finish()
            }
        }

        /// Builder for a flatbuffer `TableInNestedNS` object
        ///
        /// This struct is used for serializing. For deserializing see [`TableInNestedNSView`](struct.TableInNestedNSView.html).
        ///
        #[derive(Copy, Clone, Debug, PartialEq)]
        pub struct TableInNestedNS {
            pub foo: i32,
        }

        impl Default for TableInNestedNS {
            #[inline]
            fn default() -> TableInNestedNS {
                TableInNestedNS {
                    foo: 0,
                }
            }
        }

        unsafe impl FlatbufferTable for TableInNestedNS {
            #[inline]
            fn validate_required(&self) {
            }

            #[inline]
            fn serialize<F: FlatbufferWriter>(
                &self,
                flatbuffer: &mut F,
            ) -> Result<RawOffset, OutOfBufferSpace> {
                let mut vtable = [0u8; 6];

                let mut size = 0;
                let mut alignment = 4;
                let mut vtable_len = 4;

                if self.foo != 0 {
                    vtable_len = vtable_len.max(4 + 2);
                    const CUR_ALIGN: usize = <i32 as FlatbufferPrimitive>::ALIGNMENT;
                    alignment = alignment.max(CUR_ALIGN);
                    vtable[4..4+2].copy_from_slice(
                        &((size + 4) as u16).to_le_bytes());
                    size += <i32 as FlatbufferPrimitive>::SIZE;
                }
                flatbuffer.align_before_write(size, alignment - 1)?;
                if self.foo != 0 {
                    flatbuffer.write_primitive(&self.foo)?;
                }
                flatbuffer.write_vtable_and_offset(&mut vtable[..vtable_len], size + 4)
            }
        }

        /// View of a flatbuffer `StructInNestedNS` object
        ///
        /// This struct is used for deserializing. For serializing see [`StructInNestedNS`](struct.StructInNestedNS.html).
        ///
        #[derive(Copy, Clone)]
        pub struct StructInNestedNSView<'a> {
            slice: &'a [u8; 8],
        }

        #[doc(hidden)]
        impl<'a> FromTableField<'a> for StructInNestedNSView<'a> {
            const INLINE_SIZE: usize = 8;

            #[inline]
            fn from_field(buf: &'a [u8], offset: usize) -> Result<Self, InvalidFlatbuffer> {
                let slice = buf.get(offset..offset + 8).ok_or(InvalidFlatbuffer)?;
                Ok(Self {
                    slice: unsafe { &*(slice.as_ptr() as *const [u8; 8]) },
                })
            }
        }

        #[doc(hidden)]
        unsafe impl<'a> FromStructField<'a> for StructInNestedNSView<'a> {
            type Input = [u8; 8];

            #[inline]
            fn from_struct_field(slice: &'a Self::Input) -> Result<Self, InvalidFlatbuffer> {
                Ok(Self { slice })
            }
        }

        impl<'a> StructInNestedNSView<'a> {
            /// Getter for the `a` field.
            ///
            ///
            /// # Panics
            ///
            /// If the value cannot be deserialized.
            #[inline]
            pub fn a(self) -> i32 {
                self.try_get_a().unwrap()
            }

            /// Getter for the `a` field.
            ///
            #[inline]
            pub fn try_get_a(self) -> Result<i32, InvalidFlatbuffer> {
                type SliceType<'a> = <i32 as FromStructField<'a>>::Input;
                const OFFSET: usize = 0;
                const SIZE: usize = core::mem::size_of::<SliceType>();
                let slice = self.slice.get(OFFSET..OFFSET+SIZE).unwrap();
                let slice: &'a SliceType<'a> = unsafe { &*(slice.as_ptr() as *const SliceType<'a>) };
                <i32 as FromStructField<'a>>::from_struct_field(slice)
            }

            /// Getter for the `b` field.
            ///
            ///
            /// # Panics
            ///
            /// If the value cannot be deserialized.
            #[inline]
            pub fn b(self) -> i32 {
                self.try_get_b().unwrap()
            }

            /// Getter for the `b` field.
            ///
            #[inline]
            pub fn try_get_b(self) -> Result<i32, InvalidFlatbuffer> {
                type SliceType<'a> = <i32 as FromStructField<'a>>::Input;
                const OFFSET: usize = 4;
                const SIZE: usize = core::mem::size_of::<SliceType>();
                let slice = self.slice.get(OFFSET..OFFSET+SIZE).unwrap();
                let slice: &'a SliceType<'a> = unsafe { &*(slice.as_ptr() as *const SliceType<'a>) };
                <i32 as FromStructField<'a>>::from_struct_field(slice)
            }

        }

        impl<'a> fmt::Debug for StructInNestedNSView<'a> {
            fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
                formatter
                    .debug_struct("StructInNestedNSView")
                    .field("a", &self.try_get_a())
                    .field("b", &self.try_get_b())
                    .finish()
            }
        }

        impl<'a> PartialEq for StructInNestedNSView<'a> {
            #[inline]
            fn eq(&self, other: &Self) -> bool {
                self.slice[..] == other.slice[..]
            }
        }

        /// Builder for a flatbuffer `StructInNestedNS` object
        ///
        /// This struct is used for serializing. For deserializing see [`StructInNestedNSView`](struct.StructInNestedNSView.html).
        ///
        #[derive(Copy, Clone, Debug, PartialEq)]
        pub struct StructInNestedNS {
            pub a: i32,
            pub b: i32,
        }

        unsafe impl FlatbufferPrimitive for StructInNestedNS {
            const SIZE: usize = 8;
            const ALIGNMENT: usize = 4;

            #[inline]
            unsafe fn serialize(&self, buffer: *mut u8, offset: RawOffset) {
                FlatbufferPrimitive::serialize(&self.a, buffer.add(0), offset + 0);
                FlatbufferPrimitive::serialize(&self.b, buffer.add(4), offset + 4);
            }
        }
    }
}
