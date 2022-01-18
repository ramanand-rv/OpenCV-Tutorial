import cv2 as cc
import numpy as np

def click_event(event,x,y,flags, param):

    if event == cc.EVENT_LBUTTONDOWN:
        
        bl=img[x,y,0]
        gr=img[x,y,1]
        rd=img[x,y,2]

        # strbgr= str(bl)+','+str(gr)+','+str(rd)
        cc.circle(img, (x,y), 3, (0,0,255), -1)
        myimg= np.zeros((512,512,3), np.uint8)
        myimg[:]=[bl, gr,rd]
        cc.imshow('color', myimg )


# img = np.zeros((512,512,3), np.uint8)
img= cc.imread('lena.jpg',1)
cc.imshow('image',img)
points = [ ]
cc.setMouseCallback('image', click_event)

cc.waitKey(0)
cc.destroyAllWindows()