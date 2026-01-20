class Person:
    def __init__(self, pid, name, department):
        self.pid = pid
        self.name = name
        self.department = department

    def get_details(self):
        return f"ID: {self.pid}, Name: {self.name}, Dept: {self.department}"
