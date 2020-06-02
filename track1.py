tar = select_tracker()

tar_used = str(tar).split()[0][1:]

cap = cv2.VideoCapture(r'')#pass the video file as the parametes 

ret,frame = cap.read()

roi = cv2.selectROI(frame,False)

ret = tar.init(frame,roi)

while True:
    
    ret,frame = cap.read()
    
    success,roi = tar.update(frame)
    
    (x,y,w,h) = tuple(map(int, roi))
    
    if success:
        
        pts1 = (x,y)
        
        pts2 = (x+w,y+h)
        
        cv2.rectangle(frame,pts1,pts2,(255,125,25),3)
        
    else:
        
        cv2.putText(frame,'Failed',(100,200),cv2.FONT_HERSHEY_SIMPLEX,1,(25,125,255),3)
        
    cv2.putText(frame,tarcker_used,(20,400),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),3)
   

    cv2.imshow(tar_used)
    
    
    if cv2.waitKey(50) & 0xFF ==27:
            break
            
            
cap.release()
cv2.destroyAllWindows()
        
