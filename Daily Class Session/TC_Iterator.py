# it is an a object it allows to acces the data at one time

data = (10,20,30)
it = iter(data)
print(next(it))
print(next(it))


# custom iteration
for x in [10,20,30]:
    print(x)

class count:

    def __init__(self,limit):
        self.limit = limit
        self.current =1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current<=self.limit:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration

obj = count(3)

for num in obj:
    print(num)