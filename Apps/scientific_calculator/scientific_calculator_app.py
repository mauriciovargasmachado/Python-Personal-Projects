import tkinter as tk
import math

def calcular(expresion):
    try:
        resultado = eval(expresion)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

def agregar(caracter):
    entrada.insert(tk.END, caracter)

ventana = tk.Tk()
ventana.title("Calculadora Científica")

entrada = tk.Entry(ventana, width=35)
entrada.grid(row=0, column=0, columnspan=4)

botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    '(', ')', 'sin', 'cos',
    'tan', 'pi', 'log', 'sqrt'
]

row_val = 1
col_val = 0

for boton in botones:
    if boton in '0123456789.()':
        tk.Button(ventana, text=boton, width=10, command=lambda boton=boton: agregar(boton)).grid(row=row_val, column=col_val)
    elif boton in 'sincostan':
        tk.Button(ventana, text=boton, width=10, command=lambda boton=boton: agregar(boton+'(')).grid(row=row_val, column=col_val)
    elif boton == 'pi':
        tk.Button(ventana, text=boton, width=10, command=lambda: agregar(str(math.pi))).grid(row=row_val, column=col_val)
    elif boton == '=':
        tk.Button(ventana, text=boton, width=10, command=lambda: calcular(entrada.get())).grid(row=row_val, column=col_val)
    else:
        tk.Button(ventana, text=boton, width=10, command=lambda boton=boton: agregar(' '+boton+' ')).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

ventana.mainloop()
