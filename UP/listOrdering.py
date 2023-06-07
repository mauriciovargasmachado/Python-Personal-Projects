
number = [5, 9, 44, 22, 33, 44, 8, 16, 99, 88, 2, 3]

number.sort()
print(number)

number.sort(reverse=True)
print(number)

number_2 = sorted(number)
print(number)
print(number_2)

usuarios = [[4, "carlos"], [8, "david"], [1, "Oscar"], [15, "Kang"]]

usuarios.sort()
print(usuarios)


usuarios = [["carlos", 66], ["david", 69], ["Oscar", 33], ["Kang", 25]]


def paraOrdenar(elemento):
    return elemento[1]


usuarios.sort(key=paraOrdenar, reverse=True)
print(usuarios)


usuarios = [["carlos", 66], ["david", 69], ["Oscar", 33], ["Kang", 25]]

usuarios.sort(key=lambda elemento: elemento[1])
print(usuarios)
