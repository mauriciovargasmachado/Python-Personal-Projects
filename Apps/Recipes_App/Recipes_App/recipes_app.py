import os
from pathlib import Path
from os import system

files_route = Path(Path.home(),'OneDrive','CMV 2022','Personal CMV','Programacion','Python','Apps','Recipes_App','Recipes_App')

#count the amount of recipes available.
def count_recipes(route):
    counter = 0
    for i in Path(route).glob('**/*.txt'):
        counter+=1
    return counter

def index():
    system('cls')
    print('*'*50)
    print('\tWelcome to the recipes administrator system')
    print('*' * 51)
    print(' ')
    print(f'The recipes are located in {files_route}')
    print(f'The total amount of recipes available at the moment is: {count_recipes(files_route)}')

    print(' ')
    user_selection = 'x'
    while not user_selection.isnumeric() or int(user_selection) not in range(1,7):

        print('Choose one of the following options')
        print('''
        [1] - Read recipe
        [2] - Create a new recipe
        [3] - Create a new categorie
        [4] - Delete recipe
        [5] - Delete categorie
        [6] - exit
        ''')
        user_selection = input('What is your selection: ')


index()






user_menu = 0

if user_menu == 1:

    #show cathegories
    #choose categories
    #show recipes
    #choose recipes
    #read recipes
    #back to main menu
    pass

elif user_menu ==2:
    #show cathegories
    #choose categories
    #create a new recipe
    # back to main menu
    pass

elif user_menu ==3:
    #create a new cathegorie
    # back to main menu
    pass

elif user_menu ==4:
    #show cathegories
    #choose categories
    #show recipes
    #choose recipes
    #delete recipe
    #back to main menu
    pass

elif user_menu ==5:
    # show cathegories
    # choose categories
    # delete cathegorie
    # back to main menu
    pass

elif user_menu ==6:
    #End program
    pass

