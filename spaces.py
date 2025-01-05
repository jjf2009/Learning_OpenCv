import cv2 as cv 
import numpy as np

img = cv.imread('image/image.jpg')

if img is None:
    print("Error: Image not found. Check the file path.")
    exit()

cv.imshow('Image',img)
#BGR to Grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)



cv.waitKey(0)