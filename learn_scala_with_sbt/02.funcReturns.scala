/**
 * 问题：在Scala语言中，函数返回值是最后一行。
 * 1. 那么如果最后一行写的是一个方法的名字那么返回结果是什么？
 * 2. 如果该函数返回类型写的是Unit，则最后一行写的是方法名字那么会如何执行？
 *
 *
 * 解答：
 * 1. 如果调用时不是一个赋值语句，那么最后一行的方法就是调用该方法。
 * 2. 如果调用时时一个赋值语句，但是赋值给一个变量（var var1 = func1），那么最后一行的方法就还是调用该方法。
 * 3. 如果调用时时一个赋值语句，但是赋值给一个方法（def def1 = func1），那么最后一行的方法就不是调用该方法了，而是返回该方法，并等待赋值方法（def1）被调用时，返回的方法（func1）才被调用。
 */

object Main {

    def func1 = {
        println("This is func1.")
        func2
    }

    def func2 = {
        println("This is func2.")
    }

    def main(args: Array[String]): Unit = {
        val a = func1
        println("1. ---")
        println(a)
        println("2. ---")
        a
        println("3. ---")
        def b = func1
        println("4. ---")
        println(b)
        println("5. ---")
        b
    }
}
