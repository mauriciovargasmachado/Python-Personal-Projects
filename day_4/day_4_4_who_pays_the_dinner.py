
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_number=random.randint(1,4)

selection = names[random_number]

print(f'{selection} is going to buy the meal today!')