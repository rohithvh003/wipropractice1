# 1. Validates a strong password using regular expressions with
# the following rules: Minimum 8 characters At least one uppercase letter At least one lowercase letter At least one digit At least one special character

import re

password = "Rohithvh@09"

if re.search(r"^[A-Z]+[a-z]+(?=.*\d)(?=.*[!@#$%^&*]).{8,}$",password):
    print("strong Password")
else:
    print("weak password")