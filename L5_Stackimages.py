import cv2
import  numpy as np

kernel = np.ones((5,5), np.uint8)

img = cv2.imread('lena.jpg', 1)


imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (9,9), 0)
imgCanny =cv2.Canny(img, (100),(500)) #Edge Detection
imgDilation = cv2.dilate(imgCanny, kernel, iterations= 1) #define kernel for dilation
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)


 

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
 




r1 = stackImages(0.5, ([img, imgBlur, imgGrey], [imgCanny, imgDilation, imgEroded]))

cv2.imshow('Row1', r1)
# cv2.imshow('Row2', r2)



# cv2.imshow('img', img)
# cv2.imshow('imgGrey', imgGrey)
# cv2.imshow('imgBlur', imgBlur)
# cv2.imshow('imgCanny', imgCanny)
# cv2.imshow('imgDilation', imgDilation)
# cv2.imshow('imgEroded', imgEroded)



cv2.waitKey(0)