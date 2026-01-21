import json
import csv

def save_students_json(students):
    try:
        data = []
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

        print("students data successfully saved to student.json")

    except Exception:
        print("Error: FIle not found")


def generate_csv(students):
    with open("students.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department"])
        for s in students:
            writer.writerow([s.pid, s.name, s.department])
