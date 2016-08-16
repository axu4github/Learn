from django.test import TestCase
from mysite.multiprocesses import ConnectionDB
from mysite.models import Foo

import time
import os
import multiprocessing

# Create your tests here.


def logic_body(sleepTime):
    from django.db import connections
    debugStr = 'pid(%d) ' % os.getpid()
    for dbAlias in connections.databases.keys():
        cn = connections[dbAlias]
        debugStr += '"%s":%d:%s (child)' % (dbAlias, id(cn), cn)
    print(debugStr)
    time.sleep(sleepTime)


class TestMulitpProcessDBConnection(TestCase):

    # def test_single(self):
    #     print "==== {func_name} ====".format(func_name="test_single")
    #     ConnectionDB().single_process()

    # def test_mulitp(self):
    #     print('**************************************** test_mulitp')
    #     ConnectionDB().multip_process()

    def test_multiprocessing_connection(self):
        print('**************************************** test_multiprocessing_connection')

        from django.db import connections
        debugStr = 'pid(%d) ' % os.getpid()
        for dbAlias in connections.databases.keys():
            cn = connections[dbAlias]
            debugStr += '"%s":%d:%s (parent)' % (dbAlias, id(cn), cn)
        print(debugStr)

        processList = list()
        for index in range(10):
            tmpProcess = multiprocessing.Process(
                target=logic_body, name="process-%d" % index, args=(10,))
            tmpProcess.start()
            processList.append(tmpProcess)

        time.sleep(5)
        print('************%d active child processes**********' %
              len(processList))
        for tmpProcess in processList:
            print('*%s %d' % (tmpProcess.name, tmpProcess.ident))
        print('****************************************')

        for tmpPorcess in processList:
            tmpPorcess.join()

    # def test_os_fork_connection(self):
    #     print('**************************************** test_os_fork_connection')
    #     from django.db import connections
    #     debugStr = 'pid(%d) ' % os.getpid()
    #     for dbAlias in connections.databases.keys():
    #         cn = connections[dbAlias]
    #         debugStr += '"%s":%d (parent)' % (dbAlias, id(cn))
    #     print(debugStr)

    #     rt = os.fork()
    #     if rt == 0:  # child process
    #         logic_body(10)
    #     else:
    #         time.sleep(12)
