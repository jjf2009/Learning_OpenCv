import cv2 as cv

# img = cv.imread('image.jpg')
# cv.imshow('Image', img)

capture = cv.VideoCapture('0')
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # Live video
    capture.set(3, width)
    capture.set(4, height)
    return width, height