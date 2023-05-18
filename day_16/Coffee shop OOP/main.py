from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
my_menu = Menu

game_on = True

while game_on:
    options = my_menu.get_items()
    selection = input(f'What drink do you like to have? {options}: ')
    if selection == "off":
        game_on = False
    elif selection == "report":
        my_money_machine.report()
        my_coffee_maker.report()
    else:
        drink = my_menu.find_drink(selection)
        if my_coffee_maker.is_resource_sufficient(drink):
            my_money_machine.make_payment(drink.cost)


