import numpy as np

class geometric_mean:
    def __init__(self,kernel_size=(3,3)):
        if kernel_size[0]%2==0 or kernel_size[1]%2==0:
            raise ValueError("Kernel size must be odd")

        self.shape = kernel_size
    def __mul__(self,other):
        if other.shape != self.shape:
            raise ValueError("Kernel size must be the same")
        other[other == 0] = 1
        if np.prod(self.shape) > 15:
            output = np.prod(other.astype(np.complex128).real)**(1/self.shape[0]/self.shape[1])
        else:
            output = np.prod(other)**(1/self.shape[0]/self.shape[1])
        return output