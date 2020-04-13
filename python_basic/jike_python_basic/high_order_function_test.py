from functools import reduce

a_list = [i for i in range(10)]
b_list = [i for i in range(10)]

filter1 = filter(lambda x: x % 2 == 0, a_list)
print(type(filter1))
print(list(filter1))

map_square = map(lambda x: x * x, a_list)
print(type(map_square))
print(list(map_square))

map_add = map(lambda x, y: x + y, a_list, b_list)
print(type(map_add))
print(list(map_add))

reduce_add = reduce(lambda x, y: x + y, a_list)
print(type(reduce_add))
print(reduce_add)

# transpose matrix [(1, 2, 3),(4, 5, 6)] to [(1, 4), (2, 5), (3, 6)]
zip1 = zip((1, 2, 3), (4, 5, 6))
print(type(zip1))
print(zip1)
print(dict(zip1))

# exchange key and value of dic
a_dic = {1: 'a', 2: 'b', 3: "c"}
zip2 = zip(a_dic.values(), a_dic.keys())
for i in zip2:
    print(i)

