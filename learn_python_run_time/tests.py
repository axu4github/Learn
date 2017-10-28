# -*- coding: utf-8 -*-

import unittest
from datetime import datetime
import time


class RunTimeTest(unittest.TestCase):
    """ 测试程序运行时间 """

    def test_process_total_run_time(self):
        """ 测试程序运行总时间 """
        s = datetime.now()
        time.sleep(5)
        e = datetime.now()
        print(e - s)
        pass

    def test_process_sys_run_time(self):
        """ 测试程序运行CPU时间 """
        s = time.clock()
        time.sleep(5)
        e = time.clock()
        print((e - s) * 1000)
        pass


if __name__ == "__main__":
    unittest.main()
