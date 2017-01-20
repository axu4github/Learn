# -*- coding: UTF-8 -*-
'''
获取文件路径
'''

import os

if __name__ == '__main__':
    # 获取当前文件路径
    print os.path.abspath(__file__)
    # 获取当前文件所在目录
    print os.path.dirname(os.path.abspath(__file__))
    # 获取当前文件上级目录
    print os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -EOF-
