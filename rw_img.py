import cv2
img=cv2.imread('lena.jpg', -1 ) ## To read image

cv2.imshow('image', img)    ## To show image
k= cv2.waitKey(0)      ## To hold the image on screen

if k==27: ##for escape key
    cv2.destroyAllWindows() ## Destroy all windows if Esc is pressed
elif k== ord('s'):  ## If s is pressed then
    cv2.imwrite('lena_copy.png',img)    ## Save this image with new name and extension

cv2.destroyAllWindows() ## Destroy all windows


# print(img)