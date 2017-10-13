# -*- coding: utf-8 -*-

import happybase
from functools import wraps
from time import clock
import click
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


HBASE_HOST = "10.0.3.41"
HBASE_TABLE = "smartv"
DEFAULT_ROW_KEY = b"dy-gz-t54548716_20150201_8221862.mp3"
GET_ROW_NUMBER = 1000


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
def single_get(row_number):
    """ 单条获取 hbase 记录 """
    connection = happybase.Connection(HBASE_HOST)
    table = connection.table(HBASE_TABLE)

    return [table.row(DEFAULT_ROW_KEY) for i in range(row_number)]


@time_analyze
def multiple_get(row_number):
    """ 多条获取 hbase 记录 """
    # 设置 socket 超时时间为 10 分钟
    connection = happybase.Connection(HBASE_HOST, timeout=600000)
    table = connection.table(HBASE_TABLE)

    return table.rows([DEFAULT_ROW_KEY for i in range(row_number)])


@click.command()
@click.option("--row_number", default=0, type=click.INT, help="获取记录数量")
def main(row_number):
    if row_number == 0:
        row_number = GET_ROW_NUMBER

    print(len(single_get(row_number)))
    print(len(multiple_get(row_number)))


if __name__ == "__main__":
    main()
