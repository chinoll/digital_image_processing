from scipy import signal
import numpy as np
def convolve3d(img,kernel,boundary='symm',mode='same'):
    if img.ndim == 3:
        R,G,B = img[:,:,0],img[:,:,1],img[:,:,2]
        
        R = signal.convolve2d(R,kernel,boundary=boundary,mode=mode)
        G = signal.convolve2d(G,kernel,boundary=boundary,mode=mode)
        B = signal.convolve2d(B,kernel,boundary=boundary,mode=mode)
        
        return np.stack([R,G,B],axis=2)
    else:
        return signal.convolve2d(img,kernel,boundary=boundary,mode=mode)