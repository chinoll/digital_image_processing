import numpy as np
import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
from kernel import *
from conv import *

if __name__ == "__main__":
    s = visualization(1,4)
    #罗伯特梯度算子
    kernel = roberts_kernel(1)
    img = get_examples_image(3)
    s.append_img(img)
    img1 = convolve3d(img,kernel)
    s.append_img(img1)
    s.append_img(img - img1)
    s.append_img(img + img1)
    s.show()