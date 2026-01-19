class Parent:
    def parent(self):
        print("parent1")

class child1(Parent):
    def c1(self):
        print("Child1")

class child2(Parent):
    def c2(self):
        print("Child2")


c1 =child1()
c1.c1()
c1.parent()
c2 = child2()
c2.c2()
c2.parent()
