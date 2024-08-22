# import cv2
# import numpy as np
#
# img = cv2.imread('E:\python-images\image6.jpg')
#
# mask = np.zeros(img.shape[:2],dtype = "uint8")
#
# cv2.circle(mask , (img.shape[1] // 2 , img.shape[0] // 2) ,100 ,255,-1)
#
# masked_image = cv2.bitwise_and(img,img,mask=mask)
#
# cv2.imshow('Orginal_image',img)
# cv2.imshow('Masked_image',masked_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# import numpy as np
#
# img = cv2.imread('E:\\python-images\\image6.jpg')
#
# mask = np.zeros(img.shape[:2],dtype="uint8")
#
#
# cv2.circle(mask, (img.shape[1]//2 , img.shape[0]//2),100,255,-1)
#
# masking_image = cv2.bitwise_and(img,img,mask=mask)
#
# cv2.imshow('Orginal Image',img)
#
# cv2.imshow('Masking_image',masking_image)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#
import cv2

img = cv2.imread(r'E:\python-images\image6.jpg')

mask = cv2.imread(r'E:\python-images\mask3.jpg',flags=cv2.IMREAD_GRAYSCALE)

masking_image = cv2.bitwise_and(img,img,mask=mask)


cv2.imshow('Orginal_image',img)
cv2.imshow('Black and White',mask)
cv2.imshow('Masking_image',masking_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# import cv2
# import numpy as np
# # Load an image
# image = cv2.imread(r'E:\python-images\image6.jpg')
#
# size = np.array(image.shape)
#
# # Define the center, radius, and color of the circle
# center = (size[1]//2, size[0]//2)  # x=100, y=100
# radius = 50  # Radius of the circle
# color = (0, 255, 0)  # Green color in BGR format
#
# # Draw the circle on the image
# cv2.circle(image, center, radius, color, thickness=5)
#
# # Save or display the image with the circle
# #cv2.imwrite('circle_image.jpg', image)
# cv2.imshow('Circle Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
