# -*- coding: UTF-8 -*-

'''
测试 python 方法中 *args 和 **kwargs 用法

'''

dic = {'username': 'xiaoqiang', 'password': 'xiaoqiang123'}


def func(*args, **kwargs):
    print '---'
    print args
    print kwargs
    print '---'

def func_a(username=None, password=None, *args, **kwargs):
    print '---'
    print username, password, args, kwargs
    print '---'

if __name__ == '__main__':
    # ({'username': 'xiaoqiang', 'password': 'xiaoqiang123'},)
    # {}
    func(dic)

    # ('username', 'password')
    # {}
    func(*dic)

    # ()
    # {'username': 'xiaoqiang', 'password': 'xiaoqiang123'}
    func(**dic)

    func_a(dic)
    func_a(*dic)
    func_a(**dic)
