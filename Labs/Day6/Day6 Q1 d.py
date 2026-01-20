# 4. Prints matched groups using capturing parentheses

import re

text = "Employee ID: EMP_123"

match = re.search(r"(EMP)+_+(\d{3})", text)

if match:
    print("Full match :", match.group(0))
    print("Group 1    :", match.group(1))
    print("Group 2    :", match.group(2))
