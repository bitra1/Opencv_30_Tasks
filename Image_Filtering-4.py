import cv2
import numpy as np

img = cv2.imread('E:\python-images\image4.jpg')

kernal_array = np.array([[-1,-1,-1],
                         [-1,9,-1],
                         [-1,-1,-1]])

Blurring = cv2.GaussianBlur(img,ksize=(29,29),sigmaX=0)
Sharpening = cv2.filter2D(img,ddepth=-1,kernel=kernal_array)
EdgeDetection = cv2.Canny(img,threshold1=200,threshold2=300)
MedianFiltering = cv2.medianBlur(img,ksize=5)
Bilateral_Filter = cv2.bilateralFilter(img, d=15, sigmaColor=75, sigmaSpace=75)

cv2.imshow('Normal_Image',img)
cv2.imshow('GRAYSCALE_IMAGE',Blurring)
cv2.imshow('Filter2D_image',Sharpening)
cv2.imshow('Canny_image',EdgeDetection)
cv2.imshow('Median_Blur',MedianFiltering)
cv2.imshow('Bilateral_Filter',Bilateral_Filter)
cv2.waitKey()
cv2.destroyAllWindows()