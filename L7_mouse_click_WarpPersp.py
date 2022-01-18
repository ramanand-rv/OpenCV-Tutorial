import cv2
import numpy as np
 
img = cv2.imread(r'C:\Users\raman\OneDrive\Documents\Codes\CV\cv2\messi.jpg')
counter = 0

circles = np.zeros((4,2), np.int16)

def mousePoints(event, x, y, flg, params):
    global counter 
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(x, y)
        circles[counter] = x,y
        counter = counter + 1
        print(circles)



while (True):
    width, height = 280, 500
    if counter == 4:


        pts = np.float32([[circles[0]], [circles[1]], [circles[2]], [circles[3]]])
        pts1 = np.float32([[0,0], [width, 0], [0,height], [width,height]])

        mat = cv2.getPerspectiveTransform(pts, pts1)
        imgOp =cv2.warpPerspective(img, mat, (width,height))
        cv2.imshow('imgOp', imgOp)


    for x in range(0,4):
        cv2.circle(img, (circles[x][0],circles[x][1]), 8, (255,100, 0), cv2.FILLED)


    cv2.imshow('Image',img)
    # cv2.imshow('imgOp', imgOp)

    cv2.setMouseCallback('Image', mousePoints)



    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()