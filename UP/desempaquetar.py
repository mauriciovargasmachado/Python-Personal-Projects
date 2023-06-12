
lista = [1, 2, 3, 4]

print(2, 3, 4, 5)

print(*lista)

lista_2 = [5, 6, 7, 8]
print(*lista_2)

conbinada = [*lista, *lista_2]
print(*conbinada)

punto_1 = {"x": 399}
punto_2 = {"y": 993}

punto_final = {**punto_1, **punto_2}

print(punto_final)
