import cv2

cap= cv2.VideoCapture(0);       ##to capture video from Camera
                                ## to read video put video name instead of '0'

fourcc= cv2.VideoWriter_fourcc(*'xvid')     ##  Fourcc code used to specify video encoding

out= cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))     ## name of output vide, fourcc code, frame rate, resolution

print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))   ## Prints height and width of the video
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

while(True):
    ret, frame= cap.read()      ## ret will store true or false whether frame is available
                                ## frame will capture or save the frames

   ## gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  ## To convert color to gray

    if ret==True:


        out.write(frame)

        cv2.imshow('frame', frame)      ## put gray as second parameter to change color
        if cv2.waitKey(1) & 0xFF   == ord('q'):     ## exit if q is pressed
            break
    else:
        break


cap.release()       ## We've to release video after capturing
out.release()       ## release after writing video
cv2.destroyAllWindows()    