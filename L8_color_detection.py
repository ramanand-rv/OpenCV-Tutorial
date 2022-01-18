import cv2
import numpy as np

# frameWidth = 500
# frameHeight = 500

cap = cv2.VideoCapture(0)

cap.set(3, 480)
cap.set(4, 480)

def empty(a):
    pass


cv2.namedWindow("HSV_tb")
# cv2.resize('HSV', 480, 480)

cv2.createTrackbar("Hue Min", "HSV_tb", 0, 179, empty)
cv2.createTrackbar("Hue Max", "HSV_tb", 179, 179, empty)
cv2.createTrackbar("Sat Min", "HSV_tb", 0, 255, empty)
cv2.createTrackbar("Sat Max", "HSV_tb", 255, 255, empty)
cv2.createTrackbar("Value Min", "HSV_tb", 0, 255, empty)
cv2.createTrackbar("Value Max", "HSV_tb", 255, 255, empty)

while True:
    _, img = cap.read()

    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min  = cv2.getTrackbarPos("Hue Min", "HSV_tb")
    h_max  = cv2.getTrackbarPos("Hue Max", "HSV_tb")
    s_min  = cv2.getTrackbarPos("Sat Min", "HSV_tb")
    s_max  = cv2.getTrackbarPos("Sat Max", "HSV_tb")
    v_min  = cv2.getTrackbarPos("Value Min", "HSV_tb")
    v_max  = cv2.getTrackbarPos("Value Max", "HSV_tb")
    # print(h_min)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(img,lower,upper)
    result = cv2.bitwise_and(img, img, mask= mask)

    

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    hstack = np.hstack([img, result])



    # cv2.imshow('Original', img)
    # cv2.imshow('HSV', imghsv)
    # cv2.imshow('mask', mask)
    # cv2.imshow('result', result)
    cv2.imshow('Hstack', hstack)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()