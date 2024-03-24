import cv2

# Open a connection to the camera (webcam)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Create a window to display the camera output
cv2.namedWindow("Camera Output", cv2.WINDOW_NORMAL)

# Loop to continuously capture frames from the camera and display them
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Could not capture frame.")
        break

    # Display the frame in the window
    cv2.imshow("Camera Output", frame)

    # Check for key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close any open windows
cap.release()
cv2.destroyAllWindows()
