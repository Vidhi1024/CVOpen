import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

IMG_PATH = os.path.join("C:\\Users\Vidhi\Downloads\pothole.jpg")
img = cv2.imread(IMG_PATH)
h, w, _ = img.shape
t_area = h*w
print("area of image: ", float(t_area))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.blur(gray, (7,7))
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edges = cv2.Canny(gray, 20, 145)

cnts, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img, cnts, -1, (0, 255, 0), 3)

cv2.imshow('Frane View', img)

area_list = []
areaLists = []
for contour in cnts:
    area = cv2.contourArea(contour)
    area_list.append(area)
for i in area_list:
    a = (i / t_area) * 100
    areaLists.append(a)
    areaLists.sort(reverse=True)
print(areaLists)

# print(area_list)
# i_area = max(area_list)
# print("area of hole: ", max(area_list))
# print("jo bhi aapne formula bola wo: ", a)
# print("(rows, column, channels): ", img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()