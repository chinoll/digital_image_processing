import numpy as np
from scipy.ndimage.interpolation import rotate
import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
def multi_channel(mask,channel):
    if channel == 3:
        return np.stack([mask,mask,mask],axis=2)
    else:
        return mask

def TBLPF(h:int,w:int,radius:int,n:int,k,channel:int=1) -> np.ndarray:
    '''
    巴特沃斯低通滤波器
    :param h: 高
    :type h: int
    :param w: 宽
    :type w: int
    :param radius: 半径
    :type radius: int
    :param n: 滤波器阶数
    :type n: int,list,tuple
    :param k: 滤波器对称中心
    :type k: int,list,tuple
    :param channel: 通道数
    :return: np.ndarray(channel,h,w)
    '''
    def H(ki,D0):
        xi,yi = ki
        X,Y = np.mgrid[-h//2+1-xi:h//2+1-xi,-w//2+1-yi:w//2+1-yi]
        D = np.sqrt(X**2+Y**2)
        D[D==0] = 1e-8
        mask = 1/(1+pow(D0/D,2*n))
        X,Y = np.mgrid[-h//2+1+xi:h//2+1+xi,-w//2+1+yi:w//2+1+yi]
        D = np.sqrt(X**2+Y**2)
        D[D==0] = 1e-8
        mask *= 1/(1+pow(D0/D,2*n))
        return mask
    mask = None
    if type(k) == list and len(k) != n:
        kl = []
        for i in range(n):
            if i < len(k):
                if type(k[i]) != tuple and type(k[i]) != list:
                    kl.append((k[i],k[i]))
                else:
                    kl.append(k[i])
            else:
                if type(k[-1]) != tuple and type(k[-1]) != list:
                    kl.append((k[-1],k[-1]))
                else:
                    kl.append(k[-1])
        k = kl
    elif type(k) == int:
        k = [(k,k)]*n

    if type(radius) == list and len(k) != n:
        raise Exception("radius must be a list with length of n")
    elif type(radius) == int:
        if radius < 0:
            raise Exception("radius must be a positive integer")
        radius = [radius]*n
    else:
        for i in range(len(radius)):
            if radius[i] < 0:
                raise Exception("radius must be a positive integer")
            if type(radius[i]) == float:
                radius[i] = int(radius[i])
            elif type(radius[i]) != int:
                raise Exception("radius must be a positive integer")

    for i,j in zip(k,radius):
        if type(mask) != np.ndarray:
            mask = H(i,j)
        else:
            mask *= H(i,j)
    return multi_channel(mask,channel)

def ifft(img):
    fshift = np.fft.ifftshift(img)
    img_back = np.fft.ifftn(fshift)
    img_back = np.abs(img_back)
    return img_back

def fft(img):
    dft = np.fft.fftn(img)
    dft_shift = np.fft.fftshift(dft)
    return dft_shift

def fft_log(img,K=14):
    if img.ndim == 2:
        return np.log(1 + np.abs(img))
    elif img.ndim == 3:
        #彩色图像，乘上一个缩放系数，以免在显示的时候看不见
        return np.log(1 + np.abs(img))*K