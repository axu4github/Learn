# coding=utf-8

import happybase
import threading
import time
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

HBASE_HOST = "172.31.117.94"
HBASE_TABLE = "smartv"


def conn(host=HBASE_HOST, table=HBASE_TABLE):
    connection = happybase.Connection(host)
    table = connection.table(table)
    return table


def fetch_hbase_record():
    table = conn()
    print(table.row(b"B2C-IM-20180411-Lancome-1002.wav")["cf:area_of_job"])


def put_record():
    table = conn(table="parallel_put_record_table")
    rowkey = str(random.randint(0, 100000 * 100000))
    print(rowkey)
    table.put(rowkey, {b"cf:test": b"a%s" % str(random.randint(0, 100000))})


def main():
    loop_number = 100
    for j in range(loop_number):
        thread_number = 5000
        threads = []
        for i in range(thread_number):
            t = threading.Thread(target=put_record, name="fhr_thread")
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        print(j)
        time.sleep(2)


if __name__ == "__main__":
    main()
