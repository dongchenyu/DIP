# -*- coding: utf-8 -*-
import cv2  
import numpy 
import math
def quantize(src, level):
    height=src.shape[0]
    weight=src.shape[1]
    res = numpy.zeros((height, weight, 3))
    dis=256/level
    for k in range(3):
        for i in range(height):
            for j in range(weight):
                res[i][j][k]=src[i][j][k]//dis*dis
    cv2.imwrite('/Users/dongchenyu/Documents/res.png', res)
src=cv2.imread('/Users/dongchenyu/Documents/abc.png',1)
q=input()
q=int(q)
quantize(src, q)

