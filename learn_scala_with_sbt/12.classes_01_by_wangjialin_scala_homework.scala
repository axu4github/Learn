/**
 * Spark IMF 第一课 Scala光速入门 作业
 *
 * 题目：删除数组除第一个负数以外的负数，注意考虑性能
 */

import util.control.Breaks._
import scala.collection.mutable.ArrayBuffer

object Enter {

    // 删除数组除第一个负数以外的负数
    def array_filter(arr: Array[Int]) = {
        val result = ArrayBuffer[Int]()
        var is_pass = false
        for (number <- arr) {
            breakable {
                if (number < 0) {
                    // 第一次遇到负数
                    if (!is_pass) is_pass = true; else break();
                }

                result += number
            }
        }

        result
    }

    def main(args: Array[String]): Unit = {
        val arr = Array(1, 2, 3, -1, -2, -3, 4, -5, 6, 7, 8, 0, -2, 10)
        println(array_filter(arr))
    }
}
