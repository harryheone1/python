# General Recursion
def recsum(x):
    if x == 1:
        return x
    else:
        return x + recsum(x - 1)

# loop
def recsum(x):
    for i in range(6):
        sum += i
    return sum

# Tail Recursion
def tailrecsum(x, running_total=0):
    if x == 0:
        return running_total
    else:
        return tailrecsum(x - 1, running_total + x)
