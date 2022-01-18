import cv2
import  numpy as np

img = np.zeros((500,500,3), np.uint8)

# img[:] = 0,0,255 #To color fill

cv2.line(img, (400,100), (100,400),(255,0,0), 3 )
cv2.line(img, (100,100), (400,400),(0,0,255), 3 )

cv2.rectangle(img, (100,100), (400,400), (0,255,0), 7)
cv2.rectangle(img, (200,200), (300,300), (0,255,255), cv2.FILLED)

cv2.circle(img, (250,250), 100, (255,255,0), 9 )
cv2.circle(img, (250,250), 50, (255,155,0), cv2.FILLED )


text = "RV"
cv2.putText(img, text, (219, 265), cv2.FONT_HERSHEY_COMPLEX, 1.5,(0,0,255), 4)

cv2.imshow('img', img)


cv2.waitKey(0)
