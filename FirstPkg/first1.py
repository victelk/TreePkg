import inspect


def fun1():
    return inspect.stack()[0][3]


if __name__ == '__main__':
    print("{} called in {} file".format(fun1(), __file__))
