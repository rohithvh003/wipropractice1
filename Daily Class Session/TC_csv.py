import csv
with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","id","age"])
    writer.writerow(["rohit",1,24])
    writer.writerow(["rajesh",2,25])