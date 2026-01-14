# 2. Create a generator function that yields the first N Fibonacci numbers

def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        yield x
        x, y = y, x + y

gen = fibonacci(7)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))