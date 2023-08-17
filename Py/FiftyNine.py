
list = ["a","e","i","o","u","i"]

print(list)

letter = input("Please type the element you want to remove from the list: ")

for i in list:

    if letter.lower() == i:

        list.remove(i)

print(list)