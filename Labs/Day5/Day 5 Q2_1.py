# Q2 1.1. Create a class Calculator that demonstrates method overriding


class Calculator:
    def operation(self,a,b):
        print(a+b)

class SimpleCalc(Calculator):
    def operation(self,a,b):
        print(a - b)

c = SimpleCalc()
c.operation(10,3)



