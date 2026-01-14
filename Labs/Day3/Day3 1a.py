import time

def execution_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution time:", end - start)
    return wrapper


@execution_time
def my_function():
    time.sleep(1)

my_function()
