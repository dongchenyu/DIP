import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import pylab
def padding(image,n,m):
    N=image.shape[0]
    M=image.shape[1]
    output=np.zeros((n,m))
    for i in range(n):
        for j in range(m):
            output[i,j]=0
    for i in range(N):
        for j in range(M):
            output[i,j]=image[i,j]
    return output
def center(image):
    m = image.shape[0]
    n = image.shape[1]
    output=np.zeros((m,n))
    for x in range(m):
        for y in range(n):
            output[x,y]=image[x, y]*((-1) ** (x+y))
    return output
def dft_2d(image):
    N=image.shape[0]
    M=image.shape[1]
    s=complex(0)
    t=complex(0)
    output=np.zeros((N,M),np.complex)
    temp=np.zeros((N,M),np.complex)
    for x in range(M):
        for v in range(N):
            for y in range(N):
                s+=image[y,x]*np.exp(-1.j*2*np.pi*v*y/N)
            temp[v,x]=s
            s=complex(0)
    for v in range(N):
        for u in range(M):
            for x in range(M):
                t+=temp[v,x]*np.exp(-1.j*2*np.pi*u*x/M)
            output[v,u]=t
            t=complex(0)
    return output
def dft2d(image,flags):
    h1=image.shape[0]
    w1=image.shape[1]
    if(flags == 0):
        cen = center(image)
        result=dft_2d(cen)
        return result
    else:
        temp=np.zeros((h1,w1),np.complex)
        t=0
        for i in range (h1):
            for j in range (w1):
                t=np.conjugate(image[i,j])
                temp[i,j]=t
        temp2=dft_2d(temp)
        temp3=np.zeros((h1,w1),np.complex)
        for i in range (h1):
            for j in range (w1):
                temp3[i,j]=np.conjugate((temp2[i,j]/(h1*w1)))
        result3=center(temp3)
        return result3
image = cv.imread('/Users/dongchenyu/Documents/23.png',0)
h = image.shape[0]
w = image.shape[1]
image1=padding(image,h+5,w+5)
image2=padding(image,h+3,w+3)
Fuv=dft2d(image1,0)
fimg = np.log(np.abs(Fuv)+1)
filter1=np.ones((5,5))
m=filter1.shape[0]
n=filter1.shape[1]
filter2=padding(filter1,h+5,w+5)
Huv=dft2d(filter2,0)
Guv = Huv * Fuv

gimg = np.log(np.abs(Guv)+1)
plt.imshow(np.abs(gimg),'gray')
plt.axis('off')
plt.show()
iimg=dft2d(Guv,1)
iimg = center(iimg)
output=np.zeros((h,w))
for i in range(h):
        for j in range(w):
            output[i,j]=iimg[i+2,j+2]
plt.imshow(np.abs(output),'gray')
plt.axis('off')
plt.show()

filter_lap=np.zeros((3,3))
filter_lap[0,0]=0
filter_lap[0,1]=1
filter_lap[0,2]=0
filter_lap[1,0]=1
filter_lap[1,1]=-3
filter_lap[1,2]=0
filter_lap[2,0]=1
filter_lap[2,1]=0
filter_lap[2,2]=1
filter_lap2=padding(filter_lap,h+3,w+3)
Fuv2=dft2d(image2,0)
Huv2=dft2d(filter_lap2,0)
Guv2 = Huv2 * Fuv2
gimg2 = np.log(np.abs(Guv2)+1)
plt.imshow(np.abs(gimg2),'gray')
plt.axis('off')
plt.show()
iimg2=dft2d(Guv2,1)
iimg2=center(iimg2)
output2=np.zeros((h,w))
for i in range(h):
    for j in range(w):
        output2[i,j]=int(iimg2[i+1,j+1])
        output2[i,j]=abs(output2[i,j])
        output2[i,j]=output2[i,j]%256
print(output2)
plt.imshow(np.abs(output2),'gray')
plt.axis('off')
plt.show()
