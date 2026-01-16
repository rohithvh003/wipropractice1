from abc import ABC,abstractmethod


class Employee(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def salary(self):
        pass


class manager(Employee):
    def salary(self):
        print(self.name,"salary is 10000")

class manager1(Employee):
    def salary(self):
        print(self.name,"salary is 5000")


m1 = manager("rohith")
m2 = manager1("ravi")
m1.salary()
m2.salary()


