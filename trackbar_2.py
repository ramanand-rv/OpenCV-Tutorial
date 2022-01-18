import numpy as nn
import cv2 as cc

def nothing(x):
    print(x)

# img = nn.zeros((240,320,3), nn.uint8)

# cc.imread('messi.jpg')
cc.namedWindow('image')

cc.createTrackbar('cp', 'image', 10, 400, nothing)    # creates a tracker 
                                                    #exclusive trackbar name,  window name,  initial value,  max value,  return if changes take place
switch='color/gray'
cc.createTrackbar(switch,'image',0,1, nothing)


while(1):


    img=cc.imread('messi.jpg')

    pos=cc.getTrackbarPos('cp', 'image')
    font=cc.FONT_HERSHEY_SIMPLEX
    cc.putText(img, str(pos), (50,150), font, 5, (0,255,255))


    k= cc.waitKey(1) & 0xFF 
    if k==27:
        break
    
    # b= cc.getTrackbarPos('B','image')
    # g= cc.getTrackbarPos('G','image')
    # r= cc.getTrackbarPos('R','image')
    s = cc.getTrackbarPos(switch, 'image')

    if s==0:
        pass
    else:
        img=cc.cvtColor(img, cc.COLOR_BGR2GRAY)
    
    img=cc.imshow('image',img)



cc.destroyAllWindows()