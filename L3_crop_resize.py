import cv2

img = cv2.imread("messi.jpg")
# print(img.shape)

width, height = 480, 480

imgResize = cv2.resize(img, (width, height))

imgCrop = img[:, 210:680]

imgCropResize = cv2.resize(imgCrop, (img.shape[1], img.shape[0]))



cv2.imshow('img',img)


# cv2.imshow('imgResize',imgResize)
print(imgResize.shape)

cv2.imshow('imgCrop',imgCrop)
print(imgCrop.shape)

cv2.imshow('imgCropResize', imgCropResize)
print(imgCropResize.shape)

cv2.waitKey(0)