import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalcatface.xml')
#eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')

while True:
    
    # Read the input image
    img = cv2.imread('cat.jpg')

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
    
        #roi_gray = gray[y:y+h, x:x+w]
        #roi_color = img[y:y+h, x:x+w]
    
        #eyes = eye_cascade.detectMultiScale(roi_gray,1.1,4)
        #print(eyes)
        #for (ex,ey,ew,eh) in eyes:
            #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    
    cv2.imshow('img',img)
    #cv2.imshow('img',roi_gray)
# Stop if escape key is pressed
    
    if cv2.waitKey() == 27:
        break
        
cv2.destroyAllWindows()