def tips(argv):
    def tip(func):
        def wrapper(a, b):
            print('start %s %s' %(argv, func.__name__))
            func(a, b)
            print('stop %s %s' %(argv, func.__name__))
        return wrapper
    return tip


@tips('add')
def add(a, b):
    print(a + b)


@tips('sub')
def sub(a, b):
    print(a - b)

add(1, 2)
sub(1, 2)