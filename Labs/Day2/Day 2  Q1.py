class Count:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


n = 5
obj = Count(n)

for num in obj:
    print(num)





