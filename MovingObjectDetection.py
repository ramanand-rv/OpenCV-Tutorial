import cv2
import numpy as np

cap = cv2.VideoCapture(0)

obDetect = cv2.createBackgroundSubtractorMOG2()



while True:
    
    ret, img = cap.read()

    
    #Object Detection
    mask = obDetect.apply(img)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        cv2.drawContours(img, [cnt], -1, (255, 100, 0), 2)

    cv2.imshow("mask", mask)

    cv2.imshow("Cam", img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break