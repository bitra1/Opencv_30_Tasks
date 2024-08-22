#MASKIN on IMAGES
# import cv2
# import numpy as np
#
# # Load an image
# img = cv2.imread("E:\python-images\image4.jpg")
#
# # Create a circular mask
# mask = np.zeros(img.shape[:2], dtype="uint8")
# #cv2.circle(mask, (150, 150), 100, 255, -1)
# cv2.rectangle(mask, (28, 22),(575,362),(255,255,255),-1)
#
# # Apply the mask (Mask In operation)
# masked_img = cv2.bitwise_and(img, img, mask=mask)
# cv2.imshow('Orginal_Image',img)
# cv2.imshow('Mask_Image',mask)
# cv2.imshow("Masked In Image", masked_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#MASK-IN on Videos
import cv2
import numpy as np

cap = cv2.VideoCapture(r"C:\Users\Guest account\Desktop\Narasimha Murthy\video.mp4")

while(True):
    rat,frame = cap.read()
    if not rat:
        break

    mask = np.zeros(frame.shape[:2],dtype='uint8')
    cv2.circle(mask,(frame.shape[1]//2,frame.shape[0]//2),100,(255,255,255),-1)
    masked_frame = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('Video',masked_frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
