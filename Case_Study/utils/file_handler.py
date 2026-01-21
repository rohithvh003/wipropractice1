import json
import csv
import os

def save_students_json(students):
    data = []
    if os.path.exists("students.json"):
        with open("students.json", "r") as f:
            data = json.load(f)
    for s in students:
        data.append({
            "id": s.pid,
            "name": s.name,
            "department": s.department,
            "semester": s.semester,
            "marks": s.marks
        })
    with open("students.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Student data successfully saved to students.json")



def generate_csv(students):
    file_exists = os.path.exists("students.csv")

    with open("students.csv", "a", newline="") as f:
        write = csv.writer(f)

        if not file_exists:
            write.writerow(["ID", "Name", "Department"])
        for s in students:
            write.writerow([s.pid, s.name, s.department])

    print("Student data successfully saved to students.csv")