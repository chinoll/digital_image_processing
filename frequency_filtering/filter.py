import numpy as np
def LIPF(h, w, radius,channel=1):
    center = (int(w/2), int(h/2))
    Y, X = np.ogrid[:h, :w]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)
    mask = dist_from_center <= radius
    if channel == 1:
        return mask
    else:
        return np.stack([mask,mask,mask],axis=2)
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