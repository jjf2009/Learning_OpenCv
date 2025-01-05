import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('image/image.jpg')
img = cv.resize(img, (0, 0), fx=0.5, fy=0.5)
# cv.imshow('image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

#Gray histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()


#Color histogram
colors = ('b', 'g', 'r')
for i, color in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])
    plt.show()


cv.waitKey(0)