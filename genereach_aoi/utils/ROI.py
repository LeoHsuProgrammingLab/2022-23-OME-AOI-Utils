import cv2
import numpy as np

# https://blog.electroica.com/select-roi-or-multiple-rois-bounding-box-in-opencv-python/

# 'androidparty.png'

def ROI(img_path):
    img = cv2.imread(img_path)
    cnt = 0
    while(True):
        roi = cv2.selectROI(img)
        cnt += 1
        #get (x, y, width, height)
        print(f"(x, y, width, height)= {roi}")
        print(f"(x1, y1, x2, y2)= {(roi[0], roi[1], roi[0]+roi[2], roi[1]+roi[3])}\n")
        if cnt >= 3:
            ipt = input('Do you keep selecting?(y/n)\n')
            if ipt == 'y' :
                cnt = 0
            elif ipt == 'n':
                break
            else:
                print('Wrong answer!')
        


if __name__ == '__main__':
    ROI('./2nd/1/1_1.jpg')