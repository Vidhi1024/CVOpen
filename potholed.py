import cv2
import numpy as np
import pandas as pd
import os
from matplotlib import pyplot as plt
from matplotlib import image as mping

IMG_PATH = os.path.join("C:\\Users\Vidhi\OneDrive\Documents\pothole.jpg")
img1 = cv2.imread(IMG_PATH)
print(img1.shape)
img = img1[250:720, 0:1280]
# rimg=cv2.resize(img, (int(img.shape[0]*2), int(img.shape[1]*2)))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
# lower_blue = np.array([100, 100, 0])
# upper_blue = np.array([100, 100, 160])
# mask = cv2.inRange(hsv, lower_blue, upper_blue)
gray = cv2.blur(gray, (3,3))
gray = cv2.bilateralFilter(gray, 11, 17, 17)
canny = cv2.Canny(gray, 20, 50)

cnts, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, cnts, 0, (0, 255, 0), 3)

cv2.imshow('Frame View', img)
cv2.waitKey(0)
cv2.destroyAllWindows()