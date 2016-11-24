/**
 * Spark IMF 第三课 Scala函数式编程彻底精通及Spark源码阅读 作业
 *
 * 题目：统计一个文件夹下面所有的单词出现的总次数。
 */

 import java.io.File

object Enter {

    def walk(file: File): Unit = {
        if (file.isFile()) println(file.getName()) else file.listFiles().foreach(walk)
    }

    // 思路：
    // 1. 递归输入目录找到所有文件
    // 2. 依次处理每个文件
    // 3. 依次处理每个文件的每行文字
    // 4. 针对每行文字进行分词算法，生成针对每行文字的词数组
    // 5. 循环词数组和结果的哈希数组比对
    // 6. 若无该词则将该词添加到哈希数组中并制定值为1
    // 7. 若有该词则将该词在哈希数组中的值加1
    def wordCount(dir: String) = {
        walk(new File(dir))
    }

    def main(args: Array[String]): Unit = {
        wordCount("./")
    }
}