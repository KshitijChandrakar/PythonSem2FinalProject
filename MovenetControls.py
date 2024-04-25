from movenet import *
FirstRun = 0

xavg, yavg, xstd, ystd, threshold = 0,0,0,0,3.3
xlist,ylist,xslist,yslist = [1] * 20, [1] * 20, [1] * 20, [1] * 20
def OpenCamera():
    global cap
    # Open a connection to the camera (webcam)
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()
    return cap
desired_height = 720
def whateverMovenetstuff(jump):
    global FirstRun, xlist,ylist, crop_region, image_height, image_width
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Could not capture frame.")
    frame = cv2.resize(frame, (int(desired_height * frame.shape[1] / frame.shape[0]), desired_height))
    image = frame
    # Display the frame in the window
    # cv2.imshow("Camera Output", frame)
    input_image = tf.expand_dims(image, axis=0)
    input_image = tf.image.resize_with_pad(input_image, input_size, input_size)
    if FirstRun == 0:
        image_height, image_width = frame.shape[:2]
        crop_region = init_crop_region(image_height, image_width)

    # Run model inference.
    # keypoints = movenet1(input_image)

    keypoints = run_inference(
      movenet1, frame, crop_region,
      crop_size=[input_size, input_size])
    crop_region = determine_crop_region(keypoints, image_height, image_width)
    # keypoint_locs,edges,edgeColors = keypoints_and_edges_for_display(keypoints, input_size, input_size)

    # Get Keypoint coords, edges, and edge colors and average it
    (keypoints_locs, edges_xy, edge_colors) = keypoints_and_edges_for_display(keypoints, image_width, image_height)
    cxavg, cyavg= np.mean(keypoints_locs, axis =0)
    # cxstd, cystd= np.std(keypoints_locs, axis =0)
    xlist = xlist[1:] + [cxavg,]
    ylist = ylist[1:] + [cyavg,]
    # xslist = xslist[1:] + [cxstd,]
    # yslist = yslist[1:] + [cystd,]
    if Outliers(xlist, threshold = threshold) or Outliers(ylist, threshold = threshold):
        print("Jumping Jack Jumping Jack")
        jump()

    ## Visualize the predictions with image.
    # display_image = tf.expand_dims(image, axis=0)
    # display_image = tf.cast(tf.image.resize_with_pad(
    #     display_image, 1280, 1280), dtype=tf.int32)
    # output_overlay = draw_prediction_on_image(
    #     np.squeeze(display_image.numpy(), axis=0), keypoints, close_figure=True, output_image_height=480)

    FirstRun = 1
    # cv2.imshow("Output", output_overlay)
    # Check for key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit(1)
        pass
