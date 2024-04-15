import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use CAP_DSHOW as an alternative backend

while True:
    ret, image = cap.read()

    if not ret:
        print("Error: Unable to capture frame")
        break

    cv2.imshow('myphoto', image)
    cv2.imwrite('myphoto.jpg', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
