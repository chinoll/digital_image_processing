import numpy as np
class geometric_mean:
    def __init__(self,kernel_size=(3,3)):
        if kernel_size[0]%2==0 or kernel_size[1]%2==0:
            raise ValueError("Kernel size must be odd")

        self.shape = kernel_size

    def __mul__(self,other:np.ndarray) -> int:
        if other.shape != self.shape:
            raise ValueError("Kernel size must be the same")
        other[other == 0] = 1
        if np.prod(self.shape) > 15:
            output = np.prod(other.astype(np.complex128).real)**(1/self.shape[0]/self.shape[1])
        else:
            output = np.prod(other)**(1/self.shape[0]/self.shape[1])
        return output

class contra_harmonic_mean:
    def __init__(self,kernel_size=(3,3),Q=0):
        if kernel_size[0]%2==0 or kernel_size[1]%2==0:
            raise ValueError("Kernel size must be odd")

        self.shape = kernel_size
        self.Q = Q

    def __mul__(self,other:np.ndarray) -> int:
        if other.shape != self.shape:
            raise ValueError("Kernel size must be the same")
        other[other == 0] = 1
        output = (np.sum(other**(self.Q+1)))/np.sum((other**self.Q))
        return output

def harmonic_mean(kernel_size=(3,3)):
    return contra_harmonic_mean(kernel_size,Q=-1)

class median:
    def __init__(self,kernel_size=(3,3)):
        if kernel_size[0]%2==0 or kernel_size[1]%2==0:
            raise ValueError("Kernel size must be odd")

        self.shape = kernel_size

    def __mul__(self,other:np.ndarray) -> int:
        if other.shape != self.shape:
            raise ValueError("Kernel size must be the same")
        output = np.median(other)
        return output

class minimum:
    def __init__(self,kernel_size=(3,3)):
        if kernel_size[0]%2==0 or kernel_size[1]%2==0:
            raise ValueError("Kernel size must be odd")

        self.shape = kernel_size

    def __mul__(self,other:np.ndarray) -> int:
        if other.shape != self.shape:
            raise ValueError("Kernel size must be the same")
        output = np.min(other)
        return output

class maximum:
    def __init__(self,kernel_size=(3,3)):
        if kernel_size[0]%2==0 or kernel_size[1]%2==0:
            raise ValueError("Kernel size must be odd")

        self.shape = kernel_size

    def __mul__(self,other:np.ndarray) -> int:
        if other.shape != self.shape:
            raise ValueError("Kernel size must be the same")
        output = np.max(other)
        return output

class alpha_trimmed_mean:
    def __init__(self,kernel_size=(3,3),d:int=1):
        if kernel_size[0]%2==0 or kernel_size[1]%2==0:
            raise ValueError("Kernel size must be odd")

        self.shape = kernel_size
        self.d = d

    def __mul__(self,other:np.ndarray) -> int:
        if other.shape != self.shape:
            raise ValueError("Kernel size must be the same")
        other = other.reshape(-1)
        output = np.mean(np.sort(other)[int(self.d/2):len(other)-1-int(np.ceil(self.d/2))])
        return output

class midpoint:
    def __init__(self,kernel_size=(3,3)):
        if kernel_size[0]%2==0 or kernel_size[1]%2==0:
            raise ValueError("Kernel size must be odd")

        self.shape = kernel_size
    def __mul__(self,other:np.ndarray) -> int:
        if other.shape != self.shape:
            raise ValueError("Kernel size must be the same")
        output = np.max(other) + np.min(other)
        return output/2

class adaptive_local:
    def __init__(self,kernel_size=(3,3),image=None,sigma=None) -> None:
        if kernel_size[0]%2==0 or kernel_size[1]%2==0:
            raise ValueError("Kernel size must be odd")
        p=0.9
        self.shape = kernel_size
        if sigma == None:
            self.sigma = self.calc_variance(image)*p
        else:
            self.sigma=sigma

        self.gx = (kernel_size[0]-1)//2
        self.gy = (kernel_size[1]-1)//2

    def calc_variance(self,image:np.ndarray) -> int:
        hist,bins = np.histogram(image.flatten(), bins=256, range=(0, 256),density=True)
        r = bins[:-1]
        m = np.sum(hist*r)
        sigma = np.sum(hist*(r-m)**2)
        return sigma
    def __mul__(self,other:np.ndarray) -> int:
        if other.shape != self.shape:
            raise ValueError("Kernel size must be the same")
        g = other[self.gx,self.gy]
        sigma = np.var(other)
        if sigma == 0:
            sigma=1e-8
        p = self.sigma/sigma
        if p > 1:
            p = 1
        return g-p*(g-np.mean(other))

class ada_median:
    def __init__(self,smax=7) -> None:
        if smax%2 == 0:
            raise ValueError("Kernel size must be odd")
        self.smax = smax
        self.shape = (smax,smax)
    def __mul__(self,other:np.ndarray) -> int:
        if other.shape != self.shape:
            raise ValueError("Kernel size must be the same")
        z = other[self.smax//2,self.smax//2]
        fmedian = np.median(other)
        x,y = (3,3)
        while x <= self.smax and y <= self.smax:
            zmatrix = other[other.shape[0]//2+x//2:int(np.ceil(other.shape[0]/2))+x//2,
                            other.shape[1]//2+y//2:int(np.ceil(other.shape[1]/2))+y//2]
            median = np.median(zmatrix)
            minimum = np.min(zmatrix)
            maximum = np.max(zmatrix)
            if minimum < median and median < maximum:
                if minimum < z and z < maximum:
                    return z
                else:
                    return median
            else:
                x+=2
                y+=2
        return fmedian
        