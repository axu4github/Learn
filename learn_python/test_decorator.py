def deco(func):
    def wrapper():
        print 'pre %s()' % func.__name__
        func()
        print 'post %s()' % func.__name__

    return wrapper


@deco
def foo():
    print 'bar'


def class_deco(func):
    def wrapper(*args, **kwargs):
        print '123'
        func(*args, **kwargs)
        print '456'

    return wrapper


class Class_Foo(object):

    @class_deco
    def class_bar(self, arg='arg', arg1='arg1', *args, **kwargs):
        print arg, arg1, args, kwargs


if __name__ == '__main__':
    foo()
    print '---'
    Class_Foo().class_bar()
