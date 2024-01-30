import random

lowerCase = 'abcdefghijklmnopqrstuvqxwz'
upperCase = 'ABCDEFGHIJKLMNOPQRSTUVQXWZ'
numbers = '123456789'
symbols = '!@#$%^&*().'

string = lowerCase + upperCase + numbers + symbols
length = 12
password = "".join(random.sample(string, length))
print(f'New random password is {password}')


