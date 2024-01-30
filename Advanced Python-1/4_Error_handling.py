# Error handling
# Error handling allow us to let the script continue running, even if there is an error.

# try:
#     age = int(input("What is your age? "))
#     print(age)
# except:
#     print("Please enter a number ")

# while True:
#     try:
#         age = int(input("What is your age? "))
#         print(age)
#     except:
#         print("Please enter a number ")
#     else:
#         print("Thankyou!")
#         break

# We can also give different specific error names
# while True:
#     try:
#         num = int(input("Please enter a number: "))
#         10 / num
#     except ValueError:
#         print("Only numbers will be accepted")
#     except ZeroDivisionError:
#         print("Enter a valid number")
#     else:
#         print("cool")
#         break


# def division(num1, num2):
#     try:
#         print(num1 / num2)
#     except (TypeError, ZeroDivisionError):
#         print("OOOPS..")
#
#
# division(1, 0)

# If we want to give a message for an error:


# def division(num1, num2):
#     try:
#         print(num1 / num2)
#     except ZeroDivisionError as err:
#         print("Error:", err)
#
#
# division(1, 0)


# def division(num1, num2):
#     try:
#         print(num1 / num2)
#     except (TypeError, ZeroDivisionError) as err:
#         print("Error:", err)
#
#
# division(1, 0)

# There is also another last thing that is used in the exception handling block:
# while True:
#     try:
#         num = int(input("Please enter a number: "))
#         10 / num
#     except ValueError:
#         print("Only numbers will be accepted")
#     except ZeroDivisionError:
#         print("Enter a valid number")
#     else:
#         print("cool")
#         break
#     finally:  # This will always get printed
#         print("Ok I am done!")


# We can throw our own errors using 'raise' keyword:
def square_root(num):
    if num < 0:
        raise Exception("Enter number greater than -1")
    return num**0.5


print(square_root(-9))
