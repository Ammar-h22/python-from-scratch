# Guessing game:
from random import randint

# answer = randint(1, 5)
# while True:
#     try:
#         guess = int(input("Guess a number 1~5: "))
#         if 0 < guess < 6:
#             if guess == answer:
#                 print(f"{answer} is the correct number, You are a genius!")
#                 break
#             else:
#                 print('Wrong guess, Try again!')
#         else:
#             print('Hey, number should be 1~5')
#     except ValueError:
#         print('Please enter a number.')

# Another way:
answer = randint(1, 5)
while True:
    try:
        guess = int(input("Guess a number 1~5: "))
        if guess < 0 or guess > 5:
            print('Hey, number should be 1~5')
        elif guess != answer:
            print('Wrong guess, Try again!')
        else:
            print(f"{answer} is the correct number, You are a genius!")
            break
    except ValueError:
        print('Please enter a number.')


# We have to run this code in terminal by giving 2 inputs:
# import sys
# answer = randint(int(sys.argv[1]), int(sys.argv[2]))
# while True:
#     try:
#         guess = int(input(f"Guess a number {sys.argv[1]}~{sys.argv[2]}: "))
#         if guess < int(sys.argv[1]) or guess > int(sys.argv[2]):
#             print(f'Hey, number should be {sys.argv[1]}~{sys.argv[2]}')
#         elif guess != answer:
#             print('Wrong guess, Try again!')
#         else:
#             print(f"{answer} is the correct number, You are a genius!")
#             break
#     except ValueError:
#         print('Please enter a number.')
