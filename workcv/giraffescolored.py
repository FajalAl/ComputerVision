import cv2

img = cv2.imread("giraffes.jpg", cv2.IMREAD_COLOR)
cv2.imshow(" Giraffes SCII/02157/2020", img)
cv2.waitKey(0)
cv2.destroyAllWindows()