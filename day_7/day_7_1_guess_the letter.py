import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

lenght = len(word_list)

random_number = random.randint(1,lenght)

random_word = word_list[random_number-1]


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input(f'Guess a letter: ').lower()


#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for word in random_word:
    if guess == word:
        print('Right')
    else:
        print('Wrong')