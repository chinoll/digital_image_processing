import numpy as np
import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
import matplotlib.pyplot as plt

def PDF(image,channel=1):
    """
    Compute the probability density function of an image.
    """
    # numpy实现
    h,w = image.shape[:2]
    hist = np.histogram(image, bins=256, range=(0, 256))
    pdf = hist[0] / (h*w*channel)
    h2 = np.cumsum(pdf)
    return np.round(h2*255).astype(np.uint8)
    '''
    histogram = np.zeros(256).astype(np.float)
    h2 = np.zeros(256).astype(np.float)
    for i in range(256):
        histogram[i] = (image[image==i].size)
    histogram = histogram / (h*w*channel)
    for i in range(1,256):
        h2[i] = histogram[:i].sum()
    return np.round(h2*255).astype(np.uint8)
    '''
def histogram_equalization(image):
    pdf = PDF(image,3)
    for i in range(256):
        image[image == i] = pdf[i]
    return image.astype(np.uint8)

if __name__ == '__main__':
    img = get_examples_image(3)

    plt.figure()
    plt.subplot(1,3,1)
    plt.imshow(img.astype(np.uint8))

    img = histogram_equalization(img)
    img = Image.fromarray(img)

    plt.subplot(1,3,2)
    plt.imshow(img)
    plt.subplot(1,3,3)
    plt.hist(np.array(img).reshape(-1),bins=256,range=(0,256))
    plt.show()