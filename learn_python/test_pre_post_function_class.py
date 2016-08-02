# -*- coding: UTF-8 -*-

'''
- 测试

'''


class Parent(object):

    def go(self):
        self.pre_go()
        self.perfom_go()
        self.post_go()

    def pre_go(self): pass

    def perfom_go(self): pass

    def post_go(self): pass


class Child(Parent):

    def perfom_go(self):
        