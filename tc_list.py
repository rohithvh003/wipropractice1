numbers = [10,20,30,40,50,60]
names= ["ram", "ravi","rohith"]
print(numbers)
print(numbers[1:3])
print(names)
mixed = [1,"python", 2, "java"]
print(mixed)


for i in numbers:
    print(i)

# find we use in and not in
if 100  in numbers:
    print("found")
else:
    print("not found")

# Nested list
matrix = [[1,2,3,4,5,6], [2,4,6,8]]
print(matrix[1][2])


names.reverse()
print(names)

names.append("satish")
print(names)

names.extend(["pavan","prashanth"])
print(names)

names.remove("ram")
print(names)

names.insert(3, "asha")
print(names)