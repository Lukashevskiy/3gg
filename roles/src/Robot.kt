open class Robot(var x: Int, var y: Int, var direction: Direction) {
    fun stepForward() {
        when (direction) {
            Direction.RIGHT -> x++
            Direction.LEFT -> x--
            Direction.UP -> y++
            Direction.DOWN -> y--
        }
    }

    fun turnLeft(){
        turn(Direction.LEFT)
    }
    fun turnRight(){
        turn(Direction.RIGHT)
    }

    private fun turn(direction: Direction){
        this.direction = newDirection(this.direction, direction)
    }
    override fun toString(): String {
        return "($x, $y), looks $direction"
    }
}
