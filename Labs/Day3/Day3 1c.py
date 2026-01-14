# Apply this decorator to a function that calculates the factorial of a number using recursion
def decorator(func):
    def wrapper(n):
        print("Function is running...")
        return func(n)
    return wrapper


@decorator
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# test
print(factorial(5))
