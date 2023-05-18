
print("       ******************        ")
print(" ")

print("Welcome to the Love Calculator!")
print("       ******************       ")
print(" ")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
print(" ")

full_name=name1+name2

name=full_name.lower()

T= name.count("t")
R= name.count("r")
U= name.count("u")
E= name.count("e")

L= name.count("l")
O= name.count("o")
V= name.count("v")
E= name.count("e")

first_number=T+R+U+E
second_number=L+O+V+E

love_number=str(first_number)+str(second_number)

love_count=int(love_number)

if love_count <10 or love_count >90:
    print (f'Your score is {love_number}, you go together like coke and mentos.')
elif love_count <40 or love_count <50:
    print(f"Your score is {love_number}, you are alright together.")
else:
    print(f'Your score is {love_number}.') 