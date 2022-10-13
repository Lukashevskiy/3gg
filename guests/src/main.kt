import java.util.*

fun isValidNeighbours(y: Int, x: Int, yn:Int, xn: Int) : Boolean{
    return y in 0 until yn && x in 0 until xn
}

fun getNeighbours(y: Int, x: Int) : List<Pair<Int,Int>>{
    return listOf(Pair(y+1, x), Pair(y, x+1))
}

fun getSeatMatrix(n : Int, m : Int) : Array<IntArray> {
    val ans = Array(n){ IntArray(m) { 0 } }
    val queue: Queue<Pair<Int, Int>> = LinkedList()
    queue.add(Pair(0, 0))

    for (i in n*m downTo 1){
        val (y, x) = queue.poll()
        ans[y][x] = i
        val ns = getNeighbours(y, x)

        for (el in ns){
            if(isValidNeighbours(el.first, el.second, n, m) && el !in queue) {
                queue.add(el)
            }
        }

    }
    return ans
}

fun printMatrix(matrix: Array<IntArray>){
    for( line in matrix ){
        for( el in line ){
            print("$el ")
        }
        println()
    }
}
fun main() {
    println("insert t (number of tests): ")
    val t: Int = readLine()!!.toInt()
    for (i in 0 until t){
        println("insert n,m (test: #${i+1}):")
        val (n, m) = readLine()!!.split(' ').map{ it.toInt() }
        printMatrix(getSeatMatrix(n, m))
    }
}
