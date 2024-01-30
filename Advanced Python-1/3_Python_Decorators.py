# Decorators:

# In Python, decorators are a powerful and flexible way to modify or
# enhance the behavior of functions or methods without changing their actual code.
# By adding some sort of decorator we can supercharge our function and
# and add extra functionality.

# Before understanding decorators we need to understand two things:

# 1) Functions as First-Class Objects/citizens: (Functions act similar as variables)
# In Python, functions are first-class objects, which means they can be assigned to variables,
# passed as arguments to other functions, and returned from functions.
# This property allows us to treat functions as data.

# 2) Nested Functions: Python allows you to define functions inside other functions.
# These inner functions are often referred to as "nested functions" or "inner functions."


# Example:
def hello():
    return "Hello"


greet = hello()
print(greet)

greet = hello
print(greet())

greet = hello()
del hello
print(greet)


# Example:
def hello(func):
    func()


def greeting():
    print("Good morning!")


a = hello(greeting)
print(a)


# Higher Order Functions (HOF):
# A higher order function is a function that either accepts a function as a parameter or returns a function.
# Example:
def greet1(func):
    func()


def greet2():
    def func2():
        return 5

    return func2()


# map(), filter(), reduce() are some of the examples of higher order function, because all take function as an argument.
# _____________________________________________________________________________________

# Now, Let's make our own decorator:
"""
Format of Decorator:
def decorator_name(func):
    def wrapper():
        Something is happening before the function is called
        func()
        Something is happening after the function is called
    return wrapper
"""


def my_decorator(func):
    def wrapper_func(*args, **kwargs):
        print("**********")
        func(*args, **kwargs)
        print("**********")

    return wrapper_func


@my_decorator
def hello():
    print("Helloo!!!")


@my_decorator
def bye(greeting, emoji):
    print(greeting, emoji)


hello()
bye("see you!", "😁")
# _____________________________________________________________________________________

# Excercise 1:
# Real-time application of decorators.
# We need to check the time taken by a function:
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        fn(*args, **kwargs)
        t2 = time()
        print(f"Time Taken: {t2 - t1} sec")

    return wrapper


@performance
def computation():
    for i in range(10000000):
        i * 5


computation()


# Excercise 2:
# Implement a checking-system where only admin can log-in, and no one else.
def authentication(fn):
    def wrapper(*args, **kwargs):
        if args[0] == "admin":
            fn(*args, **kwargs)
            return fn
        print("Login denied!")

    return wrapper


@authentication
def login_permission(person):
    print("You are logged In.")


login_permission("admin")  # Here the function will work because the argument is valid
login_permission("user")  # Here the function will not work

# Excercise 3:
# Implement the similar authentication system as above one, but for checking whether a friend
# can message or not.


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]["valid"] is True:
            fn(*args, **kwargs)
            return fn
        print("You are not allowed to message.")

    return wrapper


user1 = {"name": "Ammar", "valid": True}
user2 = {"name": "Manas", "valid": False}


@authenticated
def message_friend(random_person):
    print("You can message.")


message_friend(user1)
message_friend(user2)


