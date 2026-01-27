# 1.List

# A list is used to store multiple values in one variable.
# It is ordered and changeable, so we can modify items anytime.

list = [1,2,3,4,5,6,7,8]

print(list)

#     methods are
# 1.append - can add the data at the last
list.append(9)
print(list)

print(list.pop())

list.insert(2,3)
print(list)

print(list.count(3))


# Dictionary
# it has key and value where key are fixed and values can be change
# it is represnted as {}

dict = {}
print(type(dict))

student = {"name": "Akash", "age": 21}
print(student["name"])
print(student.get("age"))   #get method
print(student.keys())     #key_method
print(student.values())    #value_method
# update method
student.update({"age": 22})
print(student)
# pop method
student.pop("age")
print(student)


# SET
# A set is used to store multiple unique values.
# It does not allow duplicate elements and is unordered.


nums = {1, 2, 2, 3}
print(nums)
nums.add(4)
print(nums)
# remove

nums.remove(2)
print(nums)

a = {1, 2}
b = {3, 4}
print(a.union(b))


