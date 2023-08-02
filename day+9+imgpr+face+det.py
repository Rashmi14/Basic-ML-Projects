
import numpy as np
import cv2
image=cv2.imread(r"C:\Users\Dr P.c rawat\Desktop\singleperson")
face_cascade=cv2.CascadeClassifier("C:/Users/Dr P.c rawat/Anaconda3/pkgs/opencv-3.4.1-py36_200/Library/etc/haarcascades/haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("C:\Users\Dr P.c rawat\Anaconda3\pkgs\opencv-3.4.1-py36_200\Library\etc\haarcascades/haarcascade_eye.xml")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2BGRA)
faces=face_cascade.detectMultiScale(gray,1.3,5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+w),(255,0,0),2)
    roi_gray=gray[y:y+h,x:x+w]
    roi_color=gray[y:y+h,x:x+w]
    eyes=eye_cascade.detectMultiScale(roi_gray)
    for(ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    