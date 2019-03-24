import time

# def i_can_sleep():
#     time.sleep(3)
#
# # without decorator, each time before and after the function there all repeated code
# start_time = time.time()
# i_can_sleep()
# stop_time = time.time()
# print(stop_time - start_time)


def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print(stop_time - start_time)
    return wrapper


@timer
def i_can_sleep():
    time.sleep(1)


i_can_sleep()
