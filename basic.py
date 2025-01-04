import cv2 as cv 

img = cv.imread('image/image.jpg')

cv.imshow('Image', img)

#convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

#dilate
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Dilated', dilated)

#erode
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('Eroded', eroded)

#resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)


#cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)