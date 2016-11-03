/**
 * 了解 scala.collection.mutable.HashMap 的 getOrElseUpdate方法
 * 
 */

class ActionHandler() {

    def register(arg: String) = {
        println(arg)
    }
}

object Main {
    def main(args: Array[String]): Unit = {
        var handlers = new scala.collection.mutable.HashMap[String, ActionHandler]
        val handler = handlers.getOrElseUpdate("a", new ActionHandler())
        handler.register("call ActionHandler register")
    }
}
