from Case_Study.class_models.person import Person

class Student(Person):
    def __init__(self, sid, name, department, semester, marks):
        self.pid = sid
        self.semester = semester
        self.marks = marks
        self.name = name
        self.department = department

    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        if avg >= 85:
            grade = "A"
        elif avg >= 70:
            grade = "B"
        else:
            grade = "C"
        return avg, grade
