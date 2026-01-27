# range function
# we can print the range function from start to end point

for i in range(0,10):
    print(i)

# enumarate
# it is used to get the both index and values
fruits = ["apple", "banana", "mango","pineapple"]


# output will in tuples
for i in enumerate(fruits):
    print(i)

for index,value in enumerate(fruits):
    print(index,value)


# 3.iter() is used to get an iterator object from an iterable (like list, tuple, string).

nums = [10, 20, 30]
it = iter(nums)

print(next(it))
print(next(it))


# lambda it creates a one line function without using def
add = lambda a, b: a + b
print(add(2, 3))

sub = lambda a,b :a-b
print(sub(10,7))

