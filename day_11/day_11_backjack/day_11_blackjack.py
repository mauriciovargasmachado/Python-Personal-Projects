from day_11_blackJack_art import logo
import random

def random_card():
    deck =[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(deck)
    return card

def calculate_score(cards):
    
    if sum(cards) == 21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        print('Draw')
    elif computer_score ==0:
        print('You lose, The opponent has a blackjack')
    else:
        print('you win!!!')

print(logo)

user_cards = []
computer_cards = []
is_game_over=False

for i in range(2):
    user_cards.append(random_card())
    computer_cards.append(random_card())
    
while not is_game_over:

    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f'Your cards are: {user_cards}, and the computer cards are: {computer_cards}')
    print(f'The user score is: {user_score}, and the computer score is: {computer_score}')

    if user_score == 0 or computer_score == 0 or user_score >21:
        is_game_over=True
    else:
        user_ask_card=input(f"Type Y to get another card, Type N to get another pass: ")
        user_ask_card=user_ask_card.lower()
        if user_ask_card=='y':
            user_cards.append(random_card())
        else:
            is_game_over=True    
            
while computer_score !=0 and computer_score <17:
    computer_cards.append(random_card)
    computer_score = calculate_score(computer_cards)
    
compare(user_score,computer_score)

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

