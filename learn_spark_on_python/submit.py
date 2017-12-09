# -*- coding: UTF-8 -*-

"""
探索通过python如何提交spark任务
"""

import sys
import os
import time
import random
from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext

SPARK_MASTER = "spark://axumatoMacBook-Pro.local:7077"
SPARK_HOME = "/Users/axu/opt/spark-1.6.1-bin-hadoop2.6"
PYSPARK_DIR = os.path.normpath(SPARK_HOME + "/python")
PY4J_DIR = os.path.normpath(SPARK_HOME + "/python/lib/py4j-0.9-src.zip")

sys.path.insert(0, PYSPARK_DIR)
sys.path.insert(0, PY4J_DIR)

if "SPARK_HOME" not in os.environ:
    os.environ["SPARK_HOME"] = SPARK_HOME


SPARK_APP_NAME = "%s_%d" % (time.strftime(
    "%Y-%m-%d_%H:%M:%S", time.localtime(time.time())), random.randint(0, 100))

print SPARK_APP_NAME

sql = "select * from b"

SPARK_EXECUTOR_MEMORY = 1  # 单位：GB
SPARK_EXECUTOR_CORES = 1  # 单位：核数

SPARK_ENVS = {
    "spark.executor.memory": "{em}g".format(em=SPARK_EXECUTOR_MEMORY),
    "spark.executor.cores": SPARK_EXECUTOR_CORES,
}

SPARK_CONF = SparkConf().setAppName(SPARK_APP_NAME).setMaster(SPARK_MASTER)
for k, v in SPARK_ENVS.items():
    SPARK_CONF.set(k, v)

SPARK_CONTEXT = SparkContext(conf=SPARK_CONF)
SQL_CONTEXT = HiveContext(SPARK_CONTEXT)


def spark_submit(SQL_CONTEXT):
    print SQL_CONTEXT.sql(sql).collect()


for i in range(0, 10):
    spark_submit(SQL_CONTEXT)

print "-EOF-"
