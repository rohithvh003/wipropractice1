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


# Employee 1 – valid salary
emp1 = Employee("Akash", 35000)
print(emp1.name, emp1.salary)

# Employee 2 – valid salary
emp2 = Employee("Rohit", 50000)
print(emp2.name, emp2.salary)

# Employee 3 – invalid salary
try:
    emp3 = Employee("Suresh", -10000)
except ValueError as e:
    print("Error for emp3:", e)
