import cv2
import numpy
import os
from matplotlib import pyplot as plt

IMG_PATH = os.path.join("C:\\Users\Vidhi\Downloads\pothole.jpg")
img = cv2.imread(IMG_PATH)

# cv2.imshow('Frme view', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cropped_img = img[100:700, 0:1100]

# rimg=cv2.resize(cropped_img, (int(img.shape[0]*4), int(img.shape[1]*2)))
blur = cv2.GaussianBlur(cropped_img, (5,5),0)
canny= cv2.Canny(blur, threshold1=110, threshold2=400)
# polygon = cv2.polylines(canny, [circle], False, (255, 0, 0), thickness=2)


cv2.imshow('Frame view', polygon)
cv2.waitKey(0)
# cv2.destroyAllWindows()
