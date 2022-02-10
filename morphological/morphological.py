import numpy as np

def pad_image(img:np.ndarray,m:int,n:int)->np.ndarray:
    if img.ndim == 3:
        return np.pad(img,((m,m),(n,n),(0,0)),'constant',constant_values=0)
    else:
        return np.pad(img,((m,m),(n,n)),'constant',constant_values=0)

def gray_erode(img,kernel=np.ones((3,3),np.uint8),iterations=1):
    img = img.copy()
    if img.ndim == 3:
        m,n,c = img.shape
    else:
        m,n = img.shape
    k,l = kernel.shape
    template = pad_image(img,k//2,l//2)
    for i in range(iterations):
        if img.ndim != 3:
            for i in range(m):
                for j in range(n):
                    img[i,j] = np.min(template[i:i+k,j:j+l]-kernel)
        else:
            for i in range(c):
                for j in range(m):
                    for z in range(n):
                        img[j,z,i] = np.min(template[j:j+k,z:z+l,i]-kernel)
    return img

def gray_dilate(img,kernel=np.ones((3,3),np.uint8),iterations=1):
    img = img.copy()
    if img.ndim == 3:
        m,n,c = img.shape
    else:
        m,n = img.shape
    k,l = kernel.shape
    template = pad_image(img,k//2,l//2)
    for i in range(iterations):
        if img.ndim != 3:
            for i in range(m):
                for j in range(n):
                    img[i,j] = np.max(template[i:i+k,j:j+l]+kernel)
        else:
            for i in range(c):
                for j in range(m):
                    for z in range(n):
                        img[j,z,i] = np.max(template[j:j+k,z:z+l,i]+kernel)
    return img

def binary_erode(img,kernel,iterations=1):
    img = img.copy()
    m,n = img.shape
    k,l = kernel.shape
    template = pad_image(img,k//2,l//2)
    for _ in range(iterations):
        for i in range(m):
            for j in range(n):
                img[i,j] = 255 if np.sum(template[i:i+k,j:j+l]&kernel) == np.sum(kernel) else 0
    return img

def binary_dilate(img,kernel,iterations=1):
    img = img.copy()
    m,n = img.shape
    k,l = kernel.shape
    template = pad_image(img,k//2,l//2)
    for _ in range(iterations):
        for i in range(m):
            for j in range(n):
                img[i,j] = 255 if np.sum(template[i:i+k,j:j+l]&kernel) != 0 else 0
    return img

def erode(img,kernel=np.ones((3,3)),iterations=1):
    if len(np.unique(img)) == 2:
        return binary_erode(img,kernel,iterations)
    else:
        return gray_erode(img,kernel,iterations)

def dilate(img,kernel=np.ones((3,3)),iterations=1):
    if len(np.unique(img)) == 2:
        return binary_dilate(img,kernel,iterations)
    else:
        return gray_dilate(img,kernel,iterations)

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

def hmt(img,kernel,iterations=1):
    img = img.copy().astype(np.int32)
    kernel = kernel.astype(np.int32)
    for _ in range(iterations):
        k = kernel.copy()
        k[k<0] = 0
        img1 = binary_erode(img,k)
        k = kernel.copy()
        k[kernel>0] = 0
        img2 = binary_erode(255 - img,np.abs(k))
    return img1 & img2

def binary_edge(img,kernel=np.ones((3,3),np.int32)):
    return img.astype(np.int32)-erode(img,kernel.astype(np.int32))

#孔洞填充
def hole_filling(img,kernel=np.ones((3,3)),iterations=1):
    ic = 255 - img.copy().astype(np.uint8)
    i = img.copy().astype(np.uint8)
    for _ in range(iterations):
        i = dilate(i,kernel) & ic
    return i | img.astype(np.uint8)

#梯度
def gradient(img,kernel=np.ones((3,3),np.uint8)):
    return dilate(img,kernel) - erode(img,kernel)