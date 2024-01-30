# File I/O

# my_file = open('test.txt')
# print(my_file.read())
#
# my_file.seek(0) # This will bring the cursor back to the starting
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())

# my_file.seek(0)
# print(my_file.readline()) # This will read one line at a time
# print(my_file.readline())
# print(my_file.readline())

# print(my_file.readlines())  # This will print all the lines in a list

# my_file.close()

# Now there is a better way to read files in python:

# with open('test.txt') as my_file2:
#     print(my_file2.readlines())
# And by doing this way we don't need to close our file manually, it is done automatically.

# By-default the open() function is set to read mode:

# 1) The read mode is simple, it is just used to read the data in the files
# with open('test.txt', mode = 'r') as my_file3: # To read (Default)
#     print(my_file3.readline())
#     print(my_file3.readlines())
#     print(my_file3.read())

# 2) The write mode overrides the whole file. Also if the specified file is not present then it creates that file
# automatically.
# with open('test.txt', mode='w') as my_file3: # To write
#     text = my_file3.write('I love Europe!')
#     print(text)

# 3) The append mode does not override, it adds the data at the end. Also if the specified file is not present then
# it creates that file automatically, similar to the write mode.
# with open('test.txt', mode='a') as my_file5: # To append
#     text = my_file5.write(' Heeeellllooo')
#     print(text)

# 4) The 'read & write' mode is not used much, it adds the data from the front and overrides the previous data
# with open('test.txt', mode='r+') as my_file4: # To read and write
#     text = my_file4.write('How are you?')
#     print(text)

# We can access the file from anywhere using a proper path:
# with open('Path', 'r') as random_file:
#     print(random_file.readline())

# We should always read files/access files under try-except block:
try:
    with open('sample.txt', 'r') as random_file:
        print(random_file.read())
except FileNotFoundError:
    print('File does not exist!')

