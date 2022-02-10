import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
import numpy as np
from morphological import gradient
if __name__ == '__main__':
    img = get_examples_image()
    s = visualization(1,3)
    s.append_img(img)
    kernel = np.ones((5,5))
    s.append_img(gradient(img,kernel))
    kernel = np.ones((11,11))
    s.append_img(gradient(img,kernel))
    s.show()