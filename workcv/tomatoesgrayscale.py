import cv2


img = cv2.imread("tomatoes.png", 0)
cv2.imshow("Tomatoes SCII/02157/2020", img)
cv2.waitKey(0)
cv2.destroyAllWindows()