
array = ["a","b","c","d","e","f","g"]

print(array)

array.remove("e")

print(array)

array_2 = ["house","1","5","33",True,1,32]

print(array_2)

array_2.remove(True)

print(array_2)

array_3 = ["hotalistic",1,5,"33",False,1,32]

print(array_3)

array_3.remove("hotalistic")

print(array_3)


array_4 = ["house","1","5","33",True,1,32]

print(array_4)

del array_4[2:5]

print(array_4)

array_5 = ["house","1","5","33",True,1,32]

print(array_5)

del array_5[1:-1]

print(array_5)