import cv2
import cv2.data
import os

#print(os.listdir(cv2.data.haarcascades))
filename= "haarcascade_frontalface_default.xml"
path = cv2.data.haarcascades+ filename
modal = cv2.CascadeClassifier(path)


image = cv2.imread("group.jpg")
faces = modal.detectMultiScale(image,1.3,3)
print(faces)
for face in faces:
    x1 = face[0]
    y1 = face[1]
    x2 = x1 + face[2]
    y2 = y1 + face[3]
    cv2.rectangle(image,(x1,y1),(x2,y2),[255,255,255],2)

image = cv2.resize(image,(600,400))
cv2.imshow("persons image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()