student = {"name": "Rahul",
           "age": 25,
           "course":"Python"}
print(student)
# Access
print(student["name"])
print(student.get("age"))

# add into the dictionary
student["marks"]= 86
student["age"] = 25
print(student.pop("age"))
print(student)
student.popitem()
print(student)



# to print the keys and values
print(student.keys())
print(student.values())

for key in student:
    print(key,student[key])

if "name" in student:
    print("key exists")

employees = {
    101:{"name":"rohith","salary":20000},
    102:{"name":"rocky","salary":21000}
}

print(employees)
print(employees [101]["name"])
