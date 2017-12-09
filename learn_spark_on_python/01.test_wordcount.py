# -*- coding: UTF-8 -*-

import sys
from pyspark.sql import SparkSession

APP_NAME = "test_wordcount"


def _init_spark_session():
    return SparkSession.builder.appName(APP_NAME).getOrCreate()


def _reverse(pair):
    (x, y) = pair
    return (y, x)


def main():
    """
    执行命令：

    > cd /Users/axu/opt/apache-spark/latest
    > bin/spark-submit --master spark://localhost:7077 \
                       ~/code/axuProject/Learn/learn_spark_on_python/01.test_wordcount.py \
                       ~/opt/apache-spark/latest/README.md
    """
    file_path = sys.argv[1]
    spark = _init_spark_session()
    text_file = spark.read.text(file_path).rdd
    wordcounts = text_file.map(lambda r: r[0]) \
                          .flatMap(lambda x: x.split(' ')) \
                          .map(lambda x: (x, 1)) \
                          .reduceByKey(lambda x, y: x + y) \
                          .map(_reverse) \
                          .sortByKey(False) \
                          .map(_reverse)

    output = wordcounts.collect()
    print(output)


if __name__ == "__main__":
    main()
