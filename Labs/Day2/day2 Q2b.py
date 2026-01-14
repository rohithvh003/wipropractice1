class SalaryDescriptor:
    def __get__(self, obj, owner):
        return obj._salary

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("Salary must be a positive number")
        obj._salary = value


class Employee:
    salary = SalaryDescriptor()

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


e1 = Employee("Akash", 40000)
print(e1.salary)

e2 = Employee("Rohit", -5000) # Raises ValueError
