import cv2

img = cv2.imread(r"E:\python-images\nar2.png")

image_rescaling = cv2.resize(img,(455,403),interpolation=cv2.INTER_LINEAR)

cv2.imshow('Normal_image',img)
cv2.imshow('Image_Rescaling',image_rescaling)
cv2.imwrite(r"E:\python-images\nar22.png",image_rescaling)
cv2.waitKey(0)
cv2.destroyAllWindows()