/**
 * 研究lazy对象
 */

class Class01 {
    lazy val val01 = {
        println("初始化一个lazy对象。")
        "val01"
    }
}

object Enter {
    def main(args: Array[String]): Unit = {
        // 初始化类时，是不会调用初始化lazy变量的
        val c01 = new Class01
        // 只有当调用lazy变量时，才会初始化该变量
        println(c01.val01)
    }
}
