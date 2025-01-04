import cv2 as cv

# img =cv.imread('image.jpg')


# cv.imshow('Image', img)

cap = cv.VideoCapture('video.mp4')

while True:
    ret, frame = cap.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# cv.waitKey(0)
cap.release()
cv.destroyAllWindows()
