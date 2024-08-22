#Motion Detection on images
import cv2
import numpy as np

# Load the two images
image1 = cv2.imread(r"E:\python-images\frame_1076.jpg")
image2 = cv2.imread(r"E:\python-images\frame_1077.jpg")

# Convert the images to grayscale
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Optionally, apply Gaussian blur to reduce noise
gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)
gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

# Compute the absolute difference between the two images
diff = cv2.absdiff(gray1, gray2)

# Apply a binary threshold to the difference image
_, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

# Optional: Apply morphological operations to clean up the image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# Find contours in the thresholded image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw bounding boxes around detected motion areas
for contour in contours:
    # if cv2.contourArea(contour) < 500:  # Ignore small contours
    #     continue
    (x, y, w, h) = cv2.boundingRect(contour)
    cv2.rectangle(image1, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.rectangle(image2, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the results
cv2.imshow('Motion Detection Image 1', image1)
cv2.imshow('Motion Detection Image 2', image2)
cv2.imshow('Difference Image', diff)
cv2.imshow('Thresholded Image', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''--------------------------------Motion Detection on Video------------------------------------------'''
# import cv2
#
# # Initialize video capture (0 for webcam or provide a video file path)
# cap = cv2.VideoCapture(r"C:\Users\Guest account\Desktop\Narasimha Murthy\07-08-24-murthy\GISUS3043C1_2024-08-07_13-00-52_2024-08-07_14-00-52.mp4")
#
# # Read the first frame to initialize the background
# ret, frame = cap.read()
# gray_reference = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# gray_reference = cv2.GaussianBlur(gray_reference, (21, 21), 0)
#
# while True:
#     # Capture the current frame
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     # Convert the current frame to grayscale and blur it
#     gray_current = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     gray_current = cv2.GaussianBlur(gray_current, (21, 21), 0)
#
#     # Compute the absolute difference between the reference frame and the current frame
#     diff_image = cv2.absdiff(gray_reference, gray_current)
#
#     # Apply a binary threshold to the difference image
#     _, thresh = cv2.threshold(diff_image, 25, 255, cv2.THRESH_BINARY)
#
#     # Dilate the thresholded image to fill in gaps
#     thresh = cv2.dilate(thresh, None, iterations=2)
#
#     # Find contours in the thresholded image
#     contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#     # Draw bounding boxes around the detected contourss
#     for contour in contours:
#         # if cv2.contourArea(contour) < 500:  # Ignore small areas of motion
#         #     continue
#         (x, y, w, h) = cv2.boundingRect(contour)
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#     # Display the results
#     cv2.imshow('Motion Detection', frame)
#
#     # Update the reference frame to adapt to the scene (optional)
#     gray_reference = gray_current
#
#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(100) & 0xFF == ord('q'):
#         break
#
# # Release the video capture and close windows
# cap.release()
# cv2.destroyAllWindows()
#
#
#
#
#
#
