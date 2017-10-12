# -*- coding: utf-8 -*-

import happybase
from functools import wraps
from time import clock

HBASE_HOST = "10.0.3.41"
HBASE_TABLE = "smartv"
DEFAULT_ROW_KEY = b"dy-gz-t54548716_20150201_8221862.mp3"
GET_ROW_NUMBER = 10000


def time_analyze(func):
    """ 装饰器 获取程序执行时间 """
    @wraps(func)
    def consume(*args, **kwargs):
        # 重复执行次数（单次执行速度太快）
        exec_times = 1
        start = clock()
        for i in range(exec_times):
            r = func(*args, **kwargs)

        finish = clock()
        print "{:<20}{:10.6} s".format(func.__name__ + ":", finish - start)
        return r

    return consume


@time_analyze
def single_get():
    """ 单条获取 hbase 记录 """
    connection = happybase.Connection(HBASE_HOST)
    table = connection.table(HBASE_TABLE)
    for i in range(GET_ROW_NUMBER):
        table.row(DEFAULT_ROW_KEY)


@time_analyze
def multiple_get():
    """ 多条获取 hbase 记录 """
    connection = happybase.Connection(HBASE_HOST)
    table = connection.table(HBASE_TABLE)
    row_keys = []
    for i in range(GET_ROW_NUMBER):
        row_keys.append(DEFAULT_ROW_KEY)

    table.rows(row_keys)


def main():
    single_get()
    multiple_get()


if __name__ == "__main__":
    main()
