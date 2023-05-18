import cv2


# Función para detectar el movimiento de las manos
def detectar_movimiento(frame_anterior, frame_actual):
    # Convertir los frames a escala de grises
    frame_anterior_gris = cv2.cvtColor(frame_anterior, cv2.COLOR_BGR2GRAY)
    frame_actual_gris = cv2.cvtColor(frame_actual, cv2.COLOR_BGR2GRAY)

    # Calcular la diferencia absoluta entre los frames
    diferencia = cv2.absdiff(frame_anterior_gris, frame_actual_gris)

    # Aplicar un umbral para obtener una imagen binaria
    umbral = cv2.threshold(diferencia, 30, 255, cv2.THRESH_BINARY)[1]

    # Aplicar una serie de transformaciones morfológicas para eliminar el ruido
    umbral = cv2.dilate(umbral, None, iterations=2)
    umbral = cv2.erode(umbral, None, iterations=2)

    # Encontrar los contornos de las áreas con movimiento
    contornos, _ = cv2.findContours(umbral.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Inicializar las coordenadas del área de movimiento
    x, y, w, h = 0, 0, 0, 0

    # Encontrar el contorno más grande (que se asume como la mano)
    for contorno in contornos:
        if cv2.contourArea(contorno) > 10000:
            (x, y, w, h) = cv2.boundingRect(contorno)

    return x, y, w, h


# Inicializar la cámara
captura = cv2.VideoCapture(0)

# Leer el primer frame
_, frame_anterior = captura.read()

while True:
    # Leer el siguiente frame
    _, frame_actual = captura.read()

    # Detectar el movimiento de las manos
    x, y, w, h = detectar_movimiento(frame_anterior, frame_actual)

    # Dibujar un rectángulo alrededor del área de movimiento
    cv2.rectangle(frame_actual, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostrar el frame con el área de movimiento
    cv2.imshow('Movimiento de manos', frame_actual)

    # Salir del bucle al presionar la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Actualizar el frame anterior
    frame_anterior = frame_actual

# Liberar los recursos
captura.release()
cv2.destroyAllWindows()