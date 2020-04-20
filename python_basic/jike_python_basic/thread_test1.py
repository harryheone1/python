# Define a task with a function and run it with single thread
# Run it with multi-thread

import time
from threading import current_thread
import threading


def my_task(arg1, arg2):
    print(current_thread().getName(), 'start')
    print('%s %s' % (arg1, arg2))
    time.sleep(2)
    print(current_thread().getName(), 'stop')

# This run should always print the same thread name of main thread and very slow of 10 seconds
# for i in range(0, 5, 1):
#     my_task(i, i + 1)


# This run should always pring the different thread name and quickly
for i in range(0, 5, 1):
    task = threading.Thread(target=my_task, args=(i, i + 1))
    task.start()

print(current_thread().getName(), 'end')

