# create a pattern for entire or partial string match
# create a pattern for pattern as cat, caaaat, caaat, etc

import re

# entire match
pattern_exact = re.compile('cat')
print(pattern_exact.match('cat'))

# partial match
pattern_partial = re.compile('ca')
print(pattern_partial.match('cat'))

# partial match
pattern_all = re.compile('ca*t')
print(pattern_all.match('ct'))
print(pattern_all.match('cat'))
print(pattern_all.match('caaat'))
print(pattern_all.match('caaaaaat'))


# 3 any characters
pattern_three = re.compile('.{3}')
print(pattern_three.match('cat'))
print(pattern_three.match('dog'))
print(pattern_three.match('abcd'))
print(pattern_three.match('ab'))

# difference between search and match
pattern_date = re.compile(r'(\d{4})-(\d{2})-(\d{2})')
print(pattern_date.match('2020-04-14'))
print(pattern_date.match('dd2020-04-14'))
print(pattern_date.search('dd2020-04-14'))
print(pattern_date.findall('2020-04-14'))
year, month, day = pattern_date.findall('2020-04-14')[0]
print(year, month, day)

print(re.search(r'\W+', 'Words, words, words.'))
print(re.findall(r'\W+', 'Words, words, words.'))
print(re.split(r'\W+', 'Words, words, words.'))
print(re.split(r'\W+', 'Words, words, words.', 1))

# remove all other word than telephone number
telephone_no = 'My telephone number is: 581-777-0269'
print(re.sub(r'\D', '', telephone_no))




