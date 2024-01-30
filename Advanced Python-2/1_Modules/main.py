# All python files (.py) are called as modules and folders are known as packages.
# So, a package is a folder containing modules(files).


"""
There are different ways to import modules and packages:
import module
import package.module
import package.subPackage.module
from module import function
from module import function1, function2,..
from module import * (* means everything)
from package.module import function
from package import module
"""

import utility
import shopping.shopping_cart

print(utility)
print(utility.addition(12, 2))
print(utility.divide(20, 14))

print(shopping.shopping_cart)
print(shopping.shopping_cart.buy("earphones", "laptop", "mouse"))

from utility import addition, divide

print(addition(2, 2))
print(divide(2, 2))


from shopping.shopping_cart import buy

print(buy("apple"))

from shopping import shopping_cart

print(shopping_cart.buy("apple"))

# _____________________________________________________________________________________
# The concept of (if __name__ == '__main__:')

# In Python, it is used to determine whether a Python script is being run as the main program or
# if it is being imported as a module into another script.
# (Because a file can be either run or imported.)

# Here's how it works:
# When a Python script is executed, the Python interpreter assigns a special built-in variable
# called __name__ for each script/module.
# If a Python script is being run as the main program, the value of __name__ is set to '__main__'.
# If a Python script is being imported as a module into another script, the value of __name__
# is set to the name of the script/module.

# This is particularly useful when you have functions, classes, or variables defined in a script that
# you want to be accessible when the script is run as a main program but not execute automatically
# when the script is imported as a module into another program.

if __name__ == "__main__":
    print("This code is being run as a main program.")
else:
    print("This code is being imported as a module into another script.")
