import cv2
from mtcnn import MTCNN

# Inicializa la cámara
cap = cv2.VideoCapture(1)

detector = MTCNN()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    caras = detector.detect_faces(frame)

    for face in caras:
        x, y, w, h = face['box']
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Detector de Caras', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
