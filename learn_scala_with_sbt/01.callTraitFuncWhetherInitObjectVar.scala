/**
 * 问题：调用已经继承的Trait类中已声明的变量或者方法时，会不会首先调用该Trait类的object类。
 * 结果：不会先调用object类  
 */

trait Logging {
    def log(msg: String) = {
        println("This is Trait Logging log funciton. println: " + msg)
    }
}

object Logging {

    val var1 = "var1";

    println("This is print Object Logging var1: " + var1)

    def func(arg: String) = {
        println("This is Object Logging func.")
    }
}


object Main extends Logging {
    def main(args: Array[String]) {
        log("123")
    }
}
