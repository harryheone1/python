# iterator
list1 = (1, 2, 3)
it = iter(list1)
print(next(it))
print(next(it))
print(next(it))
#print(next(it)) # error

# for i in range(10, 20, 0.5): # range could not accept float
#     print(i)


def frange_gene(start, end, step):
    x = start
    while x < end:
        yield x
        x += step


def frange(start, end, step):
    x = start
    while x < end:
        print('without lazy computing %f' %x)
        x += step


#classic = frange(0, 20, 2)
#print(next(classic)) # there is no return in normal range
gene = frange_gene(0, 20, 2)
print(next(gene))
print(next(gene))

for i in frange_gene(0, 20, 2):
    print('lazy computing %f' % i)

for i in range(0, 20, 2):
    print(i)
