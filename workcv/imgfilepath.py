import cv2

path = r'C:\Users\ADMIN\OneDrive\Pictures\pink.jpg'

image = cv2.imread(path, 0)

cv2.imshow("Shadrack", image)

cv2.waitKey(0)

cv2.destroyAllWindows()
