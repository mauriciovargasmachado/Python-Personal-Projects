import tkinter as tk
import time

# Variables para el cronómetro de escritura
start_time_typing = 0
typing_time = 0

# Variables para el cronómetro de movimiento del mouse
start_time_mouse = 0
mouse_time = 0

# Función para actualizar el cronómetro de escritura
def update_typing_timer():
    global typing_time
    current_time = time.time() - start_time_typing
    typing_time = current_time
    typing_label.config(text="Tiempo escribiendo: {:.2f} segundos".format(typing_time))
    typing_label.after(100, update_typing_timer)

# Función para actualizar el cronómetro de movimiento del mouse
def update_mouse_timer(event):
    global mouse_time
    current_time = time.time() - start_time_mouse
    mouse_time = current_time
    mouse_label.config(text="Tiempo moviendo el mouse: {:.2f} segundos".format(mouse_time))

# Función para iniciar los cronómetros
def start_timers(event):
    global start_time_typing, start_time_mouse
    start_time_typing = time.time()
    start_time_mouse = time.time()
    root.bind('<KeyPress>', start_timers)

# Crear la ventana principal
root = tk.Tk()
root.title("Cronómetros")

# Etiqueta para mostrar el tiempo de escritura
typing_label = tk.Label(root, text="Tiempo escribiendo: 0.00 segundos")
typing_label.pack()

# Etiqueta para mostrar el tiempo de movimiento del mouse
mouse_label = tk.Label(root, text="Tiempo moviendo el mouse: 0.00 segundos")
mouse_label.pack()

# Actualizar el cronómetro de escritura cada 100 ms
update_typing_timer()

# Registrar el movimiento del mouse y actualizar el cronómetro correspondiente
root.bind('<Motion>', update_mouse_timer)

# Iniciar los cronómetros al presionar cualquier tecla
root.bind('<KeyPress>', start_timers)

# Ejecutar la ventana principal
root.mainloop()