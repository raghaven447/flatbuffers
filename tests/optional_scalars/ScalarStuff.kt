// automatically generated by the FlatBuffers compiler, do not modify

package optional_scalars

import com.google.flatbuffers.BaseVector
import com.google.flatbuffers.BooleanVector
import com.google.flatbuffers.ByteVector
import com.google.flatbuffers.Constants
import com.google.flatbuffers.DoubleVector
import com.google.flatbuffers.FlatBufferBuilder
import com.google.flatbuffers.FloatVector
import com.google.flatbuffers.LongVector
import com.google.flatbuffers.StringVector
import com.google.flatbuffers.Struct
import com.google.flatbuffers.Table
import com.google.flatbuffers.UnionVector
import java.nio.ByteBuffer
import java.nio.ByteOrder
import kotlin.math.sign

@Suppress("unused")
class ScalarStuff : Table() {

    fun __init(_i: Int, _bb: ByteBuffer)  {
        __reset(_i, _bb)
    }
    fun __assign(_i: Int, _bb: ByteBuffer) : ScalarStuff {
        __init(_i, _bb)
        return this
    }
    val justI8 : Byte
        get() {
            val o = __offset(4)
            return if(o != 0) bb.get(o + bb_pos) else 0
        }
    val maybeI8 : Byte?
        get() {
            val o = __offset(6)
            return if(o != 0) bb.get(o + bb_pos) else null
        }
    val defaultI8 : Byte
        get() {
            val o = __offset(8)
            return if(o != 0) bb.get(o + bb_pos) else 42
        }
    val justU8 : UByte
        get() {
            val o = __offset(10)
            return if(o != 0) bb.get(o + bb_pos).toUByte() else 0u
        }
    val maybeU8 : UByte?
        get() {
            val o = __offset(12)
            return if(o != 0) bb.get(o + bb_pos).toUByte() else null
        }
    val defaultU8 : UByte
        get() {
            val o = __offset(14)
            return if(o != 0) bb.get(o + bb_pos).toUByte() else 42u
        }
    val justI16 : Short
        get() {
            val o = __offset(16)
            return if(o != 0) bb.getShort(o + bb_pos) else 0
        }
    val maybeI16 : Short?
        get() {
            val o = __offset(18)
            return if(o != 0) bb.getShort(o + bb_pos) else null
        }
    val defaultI16 : Short
        get() {
            val o = __offset(20)
            return if(o != 0) bb.getShort(o + bb_pos) else 42
        }
    val justU16 : UShort
        get() {
            val o = __offset(22)
            return if(o != 0) bb.getShort(o + bb_pos).toUShort() else 0u
        }
    val maybeU16 : UShort?
        get() {
            val o = __offset(24)
            return if(o != 0) bb.getShort(o + bb_pos).toUShort() else null
        }
    val defaultU16 : UShort
        get() {
            val o = __offset(26)
            return if(o != 0) bb.getShort(o + bb_pos).toUShort() else 42u
        }
    val justI32 : Int
        get() {
            val o = __offset(28)
            return if(o != 0) bb.getInt(o + bb_pos) else 0
        }
    val maybeI32 : Int?
        get() {
            val o = __offset(30)
            return if(o != 0) bb.getInt(o + bb_pos) else null
        }
    val defaultI32 : Int
        get() {
            val o = __offset(32)
            return if(o != 0) bb.getInt(o + bb_pos) else 42
        }
    val justU32 : UInt
        get() {
            val o = __offset(34)
            return if(o != 0) bb.getInt(o + bb_pos).toUInt() else 0u
        }
    val maybeU32 : UInt?
        get() {
            val o = __offset(36)
            return if(o != 0) bb.getInt(o + bb_pos).toUInt() else null
        }
    val defaultU32 : UInt
        get() {
            val o = __offset(38)
            return if(o != 0) bb.getInt(o + bb_pos).toUInt() else 42u
        }
    val justI64 : Long
        get() {
            val o = __offset(40)
            return if(o != 0) bb.getLong(o + bb_pos) else 0L
        }
    val maybeI64 : Long?
        get() {
            val o = __offset(42)
            return if(o != 0) bb.getLong(o + bb_pos) else null
        }
    val defaultI64 : Long
        get() {
            val o = __offset(44)
            return if(o != 0) bb.getLong(o + bb_pos) else 42L
        }
    val justU64 : ULong
        get() {
            val o = __offset(46)
            return if(o != 0) bb.getLong(o + bb_pos).toULong() else 0UL
        }
    val maybeU64 : ULong?
        get() {
            val o = __offset(48)
            return if(o != 0) bb.getLong(o + bb_pos).toULong() else null
        }
    val defaultU64 : ULong
        get() {
            val o = __offset(50)
            return if(o != 0) bb.getLong(o + bb_pos).toULong() else 42UL
        }
    val justF32 : Float
        get() {
            val o = __offset(52)
            return if(o != 0) bb.getFloat(o + bb_pos) else 0.0f
        }
    val maybeF32 : Float?
        get() {
            val o = __offset(54)
            return if(o != 0) bb.getFloat(o + bb_pos) else null
        }
    val defaultF32 : Float
        get() {
            val o = __offset(56)
            return if(o != 0) bb.getFloat(o + bb_pos) else 42.0f
        }
    val justF64 : Double
        get() {
            val o = __offset(58)
            return if(o != 0) bb.getDouble(o + bb_pos) else 0.0
        }
    val maybeF64 : Double?
        get() {
            val o = __offset(60)
            return if(o != 0) bb.getDouble(o + bb_pos) else null
        }
    val defaultF64 : Double
        get() {
            val o = __offset(62)
            return if(o != 0) bb.getDouble(o + bb_pos) else 42.0
        }
    val justBool : Boolean
        get() {
            val o = __offset(64)
            return if(o != 0) 0.toByte() != bb.get(o + bb_pos) else false
        }
    val maybeBool : Boolean?
        get() {
            val o = __offset(66)
            return if(o != 0) 0.toByte() != bb.get(o + bb_pos) else null
        }
    val defaultBool : Boolean
        get() {
            val o = __offset(68)
            return if(o != 0) 0.toByte() != bb.get(o + bb_pos) else true
        }
    val justEnum : Byte
        get() {
            val o = __offset(70)
            return if(o != 0) bb.get(o + bb_pos) else 0
        }
    val maybeEnum : Byte?
        get() {
            val o = __offset(72)
            return if(o != 0) bb.get(o + bb_pos) else null
        }
    val defaultEnum : Byte
        get() {
            val o = __offset(74)
            return if(o != 0) bb.get(o + bb_pos) else 1
        }
    companion object {
        fun validateVersion() = Constants.FLATBUFFERS_25_2_10()
        fun getRootAsScalarStuff(_bb: ByteBuffer): ScalarStuff = getRootAsScalarStuff(_bb, ScalarStuff())
        fun getRootAsScalarStuff(_bb: ByteBuffer, obj: ScalarStuff): ScalarStuff {
            _bb.order(ByteOrder.LITTLE_ENDIAN)
            return (obj.__assign(_bb.getInt(_bb.position()) + _bb.position(), _bb))
        }
        fun ScalarStuffBufferHasIdentifier(_bb: ByteBuffer) : Boolean = __has_identifier(_bb, "NULL")
        fun createScalarStuff(builder: FlatBufferBuilder, justI8: Byte, maybeI8: Byte?, defaultI8: Byte, justU8: UByte, maybeU8: UByte?, defaultU8: UByte, justI16: Short, maybeI16: Short?, defaultI16: Short, justU16: UShort, maybeU16: UShort?, defaultU16: UShort, justI32: Int, maybeI32: Int?, defaultI32: Int, justU32: UInt, maybeU32: UInt?, defaultU32: UInt, justI64: Long, maybeI64: Long?, defaultI64: Long, justU64: ULong, maybeU64: ULong?, defaultU64: ULong, justF32: Float, maybeF32: Float?, defaultF32: Float, justF64: Double, maybeF64: Double?, defaultF64: Double, justBool: Boolean, maybeBool: Boolean?, defaultBool: Boolean, justEnum: Byte, maybeEnum: Byte?, defaultEnum: Byte) : Int {
            builder.startTable(36)
            addDefaultF64(builder, defaultF64)
            maybeF64?.run { addMaybeF64(builder, maybeF64) }
            addJustF64(builder, justF64)
            addDefaultU64(builder, defaultU64)
            maybeU64?.run { addMaybeU64(builder, maybeU64) }
            addJustU64(builder, justU64)
            addDefaultI64(builder, defaultI64)
            maybeI64?.run { addMaybeI64(builder, maybeI64) }
            addJustI64(builder, justI64)
            addDefaultF32(builder, defaultF32)
            maybeF32?.run { addMaybeF32(builder, maybeF32) }
            addJustF32(builder, justF32)
            addDefaultU32(builder, defaultU32)
            maybeU32?.run { addMaybeU32(builder, maybeU32) }
            addJustU32(builder, justU32)
            addDefaultI32(builder, defaultI32)
            maybeI32?.run { addMaybeI32(builder, maybeI32) }
            addJustI32(builder, justI32)
            addDefaultU16(builder, defaultU16)
            maybeU16?.run { addMaybeU16(builder, maybeU16) }
            addJustU16(builder, justU16)
            addDefaultI16(builder, defaultI16)
            maybeI16?.run { addMaybeI16(builder, maybeI16) }
            addJustI16(builder, justI16)
            addDefaultEnum(builder, defaultEnum)
            maybeEnum?.run { addMaybeEnum(builder, maybeEnum) }
            addJustEnum(builder, justEnum)
            addDefaultBool(builder, defaultBool)
            maybeBool?.run { addMaybeBool(builder, maybeBool) }
            addJustBool(builder, justBool)
            addDefaultU8(builder, defaultU8)
            maybeU8?.run { addMaybeU8(builder, maybeU8) }
            addJustU8(builder, justU8)
            addDefaultI8(builder, defaultI8)
            maybeI8?.run { addMaybeI8(builder, maybeI8) }
            addJustI8(builder, justI8)
            return endScalarStuff(builder)
        }
        fun startScalarStuff(builder: FlatBufferBuilder) = builder.startTable(36)
        fun addJustI8(builder: FlatBufferBuilder, justI8: Byte) = builder.addByte(0, justI8, 0)
        fun addMaybeI8(builder: FlatBufferBuilder, maybeI8: Byte) = builder.addByte(1, maybeI8, 0)
        fun addDefaultI8(builder: FlatBufferBuilder, defaultI8: Byte) = builder.addByte(2, defaultI8, 42)
        fun addJustU8(builder: FlatBufferBuilder, justU8: UByte) = builder.addByte(3, justU8.toByte(), 0)
        fun addMaybeU8(builder: FlatBufferBuilder, maybeU8: UByte) = builder.addByte(4, maybeU8.toByte(), 0)
        fun addDefaultU8(builder: FlatBufferBuilder, defaultU8: UByte) = builder.addByte(5, defaultU8.toByte(), 42)
        fun addJustI16(builder: FlatBufferBuilder, justI16: Short) = builder.addShort(6, justI16, 0)
        fun addMaybeI16(builder: FlatBufferBuilder, maybeI16: Short) = builder.addShort(7, maybeI16, 0)
        fun addDefaultI16(builder: FlatBufferBuilder, defaultI16: Short) = builder.addShort(8, defaultI16, 42)
        fun addJustU16(builder: FlatBufferBuilder, justU16: UShort) = builder.addShort(9, justU16.toShort(), 0)
        fun addMaybeU16(builder: FlatBufferBuilder, maybeU16: UShort) = builder.addShort(10, maybeU16.toShort(), 0)
        fun addDefaultU16(builder: FlatBufferBuilder, defaultU16: UShort) = builder.addShort(11, defaultU16.toShort(), 42)
        fun addJustI32(builder: FlatBufferBuilder, justI32: Int) = builder.addInt(12, justI32, 0)
        fun addMaybeI32(builder: FlatBufferBuilder, maybeI32: Int) = builder.addInt(13, maybeI32, 0)
        fun addDefaultI32(builder: FlatBufferBuilder, defaultI32: Int) = builder.addInt(14, defaultI32, 42)
        fun addJustU32(builder: FlatBufferBuilder, justU32: UInt) = builder.addInt(15, justU32.toInt(), 0)
        fun addMaybeU32(builder: FlatBufferBuilder, maybeU32: UInt) = builder.addInt(16, maybeU32.toInt(), 0)
        fun addDefaultU32(builder: FlatBufferBuilder, defaultU32: UInt) = builder.addInt(17, defaultU32.toInt(), 42)
        fun addJustI64(builder: FlatBufferBuilder, justI64: Long) = builder.addLong(18, justI64, 0L)
        fun addMaybeI64(builder: FlatBufferBuilder, maybeI64: Long) = builder.addLong(19, maybeI64, 0)
        fun addDefaultI64(builder: FlatBufferBuilder, defaultI64: Long) = builder.addLong(20, defaultI64, 42L)
        fun addJustU64(builder: FlatBufferBuilder, justU64: ULong) = builder.addLong(21, justU64.toLong(), 0)
        fun addMaybeU64(builder: FlatBufferBuilder, maybeU64: ULong) = builder.addLong(22, maybeU64.toLong(), 0)
        fun addDefaultU64(builder: FlatBufferBuilder, defaultU64: ULong) = builder.addLong(23, defaultU64.toLong(), 42)
        fun addJustF32(builder: FlatBufferBuilder, justF32: Float) = builder.addFloat(24, justF32, 0.0)
        fun addMaybeF32(builder: FlatBufferBuilder, maybeF32: Float) = builder.addFloat(25, maybeF32, 0.0)
        fun addDefaultF32(builder: FlatBufferBuilder, defaultF32: Float) = builder.addFloat(26, defaultF32, 42.0)
        fun addJustF64(builder: FlatBufferBuilder, justF64: Double) = builder.addDouble(27, justF64, 0.0)
        fun addMaybeF64(builder: FlatBufferBuilder, maybeF64: Double) = builder.addDouble(28, maybeF64, 0.0)
        fun addDefaultF64(builder: FlatBufferBuilder, defaultF64: Double) = builder.addDouble(29, defaultF64, 42.0)
        fun addJustBool(builder: FlatBufferBuilder, justBool: Boolean) = builder.addBoolean(30, justBool, false)
        fun addMaybeBool(builder: FlatBufferBuilder, maybeBool: Boolean) = builder.addBoolean(31, maybeBool, false)
        fun addDefaultBool(builder: FlatBufferBuilder, defaultBool: Boolean) = builder.addBoolean(32, defaultBool, true)
        fun addJustEnum(builder: FlatBufferBuilder, justEnum: Byte) = builder.addByte(33, justEnum, 0)
        fun addMaybeEnum(builder: FlatBufferBuilder, maybeEnum: Byte) = builder.addByte(34, maybeEnum, 0)
        fun addDefaultEnum(builder: FlatBufferBuilder, defaultEnum: Byte) = builder.addByte(35, defaultEnum, 1)
        fun endScalarStuff(builder: FlatBufferBuilder) : Int {
            val o = builder.endTable()
            return o
        }
        fun finishScalarStuffBuffer(builder: FlatBufferBuilder, offset: Int) = builder.finish(offset, "NULL")
        fun finishSizePrefixedScalarStuffBuffer(builder: FlatBufferBuilder, offset: Int) = builder.finishSizePrefixed(offset, "NULL")
    }
}
