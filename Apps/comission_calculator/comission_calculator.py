
name= input('Please type your name: ')
sales =int( input('Please type your monthly total sales: '))

comission = round(sales*13/100, 4)



print(f'{name}, your total comission value is: ${comission}')
