import java.io.File
import java.util.*
import java.util.regex.Pattern
import kotlin.collections.ArrayList
import kotlin.collections.HashMap


fun main(){
    val file = File("/home/dmitriy/Downloads/roles.txt")
    val text = file.readText()
    //var roles = ArrayList<String>()

    val play = mutableMapOf<String, String>()
    val a = Pattern.compile("\\w+\\w:").split(text).toList()
    //print(a[1])
    a[1].trim().split("\n").forEach{ role ->
        println(role)
        println("${role.toString()} -> 0")

        play[role] = ""
    }
    //println(play.keys)
////    play.forEach{ (key, value) ->
////        println("$key ---> $value")
////    }
//    var previewsName = ""
//    println(Pattern.compile("\\w+\\w:").split(text)[2])
//    val textLines = Pattern.compile("\\w+\\w:").split(text)[2].split('\n').forEachIndexed{
//            index, textLine ->
//            textLine.split(':').forEach { print(it) }
//            val t = textLine.split(':')
//            //println(t)
//            var currentString = ""
//            if(t.size == 2){
//                if(play.containsKey(t[0])){
//                    previewsName = t[0]
//                    currentString = t[1]
//                }else{
//                    currentString = textLine
//                }
//            }else{
//                currentString = textLine
//            }
//
//
//            play[previewsName] += "$index) $currentString \n"
//    }
//
//    //println(play)
}
