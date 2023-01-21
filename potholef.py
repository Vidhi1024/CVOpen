import cv2
import numpy as np
import pandas as pd
import os
from matplotlib import pyplot as plt
from matplotlib import image as mping

IMG_PATH = os.path.join("C:\\Users\Vidhi\Downloads\pothole.jpg")
img = cv2.imread(IMG_PATH)
h, w, _ = img.shape
t_area = h*w
print("area of image: ", float(t_area))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.blur(gray, (7,7))
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edges = cv2.Canny(gray, 10, 145)

cnts, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
l_area = sorted(cnts, key = cv2.contourArea, reverse=True)
# cv2.fillPoly(img, cnts, color=(255, 255, 255))
cv2.drawContours(img, cnts, 0, (0, 255, 0), 3)

for cnt in cnts:
    area = cv2.contourArea(cnt)
    if area > 200: #filtering contours
        x, y, w, h = cv2.boundingRect(cnt)
        if w/h < 4: # filtering even more
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)


# for cnt in cnts:
#    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
#    (x,y)=cnt[0,0]
#
#    if len(approx) >= 5:
#       img = cv2.drawContours(img, [approx], -1, (0,255,255), 3)
#       cv2.putText(img, 'o', (x, y),
# cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

cv2.imshow('Frame View', img)



area_list = []
areaLists = []
for contour in cnts:
    area = cv2.contourArea(contour)
    area_list.append(area)
for i in area_list:
    a = (i / t_area) * 100
    areaLists.append(a)
    areaLists.sort(reverse=True)
i_area =str(max(area_list))
print("area of hole: ", max(area_list))
print("jo bhi aapne formula bola wo: ", a)
print("(rows, column, channels): ", img.shape)



cv2.waitKey(0)
cv2.destroyAllWindows()