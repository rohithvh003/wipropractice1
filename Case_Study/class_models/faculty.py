from Case_Study.class_models.person import Person

class Faculty(Person):
    def __init__(self, fid, name, department, salary):
        self.salary = salary
        self.fid = fid
        self.name = name
        self.department = department
