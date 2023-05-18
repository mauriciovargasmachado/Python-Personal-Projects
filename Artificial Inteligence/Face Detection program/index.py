import cv2

# Cargar el clasificador Haar Cascade pre-entrenado para la detección de caras
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicializar la captura de video desde la cámara
video_capture = cv2.VideoCapture(0)

while True:
    # Leer el frame actual de la cámara
    ret, frame = video_capture.read()

    # Convertir el frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar caras en el frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Iterar sobre las caras detectadas y dibujar un rectángulo alrededor de ellas
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostrar el frame con las caras detectadas
    cv2.imshow('Face Tracking', frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
video_capture.release()
cv2.destroyAllWindows()