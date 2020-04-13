# general way to use add
def func(a, b):
    return a + b


print(func(1, 2))
print(func(1, 3))
print(func(1, 4))
print(func(1, 5))


def func_clo(a):
    def func(b):
        return a + b

    return func


add_with_1 = func_clo(1)
print(type(add_with_1))
print(type(func_clo))
print(add_with_1(2))
print(add_with_1(3))
print(add_with_1(4))
print(add_with_1(5))
