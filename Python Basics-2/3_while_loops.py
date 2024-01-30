# while loops:

i = 0
while i < 10:
    print(i)
    i += 1

# We can also put an else statement after the while loop
while i < 10:
    print(i)
    i += 1
else:
    print("Done with all the work!")
# The else part will be executed when the while loop becomes false or its finish being executed,
# but if there is a break statement inside while block then the else part will not be executed.

my_list = [11, 12, 13]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

while True:
    response = input("Say something: ")
    if response == "bye":
        break
print("Good Bye!")

j = 0
while j < 10:
    j += 1
    if j == 6:
        continue
    print(j)

# Excercise:
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

for row in picture:
    for pixel in row:
        if pixel == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print("")  # Because we need a new line for each row

# Excercise:
# Check for duplicates in list
some_list = ["a", "b", "c", "b", "d", "n", "m", "n", "c"]

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)
