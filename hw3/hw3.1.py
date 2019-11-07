import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import pylab
'''
def dft2d(image):
    h=image.shape[0]
    w=image.shape[1]
    output=np.zeros((h,w),np.complex)
    for u in range(h):
        for v in range(w):
            s=complex(0)
            for x in range(h):
                for y in range(w):
                    s +=image[x,y]*np.exp(-2j*np.pi*(u*x/float(h)+v*y/float(w)))
            output[u,v]=s
    return output
'''
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
    if(flags == 0):
        cen = center(image)
        result=dft_2d(cen)
        return result
    else:
        temp=np.zeros((h,w),np.complex)
        t=0
        for i in range (h):
            for j in range (w):
                t=np.conjugate(image[i,j])
                temp[i,j]=t
        temp2=dft_2d(temp)
        temp3=np.zeros((h,w),np.complex)
        for i in range (h):
            for j in range (w):
                temp3[i,j]=np.conjugate((temp2[i,j]/(h*w)))
        result3=center(temp3)
        return result3
def center(image):
    m = image.shape[0]
    n = image.shape[1]
    output=np.zeros((m,n),np.uint8)
    for x in range(m):
        for y in range(n):
            output[x,y]=image[x, y]*((-1) ** (x+y))
    return output
image = cv.imread('/Users/dongchenyu/Documents/23.png',0)
h = image.shape[0]
w = image.shape[1]
dft=dft2d(image,0)
result = np.log(1 + np.abs(dft))
plt.imshow(np.abs(result),'gray')
plt.axis('off')
plt.show()
idft=dft2d(dft,1)
plt.imshow(np.abs(idft),'gray')
plt.axis('off')
plt.show()


