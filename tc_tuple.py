# Tuples are immutable and enclosed within paranthesis and without paranthesis
# tuples allows duplicate values
t1 = (10,20,30,40,50)
t2 = "apple","orange","cheery"
print(t1)
print(t2)
print(t1[0])
print(t2[2])
print(t1[1:3])
print(t1[3:])

# Methods are 1.count, index
# count is a used to tell how many times it is repeated
print(t2.count(2))
print(t1.count(20))
print(t1.index(40))

# reverse 0r swaping
a =5
b = 10
a,b =b,a
print(a,b)


# packing and unpacking
data = 10,20,30
a,b,c = data
print(a,b,c)

print(t1[2:5])
print(t1[1:5])
