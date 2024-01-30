"""'
Functional Programming:
1) Functional programming is a way of writing computer programs by focusing on
using functions to perform tasks.
2) In functional programming, we avoid changing-state and mutable data.

Pure functions:
A Pure function has two fundamental properties:

1) Deterministic:
A pure function always produces the same output for the same set of input parameters.

2) No Side Effects:
A pure function does not have any side effects, meaning it doesn't modify any data
outside of its own scope or have any observable interactions with the external world,
such as writing to files, making network requests, or changing global variables.
It only relies on its input parameters to compute the output.
"""


# Example of a Pure Function:
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiply_by2([1, 2, 3]))
# _____________________________________________________________________________________

# There are 4 very important functions that are very useful in functional/python programming:
# map(), filter(), zip() and reduce()
# One very important point to note is that all these functions do not change/modify the original iterables, they generate a new iterable.

# 1) map(): [map(function, iterable)]
# The map() function is used for applying a given function to all elements/items in the iterable (like list, tuple etc)
# and returns back a new iterable as a result.

# The map() function takes two arguments:
# i. A function that defines the transformation you want to apply to each element in the iterable.
# ii. An iterable (e.g. a list) that contains the elements you want to transform.


# Example, see how map() function simplifies the above multiply_by2 function
my_list = [1, 2, 3, 4]


def multiple_by2(item):
    return item * 2


print(list(map(multiple_by2, my_list)))


# Another Example:
def square(x):
    return x * x


print(list(map(square, my_list)))
# _____________________________________________________________________________________

# 2) filter(): [filter(function, iterable)]
# The filter() function is used for filtering elements from an iterable (list, tuple, etc)
# based on a specified condition. It returns a new iterable containing only the elements that satisfy
# the given condition.

# The filter() function takes two arguments:
# i. A function that defines the filtering condition.
# ii. An iterable (e.g. a list) that contains the elements you want to filter.


# Example:
my_list = [1, 2, 3, 4]


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))
# _____________________________________________________________________________________

# 3) zip(): [zip(iterable1, iterable2, ...)]
# The zip() function is used to combine multiple iterables (lists, tuples, etc) element-wise into a
# single iterable. It pairs up corresponding elements from each input iterable, creating tuples
# for each set of elements.

# Example:
my_list = [1, 2, 3]
your_list = [10, 20, 30]

print(list(zip(my_list, your_list)))

# Another example:
names = ["Ammar", "Lubaina", "Mufaddal", "Ali"]
ages = [21, 25, 17, 13]
print(list(zip(names, ages)))
# _____________________________________________________________________________________

# 4) reduce(): [reduce(function, iterable, [initializer])]
# The reduce() function is used for performing a cumulative computation on a list of values.
# It continually applies a given function to the elements of an iterable, reducing them to a
# single accumulated value.
# Example:
from functools import reduce

my_list = [1, 2, 3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))

# Another example:
numbers = [1, 2, 3, 4, 5]


def multiply(x, y):
    print(x, y)
    return x * y


print(reduce(multiply, numbers))
# _____________________________________________________________________________________

# Excercise:
# 1) Capitalize all of the pet names and print the new list.
pet_list = ["timmy", "jimmy", "fufy", "sufy"]


def capital_name(item):
    return item.capitalize()


print(list(map(capital_name, pet_list)))

# 2) Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
list1 = ["a", "b", "c", "d", "e"]
list2 = [1, 5, 4, 2, 3]
list2.sort()
print(list(zip(list1, list2)))

# 3) Filter the scores that pass over 50%
student_marks = [76, 54, 43, 31, 58, 30, 89]


def passing_score(item):
    return item > 50


print(list(filter(passing_score, student_marks)))

# 4) Combine all the numbers that are in the list 'li1' and 'li2' using reduce.
#    What is the total?

li1 = [1, 5, 4, 2, 3]
li2 = [76, 54, 43, 31, 58, 30, 89]


def total_num(acc, item):
    return acc + item


print(reduce(total_num, (li1 + li2)))
# _____________________________________________________________________________________

# Lambda Expressions: [lambda parameter: action(parameter)]
# Lambda expressions are one-time anonymous functions

scores = [1, 2, 3, 4]
print(list(map(lambda item: item * item, scores)))

print(list(filter(lambda item: item % 2 == 0, scores)))

print(reduce(lambda acc, item: acc + item, scores))

# Excercise:
# 1) Find the square root of all the items in the scores list
import math

print(list(map(lambda item: math.sqrt(item), scores)))

# 2) We have to Sort this list which have tuples as items inside list and
# we need to sort based on the second value of the tuple.
a = [(0, 2), (4, 3), (10, -1), (9, 9)]
a.sort(key=lambda x: x[1])
print(a)

# Another example of sorting based on some different value:
students = [
    {"name": "Lubaina", "age": 25},
    {"name": "Ammar", "age": 21},
    {"name": "Mufaddal", "age": 17},
]
students.sort(key=lambda x: x["age"])
print(students)
# _____________________________________________________________________________________

# List/Set/Dictionary Comprehensions:
# 1) List comprehension:
# [variable for variable in iterable] or sometimes [expression for variable in iterable] or
# sometimes [variable/expression for variable in iterable condition]


my_list = []
for char in "Hello":
    my_list.append(char)
print(my_list)

# So instead of this we can use list comprehension:
my_list1 = [char for char in "Hello"]
# print(my_list)

my_list2 = [num for num in range(0, 100)]
# print(my_list2)

my_list3 = [num ** 2 for num in range(0, 100)]
# print(my_list3)

my_list4 = [num ** 2 for num in range(0, 100) if num % 2 != 0]
print(my_list4)

# 2) Set Comprehension: (It is exactly same as list comprehension)
my_set = {char for char in "hello"}
print(my_set)
my_set2 = {num * 2 for num in range(0, 10)}
print(my_set2)

# Dictionary Comprehension:
simple_dict = {"a": 1, "b": 2}
my_dict = {key: value ** 2 for key, value in simple_dict.items()}
print(my_dict)

my_dict2 = {k: v ** 2 for k, v in simple_dict.items() if v % 2 == 0}
print(my_dict2)

my_dict3 = {k: v * 2 for k, v in {"a": 1, "b": 2}.items()}
print(my_dict3)

my_dict4 = {num: num * 2 for num in [1, 2, 3]}
print(my_dict4)

# _____________________________________________________________________________________

# Excercise: Implement the below code using comprehension technique:
some_list = ["a", "b", "e", "n", "b", "d", "n"]

duplicate_list = []
for item in some_list:
    if some_list.count(item) > 1:
        if item not in duplicate_list:
            duplicate_list.append(item)
print(duplicate_list)

# Solution:
duplicate_list = list(set([item for item in some_list if some_list.count(item) > 1]))
print(duplicate_list)
