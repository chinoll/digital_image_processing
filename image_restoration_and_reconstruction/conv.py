import numpy as np
def pad_image(img:np.ndarray,m:int,n:int)->np.ndarray:
    if img.ndim == 3:
        return np.pad(img,((m,m),(n,n),(0,0)),'edge')
    else:
        return np.pad(img,((m,m),(n,n)),'edge')

def conv2d(img:np.ndarray,kernel) -> np.ndarray:
    """
    img: input image
    kernel: convolution kernel
    """
    # img: (m,n)
    # kernel: (k,l)
    # output: (m,n)

    img = img.copy()
    if img.ndim == 3:
        c,m,n = img.shape
    else:
        m,n = img.shape

    k,l = kernel.shape
    output = np.zeros(img.shape)
    img = pad_image(img,k//2,l//2)        
    if img.ndim != 3:
        for i in range(m):
            for j in range(n):
                output[i,j] = kernel*img[i:i+k,j:j+l]
    else:
        for i in range(c):
            for j in range(m):
                for z in range(n):
                    output[i,j,z] = kernel*img[i,j:j+k,z:z+l]
    return output