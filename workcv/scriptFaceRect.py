import cv2 as cv
#import numpy as np

face_cascade = cv.CascadeClassifier(cv.data.haarcascades +'haarcascade_frontalface_default.xml')


cap = cv.VideoCapture('Denis.jpg')

while True:
    # Read the frame
    ret, colorFrame = cap.read()

    # Convert to grayscale
    grayFrame = cv.cvtColor(colorFrame, cv.COLOR_BGR2GRAY)
    
    # Detect the faces
    faces = face_cascade.detectMultiScale(colorFrame, 1.1, 4)
    
    print(faces)
    
    # Draw the rectangle around each
    for (x, y, w, h) in faces:
        cv.rectangle(colorFrame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Display
    cv.imshow('Nadia', colorFrame)
# Stop if q key is pressed
    if cv.waitKey(0) & 0xFF == ord('q'):
        break
        
# Release the VideoCapture object
cap.release()
cv.destroyAllWindows()