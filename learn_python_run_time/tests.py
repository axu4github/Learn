# -*- coding: utf-8 -*-

import unittest
from datetime import datetime
import time
import sys


class RunTimeTest(unittest.TestCase):
    """ 测试程序运行时间 """

    def setUp(self):
        self.sleep_time = 5

    def delay_func(self):
        """ 延迟方法 """
        time.sleep(self.sleep_time)

    def test_process_total_run_time(self):
        """ 测试程序运行总时间 """
        s = datetime.now()
        self.delay_func()
        e = datetime.now()
        print("{} : {}".format(sys._getframe().f_code.co_name, e - s))
        pass

    def test_process_sys_run_time(self):
        """ 测试程序运行CPU时间 """
        s = time.clock()
        self.delay_func()
        e = time.clock()
        print("{} : {}".format(sys._getframe().f_code.co_name, (e - s) * 1000))
        pass

    def test_prcess_total_run_time_by_time(self):
        """ 使用 time() 方法，测试程序运行总时间 """
        s = time.time()
        self.delay_func()
        e = time.time()
        print("{} : {}".format(sys._getframe().f_code.co_name, e - s))
        pass


if __name__ == "__main__":
    unittest.main()
