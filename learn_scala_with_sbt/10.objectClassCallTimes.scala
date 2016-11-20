/**
 * 研究调用半生类中声明变量次数
 */

class Class01 {
    def func01 = {
        // 会初始化半生类其他变量，但是只初始化其他变量一遍
        for (i <- 1 to 10) {
            println(i + "(times) call: " + Class01.val01)
        }
    }
}

object Class01 {
    println("初始化半生类Class01")

    val val00 = {
        println("初始化val00")
        "val00"
    }

    val val01 = "val01"
    val val02 = {
        println("初始化val02")
        "val02"
    }
}

object Enter {
    def main(args: Array[String]): Unit = {
        val c01 = new Class01
        c01.func01
    }
}