# 3. Uses regular expression modifiers such as:
# re.IGNORECASE
# re.MULTILINE
# re.DOTALL

import re

# re.IGNORECASE
text = "python is Powerful"

print(re.findall("powerful", text, re.I ))


# re.MULTILINE
text = "one\ntwo\nthree\nthirty"
print(re.findall(r"^t\w+",text, re.MULTILINE))

# re.DOTALL
text = "Hello\nGoodMorning"

m =re.search("Hello.*GoodMorning", text,re.DOTALL)
print(m.group())