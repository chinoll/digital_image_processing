import numpy as np
from PIL import Image
import sys
sys.path.append("..")
from utils import normalize_image

def image_inversion(img,L):
    """
    反转图像的灰度值，计算公式为 s = L - img
    """
    m = L - img.astype(np.float)
    m = normalize_image(m)
    return Image.fromarray(m)

img = np.array(Image.open('../temp.jpg'))
img = image_inversion(img,200)
img.show()