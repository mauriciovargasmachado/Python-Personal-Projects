
def numbers_perfurmes():

    for i in range(1,50000):
        yield f'P - {i}'


def numbers_Pharmacy():
    for i in range(1, 50000):
        yield f'F - {i}'


def numbers_cosmetic():
    for i in range(1, 50000):
        yield f'C - {i}'


perfumes = numbers_perfurmes()

pharmacy = numbers_Pharmacy()

cosmetic = numbers_cosmetic()


def decorator(type):

    print("\n"+"*"*23)
    print('your number is: ')

    if type == 'P':
        print(next(perfumes))
    elif type == 'F':
        print(next(pharmacy))
    else:
        print(next(cosmetic))

    print("please wait for assitance")
    print("\n" + "*" * 23)
