import cv2

def rotate_wholeimg(event):
    if event == cv2.EVENT_FLAG_CTRLKEY:
        cv2.rotate(img, 90)

img = cv2.imread('OpenCV/Images/Unknown.jpeg', -1)
img1 = cv2.resize(img, (0, 0), fx=4, fy=4)

cv2.imshow('window', img)
keypress = cv2.waitKey(0)
if keypress == ord('s'):
    cv2.imwrite('Known.png', img1)
    cv2.imwrite('Known2.png', img1)
cv2.destroyAllWindows()
print(f'{cv2.compareHist(img, img , -1)}')

# print(img)