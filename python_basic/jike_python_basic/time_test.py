import random
import datetime
import time

print(time.time())
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))


print(datetime.datetime.now())
time_offset = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + time_offset)

someday = datetime.datetime(2018, 10, 27)
time_offset = datetime.timedelta(days=-2, seconds=10)
print(someday + time_offset)


print(random.randint(1, 5))
print(random.choice(['aa', 'bb', 'cc']))
