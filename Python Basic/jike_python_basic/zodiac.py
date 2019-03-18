#
zodiac_name = (u'魔蝎座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座', u'处女座', u'天枰座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

(month, day) = (int(input('birth month')) , int(input('birth day')))
zodiac_len = len(list(filter(lambda x: x <= (month, day), zodiac_days)))
print(zodiac_name[zodiac_len])


# Exercise for list
a_list = ['abc', 'xyz']
a_list.append('X')
print(a_list)
a_list.remove('xyz')
print(a_list)