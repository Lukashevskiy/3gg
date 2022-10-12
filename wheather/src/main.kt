
fun main() {
    println("input size of array: ")
    val a: Int = readLine()!!.toInt()
    println("input array element with separator: ' ' ")
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
    println("Smoothed array:")
    println(smoothedArray.contentToString())
}