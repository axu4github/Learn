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


def func_d(username=None, **kwargs):
    print '---func_d---'
    print username, kwargs
    print '---func_d---'

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

    ''' output
    ---func_d---
    xiaoqiang {'password': '123'}
    ---func_d---
    '''
    func_d(username='xiaoqiang', password='123')
