import numbers

def preguntar():

    print("Welcome to the shift generator system")

    while True:

        print("[P] - Perfumes.\n[F] - Pharmacy.\n[C] - Cosmetic.")

        try:
            my_type = input("Please choose your preference: ").upper()
            ['P','F','C'].index(my_type)

        except ValueError as e:

            print("That's not a valid option")
            print(e)

        else:
            break

    numbers.decorator(my_type)

def index():

    while True:
        preguntar()
        try:
            another_shift = input('Do you need another tiquet? [Y] , [N]: ').upper()
            ['S','N'].index(another_shift)

        except ValueError as e:
            print(f'Thats not a valir value: {e}')

        else:
            if another_shift =='N':
                print("thanks for choosing us!")
                break

index()


