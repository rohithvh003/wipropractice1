import os
import csv


def read_csv_data(file_path):
    # Get project root directory
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Create full absolute path
    full_path = os.path.join(project_root, file_path)

    print("Reading file from:", full_path)  # Debug line

    with open(full_path, newline='', encoding="utf-8") as csvfile:
        return list(csv.DictReader(csvfile))