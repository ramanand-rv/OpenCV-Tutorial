import cv2 as cc
import numpy as np

img = cc.imread('lena.jpg', 1)
cc.imshow("org", img)
mat = 3
median = cc.medianBlur(img, mat)
cc.imshow("median", median)

cc.waitKey(0)

cc.destroyAllWindows()

