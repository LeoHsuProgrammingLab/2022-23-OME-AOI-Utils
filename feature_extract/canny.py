import cv2
import cv2.ximgproc as xip

def canny_(img, kernel_size, low_thr, high_thr):

    # wmf = xip.weightedMedianFilter(img, img, 10, 30)
    # cv2.imshow('wmf', wmf)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    img_ = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur_gray = cv2.GaussianBlur(img_, (kernel_size, kernel_size), 100)
    sharpen = cv2.addWeighted(img_, 2.5, blur_gray, -1, -10)
    
    edges = cv2.Canny(sharpen, low_thr, high_thr)
    cv2.imshow('edge', edges)
    cv2.waitKey(0)
    cv2.imwrite('edge.png', edges)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    img = cv2.imread('S__3809282.jpg')
    img1 = cv2.imread('S__3809284.jpg')
    img2 = cv2.imread('S__3809285.jpg')

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel_size = 3
    blur_gray = img
    blur_gray = cv2.GaussianBlur(img,(kernel_size, kernel_size), 0)
    low_threshold = 70
    high_threshold = 140
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
    cv2.imshow('edge', edges)
    cv2.imwrite('original.png', edges)

    cv2.waitKey(0)