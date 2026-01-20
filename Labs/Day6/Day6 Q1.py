# 1. Uses re.match() to check whether a string starts with a valid employee ID in the format EMP followed by 3 digits (e.g., EMP123)
import re

emp_id = "EMP123"
if re.match(r"EMP\d{3}",emp_id):

    print("match found")
else:
    print("match not found")


text = "Please do contact us at abc123@gmail.com for more information"
result = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

if result:
    print("Email found:", result.group())
else:
    print("No email found")