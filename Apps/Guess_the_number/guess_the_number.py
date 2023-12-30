from random import *

attemps = 0

user_guess = 0

random_number = randint(1,1000)

user_name = input('Please insert your name: ')

print('\n')

print(f'Welcome {user_name}, Im thinking in a number between 1 and 1000, can you guessed, you have 8 attemps!!!')

print('\n')

while attemps < 8 :

    user_guess = int(input(f'What is the your {attemps+1} guess?: '))
    attemps+=1
    if user_guess > random_number:
        print('Your number is bigger than the number I thought, try again!!! ')
    elif user_guess < random_number:
        print('The number I thought is bigger than your number, try again!!! ')
    else:
        print('YOU WIN!!!')
        break
    print(f'You have {8-attemps} attemps left.')

if user_guess != random:
    print('YOU LOSE')
