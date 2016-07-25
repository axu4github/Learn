# -*- coding: UTF-8 -*-
'''
测试当调用类方法返回值后，类析构函数修改返回值内容是否有效

'''


class Test(object):
    """docstring for Test"""

    def __init__(self):
        self.arg = {'a': 'a'}

    def __del__(self):
        print "this is test del func"
        self.arg.update({'b': 'b'})
        print "--del--"
        print self.arg
        print "--del--"

    def run(self):
        self.arg.update({'c': 'c'})
        print "this is run func"
        return self.arg

if __name__ == '__main__':
    print Test().run()
