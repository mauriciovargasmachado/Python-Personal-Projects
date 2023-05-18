import random
from art_guess_the_number import logo
from art_guess_the_number import winner
from art_guess_the_number import loser

print(logo)

user_dificulty=input('please select your difficulty, "H" for Hard, and "E" for easy: ')


def dificulty():
    if user_dificulty=="H":
        return 5
    else:
        return 10
    
computer_number=random.randint(0,101)

dead=False

lives=dificulty()

while not dead:
    user_number=int(input('Please select your number: '))
    if user_number>computer_number:
        print('Your number is too high try again') 
        lives=lives-1
        print(f'You have {lives} left!')
        if lives ==0:
            print('!!!You Lose!!!')
            print(loser)
            dead=True
    elif user_number<computer_number:
        print('Your number is too low try again')
        lives=lives-1
        print(f'You have {lives} left!')
        if lives ==0:
            print('!!!You Lose!!!')
            print(loser)
            dead=True
    elif user_number==computer_number:
        print('Your guess the number!. YOU WIN!!!')
        print(winner)
        dead=True
    else:
        print('Thats not a number, try again')