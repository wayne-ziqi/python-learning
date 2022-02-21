#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/21 13:33
# @Author   : Wayne Qi
# @FileName : imgOp.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com
#读取图片

import matplotlib.pyplot as plt
import matplotlib.image as mpimg    #类似matlab对图片的操作
import numpy as np


import cv2
imgTest = mpimg.imread("日志处理.assets/1063221-20170511145312144-488305597.png")
print(imgTest.shape)

plt.imshow(imgTest)
plt.axis('off')
plt.show()

# 转换成灰度图
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

gray = rgb2gray(imgTest)
# 也可以用 plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.imshow(gray, cmap='Greys_r')
plt.axis('off')
plt.show()

#图像二值化
#自适应阈值化
#https://blog.csdn.net/zhuyong006/article/details/88782199

img = cv2.imread("cat.png")
#必须要把图片转换成uint8

GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 中值滤波
GrayImage= cv2.medianBlur(GrayImage,5)
ret,th1 = cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY)
#3 为Block size, 5为param1值
th2 = cv2.adaptiveThreshold(GrayImage,255,cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY,3,5)
th3 = cv2.adaptiveThreshold(GrayImage,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY,3,5)
titles = ['Gray Image', 'Global Thresholding (v = 127)',
'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [GrayImage, th1, th2, th3]
for i in range(4):
   plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])
plt.savefig("bw_proc.png", dpi=72)
plt.show()