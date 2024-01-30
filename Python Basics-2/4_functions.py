# functions


def say_hello():
    print("Helloo!")


say_hello()
say_hello()
print(say_hello)  # This will give the location of that function


# parameters vs arguments:
# parameters: parameters are the name of the variables that we use while creating the function.
# arguments: arguments are the actual values that we provide to the function.
# Parameters are used when we define the function and arguments are used when we call/invoke the function.


def greet(name, emoji):  # These are parameters
    print(f"Hey {name}, what's up?{emoji}")


greet("Ammar", "😊")  # These are arguments

# Positional arguments: (These are the best practice to follow)
greet("Lubaina", "😊")

# Keyword arguments:
greet(name="Lubaina", emoji="😊")


# Default parameters:
def greet2(name="Gentlemen", emoji="😊"):
    print(f"Hey {name}, what's up?{emoji}")


greet2()
greet2("Ali")


# _______________________________________________________________________________________
# return keyword:
# The return keyword returns the desired output and automatically exits from the function.
def add(num1, num2):
    return num1 + num2


print(add(10, 12))
# or
result = add(5, 4)
print(result)
print(add(10, result))
print(add(10, add(10, 15)))


# Exercise: (check the number is even or odd)
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False
# But we can also do it in a short way:
def is_even(num):
    return num % 2 == 0


print(is_even(51))


# _____________________________________________________________________________________
# nested functions
def func(num1, num2):
    def another_func(n1, n2):
        return n1 + n2

    return another_func(num1, num2)


result = func(2, 3)
print(result)


# Excercise:
def checkDriverAge(age=0):
    if age < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif age > 18:
        print("Powering On. Enjoy the ride!")
    elif age == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


checkDriverAge(16)


# or


# def checkDriverAge2():
#     age = int(input("Enter your age: "))
#     if age < 18:
#         print("Sorry, you are too young to drive this car. Powering off")
#     elif age > 18:
#         print("Powering On. Enjoy the ride!")
#     elif age == 18:
#         print("Congratulations on your first year of driving. Enjoy the ride!")
#
#
# checkDriverAge2()


# Exercise: Adding all the elements in the array
def summation(num):
    return sum(num)


print(summation([1, 2, 3, 4]))

# _____________________________________________________________________________________
"""
Functions vs Methods:
A function is an action that can be called independently.
A method is an action or functionality performed on some object (or class).
In Python, a function is defined using "def" keyword and methods use "@".
Methods belong to classes while functions do not have any special relationship with them.

Functions are:
list()
print()
input()
max()
min()

def some_random_stuff():
    pass
    
Methods are:
'Helllooo'.capitalize()
.clear()
.pop()
.lower()
.replace()
etc...
"""


# _____________________________________________________________________________________

# DocStrings in Python:
# DocString is used to document a particular segment of code.

# def test1(a):
#     """
#     Info: this function tests and prints the parameter a
#     """
#     print(a)
#
#
# test1("Hiii")

# We can use the below two operations to see what a function does:
# help(test)
# print(test.__doc__)



# _____________________________________________________________________________________

# Special characters: *args and **kwargs
# With the help of *args parameter we can pass n number of positional arguments.
# With the help of **kwargs parameter we can pass n number of keyword arguments.


def super_func(*args):
    print(args)  # It represents in tuple format
    return sum(args)


print(super_func(1, 2, 3, 4, 5, 6))


def super_func2(**kwargs):
    print(kwargs)  # It represents in dictionary format
    return sum(kwargs.values())


print(super_func2(num1=10, num2=5, num3=10))


# We will never define all the different types of parameters at one time in a function, but just
# for knowledge the correct sequence for writing them is:
# --> normal parameters, *args, default parameters, **kwargs
# _____________________________________________________________________________________


# Excercise: (Find the highest even number from the list)
def highest_even(li):
    even_list = []

    for item in li:
        if item % 2 == 0:
            even_list.append(item)

    return max(even_list)


print(highest_even([2, 5, 10, 8, 9, 11, 21, 34, 27]))
# _____________________________________________________________________________________

# Walrus operator (:=)
# This is a new concept of Python 3.8
a = "Heellllooooooo"
if len(a) > 10:
    print(f"Too long, there are {len(a)} elements")

# As we can see that we need len(a) two times in the above code, so to avoid the repitition
# of such calculations/expressions we can assign that calculation to a variable inside
# the condition statement itself using walrus operator(:=).
# Example:
if (n := len(a)) > 10:
    print(f"Too long, there are {n} elements")
# So we can see that we have assigned a variable 'n' to the expression len(a) within
# the if-statement using walrus operator.
# We cannot do such thing with a normal variable assignment.

# _____________________________________________________________________________________
# Scope - What variables do I have access to?

a = 1  # Global variable


def confusion():
    a = 5  # Local variable
    return a


print(a)  # This will print 1
print(confusion())  # This will print 5

# How Scope Rule works:
# 1) Check with local scope
# 2) Check with Parent local scope
# 3) Check Global scope
# 4) Check built-in python functions

# Example:
a = 10  # This is gloabl variable


def parent_func():
    a = 10  # This is parent local variable

    def child_func():
        a = 10  # This is local variable
        return a

    return child_func()


print(parent_func())

# _____________________________________________________________________________________
# global keyword:
x = 10


def sample():
    global x  # In order to access the global variable x
    x += 1
    return x


print(sample())

# But instead of doing this way we can directly give the variable name in the parameter:
x = 10


def sample(x):
    x += 1
    return x


print(sample(x))


# _____________________________________________________________________________________
# nonlocal keyword:


def outer():
    x = "local"

    def inner():
        nonlocal x  # This is used to access & modify the variable x from the outer() function
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
