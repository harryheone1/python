import time
from threading import current_thread
import threading


class MyTask(threading.Thread):
    def run(self):
        print(current_thread().getName(), 'start')
        time.sleep(2)
        print(current_thread().getName(), 'stop')


# After join method is called, current MainThread will wait for task1
# If there is no join, MainThread will finish first
task1 = MyTask()
task1.start()
task1.join()

print(current_thread().getName(), 'end')

# If there is no join, MainThread will continue for loop and launch all threads then go to last print
# After MainThread finish, each sub thread could reach the part after sleeping
for i in range(0, 5, 1):
    print('Main Thread reach to %s' % i)
    task = MyTask()
    task.start()
    #task.join()

print(current_thread().getName(), 'end')
