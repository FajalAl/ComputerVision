import cv2 as cv
#import numpy as np

face_cascade = cv.CascadeClassifier(cv.data.haarcascades +'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades+ 'haarcascade_eye.xml')

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

while True:
    # Read the frame
    ret, colorFrame = cap.read()
    # Convert to grayscale
    grayFrame = cv.cvtColor(colorFrame, cv.COLOR_BGR2GRAY)
    
    # Detect the faces
    faces = face_cascade.detectMultiScale(colorFrame, 1.1, 4)
    print(faces)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv.rectangle(colorFrame, (x, y), (x+w, y+h), (0, 255, 0), 4)
        roi_color = colorFrame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_color, 1.1,2)
        print(eyes)
        for (a,b,c,d) in eyes:
            cv.rectangle(roi_color,(a,b),(a+c,b+d),(0,0,255),2)
    # Display
    cv.imshow('Nadia', colorFrame)
# Stop if q key is pressed
    if cv.waitKey(0) & 0xFF == ord('q'):
        break
# Release the VideoCapture object
cap.release()
cv.destroyAllWindows()

