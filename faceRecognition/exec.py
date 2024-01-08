import cv2
import numpy as np

image = cv2.imread("faceRecognition/photo.jpg")

detector = cv2.CascadeClassifier("faceRecognition/haarcascade_frontalface_alt.xml")

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    #capture.read()
    #frame = capture.get()

    faces = detector.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if faces:
        face = faces[0]
        points = face[:, :2]

        points = np.array(points, dtype="int")

        roi = frame[points[1]:points[3],points[0]:points[2]]

        similarity = cv2.matchTemplate(roi, image, cv2.TM_CCOEFF_NORMED)

        if similarity > 0.9:
            print("Person detected.")
        else:
            print("Person not found.")

        cv2.imshow("Frame", frame)

        k = cv2.waitKey(1)
        if k == 27:
            break
capture.release()

# Destruir todas las ventanas.
cv2.destroyAllWindows()