from Case_Study.Models.person import Person
from Case_Study.core.descriptors import SalaryDescriptor

class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, fid, name, department, salary):
        super().__init__(name, department)
        self.fid = fid
        self.salary = salary

    def get_details(self):
        print("Name:", self.name)
        print("Role: Faculty")
        print("Department:", self.department)
