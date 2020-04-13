def tips(argv):
    def tip(func):
        def wrapper(a, b):
            print('start %s %s' %(argv, func.__name__))
            func(a, b)
            print('stop %s %s' %(argv, func.__name__))
        return wrapper
    return tip

outer1 = tips('add')
tip1 = outer1(lambda a, b: print(a + b))
tip1(1, 2)

outer2 = tips('sub')
tip2 = outer1(lambda a, b: print(a - b))
tip2(1, 2)

@tips('add')
def add(a, b):
    print(a + b)


@tips('sub')
def sub(a, b):
    print(a - b)

add(1, 2)
sub(1, 2)