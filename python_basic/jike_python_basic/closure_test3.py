# a * x + b = y

# without closure, two bad choice - poison
# 1st poison, each repeat your mathematical formula
# 2nd poison, make a and b also as variable,
# so you could not think as mathematician because you cuold not use a and b math as parameter
x_list = [i for i in range(10)]
y_list = list(map(lambda x: 2 * x + 1, x_list))
print(y_list)
y_list = list(map(lambda x: 5 * x + 4, x_list))
print(y_list)


# with closure


# def ab_line(a, b):
#     def arg_y(x):
#         return a * x + b
#     return arg_y


def ab_line(a, b):
        return lambda x: a * x + b


line1 = ab_line(2, 1)
line2 = ab_line(5, 4)
print(list(map(lambda x: line1(x), x_list)))
print(list(map(lambda x: line2(x), x_list)))


# Imperative programming paradigm - two wrapper functions to reduce the poison
# Use name convention to maintain code readability and maintainable
def fcore(a, b, x):
        return a*x + b


def f21(x):
        return fcore(2, 1, x)


def f54(x):
        return fcore(5, 4, x)


print(f21(3))
print(f54(3))


# OO programming paradigm - use Object instead of function
class FCcore:
        def __init__(self, a, b):
                self.a = a
                self.b = b
        def calculate(self, x):
                return self.a * x + self.b


f12 = FCcore(1, 2)
f54 = FCcore(5, 4)
print(f12.calculate(3))
print(f54.calculate(3))
