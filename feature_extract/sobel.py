import cv2
import numpy as np

def sobel_(image):
    sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
    sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)
    sobelX = np.uint8(np.absolute(sobelX))

    sobelY = np.uint8(np.absolute(sobelY))

    sobelCombined = cv2.bitwise_or(sobelX, sobelY)

    cv2.imshow('sobel edge', sobelCombined)
    cv2.waitKey(0)
    cv2.imwrite('sobel_edge.png', sobelCombined)
    cv2.destroyAllWindows()