# from L8_color_detection import empty
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)

def empty():
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 120)
cv2.createTrackbar("Threshold_1", "Parameters", 248, 255, empty)
cv2.createTrackbar("Threshold_2", "Parameters", 6, 255, empty)
cv2.createTrackbar("Area", "Parameters", 5000, 150000, empty)


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


def getcontours(img, imgcontour):
    contour, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(imgcontour, contour, -1, (255, 0, 0), 7)


    for cnt in contour:
        area = cv2.contourArea(cnt)
        areamin = cv2.getTrackbarPos("Area", "Parameters")
        if area > areamin:
        
            cv2.drawContours(imgcontour, contour, -1, (255, 0, 0), 2)
            peri = cv2.arcLength(cnt, closed= True)

            approx = cv2.approxPolyDP(cnt, 0.02 * peri, closed=True)

            # print(len(approx))

            x,y,w,h = cv2.boundingRect(approx)

            cv2.rectangle(imgcontour, (x , y ), (x + w ,  y + h ), (0, 255, 100), 3)

            cv2.putText(imgcontour, "Points: "+ str(len(approx)), (x+w+20, y+20), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)

            cv2.putText(imgcontour, "Area: "+str(int(area)), (x+w+20, y+45), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 0), 2)





while True:
    ret, img = cap.read()

    # imgcontour = img.copy()

    imgblur = cv2.GaussianBlur(img, (7,7), 1)
    imggray = cv2.cvtColor(imgblur, cv2.COLOR_BGR2GRAY)


    Threshold_1 = cv2.getTrackbarPos("Threshold_1", "Parameters")
    Threshold_2 = cv2.getTrackbarPos("Threshold_2", "Parameters")


    imgcanny = cv2.Canny(imggray, Threshold_1, Threshold_2)

    kernel = np.ones((5,5))

    imgdil = cv2.dilate(imgcanny, kernel, iterations = 1)

    imgcontour = getcontours(imgdil,None)


    imgstack = stackImages(0.5, ([img, imgcanny, imggray, imgdil]))
    
    cv2.imshow('img', imgstack)
    cv2.imshow('Area', imgcontour)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
