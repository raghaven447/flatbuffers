// automatically generated by the FlatBuffers compiler, do not modify


pub mod my_game {
    pub mod sample {
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

        /// Enum for the flatbuffer `Color` enum
        ///
        #[derive(Copy, Clone, Debug, PartialEq, Eq, PartialOrd, Ord, Hash)]
        pub enum Color {
            Red = 0,
            Green = 1,
            Blue = 2,
        }

        impl From<Color> for i8 {
            #[inline]
            fn from(value: Color) -> i8 {
                value as i8
            }
        }

        impl TryFrom<i8> for Color {
            type Error = TryFromEnumError;
            #[inline]
            fn try_from(value: i8) -> Result<Color, TryFromEnumError> {
                match value {
                    0 => Ok(Color::Red),
                    1 => Ok(Color::Green),
                    2 => Ok(Color::Blue),
                    _ => Err(TryFromEnumError),
                }
            }
        }

        #[doc(hidden)]
        impl<'a> FromTableField<'a> for Color {
            const INLINE_SIZE: usize = 1;

            #[inline]
            fn from_field(buf: &'a [u8], offset: usize) -> Result<Color, InvalidFlatbuffer> {
                i8::from_field(buf, offset)?
                    .try_into()
                    .or(Err(InvalidFlatbuffer))
            }
        }

        #[doc(hidden)]
        unsafe impl<'a> FromStructField<'a> for Color {
            type Input = [u8; 1];

            #[inline]
            fn from_struct_field(buf: &'a Self::Input) -> Result<Color, InvalidFlatbuffer> {
                i8::from_struct_field(buf)?
                    .try_into()
                    .or(Err(InvalidFlatbuffer))
            }
        }

        unsafe impl FlatbufferPrimitive for Color {
            const SIZE: usize = 1;
            const ALIGNMENT: usize = 1;

            #[inline]
            unsafe fn serialize(&self, buffer: *mut u8, offset: RawOffset) {
                FlatbufferPrimitive::serialize(&(*self as i8), buffer, offset)
            }
        }

        #[derive(Copy, Clone)]
        enum EquipmentTag {
            NONE = 0,
            Weapon = 1,
        }

        impl<'a> FromTableField<'a> for EquipmentTag {
            const INLINE_SIZE: usize = 1;

            #[inline]
            fn from_field(buf: &'a [u8], offset: usize) -> Result<EquipmentTag, InvalidFlatbuffer> {
                match u8::from_field(buf, offset)? {
                    1 => Ok(EquipmentTag::Weapon),
                    _ => Ok(EquipmentTag::NONE),
                }
            }
        }

        unsafe impl FlatbufferPrimitive for EquipmentTag {
            const SIZE: usize = 1;
            const ALIGNMENT: usize = 1;

            #[inline]
            unsafe fn serialize(&self, buffer: *mut u8, offset: RawOffset) {
                FlatbufferPrimitive::serialize(&(*self as u8), buffer, offset)
            }
        }

        /// View of a flatbuffer `Equipment` object
        ///
        /// This enum is used for deserializing. For serializing see [`Equipment`](enum.Equipment.html).
        ///
        #[derive(Copy, Clone, Debug)]
        pub enum EquipmentView<'a> {
            Weapon(WeaponView<'a>),
        }

        #[doc(hidden)]
        impl<'a> FromTableFieldUnion<'a> for EquipmentView<'a> {
            #[inline]
            fn from_field_union(
                buf: &'a [u8],
                tag_offset: usize,
                value_offset: usize,
            ) -> Result<Option<Self>, InvalidFlatbuffer> {
                match EquipmentTag::from_field(buf, tag_offset)? {
                    EquipmentTag::NONE => Ok(None),
                    EquipmentTag::Weapon => Ok(Some(EquipmentView::Weapon(FromTableField::from_field(
                        buf,
                        value_offset,
                    )?))),
                }
            }
        }

