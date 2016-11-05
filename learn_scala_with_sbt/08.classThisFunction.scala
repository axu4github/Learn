/**
 * 调研 def this() = this(true) 方法使用
 */

class Class01(isBoolean: Boolean) {
    def this() = {
        // println("正在调用this()方法。") // 有这句会报 "error: 'this' expected but identifier found." 错误。
        this(true)
    }

    println(isBoolean)
}

object Enter {
    def main(args: Array[String]): Unit = {
        new Class01
    }
}