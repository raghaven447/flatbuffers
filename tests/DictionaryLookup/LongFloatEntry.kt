// automatically generated by the FlatBuffers compiler, do not modify

package DictionaryLookup

import java.nio.*
import kotlin.math.sign
import com.google.flatbuffers.*

@Suppress("unused")
class LongFloatEntry : Table() {

    fun __init(_i: Int, _bb: ByteBuffer)  {
        __reset(_i, _bb)
    }
    fun __assign(_i: Int, _bb: ByteBuffer) : LongFloatEntry {
        __init(_i, _bb)
        return this
    }
    val key : Long
        get() {
            val o = __offset(4)
            return if(o != 0) bb.getLong(o + bb_pos) else 0L
        }
    val value : Float
        get() {
            val o = __offset(6)
            return if(o != 0) bb.getFloat(o + bb_pos) else 0.0f
        }
    override fun keysCompare(o1: Int, o2: Int, _bb: ByteBuffer) : Int {
        val val_1 = _bb.getLong(__offset(4, o1, _bb))
        val val_2 = _bb.getLong(__offset(4, o2, _bb))
        return (val_1 - val_2).sign
    }
    companion object {
        fun validateVersion() = Constants.FLATBUFFERS_22_11_22()
        fun getRootAsLongFloatEntry(_bb: ByteBuffer): LongFloatEntry = getRootAsLongFloatEntry(_bb, LongFloatEntry())
        fun getRootAsLongFloatEntry(_bb: ByteBuffer, obj: LongFloatEntry): LongFloatEntry {
            _bb.order(ByteOrder.LITTLE_ENDIAN)
            return (obj.__assign(_bb.getInt(_bb.position()) + _bb.position(), _bb))
        }
        fun createLongFloatEntry(builder: FlatBufferBuilder, key: Long, value: Float) : Int {
            builder.startTable(2)
            addKey(builder, key)
            addValue(builder, value)
            return endLongFloatEntry(builder)
        }
        fun startLongFloatEntry(builder: FlatBufferBuilder) = builder.startTable(2)
        fun addKey(builder: FlatBufferBuilder, key: Long)  {
            builder.addLong(key)
            builder.slot(0)
        }
        fun addValue(builder: FlatBufferBuilder, value: Float) = builder.addFloat(1, value, 0.0)
        fun endLongFloatEntry(builder: FlatBufferBuilder) : Int {
            val o = builder.endTable()
            return o
        }
        fun __lookup_by_key(obj: LongFloatEntry?, vectorLocation: Int, key: Long, bb: ByteBuffer) : LongFloatEntry? {
            var span = bb.getInt(vectorLocation - 4)
            var start = 0
            while (span != 0) {
                var middle = span / 2
                val tableOffset = __indirect(vectorLocation + 4 * (start + middle), bb)
                val value = bb.getLong(__offset(4, bb.capacity() - tableOffset, bb))
                val comp = value.compareTo(key)
                when {
                    comp > 0 -> span = middle
                    comp < 0 -> {
                        middle++
                        start += middle
                        span -= middle
                    }
                    else -> {
                        return (obj ?: LongFloatEntry()).__assign(tableOffset, bb)
                    }
                }
            }
            return null
        }
    }
}
