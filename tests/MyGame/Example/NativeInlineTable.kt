// automatically generated by the FlatBuffers compiler, do not modify

package MyGame.Example

import java.nio.*
import kotlin.math.sign
import com.google.flatbuffers.*

@Suppress("unused")
class NativeInlineTable : Table() {

    fun __init(_i: Int, _bb: ByteBuffer)  {
        __reset(_i, _bb)
    }
    fun __assign(_i: Int, _bb: ByteBuffer) : NativeInlineTable {
        __init(_i, _bb)
        return this
    }
    val a : Int
        get() {
            val o = __offset(4)
            return if(o != 0) bb.getInt(o + bb_pos) else 0
        }
    fun mutateA(a: Int) : Boolean {
        val o = __offset(4)
        return if (o != 0) {
            bb.putInt(o + bb_pos, a)
            true
        } else {
            false
        }
    }
    companion object {
        fun validateVersion() = Constants.FLATBUFFERS_2_0_0()
        fun getRootAsNativeInlineTable(_bb: ByteBuffer): NativeInlineTable = getRootAsNativeInlineTable(_bb, NativeInlineTable())
        fun getRootAsNativeInlineTable(_bb: ByteBuffer, obj: NativeInlineTable): NativeInlineTable {
            _bb.order(ByteOrder.LITTLE_ENDIAN)
            return (obj.__assign(_bb.getInt(_bb.position()) + _bb.position(), _bb))
        }
        fun createNativeInlineTable(builder: FlatBufferBuilder, a: Int) : Int {
            builder.startTable(1)
            addA(builder, a)
            return endNativeInlineTable(builder)
        }
        fun startNativeInlineTable(builder: FlatBufferBuilder) = builder.startTable(1)
        fun addA(builder: FlatBufferBuilder, a: Int) = builder.addInt(0, a, 0)
        fun endNativeInlineTable(builder: FlatBufferBuilder) : Int {
            val o = builder.endTable()
            return o
        }
    }
}
