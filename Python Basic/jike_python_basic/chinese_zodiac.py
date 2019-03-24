# contain zodiac and get zodiac by input year

chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'

# slice
print(chinese_zodiac[0:4])
print(chinese_zodiac[-1])

# index
year = 2016
year_index = (year - 1984) % 12 if year > 1984 else 12 - (abs(year - 1984) % 12)
print(year_index)

print(chinese_zodiac[year_index])

# contains
print('狗' in chinese_zodiac)
print('猪' not in chinese_zodiac)

# concat and repeat
print('Chinese Zodiac are ' + chinese_zodiac + 's')
print(chinese_zodiac * 3)
