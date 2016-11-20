/**
 * 研究scala map方法
 */

case class DeprecatedConfig(
    key: String,
    version: String,
    deprecationMessage: String)

case class AlternateConfig(
    key: String,
    version: String,
    translation: String => String = null)

object Enter {
    def main(args: Array[String]): Unit = {
        val deprecatedConfigs: Map[String, DeprecatedConfig] = {
            val configs = Seq(
              DeprecatedConfig("spark.cache.class", "0.8",
                "The spark.cache.class property is no longer being used! Specify storage levels using " +
                "the RDD.persist() method instead."),
              DeprecatedConfig("spark.yarn.user.classpath.first", "1.3",
                "Please use spark.{driver,executor}.userClassPathFirst instead."),
              DeprecatedConfig("spark.kryoserializer.buffer.mb", "1.4",
                "Please use spark.kryoserializer.buffer instead. The default value for " +
                  "spark.kryoserializer.buffer.mb was previously specified as '0.064'. Fractional values " +
                  "are no longer accepted. To specify the equivalent now, one may use '64k'."),
              DeprecatedConfig("spark.rpc", "2.0", "Not used any more.")
            )

            // 下面三个输出一样，感觉第一个最好理解，第三个还没理解
            println(configs.map(cfg => (cfg.key -> cfg)).toMap)
            println()
            println(configs.map { cfg => (cfg.key -> cfg) }.toMap)
            println()
            println(Map(configs.map { cfg => (cfg.key -> cfg) } : _*))
            println()

            Map(configs.map { cfg => (cfg.key -> cfg) } : _*)
        }

        val configsWithAlternatives: Map[String, (String, AlternateConfig)] = {
            val allAlternatives = Map[String, Seq[AlternateConfig]](
                "spark.executor.userClassPathFirst" -> Seq(
                  AlternateConfig("spark.files.userClassPathFirst", "1.3"),
                  AlternateConfig("spark.files.userClassPathFirst1", "1.3")),
                "spark.history.fs.update.interval" -> Seq(
                  AlternateConfig("spark.history.fs.update.interval.seconds", "1.4"),
                  AlternateConfig("spark.history.fs.updateInterval", "1.3"),
                  AlternateConfig("spark.history.updateInterval", "1.3")),
                "spark.history.fs.cleaner.interval" -> Seq(
                  AlternateConfig("spark.history.fs.cleaner.interval.seconds", "1.4")),
                "spark.history.fs.cleaner.maxAge" -> Seq(
                  AlternateConfig("spark.history.fs.cleaner.maxAge.seconds", "1.4")),
                "spark.yarn.am.waitTime" -> Seq(
                  AlternateConfig("spark.yarn.applicationMaster.waitTries", "1.3",
                    // Translate old value to a duration, with 10s wait time per try.
                    translation = s => s"${s.toLong * 10}s")),
                "spark.reducer.maxSizeInFlight" -> Seq(
                  AlternateConfig("spark.reducer.maxMbInFlight", "1.4")),
                "spark.kryoserializer.buffer" ->
                    Seq(AlternateConfig("spark.kryoserializer.buffer.mb", "1.4",
                      translation = s => s"${(s.toDouble * 1000).toInt}k")),
                "spark.kryoserializer.buffer.max" -> Seq(
                  AlternateConfig("spark.kryoserializer.buffer.max.mb", "1.4")),
                "spark.shuffle.file.buffer" -> Seq(
                  AlternateConfig("spark.shuffle.file.buffer.kb", "1.4")),
                "spark.executor.logs.rolling.maxSize" -> Seq(
                  AlternateConfig("spark.executor.logs.rolling.size.maxBytes", "1.4")),
                "spark.io.compression.snappy.blockSize" -> Seq(
                  AlternateConfig("spark.io.compression.snappy.block.size", "1.4")),
                "spark.io.compression.lz4.blockSize" -> Seq(
                  AlternateConfig("spark.io.compression.lz4.block.size", "1.4")),
                "spark.rpc.numRetries" -> Seq(
                  AlternateConfig("spark.akka.num.retries", "1.4")),
                "spark.rpc.retry.wait" -> Seq(
                  AlternateConfig("spark.akka.retry.wait", "1.4")),
                "spark.rpc.askTimeout" -> Seq(
                  AlternateConfig("spark.akka.askTimeout", "1.4")),
                "spark.rpc.lookupTimeout" -> Seq(
                  AlternateConfig("spark.akka.lookupTimeout", "1.4")),
                "spark.streaming.fileStream.minRememberDuration" -> Seq(
                  AlternateConfig("spark.streaming.minRememberDuration", "1.5")),
                "spark.yarn.max.executor.failures" -> Seq(
                  AlternateConfig("spark.yarn.max.worker.failures", "1.5")),
                "spark.memory.offHeap.enabled" -> Seq(
                  AlternateConfig("spark.unsafe.offHeap", "1.6")),
                "spark.rpc.message.maxSize" -> Seq(
                  AlternateConfig("spark.akka.frameSize", "1.6")),
                "spark.yarn.jars" -> Seq(
                  AlternateConfig("spark.yarn.jar", "2.0"))
            )


            println("---")
            println(allAlternatives)
            println("---")
            allAlternatives.keys.flatMap { key =>
                allAlternatives(key).map { cfg => (cfg.key -> (key -> cfg)) }
            }.toMap
        }
        

        println(deprecatedConfigs.get("spark.cache.class"))
        println()
        var i = 0
        deprecatedConfigs.get("spark.cache.class").foreach { cfg => 
            println(cfg.key)
            println(cfg.version)
            println(cfg.deprecationMessage)
        }   
        println()
        println(configsWithAlternatives)

        println((1 to 10).map{x => x * 2})
        println((1 to 10).flatMap{ x => 
            println("one: " + x)
            (1 to 10).map{ y => 
                println("two: " + y + " | " + x)
                y * 2
            }
        })
    }
}