import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

IMG_PATH = os.path.join("C:\\Users\Vidhi\Downloads\pothole.jpg")
img = cv2.imread(IMG_PATH)

# cv2.imshow('Frme view', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.blur(gray, (7,7))
gray = cv2.bilateralFilter(gray, 11, 17, 17) #blur. very CPU intensive.
# cv2.imshow("Gray map", gray)

edges = cv2.Canny(gray, 20, 145)


cnts, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# cv2.imshow("Edge map", edges)
# # areas = [cv2.contourArea(c) for c in cnts]
# # max_index = np.argmax(areas)
# # cnt=cnts[max_index]
#
# area_list = []
# for contour in cnts:
#     area = cv2.contourArea(contour)
#     area_list.append(area)
# print(max(area_list))
# print(edges.shape)
cv2.drawContours(img, cnts, -1, (0, 255, 0), 3)
cv2.imshow('img', edges)
cv2.imshow('gh', img)

# cropped_img = img[100:700, 0:1100]

# rimg=cv2.resize(cropped_img, (int(img.shape[0]*4), int(img.shape[1]*2)))
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# blur = cv2.GaussianBlur(img, (5, 5),0)
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
# l_blue = np.array([38, 86, 0])
# u_blue = np.array([121, 255, 255])
# mask = cv2.inRange(hsv, l_blue, u_blue)
# # canny= cv2.Canny(hsv, threshold1=100, threshold2=400)
# cnts, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# cv2.drawContours(img, cnts, -1, (0, 255, 0), 3)
#
# cv2.imshow('Frame view', img)
# cv2.imshow('mask view', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()








# pic=np.copy(canny)
#
# pts=np.array([[408,492],[457,449], [548, 432], [633,445], [738, 484],[666,525], [563,538], [459,523], [408,492]])
# cv2.polylines(pic, [pts], False, (255, 0, 0), thickness=2)
# plt.imshow(pic)

# cnts, _= cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:1]
# screenCnt = None
#
# # loop over our contours
# for c in cnts:
#     # approximate the contour
#     peri = cv2.arcLength(c, True)
#     approx = cv2.approxPolyDP(c, 0.3 * peri, True)
#
#     cv2.drawContours(canny, [cnts[0]], -1, (0, 255, 0), 2)
#
#     # if our approximated contour has four points, then
#     # we can assume that we have found our card
#     if len(approx) == 4:
#         screenCnt = approx;
#     break
#
#     cv2.drawContours(canny, [screenCnt], -1, (0, 255, 0), 2)
