import cv2

img = cv2.imread('E:\python-images\image4.jpg',flags=cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Check the source path Address')

else:
    retval,threshold_img = cv2.threshold(img,thresh=150,maxval=255,type=cv2.THRESH_BINARY)
    # retval1,threshold_img1 = cv2.threshold(img,thresh=127,maxval=255,type=cv2.THRESH_BINARY_INV)
    # retval2,threshold_img2 = cv2.threshold(img,thresh=127,maxval=255,type=cv2.THRESH_TRUNC)
    # retval3,threshold_img3 = cv2.threshold(img,thresh=127,maxval=255,type=cv2.THRESH_TOZERO)
    # retval4,threshold_img4 = cv2.threshold(img,thresh=127,maxval=255,type=cv2.THRESH_TOZERO_INV)

    cv2.imshow('normal_image',img)


    cv2.imshow('Binary',threshold_img)
    # cv2.imshow('Binary_inverse',threshold_img1)
    # cv2.imshow('Trunc',threshold_img2)
    # cv2.imshow('ToZero',threshold_img3)
    # cv2.imshow('ToZero_inverse',threshold_img4)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
