# 2. Uses re.search() to find the first occurrence of a valid email address in a given text
import re
text = "please do contact abc1234@gmail.com for more information"

result = re.search(r"[a-zA-Z0-9.%]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}",text)

if result:
    print("Email Found:",result.group())
else:
    print("Email not found")