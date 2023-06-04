
def palindromo(text):

    x = text.replace(" ", "")

    reverse = ""
    for letter in x:
        reverse = letter+reverse

    if x == reverse:
        print(f"Your word is a palindrome.")
    else:
        print(f"Your word is not a palindrome.")


palindromo("abba")
