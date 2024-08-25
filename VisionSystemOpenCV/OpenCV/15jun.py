import cv2 as cv
import numpy as np
 
cameracapture = cv.VideoCapture(0)

def capture_picture(event):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.imwrite('image1', cameracapture)
    elif event == cv.EVENT_RBUTTONDBLCLK:
        cv.imwrite('image2', cameracapture)

cv.namedWindow('window1')
cv.setMouseCallback('window1', capture_picture)

while(1):
 cv.imshow('window', cameracapture)
 if cv.waitKey(20) & 0xFF == 27:
    break
cv.destroyAllWindows()