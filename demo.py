'''--------------------------------------Motion Detection on Images--------------------------------------------------'''
#import numpy as np

# import  cv2
#
# image1 = cv2.imread(r"E:\python-images\frame_1076.jpg")
# image2 = cv2.imread(r"E:\python-images\frame_1077.jpg")
#
# gray_image1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
# gray_image2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
#
# gray_image1 = cv2.GaussianBlur(gray_image1,(21,21),0)
# gray_image2 = cv2.GaussianBlur(gray_image2,(21,21),0)
#
# diff = cv2.absdiff(gray_image1,gray_image2)
# _,thresh = cv2.threshold(diff,25,255,cv2.THRESH_BINARY)
#
# thresh = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel=cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)))
#
# contours,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#
# for contour in contours:
#     x,y,w,h = cv2.boundingRect(contour)
#     cv2.rectangle(image1,(x,y),(x+w,y+h),(0,255,0),2)
#     cv2.rectangle(image2,(x,y),(x+w,y+h),(0,0,255),2)
#
# cv2.imshow('Gray-Image1',image1)
# cv2.imshow('Gray-Image2',image2)
# cv2.imshow('Difference',diff)
# cv2.imshow('Threshold',thresh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''--------------------------Motion detection on videos---------------------------------'''
# import cv2
#
# cap = cv2.VideoCapture(r"C:\Users\Guest account\Desktop\Narasimha Murthy\circket.mp4")
# ret,frame = cap.read()
# gray_reference = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
# gray_reference = cv2.GaussianBlur(gray_reference,(21,21),0)
#
#
# while True:
#     ret,frame = cap.read()
#     if not ret:
#         break
#     gray_current = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     gray_current = cv2.GaussianBlur(gray_current,(21,21),0)
#
#     diff_image = cv2.absdiff(gray_reference,gray_current)
#
#     _,thresh = cv2.threshold(diff_image,25,255,cv2.THRESH_BINARY)
#
#     thresh = cv2.dilate(thresh,None,iterations=2)
#
#     contours,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#     for contour in contours:
#         print(contour)
#         print(cv2.contourArea(contour))
#         if cv2.contourArea(contour) <500:
#             continue
#         x,y,w,h = cv2.boundingRect(contour)
#         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
#     cv2.imshow('Video_Capture',frame)
#
#     gray_reference = gray_current
#     if cv2.waitKey(150) & 0xFF==ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

'''--------------------Motion detection on Mask-IN Operation----------------------------'''

# import cv2
# import numpy as np
#
# cap  = cv2.VideoCapture(r"C:\Users\Guest account\Desktop\Narasimha Murthy\07-08-24-murthy\GISUS3043C1_2024-08-07_13-00-52_2024-08-07_14-00-52.mp4")
#
# ret,frame = cap.read()
#
# gray_reference = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
# gray_reference = cv2.GaussianBlur(gray_reference,(21,21),0)
#
# mask = np.zeros(frame.shape[:2],dtype=np.uint8)
# cv2.fillPoly(mask,[np.array([[195,222],[345,118],[492,209],[321,346]])],255)
# #mask_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
#
# while True:
#     ret,frame = cap.read()
#     if not ret:
#         break
#
#     gray_current = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     gray_current = cv2.GaussianBlur(gray_current,(21,21),0)
#
#     diff = cv2.absdiff(gray_reference,gray_current)
#
#     masking = cv2.bitwise_and(diff,diff,mask=mask)
#
#     _,thresh = cv2.threshold(masking,25,255,cv2.THRESH_BINARY)
#
#     thresh = cv2.dilate(thresh,None,iterations=2)
#
#     contours,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#
#     for contour in contours:
#         if cv2.contourArea(contour) < 500:
#             continue
#         x,y,w,h = cv2.boundingRect(contour)
#         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
#     cv2.polylines(frame,[np.array([[195,222],[345,118],[492,209],[321,346]])],True,(0,255,0),1)
#
#     cv2.imshow('motion_Detection_maskIN',frame)
#     if cv2.waitKey(5) & 0xFF==ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

'''--------------------Motion detection on Mask-OUT Operation----------------------------'''
# import cv2
#
# cap = cv2.VideoCapture(r"C:\Users\Guest account\Desktop\Narasimha Murthy\07-08-24-murthy\GISUS3043C1_2024-08-07_13-00-52_2024-08-07_14-00-52.mp4")
#
# ret,frame = cap.read()
#
# gray_reference = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
# gray_reference = cv2.GaussianBlur(gray_reference,(21,21),0)
#
# mask = np.zeros(frame.shape[:2],dtype=np.uint8)
# cv2.fillPoly(mask,[np.array([[1,69],[102,32],[356,125],[6,324]])],255)
#
# while True:
#     ret,frame = cap.read()
#     if not ret:
#         break
#
#     gray_current = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     gray_current = cv2.GaussianBlur(gray_current,(21,21),0)
#
#     diff = cv2.absdiff(gray_reference,gray_current)
#
#     inverse_masking = cv2.bitwise_not(mask)
#     masking = cv2.bitwise_and(diff, diff, mask=inverse_masking)
#
#     _,thresh = cv2.threshold(masking,25,255,cv2.THRESH_BINARY)
#
#     thresh = cv2.dilate(thresh,None,iterations=2)
#
#     contours , _ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#     for contour in contours:
#         if cv2.contourArea(contour) < 500:
#             continue
#         x,y,w,h = cv2.boundingRect(contour)
#         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
#     cv2.polylines(frame,[np.array([[1,69],[102,32],[356,125],[6,324]])],True,(0,0,255),1)
#     cv2.imshow('Mask Out',frame)
#
#     if cv2.waitKey(150) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()














