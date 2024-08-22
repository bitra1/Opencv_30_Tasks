import cv2
import numpy as np

image1 = cv2.imread(r'E:\python-images\sky1.jpg')

image2 = cv2.imread(r'E:\python-images\aeroplan2.jpg')

print(image1.shape)
print(image2.shape)

if image1.shape != image2.shape:
    raise ValueError('Error Check the Source path')

blending_image = cv2.addWeighted(image1,0.8,image2,0.3,0.5)
# cv2.imshow("Sea_Image",image1)
# cv2.imshow("Aeroplan_image",image2)
cv2.imshow('blending_image',blending_image)


cv2.waitKey(0)
cv2.destroyAllWindows()