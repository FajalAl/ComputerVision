import cv2

#img = cv2.imread("Nadia.jpg", cv2.IMREAD_COLOR)
img = cv2.imread("Nadia.jpg", 0)
cv2.imshow("Nadiaimage", img)
cv2.waitKey(0)
cv2.destroyAllWindows()