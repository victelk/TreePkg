import inspect

def fun1():
    return inspect.stack()[0][3] + "new"

def fun3():
    return inspect.stack()[0][3]


if __name__ == '__main__':
    print("{} called in {} file".format(fun3(), __file__))
