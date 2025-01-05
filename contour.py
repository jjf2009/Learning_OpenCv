import cv2 as cv 
import numpy as np 
img = cv.imread("image/image.jpg")

cv.imshow('Image',img)

blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)



gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',img)

# canny=cv.Canny(img,125,175)
# cv.imshow('Canny Edges',canny)

ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)



contours,hierarchies =cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)}')
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contour',blank)

cv.waitKey(0)