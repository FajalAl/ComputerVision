import cv2 as cv
import numpy as np

# SCII/02157/2020
car_cascade = cv.CascadeClassifier('cars.xml')

img = cv.imread(r'C:\Users\ADMIN\OneDrive\Desktop\happy\cars.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cars = car_cascade.detectMultiScale(img, 1.1, 4)
print(cars)
for x,y,w,h in cars:
    
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 4)
    
    cv.imshow('img', img)
    
    k = cv.waitKey(0) & 0xff
    if k==27:
        break

cv.imshow('img', img)

cv.waitKey()
cv.destroyAllWindows()