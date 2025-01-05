import cv2 as cv

img = cv.imread('image/image.jpg')
img = cv.resize(img, (500, 500))
cv.imshow('Original Image', img)


#Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)


#Gaussian Blur
gaussian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gaussian)

#Bilateral
bilateral = cv.bilateralFilter(img, 10, 35,25 )
cv.imshow('Bilateral Blur', bilateral)



cv.waitKey(0)

