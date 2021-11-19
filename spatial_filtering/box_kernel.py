import matplotlib.pyplot as plt
import numpy as np
from scipy import signal, misc
import cv2 as cv
import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
from conv import *
from kernel import *
if __name__ == "__main__":
    #盒式核
    s = visualization(1,5)
    kernel = box_kernel(3)
    original = get_examples_image2(3)
    blur1 = convolve3d(original,kernel,boundary='symm',mode='same')
    kernel = box_kernel(7)
    blur2 = convolve3d(original,kernel,boundary='symm',mode='same')
    kernel = box_kernel(11)
    blur3 = convolve3d(original,kernel,boundary='symm',mode='same')
    kernel = box_kernel(21)
    blur4 = convolve3d(original,kernel,boundary='symm',mode='same')
    s.append_img(original)
    s.append_img(blur1)
    s.append_img(blur2)
    s.append_img(blur3)
    s.append_img(blur4)
    s.show()