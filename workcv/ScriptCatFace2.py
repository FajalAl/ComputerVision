import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')

# Read the input image
img = cv2.imread('cat.jpg')

# Check if the image is read correctly
if img is None:
    print("Error loading image.")
    exit()

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
print(faces)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display
cv2.imshow('img', img)

# Stop if escape key is pressed
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
