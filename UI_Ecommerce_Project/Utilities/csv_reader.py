import csv
import os


def get_users_from_csv():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "../data/user_data.csv"
    )

    users = []

    # ✅ IMPORTANT: use utf-8-sig
    with open(file_path, newline="", encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users.append(row)

    return users