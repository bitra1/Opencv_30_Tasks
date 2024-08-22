'''----------------------------Difference between to images------------------------------------------------'''

import cv2

# Load two images
image1 = cv2.imread(r"E:\python-images\w1.jpeg")
image2 = cv2.imread(r"E:\python-images\w2.jpeg")

# Convert images to grayscale
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)



# Calculate the absolute difference between the two images
diff = cv2.absdiff(gray1, gray2)

# Threshold the difference to get the binary image (highlight changes)
_, diff_thresh = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)

contours,_ = cv2.findContours(diff_thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    if cv2.contourArea(contour) >100:
        continue
    x,y,w,h = cv2.boundingRect(contour)
    cv2.rectangle(image2,(x,y),(x+w,y+h),(0,255,0),2)

# Display the results
cv2.imshow('Difference', diff)
cv2.imshow('Thresholded Difference', diff_thresh)
cv2.imshow('Image-1',image1)
cv2.imshow('Image-2',image2)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''----------------------------Difference between to videos------------------------------------------------'''
# import cv2
#
# # Load the two video files
# video1 = cv2.VideoCapture(r"C:\Users\Guest account\Desktop\Narasimha Murthy\1 hr\counts_GISUS3043C1_2024-08-03_11-00-11_2024-08-03_12-00-11.mp4")
# video2 = cv2.VideoCapture(r"C:\Users\Guest account\Desktop\Narasimha Murthy\1 hr\counts_GISUS3043C1_2024-08-03_12-00-11_2024-08-03_13-00-11.mp4")
#
# # Check if the videos opened successfully
# if not video1.isOpened() or not video2.isOpened():
#     print("Error: Could not open one or both videos.")
#     exit()
#
# while True:
#     # Read the next frame from each video
#     ret1, frame1 = video1.read()
#     ret2, frame2 = video2.read()
#
#     # Break the loop if we reach the end of either video
#     if not ret1 or not ret2:
#         break
#
#     # Resize frames to the same size if necessary
#     frame2 = cv2.resize(frame2, (frame1.shape[1], frame1.shape[0]))
#
#     # Convert frames to grayscale
#     gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
#     gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
#
#     # Compute the absolute difference between the two frames
#     diff_frame = cv2.absdiff(gray1, gray2)
#
#     # Apply a threshold to highlight significant differences
#     _, diff_thresh = cv2.threshold(diff_frame, 25, 255, cv2.THRESH_BINARY)
#
#     # Optionally, dilate the thresholded image to fill in holes
#     diff_thresh = cv2.dilate(diff_thresh, None, iterations=2)
#
#     # Display the original frames and their difference
#     cv2.imshow('Video 1', frame1)
#     cv2.imshow('Video 2', frame2)
#     cv2.imshow('Difference', diff_thresh)
#
#     # Break the loop on 'q' key press
#     if cv2.waitKey(5) & 0xFF == ord('q'):
#         break
#
# # Release the video captures and close windows
# video1.release()
# video2.release()
# cv2.destroyAllWindows()
#
