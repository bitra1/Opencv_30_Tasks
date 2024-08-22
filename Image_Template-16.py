import cv2
import numpy as np
image = cv2.imread(r"E:\python-images\india2.jpg",cv2.IMREAD_GRAYSCALE)
template = cv2.imread(r"E:\python-images\virat1.jpg",cv2.IMREAD_GRAYSCALE)

# convert_image = cv2.resize(template,(500,500))
# cv2.imwrite(r'E:\python-images\cocacola2.jpg',convert_image)
# print('Image saved successfully')

result = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)

min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)

top_left = max_loc
height , weight = template.shape[:2]
bottom_right = (top_left[0] + weight , top_left[1] + height)

cv2.rectangle(image,top_left,bottom_right,(0,255,0),5)

# matched_image = image.copy()

cv2.imshow('Image',image)
cv2.imshow('Template',template)
cv2.imshow('Detected Template', cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
cv2.waitKey(0)
cv2.destroyAllWindows()
