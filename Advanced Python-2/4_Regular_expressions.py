# Regular expressions:
# Regular expressions are very useful for validations
import re

string = 'Search text inside this piece of text please!'

a = re.search('this', string)
print(a)
print(a.start())
print(a.end())
print(a.group())

# Best way is:
pattern = re.compile('text')  # This will also search for the text
# print(pattern.search(string))
# print(pattern.findall(string))
# print(pattern.fullmatch(string))


# Email validation:
pattern2 = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string2 = 'ammar2002@gmail.com'

e = pattern2.search(string2)
print(e)

# ___________________________________________________________________________
# Exercise: Password validation
# Condition:
# 1) Password should be at-least 8 characters long
# 2) It can contain numbers, alphabets and $%@# symbols.
# 3) Last condition is that the password should end with a number

pattern3 = re.compile(r"[A-Za-z0-9$%@#]{8,}\d")
password = 'ammarhusain02'

check = pattern3.search(password)
print(check)
