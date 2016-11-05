/**
 * 探索实例化一个新类时，何时调用半生类的问题。
 * 
 */

class Class01 {
    // 只引入是不会调用半生类的
    import Class01._

    println("实例化了一个新类Class01。")
    // 只有调用Class01.的时候才会调用半生类
    println(Class01.val01)
}

object Class01 {
    println("调用了半生类Class01。")

    val val01 = "val01"
}

object Enter {
    def main(args: Array[String]): Unit = {
        new Class01
    }
}
