class Box:
    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        return Box(self.value+other.value)


b1 = Box(50)
b2 = Box(20)
b3 = Box(30)

result = b1+b2+b3
print(result.value)
