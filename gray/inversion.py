import numpy as np
from PIL import Image
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
    return Image.fromarray(m)

img = get_examples_image(3)
img = image_inversion(img,256)
img.show()