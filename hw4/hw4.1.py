import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
def equalize_hist(image,num,n):
    percent = [0]*256 
    pdf = [0]*256
    trans = [0]*256
    h = image.shape[0]
    w = image.shape[1]
    sum = h*w*1.0
    for i in range(0,256):
        percent[i]=num[i]/sum
    pdf[0]=percent[0]
    for i in range(1,256):
        pdf[i]=pdf[i-1]+percent[i]
    #print(pdf)
    for i in range(0,256):
        temp=255.0*pdf[i]
        if(temp-int(temp)>=0.5):
            temp=int(temp)+1
        else:
            temp=int(temp)
        trans[i]=temp
    result = np.zeros([h,w],np.uint8)
    for i in range(0,h):
        for j in range(0,w):
            result[i,j]=trans[int(image[i,j,n])]
    return result
image = cv.imread('/Users/dongchenyu/Documents/23.png',1) 
#print(image)
height=image.shape[0]
width=image.shape[1]
r=np.zeros((height,width),np.uint8)
num_red=[0]*256 
num_green=[0]*256 
num_blue=[0]*256 
avag=[0]*256
for i in range(height):
    for j in range(width):
        r[i][j]=image[i][j][0]
g=np.zeros((height,width),np.uint8)
for i in range(height):
    for j in range(width):
        g[i][j]=image[i][j][1]
b=np.zeros((height,width),np.uint8)
for i in range(height):
    for j in range(width):
        b[i][j]=image[i][j][2]
for i in range(height):
    for j in range(width):
        gray = r[i,j]
        num_red[gray] = num_red[gray]+1 
for i in range(height):
    for j in range(width):
        gray = g[i,j]
        num_green[gray] = num_green[gray]+1 
for i in range(height):
    for j in range(width):
        gray = b[i,j]
        num_blue[gray] = num_blue[gray]+1 
        '''
print(num_red)
print(num_green)
print(num_blue)
'''
for i in range(256):
    avag[i]=((num_red[i]+num_green[i]+num_blue[i])/3)*1.0
res_red=np.zeros((height,width),np.uint8)
res_green=np.zeros((height,width),np.uint8)
res_blue=np.zeros((height,width),np.uint8)
res_red_a=np.zeros((height,width),np.uint8)
res_green_a=np.zeros((height,width),np.uint8)
res_blue_a=np.zeros((height,width),np.uint8)
result=np.zeros((height,width,3),np.uint8)
result1=np.zeros((height,width,3),np.uint8)
res_red=equalize_hist(image,num_red,0)
res_green=equalize_hist(image,num_green,1)
res_blue=equalize_hist(image,num_blue,2)
res_red_a=equalize_hist(image,avag,0)
res_green_a=equalize_hist(image,avag,1)
res_blue_a=equalize_hist(image,avag,2)
for i in range(height):
    for j in range(width):
        result[i,j,0]=res_red[i,j]
        result[i,j,1]=res_green[i,j]
        result[i,j,2]=res_blue[i,j]
        result1[i,j,0]=res_red_a[i,j]
        result1[i,j,1]=res_green_a[i,j]
        result1[i,j,2]=res_blue_a[i,j]
'''
cv.imwrite('/Users/dongchenyu/Documents/red.png', r)
cv.imwrite('/Users/dongchenyu/Documents/green.png', g)
cv.imwrite('/Users/dongchenyu/Documents/blue.png', b)
'''
cv.imwrite('/Users/dongchenyu/Documents/result.png', result);
cv.imwrite('/Users/dongchenyu/Documents/result1.png', result1);
print(result1)
