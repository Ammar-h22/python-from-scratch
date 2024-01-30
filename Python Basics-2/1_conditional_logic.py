# conditional logic

is_old = True
is_licenced = True

if is_old:
    print("You are old enough to drive!")
elif is_licenced:
    print("You can drive now!")
else:
    print("Sorry, you are not allowed to drive!")

if is_old and is_licenced:
    print("You are allowed to drive!")
else:
    print("Sorry, you are not allowed to drive!")

# Truthy and Falsy
is_old = 24
is_licenced = "Hello"
# Both of these values will get evaluated into True or False
# Demo
print(bool(25))  # This will print True
print(bool("Hey"))  # This will print True
print(bool(""))  # This will print False
print(bool(0))  # This will print False

if is_old and is_licenced:
    print("You are allowed to drive!")
else:
    print("Sorry, you are not allowed to drive!")

# Ternary operator:  (Also known as conditional expression)
# It is just a shortcut way to write if-else statements, but it is not
# widely used as it is little confusing.
# Syntax: condition_if_true if condition else condition_if_false
is_friend = False
can_message = "You can message" if is_friend else "You cannot message"
print(can_message)

# Short circuiting
if False and True:
    print("It will not go till True to check, it will directly go to the next block")
if True or False:
    print("It will not go till False to check, it will directly go inside the block")

# Logical operators
is_magician = True
is_expert = False

if is_magician and is_expert:
    print("You are a master magician")
elif is_magician and not is_expert:
    print("At least you are getting there")
elif not is_magician:
    print("You need magic powers")

# == vs is
# '==' checks for the equality in value.
# 'is' checks whether the location where the value is stored is same or not.
print(True == 1)
print("" == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])
# vs
print(True is 1)
print(True is True)
print(1 is 1)
print("1" is "1")
print([] is [])
