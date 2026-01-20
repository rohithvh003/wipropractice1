from Case_Study.Models.person import Person
from Case_Study.core.descriptors import MarksDescriptor

class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, sid, name, department, semester, marks):
        super().__init__(name, department)
        self.sid = sid
        self.semester = semester
        self.marks = marks

    def __del__(self):
        print("Student object deleted")

    def get_details(self):
        print("Name:", self.name)
        print("Role: Student")
        print("Department:", self.department)

    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
        return avg, grade

    def __gt__(self, other):
        return sum(self.marks) > sum(other.marks)
