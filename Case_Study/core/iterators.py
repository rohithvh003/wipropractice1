def student_generator(students):
    for student in students:
        yield f"{student.sid} - {student.name}"
