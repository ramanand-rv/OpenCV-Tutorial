import cv2 as cc
import numpy as np

def click_event(event,x,y,flags, param):

    if event == cc.EVENT_LBUTTONDOWN:
        
        cc.circle(img, (x,y), 3, (0,0,255), -1)
        points.append((x,y))
        if len(points)>=2:
            cc.line(img, points[-1], points[-2], (255,0,0), 5)
        cc.imshow('image', img )

    #     font= cc.FONT_HERSHEY_PLAIN
    #     strxy = str(x)+ ','+str(y)
    #     cc.putText(img, strxy, (x,y), font, .5, (255,255,255), 2)
    #     cc.imshow('image', img)

    # if event==cc.eve
img = np.zeros((512,512,3), np.uint8)
cc.imshow('image',img)
points = [ ]
cc.setMouseCallback('image', click_event)

cc.waitKey(0)
cc.destroyAllWindows()