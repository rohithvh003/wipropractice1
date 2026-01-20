# 3. Demonstrates the use of meta-characters (., *, +, ?) and special sequences (\d, \w, \s) in the patterns
import re

import re

text = "Hello A1 45"

# .  == matches any single character
print(re.findall(r"H.", text))

# *  == zero or more occurrences
m=re.findall(r"\d*", text)
print(m)

# +  == one or more occurrences
print(re.findall(r"\d+", text))

# ?  → zero or one occurrence
print(re.findall(r"A?", text))

# \d → matches digits
print(re.findall(r"\d", text))

# \w → matches letters, digits, underscore
print(re.findall(r"\w", text))

# \s → matches whitespace
print(re.findall(r"\s", text))
