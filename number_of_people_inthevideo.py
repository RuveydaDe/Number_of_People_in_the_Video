import cv2
import numpy as np


face_cascade=cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(0)

while True:
    et,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
  
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),3)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        
        cv2.putText(frame, "Number of person: " + str(faces.shape[0]), (x-5,y-5),
                cv2.FONT_HERSHEY_TRIPLEX, 0.5, (42, 251, 92), 1)
      

    cv2.imshow('frame',frame)
    
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()
