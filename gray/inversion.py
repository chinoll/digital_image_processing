import numpy as np
import sys
sys.path.append("..")
sys.path.append(".")
from utils import *

def image_inversion(img,L):
    """
    反转图像的灰度值，计算公式为 s = L - img
    """
    m = (L - 1) - img.astype(np.float)
    m = normalize_image(m)
    return m

if __name__ == "__main__":
    s = visualization(1,2)
    img = get_examples_image(3)
    img1 = image_inversion(img,256)
    s.append_img(img)
    s.append_img(img1)
    s.show()