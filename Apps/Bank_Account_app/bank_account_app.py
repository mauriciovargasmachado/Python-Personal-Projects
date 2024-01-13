#Creation of class person
class Person:

    def __init__ (self, name, last_name):
        self.name = name
        self.last_name = last_name


#Creation of objetc client
class Client(Person):

    def __init__ (self, name, last_name,account_number, balance = 0):
        super().__init__(name,last_name)
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f'The client: {self.name} {self.last_name}\nCurrent balance: ${self.balance}\nAccount number: {self.account_number} '

    def deposit(self,deposit_value):

        self.balance += deposit_value

        print('Deposit accepted!\n')


    def withdrawal(self,withdrawal_value):

        if self.balance >= withdrawal_value:
            self.balance -= withdrawal_value
            print('Withdrawal accepted!')
        else:
            print('Your funds are insufficient!\n')



#creation of create client funtion

def create_client():
    client_name = input('Please type your first name: ')
    client_Last_name = input('Please type your last name: ')
    client_account_number = input('please type your account number:')
    print('')


    client = Client(client_name, client_Last_name, client_account_number)

    return client

def init():
    my_client = create_client()
    print(my_client)

    option = 0

    while option != 'E':
        print('choose one of the following options:\nDeposit [D]\nWithdrawal [w]\nexit [E]')

        option = input().upper()

        if option == 'D':
            deposit_value = int(input('Please type the amount to deposit: '))
            my_client.deposit(deposit_value)
        elif option == 'W':
            withdrawal_value = int(input('Please type the amount to withdrawal: '))
            my_client.withdrawal(withdrawal_value)

        print(my_client)


    print('We hope that you have a great experience with our bank \nHave a nice day!')

init()
