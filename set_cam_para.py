import cv2
import datetime

cap=cv2.VideoCapture(0)
# print(cap.get( cv2.CAP_PROP_FRAME_HEIGHT))  #parameter value 3
# print(cap.get( cv2.CAP_PROP_FRAME_WIDTH))      #parameter value 4

# cap.set(3,500)        # 3 is for height
# cap.set(4,500)        # 4 is for width

# print(cap.get(3))       #setting height
# print(cap.get(4))       #setting width


while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        
        datet=str(datetime.datetime.now())  ## to print date and time

        font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX

        text = 'Width: '+ str(cap.get(3)) + 'Height: '+ str(cap.get(4)) 

        frame= cv2.putText(frame, datet, (10,50), font, 1, (0,255,255), 2, cv2.LINE_AA)
        #replace datet with text to print height and width
        
        
        # gray=cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        # cv2.flip(frame)
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows() 