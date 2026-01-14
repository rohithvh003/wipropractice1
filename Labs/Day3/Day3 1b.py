# 2. Prints the function name and execution time

import time

def execution_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(func.__name__, "execution time:", end - start)
    return wrapper


@execution_time
def my_function():
    time.sleep(1)

my_function()
