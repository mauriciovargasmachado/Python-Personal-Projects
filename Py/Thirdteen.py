
print("***** Mutation *****")
print("")
print("")
print("*** Menu ***")
print("Press 1 for transform a number into a word")
print("Press 2 for transform a word into a number")

option = int(input("Whats is your selection: "))

print("")

if option ==1:
    print("You will transform a number into a word")

    option_1 = int(input("please type the number you would like to transform into a word: "))

    if option_1 ==1:
        print("Your number is One.")
    elif option_1 ==2:
        print("Your number is Two.")
    elif option_1 ==3:
        print("Your number is Three.")
    elif option_1 ==4:
        print("Your number is four.")
    elif option_1 == 5:
        print("Your number is five.")
    else:
        print("out of range number.")

if option ==2:
    print("You will transform a word into a number: ")

    option_2 = input("please type the number you would like to transform into a word: ")

    if option_2 == "one":
        print("Your word is 1.")
    elif option_2 == "two":
        print("Your word is 2.")
    elif option_2 == "three":
        print("Your word is 3.")
    elif option_2 == "four":
        print("Your number is 4.")
    elif option_2 == "five":
        print("Your number is 5.")
    else:
        print("out of range number.")

else:
    print("This option is not available")

print("")
print("")
print("*****End of program*****")