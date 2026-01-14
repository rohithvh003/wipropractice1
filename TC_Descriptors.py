# Getting the attribute and setting the attribute
class mydescriptors:
    def __get__(self, obj, owner):
        print("getting value")
        return obj.__x
    def __set__(self, obj, value):
        print("setting the value")
        obj.__x=value

class Test:
    x = mydescriptors
t = Test()
t.x=20
print(t.x)