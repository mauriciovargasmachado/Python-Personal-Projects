


import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator program!")
letters_one= int(input("How many letters would you like in your password?\n")) 
symbols_one = int(input(f"How many symbols would you like?\n"))
numbers_one = int(input(f"How many numbers would you like?\n"))

password = ''
password2 = ''
password3 = ''

for letter in range(1,letters_one + 1 ):
    random_letter = random.choice(letters)
    password +=random_letter

for number in range(1,numbers_one + 1 ):
    random_number = random.choice(numbers)
    password2 +=random_number

for symbol in range(1,symbols_one + 1 ):
    random_symbols = random.choice(symbols)
    password3 +=random_symbols

password_total =password+password2+password3

print(password_total)

random.shuffle(password_total)

print(password_total)