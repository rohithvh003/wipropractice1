
# lambda argu:exps
add = lambda a,b: a+b
print(add(3,5))

# o/p
# 8

multi = lambda a,b: a*b
print(multi(5,6))


maxnum = lambda x,y :x if x>y else y
print(maxnum(10,40))

# map
# syntax : map(function,iterable)
numbers = (1,2,3,4,5)
result = map(lambda x:x*2,numbers)
print(tuple(result))