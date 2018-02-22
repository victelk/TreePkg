import inspect
from FirstPkg import fun1


def fun2():
    return inspect.stack()[0][3]


if __name__ == '__main__':
    print("{} called in {} file".format(fun2(), __file__))
    print("{} called in {} file".format(fun1(), __file__))
