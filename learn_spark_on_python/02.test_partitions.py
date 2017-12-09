# -*- coding: UTF-8 -*-

from pyspark.sql import SparkSession

APP_NAME = "test_partitions"


def _init_spark_session():
    return SparkSession.builder.appName(APP_NAME).getOrCreate()


def get_pair_first(pair):
    return pair[0]


def main():
    """
    测试 Spark Partitions

    > cd /Users/axu/opt/apache-spark/latest
    > bin/spark-submit --master spark://localhost:7077 \
                       ~/code/axuProject/Learn/learn_spark_on_python/02.test_partitions.py
    """
    spark = _init_spark_session()
    datas = [1, 2, 3, 4, 1, 4, 2, 4, 6, 5, 7]
    print("-" * 3)
    print("原始数据。")
    print("Data\t=> {}".format(datas))
    print("-" * 3)

    print("默认分区（Hash Partition）。")
    rdd = spark.sparkContext.parallelize(datas)
    print("Number\t=> {}".format(rdd.getNumPartitions()))
    print("Data\t=> {}".format(rdd.glom().collect()))
    print("-" * 3)

    # 按照数字相同的分在一个分区中
    print("按照数组相同的分在一个分区中。")
    partitions_number = len(set(datas))
    partitioned_rdd = rdd.map(lambda x: (x, x)) \
                         .partitionBy(partitions_number) \
                         .map(get_pair_first)
    print("Number\t=> {}".format(partitioned_rdd.getNumPartitions()))
    print("Data\t=> {}".format(partitioned_rdd.glom().collect()))
    print("-" * 3)

    # 自定义分区（数组中大于3的一个分区，小于3的一个分区）
    print("数组中大于3的一个分区，小于3的一个分区。")
    custom_partitioned = rdd.map(lambda x: (x, x)) \
                            .partitionBy(2, lambda x: int(x > 3)) \
                            .map(get_pair_first)
    print("Number\t=> {}".format(custom_partitioned.getNumPartitions()))
    print("Data\t=> {}".format(custom_partitioned.glom().collect()))
    print("-" * 3)

    print("按照数组每一个元素分一个区。")
    new_rdd = spark.sparkContext.parallelize(list(enumerate(datas, start=1)))
    custom_partitioned_01 = new_rdd.partitionBy(len(datas)).map(lambda x: x[1])
    print("Number\t=> {}".format(custom_partitioned_01.getNumPartitions()))
    print("Data\t=> {}".format(custom_partitioned_01.glom().collect()))
    print("-" * 3)


if __name__ == "__main__":
    main()
