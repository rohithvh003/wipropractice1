# 4. Demonstrates how modifiers affect pattern matching with examples

import re
# without any modifiers
text = "Hello\nhello\nHELLO"
print(re.findall("hello",text))

# using Modifiers
# 1.re.IGNORECASE or re.I
print(re.findall("hello",text,re.IGNORECASE))

# 2. re.Multiline or re.m
print(re.findall("^hello",text,re.M))

text1 = "Hello\nworld"

m =re.search("Hello.*world", text1,re.DOTALL)
print(m.group())