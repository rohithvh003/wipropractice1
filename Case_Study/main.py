from Case_Study.Models.student import Student
from Case_Study.Models.faculty import Faculty
from Case_Study.Models.course import Course
from Case_Study.core.iterators import student_generator
from Case_Study.utils_package.file_handler import save_students_json, generate_csv

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

    try:
        if choice == "1":
            sid = input("ID: ")
            name = input("Name: ")
            dept = input("Department: ")
            sem = int(input("Semester: "))
            marks = list(map(int, input("Enter marks: ").split()))
            students.append(Student(sid, name, dept, sem, marks))
            print("Student Created Successfully")

        elif choice == "2":
            fid = input("Faculty ID: ")
            name = input("Name: ")
            dept = input("Department: ")
            sal = int(input("Salary: "))
            faculty_list.append(Faculty(fid, name, dept, sal))
            print("Faculty Created Successfully")

        elif choice == "3":
            courses.append(Course("CS101", "Python", 4, faculty_list[0]))
            print("Course Added Successfully")

        elif choice == "4":
            avg, grade = students[0].calculate_performance()
            print("Average:", avg)
            print("Grade:", grade)

        elif choice == "5":
            save_students_json(students)
            generate_csv(students)
            for record in student_generator(students):
                print(record)

        elif choice == "6":
            print("Thank you for using Smart University Management System")
            break

    except Exception as e:
        print("Error:", e)
