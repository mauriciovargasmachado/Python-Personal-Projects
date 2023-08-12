print("*****Calculator*****")

print("Please select on of the following options: ")
print("1 for addition")
print("2 for substraction")
print("3 for multiplication")
print("4 for division")
print("5 for exponent")
print("6 for module")

n1 = int (input("Insert the requested option: "))

if n1 == 1:

    print("you have selected addition\n")
    n1 = int (input("Insert your first number: "))
    n1 += int(input("Insert your second number: "))
    print("The result is: "+n1)

elif n1 == 2:

    print("you have selected subtraction\n")
    n1 = int (input("Insert your first number: "))
    n1 -= int(input("Insert your second number: "))
    print("The result is: ",n1)

elif n1 == 3:

    print("you have selected multiplication\n")
    n1 = int (input("Insert your first number: "))
    n1 *= int(input("Insert your second number: "))
    print("The result is: ",n1)

elif n1 == 4:

    print("you have selected division\n")
    n1 = int (input("Insert your first number: "))
    n1 /= int(input("Insert your second number: "))
    print("The result is: ",n1)

elif n1 == 5:

    print("you have selected exponent\n")
    n1 = int (input("Insert your first number: "))
    n1 **= int(input("Insert your second number: "))
    print("The result is: ",n1)

elif n1 == 6:

    print("you have selected module\n")
    n1 = int (input("Insert your first number: "))
    n1 %= int(input("Insert your second number: "))
    print("The result is: ",n1)

else:
    print("Your out of range please try again!.")
