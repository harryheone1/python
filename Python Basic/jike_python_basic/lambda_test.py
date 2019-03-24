def true(): return True
lambda : True


def add(x, y):
    return x + y
lf1 = lambda x, y : x + y

print(add(3, 5))
print(lf1(3, 5))
print(type(lf1))
print(type(lf1(3, 5)))


def duck_typing(x, callback):
    return callback(x)


duck_typing(5, lambda x: print(x))