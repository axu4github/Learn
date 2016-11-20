/**
 * 研究 System.getProperties 方法
 */

import scala.collection.JavaConverters._

object Enter {
    def main(args: Array[String]): Unit = {
        println("--- System.getProperties")
        println(System.getProperties)
        println()
        println("--- System.getProperties.stringPropertyNames()")
        println(System.getProperties.stringPropertyNames())
        println()
        println("--- System.getProperties.stringPropertyNames().asScala")
        println(System.getProperties.stringPropertyNames().asScala)
        println()
        println("--- System.getProperties.stringPropertyNames().asScala.map(key => (key, System.getProperty(key)))")
        println(System.getProperties.stringPropertyNames().asScala.map(key => (key, System.getProperty(key))))
        println()
        println("--- System.getProperties.stringPropertyNames().asScala.map(key => (key, System.getProperty(key))).toMap")
        println(System.getProperties.stringPropertyNames().asScala.map(key => (key, System.getProperty(key))).toMap)
    }
}
