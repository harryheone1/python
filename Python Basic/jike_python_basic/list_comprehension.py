# square from 1 to 10, only for odd
a_list = []
for i in range(1, 10):
    if i % 2 == 0:
        a_list.append(i*i)

print(a_list)

b_list = [i*i for i in range(1,10) if i%2 != 0]
print(b_list)
