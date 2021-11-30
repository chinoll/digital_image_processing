import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
from filter import IBRF,fft,ifft,fft_log
import numpy as np
if __name__ == '__main__':
    s = visualization(2,3)
    img = get_examples_image()
    s.append_img(img)
    dft_shift = fft(img)
    rows,cols = img.shape[:2]
    mask = IBRF(rows,cols,256,60)
    f = dft_shift*mask
    s.append_img(ifft(f))
    s.append_img(fft_log(f))

    # #彩色图像
    img = get_examples_image(3)
    s.append_img(img)
    dft_shift = fft(img)
    rows,cols = img.shape[:2]
    mask = IBRF(rows,cols,256,60,3)
    f = dft_shift*mask
    s.append_img(ifft(f))
    s.append_img(fft_log(f))
    s.show()
