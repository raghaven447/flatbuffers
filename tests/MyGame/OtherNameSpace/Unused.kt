// automatically generated by the FlatBuffers compiler, do not modify

package MyGame.OtherNameSpace

import java.nio.*
import kotlin.math.sign
import com.google.flatbuffers.*

@Suppress("unused")
class Unused : Struct() {

    fun __init(_i: Int, _bb: ByteBuffer)  {
        __reset(_i, _bb)
    }
    fun __assign(_i: Int, _bb: ByteBuffer) : Unused {
        __init(_i, _bb)
        return this
    }
    val a : Int get() = bb.getInt(bb_pos + 0)
    fun mutateA(a: Int) : ByteBuffer = bb.putInt(bb_pos + 0, a)
    companion object {
        fun createUnused(builder: FlatBufferBuilder, a: Int) : Int {
            builder.prep(4, 4)
            builder.putInt(a)
            return builder.offset()
        }
    }
}
