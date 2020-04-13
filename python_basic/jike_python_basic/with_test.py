class TestWith():
    def __enter__(self):
        print('Task is ready to run')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('Task has been finished completely')
        else:
            print('The error is %s' % exc_tb)


with TestWith():
    print("Task is executing")


with TestWith():
    print("Task is executing with high risk")
    raise NameError
