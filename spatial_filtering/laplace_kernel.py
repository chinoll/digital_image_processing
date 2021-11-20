import numpy as np
import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
from kernel import *
from conv import *

if __name__ == "__main__":
    s = visualization(1,3)
    #拉普拉斯核
    kernel = laplace_kernel()
    img = get_examples_image(3)
    s.append_img(img)
    img1 = convolve3d(img,kernel)
    s.append_img(img1)
    s.append_img(img - img1)
    s.show()