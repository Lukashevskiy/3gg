

fun printEvent(r: Robot, event:String){
    println("$event - current state of robot: $r")
}

fun smartRotation(r: Robot, to: Direction): Robot{
    while (r.getDirection() != to){
        //println("$to, ${r.getDirection()}")
        val rr = r.turnLeft()
        printEvent(r, rr)
    }
    return r
}


fun move(r: Robot, toX: Int, toY: Int): Robot{
    var movingRobot = r
    var currentDirection: Direction

    while (!movingRobot.inPoint(toX, toY)) {
        currentDirection = if(movingRobot.getX() != toX){
            if( movingRobot.getX() > toX ){
                Direction.LEFT
            }else{
                Direction.RIGHT
            }
        }else{
            if( movingRobot.getY() > toY ){
                Direction.DOWN
            }else{
                Direction.UP
            }
        }
        movingRobot = smartRotation(r, currentDirection)
        printEvent(r, movingRobot.stepForward())
    }

    return movingRobot
}


fun main() {
    val r = Robot(0, 0, Direction.DOWN)
    move(r, 10, 10)
    //print("event: ${r.turnLeft()} \n\t Robot state: $r")
}