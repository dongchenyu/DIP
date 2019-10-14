import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
def draw_histogram(image): 
    num = [0]*256       
    h = image.shape[0]
    w = image.shape[1]
    for i in range(h):
        for j in range(w):
            gray = image[i,j]
            num[gray] = num[gray]+1      
    y = num
    x = [i for i in range(256)]
    plt.figure("histogram")
    plt.xlabel("gray")
    plt.ylabel("number")
    plt.plot(x,y)
    plt.xlim([0,256])
    return num        
def equalize_hist(image,num):
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
            result[i,j]=trans[image[i,j]]
    return result
def dif(image1,image2):
    height = image1.shape[0]
    width = image1.shape[1]
    num = 0
    for i in range(0,height):
        for j in range(0,width):
            if(image1[i,j]!=image2[i,j]):
                num+=1
    return num
image = cv.imread('/Users/dongchenyu/Documents/23.png',0)             
a = draw_histogram(image)    
b = equalize_hist(image,a)  
num = [0]*256       
height = b.shape[0]
width = b.shape[1]
for i in range(height):
    for j in range(width):
        gray = b[i,j]
        num[gray] = num[gray]+1 
c = equalize_hist(b,num)       
cv.imwrite('/Users/dongchenyu/Documents/equ.png', b)        
cv.imwrite('/Users/dongchenyu/Documents/equ2.png', c)     
if(dif(b,c)==0):
    print('same')
else:
    print('not same')
draw_histogram(b)       
draw_histogram(c)                   
plt.show()  
