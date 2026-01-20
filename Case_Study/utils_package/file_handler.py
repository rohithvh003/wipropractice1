import json
import csv

from Case_Study.Models import student


def save_students_json(student):
    data = []
    for s in student:
        data.append({
            "id": s.sid,
            "name": s.name,
            "department": s.department,
            "marks": s.marks
        })

    with open("students.json", "w") as file:
        json.dump(student, file, indent=4)


def generate_csv(students):
    with open("students_report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Department", "Average", "Grade"])

        for s in students:
            avg = sum(s.marks) / len(s.marks)
            grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
            writer.writerow([s.sid, s.name, s.department, avg, grade])
