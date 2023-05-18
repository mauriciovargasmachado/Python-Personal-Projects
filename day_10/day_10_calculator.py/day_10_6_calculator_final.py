from day_10_art import logo

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

should_continue = True

while should_continue:
    
    print(logo)

    num_1=int(input('What is your first number?'))

    for symbol in operations:
        print(symbol)

    operation=input('What is your operation?')

    num_2=int(input('What is your second number?'))

    calculation =operations[operation]
    answer=calculation(num_1,num_2)


    print(f'{num_1}{symbol}{num_2}={answer}')
    
    print('')
    
    question=input('Do you want to try again?. Type "yes" or "No"')
    question.lower()
    
    if question == 'no':
        should_continue = False