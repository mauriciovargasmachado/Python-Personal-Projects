
list = ["house_1","house_2","house_3","house_4","house_5","house_6"]

print(list)

position = int(input("Please select the position to insert your element: "))

list.insert(position,"house_33")

print(list)

delete = int(input("select the position of the element you want to eliminate: "))

list.pop(delete)

print(list)