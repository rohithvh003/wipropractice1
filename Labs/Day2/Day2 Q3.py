from collections.abc import Iterator
from email.generator import Generator

# Q3. Demonstrate the difference between using the iterator and generator by printing values using a for loop
# Iterator

class Iterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

obj = Iterator
for num in obj(5):
    print(num)



# Generator
def number_gen(n):
    for i in range(1, n + 1):
        yield i

obj = number_gen
for i in obj(5):
    print(i)
