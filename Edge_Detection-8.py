import cv2

img = cv2.imread('E:\\python-images\image4.jpg')

if img is None:
    print('Please once check the Source path')

else:
    Edge_Detection = cv2.Canny(img,threshold1=100,threshold2=200)
    Edge_Detection1 = cv2.Canny(img,threshold1=200,threshold2=300)

    cv2.imshow('Edge_Detection',Edge_Detection)
    cv2.imshow('Edge_Detection1',Edge_Detection1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()