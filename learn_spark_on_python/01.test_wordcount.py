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
