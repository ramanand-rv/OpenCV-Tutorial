import numpy as np
import cv2 as cc



# events = [i for i in dir(cc) if 'EVENT' in i]       # to list the events of library
# print(events)
def click_event(event,x,y,flags,param):
    if event == cc.EVENT_LBUTTONDOWN:
        print(x,',' ,y)
        font=cc.FONT_HERSHEY_SIMPLEX

        strxy = str(x) + ', '+ str(y)
        cc.putText(img, strxy, (x,y), font, 0.5, (255,255,255), 2)
        cc.imshow('image', img)

    if event == cc.EVENT_RBUTTONDOWN:
        blue= img[y,x,0]
        green= img[y,x,1]
        red= img[y,x,2]
        font=cc.FONT_HERSHEY_SIMPLEX

        strbgr= str(blue) + ','+ str(green) + ','+ str(red)
        cc.putText(img, strbgr, (x,y), font, 0.5, (0,255,255), 2)
        cc.imshow('image',img)


# img = np.zeros((512,512,3), np.uint8)
img= cc.imread('lena.jpg')
cc.imshow('image', img)

cc.setMouseCallback('image', click_event)

cc.waitKey(0)
cc.destroyAllWindows()