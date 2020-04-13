# get statistic info by each chinese zodiac and zodiac
chinese_zodiacs = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
zodiac_names = (u'魔蝎座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座', u'处女座', u'天枰座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
use_functional = True

# define and initial dict
cz_num = {k: 0 for k in chinese_zodiacs}
z_num = {k: 0 for k in zodiac_names}

# get use input continuously
total_input = 0
while total_input < 10:
    (input_year, input_month, input_day) = (int(input('birth year')), int(input('birth month')), int(input('birth day')))

    total_input += 1
    cz_index = (input_year - 1984) % 12 if input_year >= 1984 else 12 - (abs(input_year - 1984) % 12)
    # update chinese zodiac num dicts
    cz_num[chinese_zodiacs[cz_index]] += 1

    if use_functional:
        # functional is much more easier and cover all cases with edge cases include
        zodiac_index = len(list(filter(lambda x: x < (input_month, input_day), zodiac_days))) % 12
        z_num[zodiac_names[zodiac_index]] += 1
    else:
        # use while or lambda to get zodiac and chinese zodiac
        i = 0
        # edge cases, data is more than Dec 23
        while zodiac_days[i] < (input_month, input_day):
            i += 1
        if zodiac_days[-1] < (input_month, input_day):
            z_num[zodiac_names[0]] += 1
        else:
            # update zodiac num dicts
            z_num[zodiac_names[i]] += 1

    # display output
    for each_key in cz_num.keys():
        print('生肖%s有%i个'%(each_key, cz_num[each_key]))

    for each_key in z_num.keys():
        print('星座%s有%i个'%(each_key, z_num[each_key]))