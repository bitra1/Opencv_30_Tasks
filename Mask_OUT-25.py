# #MASKOUT
# import cv2
# import numpy as np
#
# # Load an image
# img = cv2.imread("E:\python-images\image4.jpg")
#
# # Create a circular mask
# mask = np.zeros(img.shape[:2], dtype="uint8")
# cv2.rectangle(mask, (28, 22),(475,362),(255,255,255),-1)
#
# # Invert the mask for Mask Out operation
# inverse_mask = cv2.bitwise_not(mask)
#
# # Apply the mask (Mask Out operation)
# masked_img = cv2.bitwise_and(img, img, mask=inverse_mask)
#
# cv2.imshow("Masked Out Image", masked_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#

import cv2
import numpy as np

cap = cv2.VideoCapture(r"C:\Users\Guest account\Desktop\Narasimha Murthy\video.mp4")

if not cap.isOpened():
    print('Error')
    exit()

while(True):
    rat,frame = cap.read()
    if not rat:
        break

    mask = np.zeros(frame.shape[:2],dtype=np.uint8)
    cv2.circle(mask,(frame.shape[1]//2,frame.shape[0]//2),100,(255,255,255),-1)
    inversed_mask = cv2.bitwise_not(mask)
    masked_out = cv2.bitwise_and(frame,frame,mask=inversed_mask)

    cv2.imshow('Orginal_Video',masked_out)
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

