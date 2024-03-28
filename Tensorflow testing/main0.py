from movenet import *
import pickle

## Load the input image
# image_path = 'input_image.jpeg'
image_path = r"D:\University\sem2\Python\PythonSem2FinalProject\Tensorflow testing\input_image.jpeg"  # Replace with your image path
image1 = tf.io.read_file(image_path)
image1 = tf.image.decode_jpeg(image1)


# input_image = tf.expand_dims(image, axis=0)
# input_image = tf.image.resize_with_pad(input_image, input_size, input_size)

# # Run model inference.
# keypoints = movenet1(input_image)
# # Visualize the predictions with image.
# display_image = tf.expand_dims(image, axis=0)
# display_image = tf.cast(tf.image.resize_with_pad(
#     display_image, 1280, 1280), dtype=tf.int32)
# output_overlay = draw_prediction_on_image(
#     np.squeeze(display_image.numpy(), axis=0), keypoints)


# Open a connection to the camera (webcam)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()
# Loop to continuously capture frames from the camera and display them
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Could not capture frame.")
        break
    image = image1
    # Display the frame in the window
    # cv2.imshow("Camera Output", frame)

    input_image = tf.expand_dims(image, axis=0)
    input_image = tf.image.resize_with_pad(input_image, input_size, input_size)

    # Run model inference.
    keypoints = movenet1(input_image)
    # Visualize the predictions with image.
    display_image = tf.expand_dims(image, axis=0)
    display_image = tf.cast(tf.image.resize_with_pad(
        display_image, 1280, 1280), dtype=tf.int32)
    output_overlay = draw_prediction_on_image(
        np.squeeze(display_image.numpy(), axis=0), keypoints)

    cv2.imshow("Output", output_overlay)
    # Check for key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close any open windows
cap.release()
cv2.destroyAllWindows()

# plt.figure(figsize=(5, 5))
# plt.axis('off')
# plt.show()
