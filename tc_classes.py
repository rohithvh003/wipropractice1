class student:
    name = "rohit"
    age = "100"

s1=student()
print(s1.name)
print(s1.age)

# constructor
class employee:
    def __init__(self,name,age):       #Constructor
        self.name = name
        self.age = age

e1 = employee("rohit", 30)
print(e1.name,e1.age)

# EXAMPL FOR CONSTRUCTOR
class car:
    def __init__(self,module,color):
        self.module = module
        self.color = color

c1 = car("BMW","Black")
print(c1.module,c1.color)