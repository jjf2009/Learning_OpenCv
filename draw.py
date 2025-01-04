import cv2 as cv 
import numpy as np

img = np.zeros((512, 512, 3), dtype='uint8')
cv.imshow('Blank', img)

#1.Paint the image a certain color
# img[200:300,300:400]=0,255,0
# cv.imshow('Green', img)


#2.Draw a rectangle
# cv.rectangle(img, (0,0), (img.shape[1]//2,img.shape[0]//2), (0,255,0), thickness=2)
# cv.imshow('Rectangle', img)


#3.Draw a circle
# cv.circle(img, (img.shape[1]//2,img.shape[0]//2), 40, (0,0,255), thickness=2)
# cv.imshow('Circle', img)

#4.Draw a line
# cv.line(img, (0,0), (img.shape[1]//2,img.shape[0]//2), (255,255,255), thickness=2)  
# cv.imshow('Line', img)

#5.Write text
cv.putText(img, 'Hello World', (255,255), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', img)

cv.waitKey(0)