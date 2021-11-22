import numpy as np
from math import ceil

def box_kernel(size):
    kernel = np.ones((size,size))
    return kernel/(size*size)

def gauss_kernel(size,K=1,sigma=-1):
    sigma_list = {3:1,43:7,21:3.5} #常用标准差
    if sigma == -1: #自动计算标准差
        if sigma_list.get(size) == None:
            sigma = ceil(size/6)
        else:
            sigma = sigma_list[size]
    x,y = np.mgrid[-size//2+1:size//2+1,-size//2+1:size//2+1]
    g = K*np.e**(-((x**2+y**2)/(2*sigma**2)))
    return g/g.sum()

def laplace_kernel():
    kernel = np.array([[0,1,0],[1,-4,1],[0,1,0]])
    return kernel

def roberts_kernel(t=1):
    '''
    @t: 0:Roberts kernel, 1:Roberts rotated 90 degrees kernel
    '''
    if t == 1:
        kernel = np.array([[1,0],[0,-1]])
    else:
        kernel = np.array([[0,1],[-1,0]])
    return kernel

def sobel_kernel(type=1):
    '''
    @type: 0:Sobel kernel X direction, 1:Sobel kernel Y direction
    '''
    if type == 1:
        kernel = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
    else:
        kernel = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
    return kernel