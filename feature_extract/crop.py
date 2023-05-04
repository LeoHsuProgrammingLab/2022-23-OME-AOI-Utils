import cv2
import ROI
import canny
import sobel

img_path = 'no_lid.jpg'
roi = ROI.ROI(img_path)
# x, y, w, h



img = cv2.imread(img_path)[int(roi[1]):(int(roi[1])+int(roi[3])), int(roi[0]):(int(roi[0])+int(roi[2]))]
cv2.imshow('crop', img)
cv2.destroyAllWindows()

canny.canny_(img, 3, 80, 100)
# sobel.sobel_(img)


