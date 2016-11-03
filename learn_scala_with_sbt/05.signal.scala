/**
 * 了解 sun.misc.{Signal, SignalHandler} 类作用
 *
 * 在程序运行中可以捕捉到指定的信号，并添加相关处理信号的逻辑
 * 
 */

import sun.misc.{Signal, SignalHandler}
import java.util.Collections
import scala.collection.JavaConverters._

class ActionHandler(signal: Signal) extends SignalHandler {
    val actions = Collections.synchronizedList(
        new java.util.LinkedList[() => Boolean])

    // 注册 signal
    val prevHandler: SignalHandler = {
            println(signal.getName())
            Signal.handle(signal, this)
    }

    // 重写 handle 方法
    override def handle(sig: Signal): Unit = {
        Signal.handle(signal, prevHandler)
        if (sig.getName == "INT") {
            val escalate = actions.asScala.map(action => action()).forall(_ == false)

            println("escalate: " + escalate)

            if (escalate) {
                prevHandler.handle(sig) // 直接退出进程
            }
        } else {
            println()
            println(sig.getName() + "override handler!")
            println()
        }

        Signal.handle(signal, this)
    }

    def register(action: => Boolean): Unit = actions.add(() => action)
}

object SignalUtils {
    def main(args: Array[String]): Unit = {
        println("signal register =start=")
        // - TERM: 终止信号
        // - HUP: 终端挂起或者控制进程终止
        // - INT: 键盘中断

        // 当 sig == INT 时，action 为 true 其余为 false
        Seq("TERM", "HUP", "INT").foreach { sig => 
            SignalUtils.register(sig){sig == "INT"}
            // SignalUtils.register(sig){false}
        }

        println("signal register =end=")

        println("Thread sleep =start=.")
        // 单位是毫秒
        for (i <- 1 to 60) {
            println(i + "...")
            Thread sleep 1000
        }

        println("Thread sleep =end=.")
    }

    // signal 信号
    // action 接收到信号以后是否执行信号动作（若是注册多个信号，那么只有当全部信号都为false的时候才执行，否则只要有一个为true那么就不会执行）（判断代码为 forall(_ == false)）
    def register(signal: String)(action: => Boolean): Unit = {
        println(signal + " register -start-")
        // ActionHandler 需要继承 SignalHandler
        val handler = handlers.getOrElseUpdate(
            signal, 
            new ActionHandler(new Signal(signal)))

        // 将信号action添加到
        handler.register(action)
    }

    val handlers = new scala.collection.mutable.HashMap[String, ActionHandler]
}