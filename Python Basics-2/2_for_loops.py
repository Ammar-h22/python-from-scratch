# 'for loops' allow us to iterate over anything that has a collection of items.

# syntax:
""" for variable in iterable:
        print(variable) or do something else
"""
# An iterable is a collection of items that can be iterated over & over again.
# Iterable can be a - string, list, dictionary, tuple, set.

for item in "I am currently in USA":
    print(item)
for item in [1, 2, 3, 4]:
    print(item)
for item in {1, 2, 3, 4}:
    print(item)
for item in (1, 2, 3, 4):
    print(item)

# But 'int' objects are not iterable means we cannot iterate them, because they
# are not a collection of items.
"""Example:
for item in 50:
    print(item)
"""

# Nested for-loop
for item in (1, 2, 3, 4, 5):
    for x in ["a", "b", "c"]:
        print(item, x)

# Let's iterate dictionary:
user = {"name": "Ammar", "age": 21, "can_swim": True}
for item in user:  # This will return only the keys
    print(item)
for item in user.items():  # This will return both
    print(item)
for item in user.keys():  # This will return keys
    print(item)
for item in user.values():  # This will return values
    print(item)

# We can also do: (If we don't want the items to be printed in tuple format)
for key, value in user.items():
    print(f"{key} : {value}")
    # print(key , ':', value)

# Excercise: (Give the total of all the elements in the array)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0
for item in my_list:
    counter = counter + item
print("The total is", counter)

# _____________________________________________________________________________
# range():
# range() is a special type of object that we can iterate over and which
# is 99% times used in for loops.
# range(start, stop, stepover) , stepover is by default 1

for number in range(1, 10):
    print(number)

# If we don't need any variable:
for _ in range(0, 10):
    print("Hellooo")

for _ in range(0, 10, 2):
    print(_)

for _ in range(10, 0, -1):
    print(_)

for _ in range(2):
    print(list(range(10)))

# _____________________________________________________________________________
# enumerate():
# The enumerate() function adds a counter to an iterable and returns it in the form of
# an enumerating object.

for item in enumerate(["a", "b", "c", "d"]):
    print(item)
for char in enumerate("Helllooo"):
    print(char)

# We can also do unpacking if we don't want the result in tuple format
for i, char in enumerate("India"):
    print(i, char)

# Excercise: (Find out the index of 50 in the list)
for i, item in enumerate(list(range(100))):
    if item == 50:
        print("The index of 50 is:", i)
