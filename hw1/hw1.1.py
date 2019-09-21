import cv2  
import numpy 
import math
def scale(src, target):
    width = target[0]
    height = target[1]
    s_height = src.shape[0]
    s_width = src.shape[1]
    res = numpy.zeros((height, width, 3))
    for n in range(3): 
        for i in range(height): 
            for j in range(width): 
                s_x = (j + 0.5) * (s_width / width) - 0.5
                s_y = (i + 0.5) * (s_height / height) - 0.5
                n1 = int(s_x)
                n2 = int(s_y)
                n3 = n1 + 1
                n4 = n2 + 1
                v1 = (n3 - s_x) * src[n2, n1, n] + (s_x - n1) * src[n2, n3, n]
                v2 = (n3 - s_x) * src[n4, n1, n] + (s_x - n1) * src[n4, n3, n]
                res[i, j, n] = int((n4 - s_y) * v1 + (s_y - n2) * v2)
    cv2.imwrite('/Users/dongchenyu/Documents/result.png', res)
src=cv2.imread('/Users/dongchenyu/Documents/abc.png',1)
w=input()
h=input()
w=int(w)
h=int(h)
target = (w,h) 
scale(src,target)
