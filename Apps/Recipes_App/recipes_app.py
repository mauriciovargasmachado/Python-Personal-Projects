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

    return int(user_selection)

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


def choose_categories(categories_list):
    selection = 'x'

    while not (selection.isnumeric() and int(selection) in range(1, len(categories_list) + 1)):
        selection = input('\nChoose a category: ')

    return categories_list[int(selection) - 1]


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

def read_recipe(recipe):
    print(Path.read_text(recipe))

def create_recipe(route):
    recipe_exist = False

    while not recipe_exist:
        print('Please type the name of your recipe: ')
        recipe_name = input() + '.txt'
        print('Please type your recipe: ')
        recipe_content = input()
        new_route = Path(route, recipe_name)

        if not os.path.exists(new_route):
            Path.write_text(new_route, recipe_content)
            print('Your recipe has been created!')
            recipe_exist = True
        else:
            print('Sorry, you already have this recepie.')


def create_category(route):
    category_exist = False

    while not category_exist:
        print('Please type the name of your category: ')
        category_name = input()
        new_route = Path(route,category_name)

        if not os.path.exists(new_route):
            Path.mkdir(new_route)
            print(f'Your category ({category_name}), has been created!')
            category_exist = True
        else:
            print('Sorry, you already have this category.')



def delete_recipe(recipe):
    Path(recipe).unlink()
    print(f'you recipe: {recipe.name}, has been delete!')


def delete_category(category):
    Path(category).rmdir()
    print(f'you category: {category.name}, has been delete!')


def back_to_main_menu():
    user_selection = 'x'

    while user_selection.lower() != 'M':
        user_selection = input('\nType "M" to go back to the main menu: ')
        if user_selection.lower() == 'm':
            return
        else:
            print('Invalid input. Please enter "M" to go back to the main menu.')



#program beginning
end_program = False


while not end_program:

    user_menu = index()
    #user_menu = 0

    if user_menu == 1:

        my_categories = show_categories(files_route)
        my_category = choose_categories(my_categories)
        my_recipes = show_recipes(my_category)
        my_recipe = choose_recepie(my_recipes)
        read_recipe(my_recipe)
        back_to_main_menu()


    elif user_menu ==2:
        my_categories = show_categories(files_route)
        my_category = choose_categories(my_categories)
        create_recipe(my_category)
        back_to_main_menu()


    elif user_menu ==3:
        create_category(files_route)
        back_to_main_menu()


    elif user_menu ==4:
        my_categories = show_categories(files_route)
        my_category = choose_categories(my_categories)
        my_recipes = show_recipes(my_category)
        my_recipe = choose_recepie(my_recipes)
        delete_recipe(my_recipe)
        back_to_main_menu()


    elif user_menu ==5:
        my_categories = show_categories(files_route)
        my_category = choose_categories(my_categories)
        delete_category(my_category)
        back_to_main_menu()


    elif user_menu ==6:
        print('\n**********Thank you for using our software, have a nice day!**********')
        end_program = True
