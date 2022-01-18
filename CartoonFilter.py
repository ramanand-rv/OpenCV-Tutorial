import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

def color_quant(img, k):
    
    #Transform image
    data = np.float32(img).reshape((-1, 3))

    ##Determine Criteria
    criteria = (cv2.TERM_CRITERIA_EPS+ cv2.TermCriteria_MAX_ITER, 20, 0.001 )

    #Implementing K-Means
    ret, label, center = cv2.kmeans(data, k, None, criteria, 15, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)

    result = center[label.flatten()]
    result = result.reshape(img.shape)
    return result
#######################################################################
blurval = 5
linesiz = 17
#######################################################################


while True:
    flg, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayblur = cv2.medianBlur(gray, blurval)

    edges = cv2.adaptiveThreshold(grayblur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, linesiz, blurval)
    # cv2.imshow('Edges', edges)

    
    img_quant = color_quant(img, k=5)
    blurred = cv2.bilateralFilter(img_quant, d= 7, sigmaColor=200, sigmaSpace=200)

    cv2.imshow('Quant_Cam', blurred)

    imgOp = cv2.bitwise_and(blurred, blurred, mask=edges)
    cv2.imshow('Cartoon', imgOp)

    cv2.imshow('Cam', img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
