// automatically generated by the FlatBuffers compiler, do not modify

import java.nio.*
import kotlin.math.sign
import com.google.flatbuffers.*

@Suppress("unused")
class TableA : Table() {

    fun __init(_i: Int, _bb: ByteBuffer)  {
        __reset(_i, _bb)
    }
    fun __assign(_i: Int, _bb: ByteBuffer) : TableA {
        __init(_i, _bb)
        return this
    }
    val b : MyGame.OtherNameSpace.TableB? get() = b(MyGame.OtherNameSpace.TableB())
    fun b(obj: MyGame.OtherNameSpace.TableB) : MyGame.OtherNameSpace.TableB? {
        val o = __offset(4)
        return if (o != 0) {
            obj.__assign(__indirect(o + bb_pos), bb)
        } else {
            null
        }
    }
    companion object {
        fun validateVersion() = Constants.FLATBUFFERS_22_10_26()
        fun getRootAsTableA(_bb: ByteBuffer): TableA = getRootAsTableA(_bb, TableA())
        fun getRootAsTableA(_bb: ByteBuffer, obj: TableA): TableA {
            _bb.order(ByteOrder.LITTLE_ENDIAN)
            return (obj.__assign(_bb.getInt(_bb.position()) + _bb.position(), _bb))
        }
        fun createTableA(builder: FlatBufferBuilder, bOffset: Int) : Int {
            builder.startTable(1)
            addB(builder, bOffset)
            return endTableA(builder)
        }
        fun startTableA(builder: FlatBufferBuilder) = builder.startTable(1)
        fun addB(builder: FlatBufferBuilder, b: Int) = builder.addOffset(0, b, 0)
        fun endTableA(builder: FlatBufferBuilder) : Int {
            val o = builder.endTable()
            return o
        }
    }
}
