import numpy as nn
import cv2 as cc

img=cc.imread('messi.jpg',1)
img1=cc.imread('lena.jpg',1)

print(img.shape)    #returns number of rows coloumns and channels
print(img.size)     #returns total numbr of pixel acessed
print(img.dtype)       #image data type is obtained

# ROI- Region of interest. a part of image where we've to work


# def click_event(event,x,y,flags,param):
#     if event == cc.EVENT_LBUTTONDOWN:
#         print(x,',' ,y)
#         font=cc.FONT_HERSHEY_SIMPLEX

#         strxy = str(x) + ', '+ str(y)
#         cc.putText(img, strxy, (x,y), font, 0.5, (255,255,255), 2)
#         cc.imshow('image', img)

b,g,r = cc.split(img)
img= cc.merge((b,g,r))

ball = img[210:270, 500:550]   
img[450:510, 550:600] = ball

img=cc.resize(img, (512,512))
img1=cc.resize(img1,(512,512))

# dst= cc.add(img,img1)       

dst=cc.addWeighted(img, .5, img1, .7, 0)


cc.imshow('image',dst)

# cc.setMouseCallback('image',click_event)

cc.waitKey(0)
cc.destroyAllWindows