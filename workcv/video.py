import cv2

cap = cv2.VideoCapture('Cars.mp4')

while cap.isOpened():
    ret, im = cap.read()
    cv2.imshow('playvideotest', im)
    
    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

cap.release()
cv2.destroyAllWindows()
