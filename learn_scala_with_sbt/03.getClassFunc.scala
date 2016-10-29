/**
 * 测试getClass方法
 */

trait Logging {
    def logName = {
        this.getClass.getName
    }
}

object Main extends Logging{
    
    def main(args: Array[String]): Unit = {
        println("---")
        println(logName)
        println("---")
    }
}
