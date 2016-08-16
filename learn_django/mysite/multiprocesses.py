# -*- coding: UTF-8 -*-

'''
# 测试单元测试，多进程数据库连接问题

'''

from multiprocessing import Process
from mysite.models import Foo


class ConnectionDB(object):

    def touch_db_table(self, sleep_time=None):
        from django.db import connections, connection

        # connections['default'].close()
        # cursor = connections['default'].cursor()
        # cursor.execute("select * from mysite_foo")
        # print cursor.fetchall()
        try:
            print '========= connection.ping() ========='
            connection.connection.ping()
        except Exception, e:
            print '========= ping exception ========='
            # 关闭当前数据库连接（之后django若遇到需使用数据库时，会重新打开一个数据库连接）
            for db_alias in connections.databases.keys():
                connections[db_alias].close()

            # try:
            #     connection.connection.ping()
            # except Exception, e:
            #     raise e

        if sleep_time is not None:
            import time
            time.sleep(int(sleep_time))

        
        print "--- in touch_db_table function. ---"
        foo = Foo.objects.all()[0]
        print "result: {foo}".format(foo=foo.bar)
        print "--- out touch_db_table function. ---"

    def single_process(self):
        self.touch_db_table()

    def multip_process(self):
        p = Process(target=self.touch_db_table)
        p.start()
