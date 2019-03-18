# contain zodiac and get zodiac by input year
#
# chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
#
# # index
# year = int(input("Please enter birth year"))
# y_distance = (year - 1984) % 12 if year > 1984 else 12 - (abs(year - 1984) % 12)
# print(y_distance)
#
# if chinese_zodiac[y_distance] == '狗':
#     print('狗年的运势越来越好')
# else:
#     print('无法预测')
#
# for cz in chinese_zodiac:
#     print(cz)
#
# for i in range(13):
#     print(i)
#
# for year in range(2000, 2019):
#     chinese_zodiac_index = (year - 1984) % 12 if year > 1984 else 12 - (abs(year - 1984) % 12)
#     print('%s 年的生肖是 %s' %(year, chinese_zodiac[chinese_zodiac_index]))
import time

num = 5
while True:
    print('a')
    num = num + 1
    if num > 10:
        break

num = 5
while num < 10:
    print('b')
    num = num + 1

num = 5
while True:
    num = num + 1
    if num == 10:
        continue
    print(num)
    time.sleep(1)

