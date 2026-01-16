# 3. Create at least two objects of the class and display their details

class student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_details(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)

s1 = student("Rohith", 46)
s2 = student("Ravi", 24)

s1.display_details()
s2.display_details()

