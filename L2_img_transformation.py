import cv2
import  numpy as np

kernel = np.ones((5,5), np.uint8)

img = cv2.imread('lena.jpg', 1)


imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (9,9), 0)
imgCanny =cv2.Canny(img, (100),(500)) #Edge Detection
imgDilation = cv2.dilate(imgCanny, kernel, iterations= 1) #define kernel for dilation
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)


# cv2.imshow('img', img)
cv2.imshow('imgGrey', imgGrey)
cv2.imshow('imgBlur', imgBlur)
cv2.imshow('imgCanny', imgCanny)
cv2.imshow('imgDilation', imgDilation)
cv2.imshow('imgEroded', imgEroded)

cv2.waitKey(0)