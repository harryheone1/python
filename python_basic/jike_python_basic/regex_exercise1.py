import re

# Write a Python program to check that a string contains only a certain
# set of characters (in this case a-z, A-Z and 0-9).
postal_code1 = 'J4Z1E3'
postal_code2 = 'J4Z 1E3'
error1 = 'jza135'
error2 = 'abcd1'
error3 = '12345'
error4 = 'J4Z     1E3'
pattern = re.compile(r'\w\d\w ?\d\w\d')
print(pattern.search(postal_code1))
print(pattern.search(postal_code2))
print(pattern.search(error1))
print(pattern.search(error2))
print(pattern.search(error3))
print(pattern.search(error4))

# Write a Python program that matches a string that has an a followed by zero or more b's.
correct1 = 'abc0'
correct2 = '123b'
error1 = '123'
error2 = 'b'
error3 = '0'
error4 = 'harry'
pattern = re.compile(r'.+[0b]')
print(pattern.search(correct1))
print(pattern.search(correct2))
print(pattern.search(error1))
print(pattern.search(error2))
print(pattern.search(error3))
print(pattern.search(error4))
