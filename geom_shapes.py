import cv2

img= cv2.imread('lena.jpg',1)


# img = cv2.line(img, (0,0), (255,255), (0,255,0), 5) ##img, cordinates stratimg and ending, colour(B,G,R), thickness
# img = cv2.arrowedLine( img, (255,0), (255,255), (255,0,0), 5) 
# img= cv2.rectangle(img, (175,175), (390,450), (0,0,255), 10)        ##img, top left vertex, right bottom vertex, color, thickness
# # give thickness as -1 to fill the rectangle with color

img= cv2.circle(img, (255,255), (255), (255,0,0), 10)       ## img, Center coordinates, radius, color, thickness

# font = cv2.FONT_HERSHEY_TRIPLEX
# img= cv2.putText(img, 'Perfect Picture' , (10,255), font , 1.5, (43,245,252), 5, cv2.LINE_4)  # img, 'your text',  strting coordinate, font style, font size, color, thickness, Line type
#                                                                  ## 252, 245, 43
cv2.imshow("image",img)

cv2.waitKey(0)

cv2.destroyAllWindows()