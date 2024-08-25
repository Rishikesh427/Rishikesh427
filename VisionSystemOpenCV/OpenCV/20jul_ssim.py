import cv2 as cv
import numpy as np
from skimage.metrics import structural_similarity as ssim

Mat = np.ndarray
def compare_images_ssim(imageA: Mat, imageB: Mat) :
    '''
    Converts two given images into grayscale, and calculates their structural similarity, a function from skimage module 
    that 
    '''
    grayA = cv.cvtColor(imageA, cv.COLOR_BGR2GRAY)
    grayB = cv.cvtColor(imageB, cv.COLOR_BGR2GRAY)
    
    score, diff = ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    
    return score, diff
cv.imread

imageA = cv.imread('path_to_imageA.jpg')
imageB = cv.imread('path_to_imageB.jpg')

score, diff = compare_images_ssim(imageA, imageB)
print(f"SSIM: {score}")


cv.imshow("Difference", diff)
cv.waitKey(0)
cv.destroyAllWindows()