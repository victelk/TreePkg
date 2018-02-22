import inspect
from FirstPkg import fun1 as f1
from FirstPkg import fun2
from SecondPkg import fun3
from SecondPkg import fun1


def fun4():
    return inspect.stack()[0][3]


if __name__ == '__main__':
    print("{} called in {} file".format(f1(), __file__))
    print("{} called in {} file".format(fun1(), __file__))
    print("{} called in {} file".format(fun2(), __file__))
    print("{} called in {} file".format(fun3(), __file__))
    print("{} called in {} file".format(fun4(), __file__))
