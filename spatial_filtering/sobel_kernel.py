import numpy as np
import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
from kernel import *
from conv import *

if __name__ == "__main__":
    s = visualization(1,4)
    #sobel算子
    x_kernel = sobel_kernel(1)
    y_kernel = sobel_kernel(0)
    img = get_examples_image(3)
    s.append_img(img)
    img1 = convolve3d(img,x_kernel)
    s.append_img(img1)
    img2 = convolve3d(img,y_kernel)
    s.append_img(img2)
    s.append_img(img1+img2)
    s.show()