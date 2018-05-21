# coding=utf-8

import happybase
import threading
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

HBASE_HOST = "172.31.117.94"
HBASE_TABLE = "smartv"


def conn():
    connection = happybase.Connection(HBASE_HOST)
    table = connection.table(HBASE_TABLE)
    return table


def fetch_hbase_record():
    table = conn()
    print(table.row(b"B2C-IM-20180411-Lancome-1002.wav")["cf:area_of_job"])


def main():
    for j in range(100):
        thread_number = 500
        threads = []
        for i in range(thread_number):
            t = threading.Thread(target=fetch_hbase_record, name="fhr_thread")
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        print(j)
        time.sleep(2)


if __name__ == "__main__":
    main()
