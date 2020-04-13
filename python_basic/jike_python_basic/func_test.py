print('abc', end='\n')


def func(a, b, c=3):
    print('a= %s' % a)
    print('b= %s' % b)
    print('c= %s' % c)


func(1, c=5, b=2)
func(1, 2)

# func(1, c=3) # error, argument 'b' is mandatory
# func(c=4)  # missing 2 required positional arguments: 'a' and 'b'


def func2(first, *middle,  end='z'):
    print('first is %s' % str(first))
    print('middle is %s' % str(middle))
    print('end is %s' % str(end))
    return len(middle) + 2


print(func2('a', 'b', 'c', 'd'))
print(func2('a', 'b', 'c', end='d'))


var1 = 123
var2 = 123


def func3():
    var1 = 456
    global var2
    var2 = 456
    print('Variable value in side function, var1 is %i' % var1)
    print('Variable value in side function, var2 is %i' % var2)
    print('All variables are overridden inside function')


func3()
print('Variable value outside function, var1 is %i' % var1)
print('Variable value outside function, var2 is %i' % var2)
print('Only global variables are overridden outside function')
