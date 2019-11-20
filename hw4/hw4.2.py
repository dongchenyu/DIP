import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math
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
    for i in range(0,256):
        temp=255.0*pdf[i]
        if(temp-int(temp)>=0.5):
            temp=int(temp)+1
        else:
            temp=int(temp)
        trans[i]=temp
    result = np.zeros([h,w])
    for i in range(0,h):
        for j in range(0,w):
            temp_=image[i,j,n]
            result[i,j]=trans[int(temp_)]
    return result

def get_s(r,g,b):
    result=np.zeros((height,width))
    for i in range(height):
        for j in range(width):
            min_num=min(r[i,j],g[i,j],b[i,j])
            if((r[i,j]+g[i,j]+b[i,j])==0):
                result[i,j]=1
            else:
                result[i,j]=1-(3*min_num)/(r[i,j]+g[i,j]+b[i,j])
    return result

def get_i(r,g,b):
    res=(r+g+b)/3
    return res

def get_h(r,g,b):
    result=np.zeros((height,width))
    for i in range(height):
        for j in range(width):
            fenzi=(2*r[i,j]-g[i,j]-b[i,j])/2
            fenmu=math.sqrt((r[i,j]-g[i,j])*(r[i,j]-g[i,j])+(r[i,j]-b[i,j])*(g[i,j]-b[i,j]))
            if(fenmu==0):
                theta=0
            else:
                theta=np.arccos(fenzi/fenmu)
            if(b[i,j]<=g[i,j]):
                result[i,j]=theta/(2*np.pi)
            else:
                theta=(2*np.pi)-theta
                result[i,j]=theta/(2*np.pi)
    return result
def hsi_to_rgb(res_h,res_s,res_i):
    height=res_h.shape[0]
    width=res_h.shape[1]
    rgb=np.zeros((height,width,3))
    for i in range(height):
        for j in range(width):
            alpha=2*np.pi*res_h[i,j]
            if(res_h[i,j]<1/3):
                rgb[i,j,2]=res_i[i,j]*(1-res_s[i,j])
                temp=np.cos(np.pi/3-alpha)
                rgb[i,j,0]=res_i[i,j]*(1+res_s[i,j]*np.cos(alpha)/temp)
                rgb[i,j,1]=3*res_i[i,j]-rgb[i,j,0]-rgb[i,j,2]
            elif(res_h[i,j]>=1/3 and res_h[i,j]<2/3):
                alpha=alpha-2*np.pi/3
                rgb[i,j,0]=res_i[i,j]*(1-res_s[i,j])
                temp=np.cos(np.pi/3-alpha)
                rgb[i,j,1]=res_i[i,j]*(1+res_s[i,j]*np.cos(alpha)/temp)
                rgb[i,j,2]=3*res_i[i,j]-rgb[i,j,0]-rgb[i,j,1]
            else:
                alpha=alpha-4*np.pi/3
                rgb[i,j,1]=res_i[i,j]*(1-res_s[i,j])
                temp=np.cos(np.pi/3-alpha)
                rgb[i,j,2]=res_i[i,j]*(1+res_s[i,j]*np.cos(alpha)/temp)
                rgb[i,j,0]=3*res_i[i,j]-rgb[i,j,1]-rgb[i,j,2]
    return rgb
image = cv.imread('/Users/dongchenyu/Documents/23.png',1) 
height=image.shape[0]
width=image.shape[1]
r=np.zeros((height,width))
g=np.zeros((height,width))
b=np.zeros((height,width))
for i in range(height):
    for j in range(width):
        r[i][j]=image[i][j][0]/255
for i in range(height):
    for j in range(width):
        g[i][j]=image[i][j][1]/255
for i in range(height):
    for j in range(width):
        b[i][j]=image[i][j][2]/255
#print(image)
'''
print(r)
print(g)
print(b)
'''
res_h=np.zeros((height,width))
res_s=np.zeros((height,width))
res_i=np.zeros((height,width))
res_hsi=np.zeros((height,width,3))
res_rgb=np.zeros((height,width,3))
res_h=get_h(r,g,b)
res_i=get_i(r,g,b)
res_s=get_s(r,g,b)
res_h_temp=get_h(r,g,b)
res_s_temp=get_s(r,g,b)
res_i_temp=get_i(r,g,b)
'''
print(res_h)
print(res_i)
print(res_s)
'''
for i in range(height):
    for j in range(width):
        res_hsi[i,j,0]=res_h[i,j]*255
        res_hsi[i,j,1]=res_s[i,j]*255
        res_hsi[i,j,2]=res_i[i,j]*255
num_i=np.zeros(256)
for i in range(height):
    for j in range(width):
        temp=res_hsi[i,j,2]
        intensy = int(temp)
        num_i[intensy] = num_i[intensy]+1 
res_inten=equalize_hist(res_hsi,num_i,2)
for i in range(height):
    for j in range(width):
        res_h[i,j]=res_hsi[i,j,0]/255
        res_s[i,j]=res_hsi[i,j,1]/255
        res_i[i,j]=res_hsi[i,j,2]/255
        res_inten[i,j]=res_inten[i,j]/255
        '''
print(res_hsi)
print(res_h)
print(res_s)
print(res_inten)
'''
res_rgb=hsi_to_rgb(res_h,res_s,res_inten)
for i in range(height):
    for j in range(width):
        res_rgb[i,j,0]=res_rgb[i,j,0]*255
        res_rgb[i,j,1]=res_rgb[i,j,1]*255
        res_rgb[i,j,2]=res_rgb[i,j,2]*255
cv.imwrite('/Users/dongchenyu/Documents/hsi.png', res_hsi);
cv.imwrite('/Users/dongchenyu/Documents/rgb.png', res_rgb);



