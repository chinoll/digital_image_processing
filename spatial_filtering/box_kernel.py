import matplotlib.pyplot as plt
import numpy as np
from scipy import signal, misc
import cv2 as cv
import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
from conv import *
if __name__ == "__main__":
    #盒式核
    kernel = np.ones((3,3))/9
    face = get_examples_image2(3)
    grad = convolve3d(face,kernel,boundary='symm',mode='same')
    plt.figure()
    plt.subplot(1,2,1)
    plt.imshow(face.astype(np.uint8))
    plt.subplot(1,2,2)
    plt.imshow(grad)
    plt.show()