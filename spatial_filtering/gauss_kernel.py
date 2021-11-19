import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
from conv import *
from kernel import *
if __name__ == "__main__":
    #高斯核
    s = visualization(1,5)
    kernel = gauss_kernel(3)
    origin = get_examples_image2(3)
    blur1 = convolve3d(origin,kernel,boundary='symm',mode='same')
    kernel = gauss_kernel(7)
    blur2 = convolve3d(origin,kernel,boundary='symm',mode='same')
    kernel = gauss_kernel(21)
    blur3 = convolve3d(origin,kernel,boundary='symm',mode='same')
    kernel = gauss_kernel(43)
    blur4 = convolve3d(origin,kernel,boundary='symm',mode='same')
    s.append_img(origin)
    s.append_img(blur1)
    s.append_img(blur2)
    s.append_img(blur3)
    s.append_img(blur4)
    s.show()