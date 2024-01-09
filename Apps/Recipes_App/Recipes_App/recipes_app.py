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


def show_categories(route):
    print("Categories: ")
    route_categories = Path(route)
    list_categories = []
    counter = 1

    for i in route_categories.iterdir():
        folder_str = str(i.name)
        print(f'{counter} - {folder_str}')
        list_categories.append(i)
        counter+=1

    return list_categories


def choose_categories(list):
    selection = 'x'

    while not selection.isnumeric() or int(selection not in range(1,len(list)+1)):
        selection = input('\nChoose a categorie: ')
    return list[int(selection)-1]


def show_recipes(route):
    print("Recipes: ")
    route_recipes = Path(route)
    recipes_list = []
    counter = 0

    for i in route_recipes.glob('*.txt'):
        recipe_str = str(i.name)
        print(f'{counter} - {recipe_str}')
        recipes_list.append(i)
        counter+=1

    return recipes_list


def choose_recepie(list):
    selection = "x"

    while not selection.isnumeric() or int(selection) not in range (1, len(list)+1):
        selection = input('\nChoose a recipe: ')

    return list[int(selection)-1]


user_menu = 0

if user_menu == 1:

    my_categories = show_categories(files_route)
    my_categorie = choose_categories(my_categories)
    my_recipes = show_recipes(my_categorie)
    mi_recipe = choose_recepie(my_recipes)
    #read recipes
    #back to main menu
    pass

elif user_menu ==2:
    my_categories = show_categories(files_route)
    my_categorie = choose_categories(my_categories)
    #create a new recipe
    # back to main menu
    pass

elif user_menu ==3:
    #create a new cathegorie
    # back to main menu
    pass

elif user_menu ==4:
    my_categories = show_categories(files_route)
    my_categorie = choose_categories(my_categories)
    my_recipes = show_recipes(my_categorie)
    mi_recipe = choose_recepie(my_recipes)
    #delete recipe
    #back to main menu
    pass

elif user_menu ==5:
    my_categories = show_categories(files_route)
    my_categorie = choose_categories(my_categories)
    # delete cathegorie
    # back to main menu
    pass

elif user_menu ==6:
    #End program
    pass

