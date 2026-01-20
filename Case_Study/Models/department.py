class Department:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.faculty = []

    def add_student(self, student):
        self.students.append(student)

    def add_faculty(self, faculty):
        self.faculty.append(faculty)
