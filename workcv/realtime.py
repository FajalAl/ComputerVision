import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('outputmyvideo.avi', fourcc, 20.0, (640,480))

while cap.isOpened():
    ret, frame = cap.read()

    if ret==True:
        frame = cv2.flip(frame,1)
        out.write(frame)
        cv2.imshow('frame', frame)
        key = cv2.waitKey(1)

        if key == 27:
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
