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

    plt.subplot(3,2,1)
    plt.imshow(source.astype(np.uint8))
    plt.subplot(3,2,2)
    plt.hist(source.reshape(-1),bins=256,range=(0,256))

    target = histogram_equalization(target)

    plt.subplot(3,2,3)
    plt.imshow(target.astype(np.uint8))
    plt.subplot(3,2,4)
    plt.hist(target.reshape(-1),bins=256,range=(0,256))

    tar_pdf = PDF(target,channel)
    src_pdf = PDF(source)
    for i in range(256):
        source[source==src_pdf[i]] = find_nearest(tar_pdf,src_pdf[i])

    plt.subplot(3,2,5)
    plt.imshow(source.astype(np.uint8))
    plt.subplot(3,2,6)
    plt.hist(source.reshape(-1),bins=256,range=(0,256))
    return source
if __name__ == '__main__':
    source = get_examples_image(3)
    target = get_examples_image2(3)
    plt.figure()
    img = Image.fromarray(histogram_specification(source,target))
    plt.show()