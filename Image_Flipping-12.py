import cv2

img = cv2.imread('E:\python-images\image6.jpg')


horizontally_flipped = cv2.flip(img, 1)

# Flip the image vertically
vertically_flipped = cv2.flip(img, 0)

# Flip the image both horizontally and vertically
both_flipped = cv2.flip(img, -1)

cv2.imshow('orginal_img',img)

cv2.imshow('horizontally_flipped',horizontally_flipped)
cv2.imshow('vertically_flipped',vertically_flipped)
cv2.imshow('both_flipped',both_flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()