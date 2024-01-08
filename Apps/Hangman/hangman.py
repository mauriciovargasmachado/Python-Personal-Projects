import random
from faker import Faker

faker = Faker()
random.seed(faker.random_int(min=0, max=100))

# Instead of using a list of preset words, we generate a Faker word with random work names.
selected_word = faker.job().upper()
letters_quantity = len(selected_word)

print(selected_word)

successes = 0
errors = 0
attempts = 8
right_letters = []
wrong_letters = []
game_off = False


def letters_in_word(selected_word):
    selected_letters = []
    for i in selected_word:
        selected_letters.append(i)
    return selected_letters


print(letters_in_word(selected_word))


def ask_user_letter():
    user_letter = ''
    is_valid = False
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while not is_valid:
        user_letter = input("Select a letter: ").upper()
        if user_letter in abc and len(user_letter) == 1:
            is_valid = True
        else:
            print('Your input is invalid')

    return user_letter


def show_new_canvas(selected_word, wrong_letters):
    hide_list = []

    for i in selected_word:
        if i in wrong_letters or i not in right_letters:
            hide_list.append("-")
        else:
            hide_list.append(i)

    print(' '.join(hide_list))


def check_word(user_letter, hide_list, attempts, coincidences):
    end = False

    if user_letter in hide_list:
        right_letters.append(user_letter)
        coincidences += 1
    else:
        attempts -= 1
        wrong_letters.append(user_letter)

    if attempts == 0:
        end = you_lose()
    elif coincidences == letters_quantity:
        end = you_win()

    return attempts, end, coincidences


def you_lose():
    print("You lose!")
    print(f'The hidden word was: {selected_word}')
    return True


def you_win():
    print("Congratulations! You win!")
    return True


while not game_off:
    show_new_canvas(selected_word, wrong_letters)
    user_letter = ask_user_letter()
    attempts, game_off, successes = check_word(user_letter, selected_word, attempts, successes)
