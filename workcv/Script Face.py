import cv2 as cv
import numpy as np

face_cascade = cv.CascadeClassifier(cv.data.haarcascades +'haarcascade_frontalface_default.xml')


img = cv.imread('Nadia.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img, 1.1, 4)

for x,y,w,h in faces:
    
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 4)
    
    cv.imshow('img', img)
    
    k = cv.waitKey(0) & 0xff
    if k==27:
        break

cv.waitKey()
cv.destroyAllWindow