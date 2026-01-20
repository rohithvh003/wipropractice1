import re

password = input()

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$"

if re.match(pattern, password):
    print("Strong password")
else:
    print("Weak password")
