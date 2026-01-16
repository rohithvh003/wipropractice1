numbers = [10,20,30]
for index, value in enumerate(numbers):
    print(index,value)


from enum import Enum

class color(Enum):
    Red =1
    Green = 2
    blue = 3
print(color.Red.value)
print(color.Red.name)