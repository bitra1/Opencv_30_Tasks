# import cv2
#
# img = cv2.imread('E:\python-images\image4.jpg')
#
# if img is None:
#     print('Check the Source path You are Entered')
#
# else:
#     convert_grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     cv2.imshow('Image_GRAWSCALE',convert_grayscale)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

import cv2

img = cv2.imread('E:\python-images\image4.jpg',flags=0)  #flags = cv2.IMREAD_GRAYSCALE
cv2.imshow('Image_grayscale',img)
cv2.waitKey()
cv2.destroyAllWindows()