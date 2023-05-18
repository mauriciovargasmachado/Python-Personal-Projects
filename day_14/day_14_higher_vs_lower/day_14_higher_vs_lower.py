from day_14_data import data
from day_14_art import logo
from day_14_art import vs
import random

print(logo)

score=0

game_on=True

while game_on:

    def format_option(option):    

        name=option["name"]
        followers=option["follower_count"]
        description=option["description"]
        country=option["country"]
        
        return f'{name}, a {description}, from {country}.'

    def check_answer(user_selection,followers_a,followers_b):
        
        if followers_a >followers_b:
            return user_selection=='a'
        else:
            return user_selection=='b'


    option_a=random.choice(data)
    option_b=random.choice(data)

    if option_a == option_b:
        option_b=random.choice(data)    


    print(f'compare A: {format_option(option_a)}')
    print(vs)
    print(f'against B: {format_option(option_b)}')
        
    user_selection=input("Who has more followers, A, or B?:").lower()


    followers_a=int(option_a["follower_count"])
    followers_b=int(option_b["follower_count"])

    print(followers_a)
    print(followers_b)

    is_correct = check_answer(user_selection,followers_a,followers_b)


    if is_correct:
        score+=1
        print(f'You Win!!!, your score was {score}')
        
    else:
        print(f'You Lose!!!, your score was {score}')
        game_on = False

