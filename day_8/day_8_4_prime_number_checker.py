

def prime_checker(number):
    its_prime = True
    for i in range(2,number):
        if (number%i) ==0:
            its_prime=False
    if its_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
