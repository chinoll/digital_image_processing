import numpy as np
import sys
sys.path.append("..")
sys.path.append(".")
from utils import *

def pow_image(img,gama=1,c=1):
    """
    幂律变换，计算公式为 s = c*img**gama
    """
    s = c*img*gama
    s[s > 255] = 255
    s[s < 0] = 0
    return s

if __name__ == '__main__':
    s = visualization(1,5)
    img = get_examples_image(3)
    img1 = pow_image(img,gama=0.2)
    img2 = pow_image(img,0.4)
    img3 = pow_image(img,1.5)
    img4 = pow_image(img,2.5)
    s.append_img(img)
    s.append_img(img1)
    s.append_img(img2)
    s.append_img(img3)
    s.append_img(img4)
    s.show()