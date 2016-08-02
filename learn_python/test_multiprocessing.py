# -*- coding: UTF-8 -*-
'''
学习 python 多进程

'''

from multiprocessing import Process
import os

class MP(object):

    name = "MP"

    def main(self):
        print 'main func'
        kwargs = {'a':'a', 'b':'b'}
        arg = 'arg'
        arg2 = 'arg2'
        arg3 = 'arg3'
        args = ['arg1', 'arg2']
        print 'Parent process %s.' % os.getpid()
        p = Process(target=self.child, args=(arg, arg2, arg3, args), kwargs=kwargs)
        print 'Process will start.'
        p.start()
        print p.pid, p.is_alive(), p.name
        p.join()
        print p.is_alive()
        print 'process end.'

    def child(self, arg, arg2, arg3, *args, **kwargs):
        print 'Run child process %s (%s)...' % (arg, os.getpid())
        print arg,arg2,arg3
        print args
        print kwargs
        print self.name

    def __call__(self):
        self.main()

    def to_print(self):
        self.main()


if __name__ == '__main__':
    print '1234'
    # MP().to_print()
    a = MP()
    a()