        impl<'a> EquipmentView<'a> {
            #[inline]
            pub fn as_weapon(self) -> Option<WeaponView<'a>> {
                if let EquipmentView::Weapon(inner) = self {
                    Some(inner)
                } else {
                    None
                }
            }

        }

        /// Builder for a flatbuffer `Equipment` object
        ///
        /// This enum is used for serializing. For deserializing see [`EquipmentView`](enum.EquipmentView.html).
        ///
        #[derive(Copy, Clone, Debug, PartialEq)]
        pub enum Equipment {
            Weapon(Offset<Weapon>),
        }

        impl Equipment {
            #[inline]
            fn tag(&self) -> EquipmentTag {
                match self {
                    Equipment::Weapon(_) => EquipmentTag::Weapon,
                }
            }

            #[inline]
            fn offset(&self) -> RawOffset {
                match self {
                    Equipment::Weapon(offset) => offset.raw_offset(),
                }
            }
        }

        /// View of a flatbuffer `Vec3` object
        ///
        /// This struct is used for deserializing. For serializing see [`Vec3`](struct.Vec3.html).
        ///
        #[derive(Copy, Clone)]
        pub struct Vec3View<'a> {
            slice: &'a [u8; 12],
        }

        #[doc(hidden)]
        impl<'a> FromTableField<'a> for Vec3View<'a> {
            const INLINE_SIZE: usize = 12;

            #[inline]
            fn from_field(buf: &'a [u8], offset: usize) -> Result<Self, InvalidFlatbuffer> {
                let slice = buf.get(offset..offset + 12).ok_or(InvalidFlatbuffer)?;
                Ok(Self {
                    slice: unsafe { &*(slice.as_ptr() as *const [u8; 12]) },
                })
            }
        }

        #[doc(hidden)]
        unsafe impl<'a> FromStructField<'a> for Vec3View<'a> {
            type Input = [u8; 12];

            #[inline]
            fn from_struct_field(slice: &'a Self::Input) -> Result<Self, InvalidFlatbuffer> {
                Ok(Self { slice })
            }
        }

        impl<'a> Vec3View<'a> {
            /// Getter for the `x` field.
            ///
            ///
            /// # Panics
            ///
            /// If the value cannot be deserialized.
            #[inline]
            pub fn x(self) -> f32 {
                self.try_get_x().unwrap()
            }

            /// Getter for the `x` field.
            ///
            #[inline]
            pub fn try_get_x(self) -> Result<f32, InvalidFlatbuffer> {
                type SliceType<'a> = <f32 as FromStructField<'a>>::Input;
                const OFFSET: usize = 0;
                const SIZE: usize = core::mem::size_of::<SliceType>();
                let slice = self.slice.get(OFFSET..OFFSET+SIZE).unwrap();
                let slice: &'a SliceType<'a> = unsafe { &*(slice.as_ptr() as *const SliceType<'a>) };
                <f32 as FromStructField<'a>>::from_struct_field(slice)
            }

            /// Getter for the `y` field.
            ///
            ///
            /// # Panics
            ///
            /// If the value cannot be deserialized.
            #[inline]
            pub fn y(self) -> f32 {
                self.try_get_y().unwrap()
            }

            /// Getter for the `y` field.
            ///
            #[inline]
            pub fn try_get_y(self) -> Result<f32, InvalidFlatbuffer> {
                type SliceType<'a> = <f32 as FromStructField<'a>>::Input;
                const OFFSET: usize = 4;
                const SIZE: usize = core::mem::size_of::<SliceType>();
                let slice = self.slice.get(OFFSET..OFFSET+SIZE).unwrap();
                let slice: &'a SliceType<'a> = unsafe { &*(slice.as_ptr() as *const SliceType<'a>) };
                <f32 as FromStructField<'a>>::from_struct_field(slice)
            }

            /// Getter for the `z` field.
            ///
            ///
            /// # Panics
            ///
            /// If the value cannot be deserialized.
            #[inline]
            pub fn z(self) -> f32 {
                self.try_get_z().unwrap()
            }

            /// Getter for the `z` field.
            ///
            #[inline]
            pub fn try_get_z(self) -> Result<f32, InvalidFlatbuffer> {
                type SliceType<'a> = <f32 as FromStructField<'a>>::Input;
                const OFFSET: usize = 8;
                const SIZE: usize = core::mem::size_of::<SliceType>();
                let slice = self.slice.get(OFFSET..OFFSET+SIZE).unwrap();
                let slice: &'a SliceType<'a> = unsafe { &*(slice.as_ptr() as *const SliceType<'a>) };
                <f32 as FromStructField<'a>>::from_struct_field(slice)
            }

        }

        impl<'a> fmt::Debug for Vec3View<'a> {
            fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
                formatter
                    .debug_struct("Vec3View")
                    .field("x", &self.try_get_x())
                    .field("y", &self.try_get_y())
                    .field("z", &self.try_get_z())
                    .finish()
            }
        }

        impl<'a> PartialEq for Vec3View<'a> {
            #[inline]
            fn eq(&self, other: &Self) -> bool {
                self.slice[..] == other.slice[..]
            }
        }

        /// Builder for a flatbuffer `Vec3` object
        ///
        /// This struct is used for serializing. For deserializing see [`Vec3View`](struct.Vec3View.html).
        ///
        #[derive(Copy, Clone, Debug, PartialEq)]
        pub struct Vec3 {
            pub x: f32,
            pub y: f32,
            pub z: f32,
        }

        unsafe impl FlatbufferPrimitive for Vec3 {
            const SIZE: usize = 12;
            const ALIGNMENT: usize = 4;

            #[inline]
            unsafe fn serialize(&self, buffer: *mut u8, offset: RawOffset) {
                FlatbufferPrimitive::serialize(&self.x, buffer.add(0), offset + 0);
                FlatbufferPrimitive::serialize(&self.y, buffer.add(4), offset + 4);
                FlatbufferPrimitive::serialize(&self.z, buffer.add(8), offset + 8);
            }
        }

        /// View of a flatbuffer `Monster` object
        ///
        /// This struct is used for deserializing. For serializing see [`Monster`](struct.Monster.html).
        ///
        #[derive(Copy, Clone)]
        pub struct MonsterView<'a> {
            table: Table<'a>,
        }

        #[doc(hidden)]
        impl<'a> FromTableField<'a> for MonsterView<'a> {
            const INLINE_SIZE: usize = Table::INLINE_SIZE;

            #[inline]
            fn from_field(buf: &'a [u8], offset: usize) -> Result<Self, InvalidFlatbuffer> {
                FromTableField::from_field(buf, offset).map(|table| Self { table })
            }
        }

        impl<'a> MonsterView<'a> {
            /// Getter for the `pos` field.
            ///
            ///
            /// # Panics
            ///
            /// If the value cannot be deserialized.
            #[inline]
            pub fn pos(&self) -> Option<Vec3View<'a>> {
                self.try_get_pos().unwrap()
            }

            /// Getter for the `pos` field.
            ///
            #[inline]
            pub fn try_get_pos(&self) ->  Result<Option<Vec3View<'a>>, InvalidFlatbuffer> {
                self.table.get_field(4)
            }

            /// Getter for the `mana` field.
            ///
            ///
            /// # Panics
            ///
            /// If the value cannot be deserialized.
            #[inline]
            pub fn mana(&self) -> i16 {
                self.try_get_mana().unwrap()
            }

            /// Getter for the `mana` field.
            ///
            #[inline]
            pub fn try_get_mana(&self) -> Result<i16, InvalidFlatbuffer> {
                self.table.get_field(6).map(|value| value.unwrap_or(150))
            }

            /// Getter for the `hp` field.
            ///
            ///
            /// # Panics
            ///
            /// If the value cannot be deserialized.
            #[inline]
            pub fn hp(&self) -> i16 {
                self.try_get_hp().unwrap()
            }

            /// Getter for the `hp` field.
            ///
            #[inline]
            pub fn try_get_hp(&self) -> Result<i16, InvalidFlatbuffer> {
                self.table.get_field(8).map(|value| value.unwrap_or(100))
            }

            /// Getter for the `name` field.
            ///
            ///
            /// # Panics
            ///
            /// If the value cannot be deserialized.
            #[inline]
            pub fn name(&self) -> Option<Str<'a>> {
                self.try_get_name().unwrap()
            }

            /// Getter for the `name` field.
            ///
            #[inline]
            pub fn try_get_name(&self) ->  Result<Option<Str<'a>>, InvalidFlatbuffer> {
                self.table.get_field(10)
            }

            /// Getter for the `inventory` field.
            ///
            ///
            /// # Panics
            ///
            /// If the value cannot be deserialized.
            #[inline]
            pub fn inventory(&self) -> Option<Vector<'a, u8>> {
                self.try_get_inventory().unwrap()
            }

            /// Getter for the `inventory` field.
            ///
            #[inline]
            pub fn try_get_inventory(&self) ->  Result<Option<Vector<'a, u8>>, InvalidFlatbuffer> {
                self.table.get_field(14)
            }

            /// Getter for the `color` field.
            ///
            ///
            /// # Panics
            ///
            /// If the value cannot be deserialized.
            #[inline]
            pub fn color(&self) -> Color {
                self.try_get_color().unwrap()
            }

            /// Getter for the `color` field.
            ///
            #[inline]
            pub fn try_get_color(&self) -> Result<Color, InvalidFlatbuffer> {
                self.table.get_field(16).map(|value| value.unwrap_or(Color::Blue))
            }

            /// Getter for the `weapons` field.
            ///
            ///
            /// # Panics
            ///
            /// If the value cannot be deserialized.
            #[inline]
            pub fn weapons(&self) -> Option<Vector<'a, WeaponView<'a>>> {
                self.try_get_weapons().unwrap()
            }

            /// Getter for the `weapons` field.
            ///
            #[inline]
            pub fn try_get_weapons(&self) ->  Result<Option<Vector<'a, WeaponView<'a>>>, InvalidFlatbuffer> {
                self.table.get_field(18)
            }

            /// Getter for the `equipped` field.
            ///
            ///
            /// # Panics
            ///
            /// If the value cannot be deserialized.
            #[inline]
            pub fn equipped(&self) -> Option<EquipmentView<'a>> {
                self.try_get_equipped().unwrap()
            }

            /// Getter for the `equipped` field.
            ///
            #[inline]
            pub fn try_get_equipped(&self) ->  Result<Option<EquipmentView<'a>>, InvalidFlatbuffer> {
                self.table.get_field_union(20, 22)
            }

            /// Getter for the `path` field.
            ///
            ///
            /// # Panics
            ///
            /// If the value cannot be deserialized.
            #[inline]
            pub fn path(&self) -> Option<Vector<'a, Vec3View<'a>>> {
                self.try_get_path().unwrap()
            }

            /// Getter for the `path` field.
            ///
            #[inline]
            pub fn try_get_path(&self) ->  Result<Option<Vector<'a, Vec3View<'a>>>, InvalidFlatbuffer> {
                self.table.get_field(24)
            }

            /// Begin parsing a flatbuffer with a `Weapon` as the root object
            #[inline]
            pub fn from_buffer_as_root(buffer: &'a [u8]) -> Result<Self, InvalidFlatbuffer> {
                FromTableField::from_field(buffer, 0)
            }
        }

        #[inline]
        pub fn get_root_as_monster<'a>(buffer: &'a [u8]) -> Result<MonsterView<'a>, InvalidFlatbuffer> {
            MonsterView::from_buffer_as_root(buffer)
        }

        impl<'a> fmt::Debug for MonsterView<'a> {
            fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
                formatter.debug_struct("MonsterView")
                    .field("pos", &self.try_get_pos())
                    .field("mana", &self.try_get_mana())
                    .field("hp", &self.try_get_hp())
                    .field("name", &self.try_get_name())
                    .field("inventory", &self.try_get_inventory())
                    .field("color", &self.try_get_color())
                    .field("weapons", &self.try_get_weapons())
                    .field("equipped", &self.try_get_equipped())
                    .field("path", &self.try_get_path())
                    .finish()
            }
        }

        /// Builder for a flatbuffer `Monster` object
        ///
        /// This struct is used for serializing. For deserializing see [`MonsterView`](struct.MonsterView.html).
        ///
        #[derive(Copy, Clone, Debug, PartialEq)]
        pub struct Monster {
            pub pos: Option<Vec3>,
            pub mana: i16,
            pub hp: i16,
            pub name: Option<Offset<str>>,
            pub inventory: Option<Offset<[u8]>>,
            pub color: Color,
            pub weapons: Option<Offset<[Offset<Weapon>]>>,
            pub equipped: Option<Equipment>,
            pub path: Option<Offset<[Vec3]>>,
        }

        impl Default for Monster {
            #[inline]
            fn default() -> Monster {
                Monster {
                    pos: None,
                    mana: 150,
                    hp: 100,
                    name: None,
                    inventory: None,
                    color: Color::Blue,
                    weapons: None,
                    equipped: None,
                    path: None,
                }
            }
        }

        unsafe impl FlatbufferTable for Monster {
            #[inline]
            fn validate_required(&self) {
            }

            #[inline]
            fn serialize<F: FlatbufferWriter>(
                &self,
                flatbuffer: &mut F,
            ) -> Result<RawOffset, OutOfBufferSpace> {
                let mut vtable = [0u8; 26];

                let mut size = 0;
                let mut alignment = 4;
                let mut vtable_len = 4;

                if self.pos != None {
                    vtable_len = vtable_len.max(4 + 2);
                    const CUR_ALIGN: usize = <Vec3 as FlatbufferPrimitive>::ALIGNMENT;
                    alignment = alignment.max(CUR_ALIGN);
                    vtable[4..4+2].copy_from_slice(
                        &((size + 4) as u16).to_le_bytes());
                    size += <Vec3 as FlatbufferPrimitive>::SIZE;
                }
                if self.name != None {
                    vtable_len = vtable_len.max(10 + 2);
                    const CUR_ALIGN: usize = <Offset<str> as FlatbufferPrimitive>::ALIGNMENT;
                    alignment = alignment.max(CUR_ALIGN);
                    vtable[10..10+2].copy_from_slice(
                        &((size + 4) as u16).to_le_bytes());
                    size += <Offset<str> as FlatbufferPrimitive>::SIZE;
                }
                if self.inventory != None {
                    vtable_len = vtable_len.max(14 + 2);
                    const CUR_ALIGN: usize = <Offset<[u8]> as FlatbufferPrimitive>::ALIGNMENT;
                    alignment = alignment.max(CUR_ALIGN);
                    vtable[14..14+2].copy_from_slice(
                        &((size + 4) as u16).to_le_bytes());
                    size += <Offset<[u8]> as FlatbufferPrimitive>::SIZE;
                }
                if self.weapons != None {
                    vtable_len = vtable_len.max(18 + 2);
                    const CUR_ALIGN: usize = <Offset<[Offset<Weapon>]> as FlatbufferPrimitive>::ALIGNMENT;
                    alignment = alignment.max(CUR_ALIGN);
                    vtable[18..18+2].copy_from_slice(
                        &((size + 4) as u16).to_le_bytes());
                    size += <Offset<[Offset<Weapon>]> as FlatbufferPrimitive>::SIZE;
                }
                if self.equipped != None {
                    vtable_len = vtable_len.max(22 + 2);
                    const CUR_ALIGN: usize = <Offset<()> as FlatbufferPrimitive>::ALIGNMENT;
                    alignment = alignment.max(CUR_ALIGN);
                    vtable[22..22+2].copy_from_slice(
                        &((size + 4) as u16).to_le_bytes());
                    size += <Offset<()> as FlatbufferPrimitive>::SIZE;
                }
                if self.path != None {
                    vtable_len = vtable_len.max(24 + 2);
                    const CUR_ALIGN: usize = <Offset<[Vec3]> as FlatbufferPrimitive>::ALIGNMENT;
                    alignment = alignment.max(CUR_ALIGN);
                    vtable[24..24+2].copy_from_slice(
                        &((size + 4) as u16).to_le_bytes());
                    size += <Offset<[Vec3]> as FlatbufferPrimitive>::SIZE;
                }
                if self.mana != 150 {
                    vtable_len = vtable_len.max(6 + 2);
                    const CUR_ALIGN: usize = <i16 as FlatbufferPrimitive>::ALIGNMENT;
                    alignment = alignment.max(CUR_ALIGN);
                    vtable[6..6+2].copy_from_slice(
                        &((size + 4) as u16).to_le_bytes());
                    size += <i16 as FlatbufferPrimitive>::SIZE;
                }
                if self.hp != 100 {
                    vtable_len = vtable_len.max(8 + 2);
                    const CUR_ALIGN: usize = <i16 as FlatbufferPrimitive>::ALIGNMENT;
                    alignment = alignment.max(CUR_ALIGN);
                    vtable[8..8+2].copy_from_slice(
                        &((size + 4) as u16).to_le_bytes());
                    size += <i16 as FlatbufferPrimitive>::SIZE;
                }
                if self.color != Color::Blue {
                    vtable_len = vtable_len.max(16 + 2);
                    const CUR_ALIGN: usize = <Color as FlatbufferPrimitive>::ALIGNMENT;
                    alignment = alignment.max(CUR_ALIGN);
                    vtable[16..16+2].copy_from_slice(
                        &((size + 4) as u16).to_le_bytes());
                    size += <Color as FlatbufferPrimitive>::SIZE;
                }
                if self.equipped != None {
                    vtable_len = vtable_len.max(20 + 2);
                    const CUR_ALIGN: usize = <EquipmentTag as FlatbufferPrimitive>::ALIGNMENT;
                    alignment = alignment.max(CUR_ALIGN);
                    vtable[20..20+2].copy_from_slice(
                        &((size + 4) as u16).to_le_bytes());
                    size += <EquipmentTag as FlatbufferPrimitive>::SIZE;
                }
                flatbuffer.align_before_write(size, alignment - 1)?;
                if let Some(ref value) = self.equipped {
                    flatbuffer.write_primitive(&value.tag())?;
                }
                if self.color != Color::Blue {
                    flatbuffer.write_primitive(&self.color)?;
                }
                if self.hp != 100 {
                    flatbuffer.write_primitive(&self.hp)?;
                }
                if self.mana != 150 {
                    flatbuffer.write_primitive(&self.mana)?;
                }
                if let Some(ref value) = self.path {
                    flatbuffer.write_primitive(value)?;
                }
                if let Some(ref value) = self.equipped {
                    flatbuffer.write_primitive(&value.offset())?;
                }
                if let Some(ref value) = self.weapons {
                    flatbuffer.write_primitive(value)?;
                }
                if let Some(ref value) = self.inventory {
                    flatbuffer.write_primitive(value)?;
                }
                if let Some(ref value) = self.name {
                    flatbuffer.write_primitive(value)?;
                }
                if let Some(ref value) = self.pos {
                    flatbuffer.write_primitive(value)?;
                }
                flatbuffer.write_vtable_and_offset(&mut vtable[..vtable_len], size + 4)
            }
        }

        /// View of a flatbuffer `Weapon` object
        ///
        /// This struct is used for deserializing. For serializing see [`Weapon`](struct.Weapon.html).
        ///
        #[derive(Copy, Clone)]
        pub struct WeaponView<'a> {
            table: Table<'a>,
        }

        #[doc(hidden)]
        impl<'a> FromTableField<'a> for WeaponView<'a> {
            const INLINE_SIZE: usize = Table::INLINE_SIZE;

            #[inline]
            fn from_field(buf: &'a [u8], offset: usize) -> Result<Self, InvalidFlatbuffer> {
                FromTableField::from_field(buf, offset).map(|table| Self { table })
            }
        }

        impl<'a> WeaponView<'a> {
            /// Getter for the `name` field.
            ///
            ///
            /// # Panics
            ///
            /// If the value cannot be deserialized.
            #[inline]
            pub fn name(&self) -> Option<Str<'a>> {
                self.try_get_name().unwrap()
            }

            /// Getter for the `name` field.
            ///
            #[inline]
            pub fn try_get_name(&self) ->  Result<Option<Str<'a>>, InvalidFlatbuffer> {
                self.table.get_field(4)
            }

            /// Getter for the `damage` field.
            ///
            ///
            /// # Panics
            ///
            /// If the value cannot be deserialized.
            #[inline]
            pub fn damage(&self) -> i16 {
                self.try_get_damage().unwrap()
            }

            /// Getter for the `damage` field.
            ///
            #[inline]
            pub fn try_get_damage(&self) -> Result<i16, InvalidFlatbuffer> {
                self.table.get_field(6).map(|value| value.unwrap_or(0))
            }

            /// Begin parsing a flatbuffer with a `Weapon` as the root object
            #[inline]
            pub fn from_buffer_as_root(buffer: &'a [u8]) -> Result<Self, InvalidFlatbuffer> {
                FromTableField::from_field(buffer, 0)
            }
        }

        impl<'a> fmt::Debug for WeaponView<'a> {
            fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
                formatter.debug_struct("WeaponView")
                    .field("name", &self.try_get_name())
                    .field("damage", &self.try_get_damage())
                    .finish()
            }
        }

        /// Builder for a flatbuffer `Weapon` object
        ///
        /// This struct is used for serializing. For deserializing see [`WeaponView`](struct.WeaponView.html).
        ///
        #[derive(Copy, Clone, Debug, PartialEq)]
        pub struct Weapon {
            pub name: Option<Offset<str>>,
            pub damage: i16,
        }

        impl Default for Weapon {
            #[inline]
            fn default() -> Weapon {
                Weapon {
                    name: None,
                    damage: 0,
                }
            }
        }

        unsafe impl FlatbufferTable for Weapon {
            #[inline]
            fn validate_required(&self) {
            }

            #[inline]
            fn serialize<F: FlatbufferWriter>(
                &self,
                flatbuffer: &mut F,
            ) -> Result<RawOffset, OutOfBufferSpace> {
                let mut vtable = [0u8; 8];

                let mut size = 0;
                let mut alignment = 4;
                let mut vtable_len = 4;

                if self.name != None {
                    vtable_len = vtable_len.max(4 + 2);
                    const CUR_ALIGN: usize = <Offset<str> as FlatbufferPrimitive>::ALIGNMENT;
                    alignment = alignment.max(CUR_ALIGN);
                    vtable[4..4+2].copy_from_slice(
                        &((size + 4) as u16).to_le_bytes());
                    size += <Offset<str> as FlatbufferPrimitive>::SIZE;
                }
                if self.damage != 0 {
                    vtable_len = vtable_len.max(6 + 2);
                    const CUR_ALIGN: usize = <i16 as FlatbufferPrimitive>::ALIGNMENT;
                    alignment = alignment.max(CUR_ALIGN);
                    vtable[6..6+2].copy_from_slice(
                        &((size + 4) as u16).to_le_bytes());
                    size += <i16 as FlatbufferPrimitive>::SIZE;
                }
                flatbuffer.align_before_write(size, alignment - 1)?;
                if self.damage != 0 {
                    flatbuffer.write_primitive(&self.damage)?;
                }
                if let Some(ref value) = self.name {
                    flatbuffer.write_primitive(value)?;
                }
                flatbuffer.write_vtable_and_offset(&mut vtable[..vtable_len], size + 4)
            }
        }
    }
}
