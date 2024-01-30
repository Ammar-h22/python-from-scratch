import random

# print(random)
# help(random)
# print(dir(random))

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))

import random as ran

my_list = [1, 2, 3, 4, 5]
ran.shuffle(my_list)
print(my_list)
# ______________________________________________________________________

# import sys


# In Python, the sys module is a built-in module that provides access to various
# system-specific parameters and functions. It is a part of the Python Standard
# Library and is commonly used for tasks related to interacting with the Python
# runtime environment and the operating system.

# We have to run this code in terminal by giving the argument in terminal:
# def hello(name):
#     print(f'Hello {name}')
#
#
# hello(sys.argv[1])
# ______________________________________________________________________

# This is a third-party package that we have installed:
import pyjokes

joke = pyjokes.get_joke('en', 'neutral')
print(joke)

# In PyCharm we can directly install any package by going in the python packages section
# or we can also install through terminal using pip command.
# Command:
# pip install package_name
# pip install package_name==version

# ______________________________________________________________________

# Another useful built-in module:
from collections import Counter, defaultdict, OrderedDict

my_string = 'Hello everyone how are you all'
print(Counter(my_string))

my_list = [1, 2, 3, 2, 5, 1, 6]
print(Counter(my_list))


my_dict = defaultdict(lambda: 'Does not exist', {'a':1, 'b':2, 'c':3})
print(my_dict['a']) # 1
print(my_dict['d']) # Does not exist


dict1 = OrderedDict()
dict1['b'] = 2
dict1['c'] = 3

dict2 = OrderedDict()
dict2['c'] = 3
dict2['b'] = 2

print(dict1 == dict2)

# Another useful module:
import datetime

print(datetime.time(3, 47, 2))
print(datetime.date.today())

# Another module:
# We can use the array module when we want to access a massive list, and we don't want
# to use generators, then we can use array module because it is more performant than lists.
from array import array
my_list = [1, 2, 3, 4, 5, 6, 7]
arr = array('i', my_list)
print(arr)
print(arr[1])

