import cv2

img = cv2.imread('E:\python-images\image4.jpg')

if img is None:
    print('please once check the source path')

else:
    Gaussian_blur = cv2.GaussianBlur(img,ksize=(15,15),sigmaX=0)
    Median_blur = cv2.medianBlur(img,ksize=11)
    normal_blur = cv2.blur(img,ksize=(15,15))
    cv2.imshow('normal image',img)
    cv2.imshow('Gaussion_blur',Gaussian_blur)
    cv2.imshow('Median_blur',Median_blur)
    cv2.imshow('blur',normal_blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()