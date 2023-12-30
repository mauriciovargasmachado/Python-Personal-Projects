
text = input('Type a text to analyze: ')

print('\n')

r = int(input('how many letter would you like to analyze?: '))

chart = []

text_lower = text.lower()

print('\n')

for i in range(r):
  letter = input(f' Type you {i+1} letter: ').lower()
  chart.append(letter)

print('\n')

for i in range(r):
  quantity_letter = text.count(chart[i])
  print(f'You have {quantity_letter} of ({chart[i]}) in your text.')

words = text.split()
quantity_words = len(words)

print('\n')


print(f'The submited text has : {quantity_words}')

print('\n')

words.reverse()
inverted_text = ' '.join(words)


print(f'Your reverted text is: {inverted_text}')

print('\n')

word_to_search = input('insert the word to search: ')

if word_to_search in text:
  print('Your word is in the inputed text')

else:
  print('Your word is not in the inputed text')

