import cv2

def contador(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    img = cv2.imread(image_path)
    escala_grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    caras = face_cascade.detectMultiScale(escala_grises, 1.1, 4)

    for (x, y, w, h) in caras:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Caras', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return len(caras)


n_caras = contador('imagen1.jpeg')
print("Caras detectadas:", n_caras)