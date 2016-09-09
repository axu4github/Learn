# -*- coding: UTF-8 -*-

'''
测试 python 类中动态方法

'''


class A(object):

    fun2 = 'fun2_str'

    def fun1(self):
        print 'fun1'

    def fun2(self):
        print 'fun2_fun'

    def execute(self):
        # print hasattr(self, 'fun2')()
        print getattr(self, 'fun2')()
        # import os
        # print 'fun2' in dir(os)


if __name__ == '__main__':
    v = A
    v().execute()
