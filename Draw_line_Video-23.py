#Draw a line,rectangle,circle and polygon on image

# import cv2
# import numpy as np
# image = cv2.imread(r"E:\python-images\image4.jpg")
#
# cv2.line(image,(134,47),(367,46),(255,0,0),5)
# cv2.rectangle(image,(110,248),(223,285),(0,255,0),5)
# cv2.circle(image,(300,209),50,(0,0,255),5)
# cv2.circle(image,(172,191),25,(255,255,255),5)
# points = np.array([[318, 83], [367, 105], [370, 152], [312, 173],[262,152],[261,175],[509,206],[472,238],[432,260],[447,220],[411,198]], np.int32)
# cv2.polylines(image,[points],True,(0,0,0),5)
# cv2.imshow('Orginal_image',image)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#Draw a line,rectangle,circle and polygon on videos

import cv2
import numpy as np
cap = cv2.VideoCapture(r"C:\Users\Guest account\Desktop\Narasimha Murthy\video.mp4")


if not cap.isOpened():
    print('Error')
    exit()

while True:
    rat,frame = cap.read()
    if not rat:
        break

    cv2.line(frame,(50,50),(450,50),(0,0,255),5)
    cv2.rectangle(frame,(50,100),(200,50),(255,0,0),5)
    cv2.circle(frame,(100,200),50,(0,0,255),5)
    points = np.array(
        [[318, 83], [367, 105], [370, 152], [312, 173], [262, 152], [261, 175], [509, 206], [472, 238], [432, 260],
         [447, 220], [411, 198]], np.int32)
    cv2.polylines(frame,[points],True,(255,0,0),5)
    cv2.imshow('Video_Capture',frame)
    if cv2.waitKey(4) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
