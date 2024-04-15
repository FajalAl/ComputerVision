import cv2
import numpy as np

# Create a black image (all zeros) with dimensions 500x500 and 3 channels (RGB)
image = np.zeros((500, 500, 3), dtype=np.uint8)

# Define the rectangle parameters
top_left = (100, 100)
bottom_right = (400, 400)
color = (0, 255, 0)  # RGB color (green in this case)
thickness = 2  # Thickness of the rectangle

# Draw the rectangle on the image
cv2.rectangle(image, top_left, bottom_right, color, thickness)

# Display the image
cv2.imshow('Rectangle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
