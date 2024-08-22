import cv2

face_cascade = cv2.CascadeClassifier(r'E:\Face_Reg\haarcascade_frontalface_default.xml')

image = cv2.imread(r'E:\python-images\people1.jpg')

#gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(image, scaleFactor=1.1,minNeighbors=5 )

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w , y+h), (255,0,0),2)

cv2.imshow('People_image',image)
#cv2.imshow('Gray_image',gray)

cv2.waitKey(0)
cv2.destroyAllWindows()