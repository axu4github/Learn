def deco(func):
    def wrapper():
        print 'pre %s()' % func.__name__
        func()
        print 'post %s()' % func.__name__

    return wrapper


@deco
def foo():
    print 'bar'


def a():
    print("a")  # 1

    def decorator(f):
        print("decorator")  # 4
        return f  # 5

    print("finish decorator")  # 2
    return decorator  # 3


@a()  # 必须带括号
def bar():
    print("bar")


def class_deco(func):
    print(func.__doc__)

    def wrapper(*args, **kwargs):
        print '123'
        func(*args, **kwargs)
        print '456'

    return wrapper


class Class_Foo(object):

    @class_deco
    def class_bar(self, arg='arg', arg1='arg1', *args, **kwargs):
        """ doc of class_bar function """
        print arg, arg1, args, kwargs


if __name__ == '__main__':
    foo()
    print '---'
    Class_Foo().class_bar()
    print("-" * 3)
    bar()
