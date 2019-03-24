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