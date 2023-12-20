import cv2
from mtcnn import MTCNN
import matplotlib.pyplot as plt

def contador(image_path):
    img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

    detector = MTCNN()

    caras = detector.detect_faces(img)

    for face in caras:
        x, y, w, h = face['box']
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    plt.imshow(img)
    plt.axis('off')
    plt.show()

    return len(caras)

n_caras = contador('imagen1.jpeg')
print("Número de caras:", n_caras)