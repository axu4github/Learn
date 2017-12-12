# -*- coding: UTF-8 -*-

import time
from operator import add
from pyspark.sql import SparkSession

APP_NAME = "test_mutiple_partitions"


def _init_spark_session():
    return SparkSession.builder.appName(APP_NAME).getOrCreate()


def process(x):
    time.sleep(1)
    return x


def main():
    """
    测试多分区并行处理

    > cd /Users/axu/opt/apache-spark/latest
    > bin/spark-submit --master spark://localhost:7077 \
                       ~/code/axuProject/Learn/learn_spark_on_python/03.test_mutiple_partitions.py
    """
    datas = range(200000)
    spark = _init_spark_session()
    rdd = spark.sparkContext.parallelize(list(enumerate(datas, start=1))) \
                            .partitionBy(len(datas)) \
                            .map(lambda x: x[1])
    print("分区数：{}".format(rdd.getNumPartitions()))
    _sum = rdd.map(process).reduce(add)
    print(_sum)


if __name__ == "__main__":
    main()
