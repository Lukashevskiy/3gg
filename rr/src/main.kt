import java.io.File
import java.util.*

fun main() {
    val filename = "/home/dmitriy/Downloads/roles.txt"
    var l = 0
    val roles = mutableListOf<String>()
    val dependencies = mutableMapOf<String, String>()
    var i = 1
    File(filename).forEachLine { line ->
        when(l){
            0 -> roles + line
            1 ->{
                val sep = line.indexOf(':')
                val name = line.substring(0, sep)
                if(name !in dependencies)
                    dependencies[name] = ""
                dependencies[name] += "\t$i) ${line.substring(sep + 2)}\n"
                i++
            }
        }
        if (line == "textLines:") l = 1
    }
    for( k in dependencies){
        println(k.key)
        println(k.value)
    }

}
