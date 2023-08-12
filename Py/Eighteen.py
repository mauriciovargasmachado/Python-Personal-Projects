
n1 = input("Insert the first number: ")
n2 = input("Insert the second number: ")
n3 = input("Insert the third number: ")

if n1>n2 and n2>n3:
    print(n1+ " is the bigger of the three numbers")
else:
    if n2>n3:
        print(n1+ " is the bigger of the three numbers")
    else:
        print(n3 + " is the bigger of the three numbers")