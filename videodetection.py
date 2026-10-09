import cv2
import cv2.data

filename = "haarcascade_frontalface_default.xml"
path = cv2.data.haarcascades + filename

modal = cv2.CascadeClassifier(path)

cam = cv2.VideoCapture(0)

while True:
    status, image = cam.read()
    if status == False:
        print("Camera Not Found..")
        break
    faces = modal.detectMultiScale(image,1.3,5)
    for face in faces:
        x1 = face[0]
        y1 = face[1]
        x2 = x1 + face[2]
        y2 = y1 + face[3]
        cv2.rectangle(image,(x1,y1),(x2,y2),[0,0,255],2)
    cv2.imshow("Face Detection",image)
    key = cv2.waitKey(1)
    if key == 97:
        cv2.destroyAllWindows()
        break