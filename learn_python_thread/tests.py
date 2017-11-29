# -*- coding: utf-8 -*-

import time
import threading

r = []


def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        r.append(n)
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)

    print 'thread %s ended.' % threading.current_thread().name


def main():
    print 'thread %s is running...' % threading.current_thread().name
    threads = []
    for i in range(5):
        t = threading.Thread(target=loop, name='LoopThread')
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print 'thread %s ended.' % threading.current_thread().name
    print(r)


if __name__ == '__main__':
    main()
