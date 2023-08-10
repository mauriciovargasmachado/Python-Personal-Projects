
print("*****  Welcome to the average student grade calculator *****")
print("")
name = input("To start please type your name: ")

n1 = int(input(name+". What is your first grade: "))
n2 = int(input(name+". What is your second grade: "))
n3 = int(input(name+". What is your third grade: "))

average = (n1+n2+n3)/3

print("your average is: "+str(average))

if average>=8:
    print("Congratulations, you have approved")
elif average>=6:
    print("You have approved")
else:
    print("You have fail!!!")




print("")
print("***** End of the program *****")