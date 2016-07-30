# -*- coding: UTF-8 -*-
'''
- 测试静态类中方法使用self调用。静态类中其他方法的问题：不可以使用self

'''

class StaticClass(object):
    
    @staticmethod
    def a():
        print StaticClass.b()

    @staticmethod
    def b():
        return "this is b()" 


if __name__ == '__main__':
    StaticClass.a()
