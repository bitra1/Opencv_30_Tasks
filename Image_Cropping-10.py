import cv2

img = cv2.imread(r"E:\python-images\5.png")

if img is None:
    print('Please Check the Source Path')

else:
    # x_start,y_start,x_end,y_end = 0,675,600,675
    image_crop = img[0:582 , 600:1200]
    cv2.imshow('Cropped_image',image_crop)
    cv2.imwrite('E:\python-images\murthy2.jpg',image_crop)
    print('sucessfully cropped and save the image')
    cv2.waitKey(0)
    cv2.destroyAllWindows()