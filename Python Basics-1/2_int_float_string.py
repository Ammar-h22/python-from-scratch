# 1) Fundamental Data Types
int
float
bool
str
list
tuple
dict
set

# 2) Classes -> custom types

# 3) Specialized Data Types (from different modules).

# 4)
None

# ------------------------------------------------------#

# int and float
print(2 + 2)
print(2 - 2)
print(2 * 2)
print(2 / 2)
print(2**3)  # 2 to the power of 3
print(5 // 4)  # Returns the integer value
print(6 % 4)  # Returns the remainder value

print(type(2 + 2))  # will return the answer in int
print(type(2 + 2.4))  # will return the answer in float
print(type(2.1 + 2.4))  # will return the answer in float

# math functions
print(round(3.8))
print(abs(-20))  # converts the negative number into positive number

# Operator precedence
# 1. ()
# 2. **
# 3. * or /
# 4. + or -

# We know that the data in a computer is stored/represented in a binary format
# So we can check the binary format of any integer value using bin() function:
print(bin(5))  # This will give the binary format
print(int("0b101", 2))  # This will give the integer number

# Strings:
first_name = "Ammar"
last_name = "Husain"
full_name = first_name + " " + last_name
print(full_name)

# String concatenation
print("Ammar" + " Husain")

# Type conversion
a = str(100)
b = int(a)
print(type(b))

# Escape sequence
print('\t Hey, it\'s "kind of " sunny day \n hope you have a great day!')

# Formatted String
name = "Ammar"
age = 21
print(f"Hi {name}, you are {age} years old.")  # This is widely used

print("Hi {}, you are {} years old.".format(name, age))  # This is not widely used

# String indexes:  [start:stop:stepover]
# This is also known as string slicing
selfish = "01234567"
print(selfish[0])
print(selfish[0:5])
print(selfish[1:])
print(selfish[:6])
print(selfish[:])
print(selfish[::1])
print(selfish[::2])
print(selfish[::])
print(selfish[-1])
print(selfish[::-1])  # This operation is very important as it reverses the whole string

# Strings are immutable means we cannot change any part/element
# of the string once they are created, Instead we can create a
# whole new string.

# Functions vs Methods:
# A method is an action or functionality performed on some object (or class).
# A function is an action that can be called independently.

quote = "to be or not to be"
print(len(quote))  # Example len() is a function
# Even print() itself is a function
print(quote.upper())  # Example upper() is a method
print(quote.replace("be", "me"))
# Similarly, .replace(), .find(), .lower() are also some of the methods specially for strings

# Excercise 1:
birth_year = int(input("In which year were you born?\n"))
current_age = 2023 - birth_year
print(f"Your age is {current_age}")

# Excercise 2:
username = input("Enter your username: ")
password = input("Enter your password: ")
password_length = len(password)
hidden_password = "*" * password_length
print(
    f"Hey {username}, your password {hidden_password} is {password_length} characters long"
)
