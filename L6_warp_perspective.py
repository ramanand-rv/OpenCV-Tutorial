import cv2
import numpy as np

img=cv2.imread("cards.jpg")

#corner values
# A= (310, 235)
# B= (490, 290)
# C= (170, 440)
# D= (360, 505)
width, height = 280, 500


pts = np.float32([[310,235], [490,290], [170,440], [360,505]])
# print(pts)
pts1 = np.float32([[0,0], [width, 0], [0,height], [width,height]])

mat = cv2.getPerspectiveTransform(pts, pts1)
imgOp =cv2.warpPerspective(img, mat, (width,height))

# for x in range(0,4):
    # cv2.circle(img, (pts[x][0],pts[x][1]), 8, (255,100, 0), cv2.FILLED)


cv2.imshow('imgOp', imgOp)

cv2.imshow('img', img)

cv2.waitKey(0)