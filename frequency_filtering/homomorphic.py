import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
from filter import fft,ifft,fft_log,homomorphic
import numpy as np
if __name__ == '__main__':
    s = visualization(2,2)
    img = get_examples_image()
    s.append_img(img)
    img = np.log(img)
    dft_shift = fft(img)
    rows,cols = img.shape[:2]
    mask = homomorphic(rows,cols,gamaH=3,gamaL=0.5,c=2)
    f = dft_shift*mask
    s.append_img(np.exp(ifft(f)))

    #彩色图像
    img = get_examples_image(3)
    s.append_img(img)
    img = np.log(img+1e-20)
    dft_shift = fft(img)
    rows,cols = img.shape[:2]
    mask = homomorphic(rows,cols,gamaH=3,gamaL=0.5,c=2,channel=3)
    f = dft_shift*mask
    s.append_img(np.exp(ifft(f)))
    s.show()
