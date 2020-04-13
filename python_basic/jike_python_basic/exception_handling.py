# exception that input value is not a number
# year = year = int(input('input year'))
#
# try:
#     year = year = int(input('input year'))
# except ValueError:
#     print('Please enter a number')


# exception that no key in the dictionary
# dict = {1 : 'a', 2 : 'b', 3 : 'c'}
# #dict[4]
# try:
#     dict[4]
# except KeyError:
#     print('try with another key')

# exception that list is out of index
# a_list = [1, 2, 3]
# #a_list[4]
# try:
#     a_list[4]
# except IndexError:
#     print('List is as long as you think')

# exception that no function exist
a_string = 123
#a_string.append('f')
# try:
#     a_string.append('f')
# except AttributeError:
#     print('There is no function or fields as you defined, please be careful that python is dynamic type language')

# exception that add a element to tuple
# a_tuple = (1, 2, 3)
# #a_tuple[3] = 4
# try:
#     a_tuple[3] = 4
# except TypeError:
#     print('tuple is immutable')

# multiple exception
a_tuple = (1, 2, 3)
try:
    a_tuple[3] = 4
except (AttributeError, TypeError, KeyError, IndexError):
    print('something wrong happened')

# use Exception to catch all types of exceptions as Java did
try:
    a_tuple[3] = 4
except Exception:
    print('something wrong happened')

# python collection support different type, no exception and code works
b_list = [1, 2, 3]
b_list.append('a')
print(b_list)