class SmartRobot(x: Int, y: Int, direction: Direction) : Robot(x, y, direction) {

    fun smartRotate(direction:Direction){
        TODO("Тут добавить функцию нормального изменения поворота тоесть за минимальное колличчество операций")
    }

    fun moveRobot(toX: Int, toY: Int){
        var moveX: Direction = Direction.LEFT
        var moveY: Direction = Direction.DOWN
        var countSteps: Int = 0

        if(toX > x){
            moveX = Direction.RIGHT
        }else if(toX < x){
            moveX = Direction.LEFT
        }

        while (moveX != this.direction){
            this.turnLeft()
            countSteps++;
            println("step: $countSteps")
            println("type: turnLeft")
            println("current direction: ${this.direction}")
        }

        while (toX != x){
            this.stepForward()
            println("step: $countSteps")
            println("type: stepForward")
            println("current cords: $x, $y")
        }

        if(toY > y){
            moveY = Direction.DOWN
        }else if(toY < y){
            moveY = Direction.UP
        }

        while (moveY != this.direction){
            this.turnLeft()
            println("step: $countSteps")
            println("type: turnLeft")
            println("current direction: ${this.direction}")
        }

        while (toY != y){
            this.stepForward()
            println("step: $countSteps")
            println("type: turnLeft")
            println("current direction: ${this.direction}")
        }

        println("Move complete!")

    }


}