# -*- coding: UTF-8 -*-
'''
- 测试当调用类方法返回值后，类析构函数修改返回值内容是否有效：有效
- 测试析构函数是否可以获取到已返回函数中修改的值：可以
- 测试析构函数是否可以获取异常：不可以

'''


class Test(object):
    """docstring for Test"""

    def __init__(self):
        self.arg = {'a': 'a'}

    def __del__(self):
        try:
            print "this is test del func"
            self.arg.update({'b': 'b'})
            print "--del--"
            print self.arg
            print "--del--"
        except Exception, e:
            print "--- is exception ---"
            print e

    def run(self):
        self.arg.update({'c': 'c'})
        raise Exception("123123")
        print "this is run func"
        return self.arg

if __name__ == '__main__':
    print Test().run()
