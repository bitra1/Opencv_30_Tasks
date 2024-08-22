import cv2
import numpy as np

# Load video capture
video = cv2.VideoCapture(r"C:\Users\Guest account\Desktop\Narasimha Murthy\07-08-24-murthy\GISUS3043C1_2024-08-07_13-00-52_2024-08-07_14-00-52.mp4")  # Replace with 0 to use webcam

# Check if the video opened successfully
if not video.isOpened():
    print("Error: Could not open video.")
    exit()

# Initialize the first frame for background subtraction
ret, first_frame = video.read()
# if not ret:
#     print("Error: Could not read the first frame.")
#     video.release()
#     cv2.destroyAllWindows()
#     exit()

first_frame_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_frame_gray = cv2.GaussianBlur(first_frame_gray, (21, 21), 0)

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Convert the current frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Compute the absolute difference between the current frame and the first frame
    diff_frame = cv2.absdiff(first_frame_gray, gray)

    # Apply a threshold to get the binary image
    _, thresh = cv2.threshold(diff_frame, 25, 255, cv2.THRESH_BINARY)

    # Dilate the thresholded image to fill in holes
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Find contours within the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours or rectangles around detected motion
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Adjust the area threshold as needed
            # Option 1: Draw a rectangle
            # x, y, w, h = cv2.boundingRect(contour)
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Option 2: Draw the contour
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)

    # Display the result
    cv2.imshow('Motion Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

# Release video capture and close windows
video.release()
cv2.destroyAllWindows()
