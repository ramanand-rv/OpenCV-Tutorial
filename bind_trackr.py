import numpy as nn
import cv2 as cc

def nothing(x):
    print(x)

img = nn.zeros((240,320,3), nn.uint8)
cc.namedWindow('image')

cc.createTrackbar('B', 'image', 0, 255, nothing)    # creates a tracker 
cc.createTrackbar('G', 'image', 0, 255, nothing)    #exclusive trackbar name,  window name,  initial value,  max value,  return if changes take place
cc.createTrackbar('R', 'image', 0, 255, nothing)

cc.createTrackbar('switch','image',0,1, nothing)


while(1):
    cc.imshow('image',img)
    k= cc.waitKey(1) & 0xFF 
    if k==27:
        break
    
    b= cc.getTrackbarPos('B','image')
    g= cc.getTrackbarPos('G','image')
    r= cc.getTrackbarPos('R','image')
    s=cc.getTrackbarPos('switch', 'image')

    if s==0:
        img[0:0] = 0
    else:
        img[:] = [b,g,r]


cc.destroyAllWindows()