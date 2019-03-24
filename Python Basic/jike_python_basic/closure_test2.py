def add_one(current):
    return current + 1


num = add_one(1)
next1 = add_one(num)
next2 = add_one(next1)
print(next2)

# with closure, we don't need to manager variable, counter function 'cnt' will manage the variable for us,
# maybe not so easy in this example, but more complicated math computation, it will become more easier and important
def counter(start):
    cnt = [start]
    #print(cnt)
    def add_one():
        #print(cnt[0])
        cnt[0] += 1
        return cnt[0]

    return add_one

counter_0 = counter(1)
print(counter_0())
print(counter_0())
print(counter_0())