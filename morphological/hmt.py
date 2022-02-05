import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
import numpy as np
from morphological import hmt
if __name__ == '__main__':
    img = get_examples_image()
    img[img > 127] = 255
    img[img <= 127] = 0
    s = visualization(1,2)
    s.append_img(img)
    kernel = np.array([[1, 0, 0],
                       [0,-1, 0],
                       [0, 0, 0]])
    s.append_img(hmt(img,kernel))
    s.show()