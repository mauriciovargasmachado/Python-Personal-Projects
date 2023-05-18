import cv2

# Cargar el clasificador Haar Cascade para detección de ojos
ruta_clasificador = cv2.data.haarcascades + 'haarcascade_eye.xml'
clasificador_ojos = cv2.CascadeClassifier(ruta_clasificador)

# Inicializar la cámara
captura = cv2.VideoCapture(0)

while True:
    # Leer el frame actual
    _, frame = captura.read()

    # Convertir el frame a escala de grises
    frame_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar los ojos en el frame
    ojos = clasificador_ojos.detectMultiScale(frame_gris, scaleFactor=1.3, minNeighbors=5)

    # Dibujar un rectángulo alrededor de cada ojo detectado
    for (x, y, w, h) in ojos:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostrar el frame con los ojos detectados
    cv2.imshow('Detección de Ojos', frame)

    # Salir del bucle al presionar la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
captura.release()
cv2.destroyAllWindows()