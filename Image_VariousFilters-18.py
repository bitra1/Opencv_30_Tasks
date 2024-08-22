import cv2
import numpy as np

img = cv2.imread(r'E:\python-images\image4.jpg')
Gray_Image = cv2.GaussianBlur(img,(15,15),sigmaX=0)

canny_image = cv2.Canny(img,100,200)

median_image = cv2.medianBlur(img,ksize=5)

kernal_array = np.array([[-1,-1,-1],
                         [-1,9,-1],
                         [-1,-1,-1]])

filter_2d = cv2.filter2D(img,ddepth=-1,kernel=kernal_array)
Bilateral_Filter = cv2.bilateralFilter(img, d=15, sigmaColor=75, sigmaSpace=75)

sobel_filter_x = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)

sobel_filter_y = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)

Laplacian_Image = cv2.Laplacian(Gray_Image,cv2.CV_64F,ksize=3)
# cv2.imshow('Orginal_Image',img)
# cv2.imshow('Gray_Image',Gray_Image)
# cv2.imshow('Canny_Image',canny_image)
# cv2.imshow('Median_image',median_image)
# cv2.imshow('Filter_2D',filter_2d)
# # cv2.imshow('Bilateral_Filter',Bilateral_Filter)
# cv2.imshow('sobel_x',sobel_filter_x)
# cv2.imshow('sobel_y',sobel_filter_y)
cv2.imshow('Laplacian_Image',Laplacian_Image)
cv2.waitKey(0)
cv2.destroyAllWindows()