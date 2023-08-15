
frase = input("Please insert a frase you want to test: ")

word = input("please type the word you want to remove from the frase: ")

finding = frase.find(word)

howLong = len(word)

final_frase = frase[0:finding]+frase[(finding+howLong):]

print(final_frase)