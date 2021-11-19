import numpy as np
from PIL import Image
import sys
import matplotlib.pyplot as plt

sys.path.append("..")
sys.path.append(".")
from utils import *
from histogram_equalization import *
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

def histogram_specification(source,target,channel=3):
    source = histogram_equalization(source)

    s.append_img(source)
    s.append_hist(source)

    target = histogram_equalization(target)

    s.append_img(target)
    s.append_hist(target)

    tar_pdf = PDF(target,channel)
    src_pdf = PDF(source)
    for i in range(256):
        source[source==src_pdf[i]] = find_nearest(tar_pdf,src_pdf[i])

    s.append_img(source)
    s.append_hist(source)
    return source
if __name__ == '__main__':
    source = get_examples_image(3)
    target = get_examples_image2(3)
    s = visualization(3,2)
    img = histogram_specification(source,target)
    s.show()