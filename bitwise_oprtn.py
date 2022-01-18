import cv2 as cc
import numpy as np

img1 = np.zeros((500,500,3), np.uint8)
img1 = cc.rectangle(img1, (200,0), (300,100), (255,255,255), -1)
img2 = cc.imread('baw.jpg')

# bitAnd= cc.bitwise_and(img2, img1)  #black->0 & white-> 1  colours are ANDED using AND tt

# bitOr =cc.bitwise_or(img2,img1)

# bitXor =cc.bitwise_xor(img2,img1)

bitNot=cc.bitwise_not(img2)



cc.imshow('img1',img1)
cc.imshow('img2',img2)

# cc.imshow('img3',img3)
# cc.imshow('bitAnd', bitAnd)
# cc.imshow('bitOr', bitOr)
# cc.imshow('bitXor', bitXor)
cc.imshow('bitNot', bitNot)


cc.waitKey(0)
cc.destroyallwindows