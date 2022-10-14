enum class Direction(val dir: Int){
    RIGHT(0), UP(1), LEFT(2), DOWN(3);
}

fun getByValue(value: Int): Direction{
    return when( value ){
        1 -> Direction.UP
        2 -> Direction.LEFT
        3 -> Direction.DOWN
        0 -> Direction.UP
        else -> Direction.DOWN
    }
}


class Robot(private var x: Int, private var y: Int, private var direction: Direction) {
    fun stepForward(): String {
        when (direction) {
            Direction.RIGHT -> x++
            Direction.LEFT -> x--
            Direction.UP -> y++
            Direction.DOWN -> y--
        }
        return "Step Forward"
    }

    fun turnLeft(): String{
        direction = getByValue(direction.dir + 1 % 4)
        return "Turn Left"
    }

    fun turnRight(): String{
        direction = getByValue(direction.dir - 1)
        return "Turn Right"
    }

    fun getDirection(): Direction{
        return direction
    }

    fun getX(): Int{
        return x
    }

    fun getY(): Int{
        return y
    }

    fun inPoint(px: Int, py:Int): Boolean{
        return px == x && py == y
    }

    override fun toString(): String {
        return "($x, $y), looks $direction"
    }
}