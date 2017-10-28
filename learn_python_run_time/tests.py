# -*- coding: utf-8 -*-

import unittest
from datetime import datetime
import time


class RunTimeTest(unittest.TestCase):
    """ 测试程序运行时间 """

    def test_process_run_total_time(self):
        """ 测试程序运行总时间 """
        s = datetime.now()
        time.sleep(5)
        e = datetime.now()
        print(e - s)


if __name__ == "__main__":
    unittest.main()
