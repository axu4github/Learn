# -*- coding: UTF-8 -*-
'''
python 继承
'''


class Loggable(object):

    # def get_class(self):
    #     return "%s" % self.__name__ 

    def log_info(self, message):
        print("%s : %s" % (self.__class__.__name__, message))


class Main(Loggable):

    def test(self, message):
        self.log_info("main func calling " + message)


class Another(Loggable):

    def test(self, message):
        self.log_info("main func calling " + message)

Main().test("123")
Another().test("234")
