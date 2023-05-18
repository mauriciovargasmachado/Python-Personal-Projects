from day_8_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def cipher(text,shift,direction):
    end_text=''
    if direction=='decode':
        shift *=-1
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position= position + shift
            end_text+=alphabet[new_position]
        else:
            end_text=letter

    print(f"The {direction} text is {end_text}")
            
answer=True
while answer ==True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))    
            
    shift=shift%26
    cipher(text,shift,direction)
    
    
    answer = input('Do you want to try again? Type "yes" or "no": ')
    if answer == 'no':
        answer == False
        print('Goodbye!')
    else:
        answer==True
