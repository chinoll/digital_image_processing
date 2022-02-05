import numpy as np

def pad_image(img:np.ndarray,m:int,n:int)->np.ndarray:
    if img.ndim == 3:
        return np.pad(img,((m,m),(n,n),(0,0)),'edge')
    else:
        return np.pad(img,((m,m),(n,n)),'edge')

def erode(img,kernel=np.ones((3,3),np.uint8),iterations=1):
    img = img.copy()
    if img.ndim == 3:
        m,n,c = img.shape
    else:
        m,n = img.shape
    k,l = kernel.shape
    img = pad_image(img,k-1,l-1)
    print(img.shape)
    for i in range(iterations):
        if img.ndim != 3:
            for i in range(m):
                for j in range(n):
                    img[i,j] = np.min(img[i:i+k,j:j+l]-kernel)
        else:
            for i in range(c):
                for j in range(m):
                    for z in range(n):
                        img[j,z,i] = np.min(img[j:j+k,z:z+l,i]-kernel)
    return img

def dilate(img,kernel=np.ones((3,3),np.uint8),iterations=1):
    img = img.copy()
    if img.ndim == 3:
        m,n,c = img.shape
    else:
        m,n = img.shape
    k,l = kernel.shape
    img = pad_image(img,k-1,l-1)
    for i in range(iterations):
        if img.ndim != 3:
            for i in range(m):
                for j in range(n):
                    img[i,j] = np.max(img[i:i+k,j:j+l]+kernel)
        else:
            for i in range(c):
                for j in range(m):
                    for z in range(n):
                        img[j,z,i] = np.max(img[j:j+k,z:z+l,i]+kernel)
    return img

def close(img,kernel,iterations=1):
    for _ in range(iterations):
        img = dilate(img,kernel)
        img = erode(img,kernel)
    return img

def open(img,kernel,iterations=1):
    for _ in range(iterations):
        img = erode(img,kernel)
        img = dilate(img,kernel)
    return img