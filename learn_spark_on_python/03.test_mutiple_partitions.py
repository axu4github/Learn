# -*- coding: UTF-8 -*-

from pyspark.sql import SparkSession
from operator import add

APP_NAME = "test_mutiple_partitions"


def _init_spark_session():
    return SparkSession.builder.appName(APP_NAME).getOrCreate()


def process(x):
    pass


def main():
    """
    测试多分区并行处理
    """
    datas = range(200)
    spark = _init_spark_session()
    rdd = spark.sparkContext.parallelize(list(enumerate(datas, start=1))) \
                            .partitionBy(len(datas)).map(lambda x: x[1])
    print(rdd.getNumPartitions())
    print(rdd.map(lambda x: x + 1).reduce(add))


if __name__ == "__main__":
    main()
