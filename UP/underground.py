from pprint import pprint

String = input("please type a frase: ")


def removeSpaces(string):
    return [char for char in string if char != " "]


def countChars(list):
    charDict = {}
    for char in list:
        if char in charDict:
            charDict[char] += 1

        else:
            charDict[char] = 1
    return charDict


print(removeSpaces(String))
removeSpacesAnswer = removeSpaces(String)
pprint(countChars(removeSpacesAnswer))
