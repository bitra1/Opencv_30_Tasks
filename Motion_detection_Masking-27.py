import cv2
import numpy as np

# Load video capture
video = cv2.VideoCapture(r"C:\Users\Guest account\Desktop\Narasimha Murthy\07-08-24-murthy\GISUS3043C1_2024-08-07_13-00-52_2024-08-07_14-00-52.mp4")  # Replace with 0 to use webcam

# Create a mask with the same dimensions as the video frame
ret, frame = video.read()
mask = np.zeros_like(frame, dtype=np.uint8)

# Define the region of interest (ROI) on the mask
# Example: Focus on a rectangular region
cv2.fillPoly(mask, [np.array([[129, 180],[280, 109],[346,139],[178,232]])],255) # Adjust the coordinates

# Convert mask to grayscale
mask_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

# Initialize the first frame for background subtraction
first_frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
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

    # Apply the mask to focus on the ROI
    diff_frame_masked = cv2.bitwise_and(diff_frame, diff_frame, mask=mask_gray)

    # Apply a threshold to get the binary image
    _, thresh = cv2.threshold(diff_frame_masked, 25, 255, cv2.THRESH_BINARY)

    # Dilate the thresholded image to fill in holes
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Find contours within the masked and thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes around detected motion
    for contour in contours:
        if cv2.contourArea(contour) > 500:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.polylines(frame,[np.array([[129, 180],[280, 109],[346,139],[178,232]])],True,(0,255,0),1)

    # Display the result

    cv2.imshow('Masked Motion Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(250) & 0xFF == ord('q'):
        break

# Release video capture and close windows
video.release()
cv2.destroyAllWindows()

'''---------------------------------motion detection on mask-out operation----------------------------------------------'''
# import cv2
#
# cap = cv2.VideoCapture(r"C:\Users\Guest account\Desktop\Narasimha Murthy\07-08-24-murthy\GISUS3043C1_2024-08-07_13-00-52_2024-08-07_14-00-52.mp4")
#
# ret,frame = cap.read()
#
# gray_reference = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
# gray_reference = cv2.GaussianBlur(gray_reference,(21,21),0)
#
# mask = np.zeros(frame.shape[:2],dtype=np.uint8)
# cv2.fillPoly(mask,[np.array([[1,69],[102,32],[356,125],[6,324]])],255)
#
# while True:
#     ret,frame = cap.read()
#     if not ret:
#         break
#
#     gray_current = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     gray_current = cv2.GaussianBlur(gray_current,(21,21),0)
#
#     diff = cv2.absdiff(gray_reference,gray_current)
#
#     inverse_masking = cv2.bitwise_not(mask)
#     masking = cv2.bitwise_and(diff, diff, mask=inverse_masking)
#
#     _,thresh = cv2.threshold(masking,25,255,cv2.THRESH_BINARY)
#
#     thresh = cv2.dilate(thresh,None,iterations=2)
#
#     contours , _ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#     for contour in contours:
#         if cv2.contourArea(contour) < 500:
#             continue
#         x,y,w,h = cv2.boundingRect(contour)
#         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
#     cv2.polylines(frame,[np.array([[1,69],[102,32],[356,125],[6,324]])],True,(0,0,255),1)
#     cv2.imshow('Mask Out',frame)
#
#     if cv2.waitKey(150) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
