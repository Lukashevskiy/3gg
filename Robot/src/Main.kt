

fun smartRotation(r: Robot, to: Direction){
    while (r.getDirection() != to){
        r.turnLeft()
    }
}


fun move(r: Robot, toX: Int, toY: Int){
    val currentDirection: Direction
    while (!r.inPoint(toX, toY)) {
        when (r.getX()) {

        }
    }
}


fun main() {
    val r = Robot(0, 0, Direction.DOWN)

}