import cv2 as cv

# Load the cascade
catFace_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalcatface.xml')

# Check if the cascade is loaded correctly
if catFace_cascade.empty():
    print("Error loading cascade classifier.")
    exit()

# Read the image
colorFrame = cv.imread(r'C:\Users\ADMIN\OneDrive\Desktop\happy\cat.jpg')

# Check if the image is read correctly
if colorFrame is None:
    print("Error loading image.")
    exit()

# Convert to grayscale
grayFrame = cv.cvtColor(colorFrame, cv.COLOR_BGR2GRAY)

# Detect the faces
faces = catFace_cascade.detectMultiScale(grayFrame, scaleFactor=1.1, minNeighbors=4)

# Draw the rectangle around each face
for (x, y, w, h) in faces:
    cv.rectangle(colorFrame, (x, y), (x+w, y+h), (0, 255, 0), 4)

# Display the result
cv.imshow('Cat', colorFrame)
cv.waitKey(0)
cv.destroyAllWindows()
