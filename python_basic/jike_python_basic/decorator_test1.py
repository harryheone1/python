import time

# def i_can_sleep():
#     time.sleep(3)
#
# # without decorator, each time before and after the function there all repeated code
# start_time = time.time()
# i_can_sleep()
# stop_time = time.time()
# print(stop_time - start_time)

# 1st way: easiest but need to re-write lambda each time
def timer(func):
   start_time = time.time()
   func()
   stop_time = time.time()
   print(stop_time - start_time)


timer(lambda: time.sleep(1))


# 2nd way: use function to manage each lambda
def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print(stop_time - start_time)
    return wrapper


sleep_func = timer(lambda: time.sleep(1))
sleep_func()


# 3rd way: use decorator as candy
@timer
def i_can_sleep():
    time.sleep(1)


i_can_sleep()
