
import cv2
def detectar_caras_en_camara():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)

    while True:
        ret, img = cap.read()
        if not ret:
            break

        escala_grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        caras = face_cascade.detectMultiScale(escala_grises, 1.1, 4)

        for (x, y, w, h) in caras:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('Detección de Caras', img)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

detectar_caras_en_camara()
