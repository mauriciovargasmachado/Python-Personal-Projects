import random

print("********** Wellcome to Rock, Paper or Scissors!! **********")
print("                       **********                          ")
print("                   *******************                     ")
print(" ")


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

number = random.randint(0,2)

list=[rock,paper,scissors]

computer_selection=list[number]

user_selection= int(input('What do you choose. Type 0 for Rock, type 1 for paper, or type 2 for scissors: '))

print(' ')

if number == user_selection :
    print(f'The computer has selected: {list[number]}')
    print(f'The user has selected: {list[user_selection]}')
    print('Draw!!!')
elif user_selection ==0 and user_selection ==2:
    print(f'The computer has selected: {list[number]}')
    print(f'The user has selected: {list[user_selection]}')
    print('You win!')
elif number < user_selection:
    print(f'The computer has selected: {list[number]}')
    print(f'The user has selected: {list[user_selection]}')
    print('You win!')
else:
    print(f'The computer has selected: {list[number]}')
    print(f'The user has selected: {list[user_selection]}')
    print('you lose!')
    
print(' ')

print(' *** End of the game *** ')
    
    