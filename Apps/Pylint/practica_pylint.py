'''
Este módulo contiene una sencilla función de suma,
y ejecuta un ejemplo mostrando el resultado en pantalla
'''

def sumar(número_1, número_2):
    '''
    Se retorna el resultado de la suma'''
    return número_1+número_2

'''Se llama la funcion'''

SUMA = sumar(5, 7)

'''Se imprime el resultado'''

print(f'El resultado de la suma fue: {SUMA}')
