import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
import numpy as np
from morphological import hole_filling
if __name__ == '__main__':
    img = get_examples_image()
    img[img > 127] = 255
    img[img <= 127] = 0
    s = visualization()
    s.append_img(img)
    kernel = np.ones((3,3),np.uint32)
    s.append_img(hole_filling(img,kernel))
    kernel = np.ones((11,11),np.uint32)
    s.append_img(hole_filling(img,kernel))

    kernel = np.ones((3,3),np.uint32)
    s.append_img(hole_filling(img,kernel,5))
    s.append_img(hole_filling(img,kernel,15))
    s.show()