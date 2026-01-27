from collections.abc import Iterator

# Iterator
# An iterator is an object that gives values one by one using iter() and next().
nums = [1, 2, 3]
it = iter(nums)

print(next(it))
print(next(it))

# Generators
# A generator is a special function that returns values one at a time using yield.

def generator():
    yield 1
    yield 2
    yield 3

g = generator()
print(next(g))
print(next(g))
print(next(g))

# Descriptors
class MyDescriptor:
    def __get__(self, obj, objtype=None):
        return "Hello"

class Test:
    x = MyDescriptor()

t = Test()
print(t.x)
