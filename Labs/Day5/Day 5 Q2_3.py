# 3. Implement operator overloading by overloading the + operator to add two objects of a custom class
class Box:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Box(self.value + other.value)


b1 = Box(10)
b2 = Box(20)

b3 = b1 + b2
print(b3.value)

