import cv2
import matplotlib.pyplot as plt

img = cv2.imread('E:\python-images\image4.jpg')

histogram_imag = cv2.calcHist([img],[0],None,[255],[0 ,256])

cv2.imshow('Orginal_Image',img)
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel('Frequency')
plt.plot(histogram_imag)
plt.xlim([0,256])
plt.show()

cv2.waitKey(0)

cv2.destroyAllWindows()