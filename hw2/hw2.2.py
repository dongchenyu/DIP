import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
def cal_ave33(image,filter,i,j):
    result=image[i,j]*filter[1,1]+image[(i-1),(j-1)]*filter[0,0]+image[(i-1),j]*filter[0,1]+image[(i-1),(j+1)]*filter[0,2]+image[i,(j-1)]*filter[1,0]+image[i,(j+1)]*filter[1,2]+image[(i+1),(j-1)]*filter[2,0]+image[(i+1),j]*filter[2,1]+image[(i+1),(j+1)]*filter[2,2]
    result=result/9
    result=int(result)
    return result
def cal_ave55(image,filter,i,j):
    result=0;
    for i_ in range(i-2,i+3):
        for j_ in range(j-2,j+3):
            result+=image[i_,j_]
    result=result/25
    result=int(result)
    return result
def cal_ave77(image,filter,i,j):
    result=0;
    for i_ in range(i-3,i+4):
        for j_ in range(j-3,j+4):
            result+=image[i_,j_]
    result=result/49
    result=int(result)
    return result
def cal_lap(image,filter,i,j):
    result=int(9*image[i,j])-int(image[(i-1),(j-1)])-int(image[(i-1),j])-int(image[(i-1),(j+1)])-int(image[i,(j-1)])-int(image[i,(j+1)])-int(image[(i+1),(j-1)])-int(image[(i+1),j])-int(image[(i+1),(j+1)])
    result=int(result)
    if(result<0):
        result=0
    return result
def filter2d33(image,filter):
    height = image.shape[0]
    width = image.shape[1]
    res = np.zeros([height+2,width+2],np.uint8)
    temp = np.zeros([height+2,width+2],np.uint8)
    fin = np.zeros([height,width],np.uint8)
    for i in range(1,height+1):
        for j in range(1,width+1):
            temp[i,j]=image[(i-1),(j-1)]
    #print(temp)
    for i in range(1,height+1):
        for j in range(1,width+1):
            res[i,j]=cal_ave33(temp,filter,i,j)
            fin[i-1][j-1]=res[i,j]
    return fin
def filter2d55(image,filter1):
    height = image.shape[0]
    width = image.shape[1]
    res1 = np.zeros([height+4,width+4],np.uint8)
    temp1 = np.zeros([height+4,width+4],np.uint8)    
    fin1 = np.zeros([height,width],np.uint8)      
    for i in range(2,height+2):
        for j in range(2,width+2):
            temp1[i,j]=image[(i-2),(j-2)]  
    for i in range(2,height+2):
        for j in range(2,width+2):
            res1[i,j]=cal_ave55(temp1,filter1,i,j)
            fin1[i-2][j-2]=res1[i,j]
    return fin1
def filter2d77(image,filter2):
    height = image.shape[0]
    width = image.shape[1]
    res2 = np.zeros([height+6,width+6],np.uint8)
    temp2 = np.zeros([height+6,width+6],np.uint8) 
    fin2 = np.zeros([height,width],np.uint8)         
    for i in range(3,height+3):
        for j in range(3,width+3):
            temp2[i,j]=image[(i-3),(j-3)]  
    for i in range(3,height+3):
        for j in range(3,width+3):
            res2[i,j]=cal_ave77(temp2,filter2,i,j)
            fin2[i-3][j-3]=res2[i,j]
    return fin2
def laplace_filter(image,laplace):
    height = image.shape[0]
    width = image.shape[1]
    res = np.zeros([height+2,width+2],np.uint8)
    temp = np.zeros([height+2,width+2],np.uint8)
    fin = np.zeros([height,width],np.uint8)
    for i in range(1,height+1):
        for j in range(1,width+1):
            temp[i,j]=image[(i-1),(j-1)]
    for i in range(1,height+1):
        for j in range(1,width+1):
            res[i,j]=cal_lap(temp,laplace,i,j)
            fin[i-1][j-1]=res[i,j]
    return fin
def subtract(img1,img2):
    height = img1.shape[0]
    width = img1.shape[1]
    res = np.zeros([height,width],np.uint8)
    for i in range(0,height):
        for j in range(0,width):
            res[i,j]=int(img1[i,j])-int(img2[i,j])
            res[i,j]=int(2*res[i,j])
            if(res[i,j]<0):
                res[i,j]=0
    return res
def add(img1,img2):
    height = img1.shape[0]
    width = img1.shape[1]
    res = np.zeros([height,width],np.uint8)
    for i in range(0,height):
        for j in range(0,width):
            res[i,j]=int(img1[i,j])+int(img2[i,j])
            if(res[i,j]>255):
                res[i,j]=255
    return res
image = cv.imread('/Users/dongchenyu/Documents/23.png',0) 
filter = np.array([[1, 1, 1],[1, 1, 1],[1, 1, 1]])
filter1 = np.array([[1, 1, 1, 1, 1],[1, 1 ,1, 1, 1],[1, 1, 1, 1, 1],[1, 1 ,1, 1, 1],[1, 1 ,1, 1, 1]])
filter2 = np.array([[1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1]])
laplace=np.array([[1, 1, 1],[1, -8, 1],[1, 1, 1]])
#print(filter2d(image,filter))
#print(image)
#print(filter[1,1])
b=filter2d33(image,filter)
c=filter2d55(image,filter1)
d=filter2d77(image,filter2)
e=laplace_filter(image,laplace)
sub=subtract(image,b)
res_img=add(sub,image)
cv.imwrite('/Users/dongchenyu/Documents/result.png', b)
cv.imwrite('/Users/dongchenyu/Documents/result2.png', c)
cv.imwrite('/Users/dongchenyu/Documents/result3.png', d)
cv.imwrite('/Users/dongchenyu/Documents/laplace.png', e)
cv.imwrite('/Users/dongchenyu/Documents/k2.png', res_img)