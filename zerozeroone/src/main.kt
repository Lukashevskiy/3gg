import java.util.*

enum class Border(val ch: Char){
    TOP_LEFT('\u2554'),
    TOP('\u2500'),
    TOP_RIGHT('\u2557'),
    LEFT('\u2502'),
    RIGHT('\u2502'),
    DOWN_LEFT('\u255a'),
    DOWN('\u2500'),
    DOWN_RIGHT('\u255d'),
    CROSS('\u253c'),
    CROSS_BOLD('\u254b'),
    RIGHT_BOLD('\u2503'),
    DOWN_BOLD('\u2501'),
    EMPTY(' ');

    override fun toString(): String {
        return "$ch"
    }
}

enum class Elements(val ch: Char){
    O('O'),
    X('X'),
    EMPTY(' ');
}

fun printAllField(b:Array<CharArray>, n:Int){
    for (i in 1 until n * n + 1){

        for( j in 1 until n * n + 1){
            print(b[i-1][j-1])
            if(j < n * n) {
                if (j % n == 0) {
                    print(Border.EMPTY)
                    print(Border.RIGHT_BOLD)
                    print(Border.EMPTY)
                } else {
                    print(Border.RIGHT)
                }
            }
        }
        print('\n')

        if( i % n == 0 && i < n*n - 1){
            for( j in 1 until n * n + 1){
                print(Border.DOWN_BOLD)
                if(j < n * n){
                    if (j % n == 0) {
                        print(Border.DOWN_BOLD)
                        print(Border.CROSS_BOLD)
                    }
                    print(Border.DOWN_BOLD)
                }
            }
        }else{
            for( j in 1 until n * n +1){
                if(i < n * n){
                    print(Border.DOWN)
                    if(j < n * n) {
                        if (j % n == 0) {
                            print(Border.EMPTY)
                            print(Border.RIGHT_BOLD)
                            print(Border.EMPTY)
                        } else {
                            print(Border.CROSS)
                        }
                    }
                }else{
                    print(Border.EMPTY)
                    print(Border.EMPTY)
                }
            }
        }
        print('\n')
    }
}
fun printSmallField(b: Array<CharArray>, n:Int, x:Int, y:Int){
    for (i in 0 until n){
        for (j in 0 until n){
            val cx = x * n + j
            val cy = y * n + i
            print(b[cy][cx])
            if( j < n - 1){
                print(Border.RIGHT)
            }
        }
        print('\n')
        if( i < n - 1){
            print(Border.DOWN)
            for (j in 0 until n){
                if( j < n - 1){
                    print(Border.CROSS)
                    print(Border.DOWN)
                }

            }
        }
        print('\n')
    }
}

fun checkField(b: Array<CharArray>, n: Int, x: Int, y: Int) : Int {
    var win1 = 0
    var win2 = 0


    return -1
}

fun checkLine(slice:CharArray): Int {
    var countX = 0
    var countY = 0
    for(el in slice){
        when (el){
            Elements.X.ch -> countX++;
            Elements.O.ch -> countY++;
        }
    }

    return if(countX == slice.size){
        1
    }else if(countY == slice.size){
        0
    }else{
        -1
    }

}

fun checkSubfield(b: Array<CharArray>, y:Int, x: Int, yn:Int, xn:Int): Int{
    val cx = x * xn
    val cy = y * yn
    for (i in cx until cx+xn){
        val check = checkLine(b[i].slice(cy until cy+yn).toCharArray())
        if(check != -1){
            return check
        }
    }
    for (i in cx until cx+xn){
        val check = checkLine(b.slice(cy until cy+yn).toTypedArray()[cx])
        if(check != -1){
            return check
        }
    }

}


fun main() {
    val n = 3
    val b = Array(n * n ){ CharArray(n * n ){ Elements.EMPTY.ch } }
    printAllField(b, n)
    var next = false
    var isEnd = -1
    val player1 = Elements.X
    val queue1: Queue<Pair<Int, Int>> = LinkedList()

    val player2 = Elements.O
    val queue2: Queue<Pair<Int, Int>> = LinkedList()

    while (isEnd == -1){
        if(next){
            println("now Move X")
            if(queue1.isEmpty()){
                printAllField(b, n)
                println("insert x, y of subfield for enemy")
                val (y, x) = readLine()!!.split(' ').map{ it.toInt() }
                queue2.add(Pair(x-1,y-1))
                next = !next
            }else{
                val (cx, cy) = queue1.poll()
                printSmallField(b, n, cx, cy)
                println("insert x, y of subfield to insert your symbol")
                val (y, x) = readLine()!!.split(' ').map{ it.toInt() }
                val currentCx = cx * n + x - 1
                val currentCy = cy * n + y - 1
                b[currentCy][currentCx] = player1.ch
                isEnd = checkSubfield(b, cy, cx, n, n)
            }
        }else{
            println("now Move O")
            if(queue2.isEmpty()){
                printAllField(b, n)
                println("insert x, y of subfield for enemy")
                val (y, x) = readLine()!!.split(' ').map{ it.toInt() }
                queue1.add(Pair(x-1,y-1))
                next = !next
            }else{
                val (cx, cy) = queue2.poll()
                printSmallField(b, n, cx, cy)
                println("insert x, y of subfield to insert your symbol")
                val (y, x) = readLine()!!.split(' ').map{ it.toInt() }
                val currentCx = cx * n + x - 1
                val currentCy = cy * n + y - 1
                b[currentCy][currentCx] = player2.ch
                isEnd = checkSubfield(b, cy, cx, n, n)
            }
        }

    }
}
