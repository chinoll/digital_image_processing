from operator import mul
import numpy as np
def ILPF(h, w, radius,channel=1):
    center = (int(w/2), int(h/2))
    Y, X = np.ogrid[:h, :w]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)
    mask = dist_from_center <= radius
    return multi_channel(mask,channel)

def BLPF(h,w,radius,n=4,channel=1):
    X,Y = np.mgrid[-h//2+1:h//2+1,-w//2+1:w//2+1]
    D = np.sqrt(X**2+Y**2)
    mask = 1/(1+pow(D/radius,2*n))
    return multi_channel(mask,channel)

def GLPF(h,w,sigma,channel=1):
    X,Y = np.mgrid[-h//2+1:h//2+1,-w//2+1:w//2+1]
    D = (np.sqrt(X**2+Y**2)**2)/(2*sigma**2)
    mask = np.exp(-D)
    return multi_channel(mask,channel)

def IHPF(h,w,radius,channel=1):
    return 1 - ILPF(h,w,radius,channel)

def BHPF(h,w,radius,n=4,channel=1):
    X,Y = np.mgrid[-h//2+1:h//2+1,-w//2+1:w//2+1]
    D = np.sqrt(X**2+Y**2) + 1e-16
    mask = 1/(1+pow(radius/D,2*n))
    return multi_channel(mask,channel)

def GHPF(h,w,sigma,channel=1):
    return 1 - GLPF(h,w,sigma,channel)

def laplace(h,w,channel=1):
    X = np.zeros((h,w))
    Y = np.zeros((h,w))
    for i in range(h):
        X[i] = h-i
    for i in range(w):
        Y[:,i] = h-i
    D = X**2+Y**2
    mask = 1+4*(np.pi**2)*D
    return multi_channel(mask,channel)

def homomorphic(h,w,D0=20,gamaH=3.0,gamaL=0.4,c=5,channel=1):
    X,Y = np.mgrid[-h//2+1:h//2+1,-w//2+1:w//2+1]
    mask = (gamaH-gamaL)*(1-np.e**(-c*(X**2+Y**2)/D0)) + gamaL
    return multi_channel(mask,channel)

def IBRF(h,w,C0,W,channel=1):
    Y, X = np.ogrid[:h, :w]
    center = (int(w/2), int(h/2))
    D = np.sqrt((X - center[0])**2 + (Y-center[1])**2)
    mask = ~((D <= (C0 + W/2)) & (D >= C0-W/2))
    return multi_channel(mask,channel)

def GBRF(h,w,C0,W,channel=1):
    Y, X = np.ogrid[:h, :w]
    center = (int(w/2), int(h/2))
    D = np.sqrt((X - center[0])**2 + (Y-center[1])**2)
    D2 = D**2
    DW = D*W
    DW[DW==0]=1e-20
    mask = 1-np.e**(-(((D2-C0**2)/(DW))**2))
    return multi_channel(mask,channel)

def BBRF(h,w,C0,W,n=1,channel=1):
    Y, X = np.ogrid[:h, :w]
    center = (int(w/2), int(h/2))
    D = np.sqrt((X - center[0])**2 + (Y-center[1])**2)
    D2 = D**2
    DC=D2-C0**2
    DC[DC==0] = 1
    mask = 1/(1+((D*W)/(DC))**(2*n))
    return multi_channel(mask,channel)

def multi_channel(mask,channel):
    if channel == 3:
        return np.stack([mask,mask,mask],axis=2)
    else:
        return mask

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