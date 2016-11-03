/**
 * 了解 sun.misc.{Signal, SignalHandler} 类作用
 *
 * 保证进程在运行过程中只到完成，中间遇到中断时，不会打断进程运行。
 * 
 */

import sun.misc.{Signal, SignalHandler}

class ActionHandler(signal: Signal) extends SignalHandler {
    val prevHandler: SignalHandler = {
            println(signal.getName())
            Signal.handle(signal, this)
        }

    override def handle(sig: Signal): Unit = {
        Signal.handle(signal, prevHandler)
        if (sig.getName == "INT") {
            prevHandler.handle(sig) // 直接退出进程   
        } else {
            println()
            println(sig.getName() + "override handler!")
            println()
        }

        Signal.handle(signal, this)
    }
}

object SignalUtils {
    def main(args: Array[String]): Unit = {
        println("signal register =start=")
        // - TERM: 终止信号
        // - HUP: 终端挂起或者控制进程终止
        // - INT: 键盘中断
        Seq("TERM", "HUP", "INT").foreach { sig => 
            SignalUtils.register(sig){false}
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

    def register(signal: String)(action: => Boolean): Unit   = {
        println(signal + " register -start-")
        new ActionHandler(new Signal(signal))
        println(signal + " register -end-")
    }
}