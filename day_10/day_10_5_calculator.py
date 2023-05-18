#This is a calculator program

#add
def add (n1,n2):
    return n1+n2
#substract
def substract (n1,n2):
    return n1-n2
#multiplication
def multiply (n1,n2):
    return n1*n2
#division
def division (n1,n2):
    return n1/n2

operations ={
    
    '+':add,
    '-':substract, 
    '*':multiply,
    '/':division,    
}

num_1=int(input('What is your first number?'))

for symbol in operations:
    print(symbol)

operation=input('What is your operation?')

num_2=int(input('What is your second number?'))

calculation =operations[operation]
answer=calculation(num_1,num_2)


print(f'{num_1}{symbol}{num_2}={answer}')