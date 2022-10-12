
fun main() {
    val a: Int = readLine()!!.toInt()
    val arr = readLine()!!.split(' ').map{ it.toFloat() }.toFloatArray()
    val smoothedArray = FloatArray(a)
    if(a < 2) {
        println("Is it impossible to accumulate this function")
        return
    }
    smoothedArray[0] = arr[0]
    for (i in 1 until a-1){
        smoothedArray[i] = (arr[i-1] + arr[i] + arr[i+1]) / 3
    }
    smoothedArray[a-1] = arr[a-1]

    println(smoothedArray.contentToString())
}