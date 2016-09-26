trait Log {
    println(s"1. tarit Log class.")

    def lg = {
        println("2. tarit def log.")
        
        println(s"4. ${Log.init_arg}")
    }
}

object Log {
    println(s"3. object Log class.")

    var init_arg = "object Log init_arg."
}


// - class 和 object 不能同时存在main函数
// - 若是class存在main还是则不能直接使用scala HelloWorld调用，报"java.lang.NoSuchMethodException: HelloWorld.main is not static"
class HelloWorld() {
    println("class.")
    // def main(args: Array[String]): Unit = {
    //     println("class main print.")

    //     for (arg: String <- args) {
    //         println(arg)
    //     }
    // }
}

object HelloWorld extends Log {

    lg

    println("defore define main.")

    var test = "这是一个test字符串"

    // def test = {
    //     "这是一个test字符串"
    // }

    System.err.println(s"axu.print [core/src/main/scala/org/apache/spark/deploy/master/Master.scala] [Debug] === 现在是class Master类，测试bin/spark-class调用时是否是直接调用object类 ===")    
    System.err.println(s"${test}testessstststt")

    def main(args: Array[String]): Unit = {
        println("object class main print.")

        for (arg: String <- args) {
            println(arg)
        }
    }

    def another_func() {
        println("object another function.")
    }

    println("after define main.")
}