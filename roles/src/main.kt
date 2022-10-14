
import kotlin.math.max
import kotlin.math.min

enum class Direction(val d: Int) {
    UP(1), RIGHT(2), DOWN(3), LEFT(4)
}

fun getDirection(d: Int): Direction{
    return when (d) {
        1 -> return Direction.UP
        2 -> return Direction.RIGHT
        3 -> return Direction.LEFT
        4 -> return Direction.DOWN

        else -> Direction.UP
    }
}

fun newDirection(old: Direction, new: Direction): Direction{
    val sum = old.d + new.d
    return when(new){
        Direction.LEFT -> getDirection(4 - sum - 1)
        Direction.RIGHT -> getDirection(sum - 1)
        else -> old
    }
}
fun process(n:Int,m:Int){
    val mN = max(n,m)
    val mM = min(n,m)
    
}

fun main() {
//    File("").forEachLine{ line ->
//        val regex = "(\\d+)\\s+(\\d+)\\s+(\\d+)".toRegex()
//        val match = regex.find(line)
//        if (match != null){
//            val (nS, mS, kS) = match.destructured
//        }
//    }
    val arr = arrayListOf<Direction>(Direction.UP, Direction.RIGHT, Direction.LEFT, Direction.DOWN)
    for (ar1 in arr){
        for(ar2 in arr) {
            println("$ar1 $ar2, ${newDirection(ar1,ar2)}")
        }
    }
//    val smartRobot: SmartRobot = SmartRobot(0,0, Direction.DOWN)
//    smartRobot.moveRobot(-10, 10)
}