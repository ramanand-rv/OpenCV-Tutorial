import cv2

frameWidth = 640
frameHeight = 400

# cap = cv2.VideoCapture(1)
cap1 = cv2.VideoCapture("ShriKrishna.mp4")

# cap1.set(3,frameWidth)
# cap1.set(4,frameHeight)

while(cap1.isOpened()):
    # ret, img = cap.read()
    ret1, img1 = cap1.read()

    if ret1 == True:

        
        img1 = cv2.resize(img1, (frameWidth, frameHeight))
        # cv2.imshow('img', img)
        cv2.imshow('img1', img1)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break   

cap.release()
cv2.destroyAllWindows() 



# cv2.waitKey(0)