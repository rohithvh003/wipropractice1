# sets are like list but contains only unique values

myset = {1,2,3,4,5,6,7,6,8}
print(myset)

# access the set
for i in myset:
    print(i)

myset.add(100)
print(myset)



A ={1,2,3}
B = {3,4,5}
print(A|B)  #union
print(A&B) # intersection
print(2 in A)
print(5 in B)
a=b=c=10,2,"rahul"
print(b)
print(c)