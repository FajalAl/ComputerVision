import cv2
cap=cv2.VideoCapture(0)

while True:
  ret,image = cap.read()
  cv2.imshow('myphoto',image)
  cv2.imwrite('myphoto.jpg',image)


  if cv2.waitKey(8000) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()