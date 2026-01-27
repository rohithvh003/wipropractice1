from Case_Study.core.iterators import faculty_generator
from class_models.student import Student
from class_models.faculty import Faculty
from class_models.course import Course
from core.iterators import student_generator
from utils.file_handler import save_students_json, generate_csv

students = []
faculty_list = []
courses = []

while True:
    print("\n1 Add Student")
    print("2 Add Faculty")
    print("3 Add Course")
    print("4 Calculate Performance")
    print("5 Generate Reports")
    print("6 Exit")

    choice = input("Enter choice: ")

# Add the Student
    if choice == "1":
        sid = input("ID: ")
        duplicate = False
        for s in students:
            if s.pid == sid:
                duplicate = True
                break
        if duplicate:
            print("Error: student ID already exists")

        name = input("Name: ")
        dept = input("Department: ")
        sem = int(input("Semester: "))
        marks = list(map(int, input("Enter marks: ").split()))

        students.append(Student(sid, name, dept, sem, marks))
        print("Student Created Successfully")

# add faculty
    elif choice == "2":
        fid = input("Faculty ID: ")
        name = input("Name: ")
        dept = input("Department: ")
        sal = int(input("Salary: "))

        faculty_list.append(Faculty(fid, name, dept, sal))
        print("Faculty Created Successfully")

# add course
    elif choice == "3":
        if faculty_list:
            code = input("Course Code: ")
            name = input("Course Name: ")
            credits = int(input("Credits: "))

            courses.append(Course(code, name, credits, faculty_list[0]))
            print("Course Added Successfully")
        else:
            print("Add Faculty First")

    #         performance calculate
    elif choice == "4":
        if students:
            avg, grade = students[0].calculate_performance()
            print("Student Performance Report")
            print("--------------------------------")
            print(f"Name    : {students[0].name}")
            print(f"Average : {avg}")
            print(f"Grade   : {grade}")
        else:
            print("No students available")

# generate reports
    elif choice == "5":

        # student report
        print("\nSTUDENT DETAILS")
        print("--------------------------------")
        for s in students:
            print(f"ID        : {s.pid}")
            print(f"Name      : {s.name}")
            print(f"Department: {s.department}")
            print(f"Semester  : {s.semester}")
            print("--------------------------------")

# faculty report
        print("\nFACULTY DETAILS")
        print("--------------------------------")
        for f in faculty_list:
            print(f"ID        : {f.fid}")
            print(f"Name      : {f.name}")
            print(f"Department: {f.department}")
            print("--------------------------------")

# course report
        print("\nCOURSE DETAILS")
        print("--------------------------------")
        for c in courses:
            print(f"Course Code : {c.code}")
            print(f"Course Name : {c.name}")
            print(f"Credits     : {c.credits}")
            print(f"Faculty     : {c.faculty.name}")
            print("--------------------------------")

# file output
        save_students_json(students)
        generate_csv(students)

# generator output
        print("\nStudent Records Generator")
        for rec in student_generator(students):
            print("Fetching Student Records...")
            print("-"*28)
            print(rec)

        print("\nFaculty Records Generator")
        for rec1 in faculty_generator(faculty_list):
            print("fetching faculty records...")
            print("---------------------------")
            print(rec1)

    # exit
    elif choice == "6":
        print("Thank you for using Smart University Management System")
        break
