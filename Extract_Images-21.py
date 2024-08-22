import os
import cv2

outputdir = r"C:\Users\Guest account\Desktop\Narasimha Murthy\murthy123"

if not os.path.exists(outputdir):
    os.makedirs(outputdir)

cap = cv2.VideoCapture(r"C:\Users\Guest account\Desktop\Narasimha Murthy\07-08-24-murthy\GISUS3043C1_2024-08-07_13-00-52_2024-08-07_14-00-52.mp4")

if not cap.isOpened():
    print('Error')
    exit()

frame_count = 0
while(True):
    rat,frame = cap.read()
    if not rat:
        break

    frame_num = os.path.join(outputdir,f'frame_{frame_count:04d}.jpg')
    cv2.imwrite(frame_num,frame)
    frame_count +=1
cap.release()
