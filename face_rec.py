import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
webcam = cv2.VideoCapture(0)

while True:
    _, img = webcam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 4)
    
    c = 0
    for (x, y, w, h) in faces:
        c += 1
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Put the count text on the image
    cv2.putText(img, f'Faces detected: {c}', (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Face Detection", img)
    
    key = cv2.waitKey(10)
    if key == 27:
        print("Number of faces detected in last frame =", c)
        break

webcam.release()
cv2.destroyAllWindows()
