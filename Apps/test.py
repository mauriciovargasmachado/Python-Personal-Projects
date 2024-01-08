# text = "ABCDEFGHIJKKLMNOPQRSTUVWXYZ"
# fragment = text[0: :2]
# print(fragment)


# def todos_positivos(numeros):
#     for i in numeros:
#         if i <= 0:
#             return False
#     return True
#
# lista_numeros = [2,-58]
# resultado = todos_positivos(lista_numeros)
#
# print(resultado)


# def suma_menores(lista_numeros):
#     suma = 0
#     for numero in lista_numeros:
#         if 0 < numero < 1000:
#             suma += numero
#     return suma
#
# lista_numeros = [500, 100, -200, 800, 1200, 5]

# def cantidad_pares(numeros):
#     cuenta = 0
#     for i in numeros:
#         cuenta += 1
#
#     return cuenta
#
#
# lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(cantidad_pares(lista_numeros))


# def cantidad_pares(numeros):
#     cuenta = 0
#     for i in numeros:
#         cuenta += 1
#
#     return cuenta
#
#
# lista_numeros = [1, 50, 502, 755, 34]
#
# print(cantidad_pares(lista_numeros))

# def cantidad_pares(numeros):
#     cuenta = 0
#     for numero in numeros:
#         if numero % 2 == 0:  # Verificar si el número es par
#             cuenta += 1
#     return cuenta
#
#
# lista_numeros = [1,50,502,755,34]

# import random
#
#
# def lanzar_dados:
#     dado1 = random.randint(1, 6)
#     dado2 = random.randint(1, 6)
#     return dado1, dado2
#
#
# def evaluar_jugada(dado1, dado2):
#     suma_dados = dado1 + dado2
#
#     if suma_dados <= 6:
#         return f"La suma de tus dados es {suma_dados}. Lamentable"
#     elif 6 < suma_dados < 10:
#         return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
#     else:
#         return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


# def reducir_lista(lista):
#     if not lista:
#         return lista
#
#     lista = list(set(lista))
#     lista.remove(max(lista))
#
#     return lista
#
#
# def promedio(lista):
#     if not lista:
#         return 0
#
#     return sum(lista) / len(lista)
#
#
# lista_numeros = [1, 2, 15, 7, 2]
#
# lista_reducida = reducir_lista(lista_numeros)
# print("Lista reducida:", lista_reducida)
#
# promedio_resultado = promedio(lista_reducida)
# print("Promedio de la lista reducida:", promedio_resultado)


# import random
#
#
# def lanzar_moneda():
#     resultado = random.choice(["Cara", "Cruz"])
#     return resultado
#
#
# def probar_suerte(resultado_moneda, lista_numeros):
#     if resultado_moneda == "Cara":
#         print("La lista se autodestruirá")
#
#         return []
#     elif resultado_moneda == "Cruz":
#         print("La lista fue salvada")
#
#         return lista_numeros
#
#
# lista_numeros = [1, 2, 3, 4, 5]
#
# resultado_moneda = lanzar_moneda()
# print("Resultado del lanzamiento de la moneda:", resultado_moneda)
#
# lista_resultante = probar_suerte(resultado_moneda, lista_numeros)
# print("Lista resultante:", lista_resultante)


# def ordenar(lista):
#
#     l = []
#
#     for i in lista:
#         l.append(i)
#
#     l.sort()
#
#     return l
#
# text =('This is a test')
#
# print(text)
#
# print(ordenar(text))


#
# my_file = open('Prueba.txt')
#
# #print(my_file.read())
#
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
#
# my_file.close()
#
# with open('texto.txt', 'r') as file:
#     # Lee todas las líneas del archivo
#     lines = file.readlines()
#
#     # Verifica si hay al menos dos líneas en el archivo
#     if len(lines) >= 2:
#         # Imprime la segunda línea (índice 1 en Python, ya que la indexación comienza en 0)
#         print(lines[1])
#     else:
#         print("El archivo no tiene al menos dos líneas.")


with open('mi_archivo.txt', 'w') as file:
    lines = file.write("Nuevo texto")

file.close()

with open('mi_archivo.txt', 'r') as file:
    lines = file.read()

    print(lines)




registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

with open("registro.txt", "a") as archivo:
    archivo.writelines('\t'.join(registro_ultima_sesion) + '\n')

with open("registro.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

