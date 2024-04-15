import cv2

# Open the default camera (camera index 0)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can choose other codecs like 'MJPG' or 'MP4V'
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # Adjust parameters as needed

# Read and display frames from the camera until the user presses 'q'
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If the frame is read correctly, ret will be True
    if not ret:
        print("Error: Failed to capture frame.")
        break

# Write the frame to the video file
    out.write(frame)

    # Display the frame
    cv2.imshow('Video Capture', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
