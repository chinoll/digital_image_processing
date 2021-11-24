import numpy as np
import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
from filter import LIPF,fft,ifft,fft_log

if __name__ == "__main__":
    s = visualization(4,4)
    img = get_examples_image()
    s.append_img(img)
    dft_shift = fft(img)
    rows,cols = img.shape[:2]
    s.append_img(fft_log(dft_shift))

    mask = LIPF(rows,cols,16)
    f = dft_shift*mask
    s.append_img(ifft(f))
    s.append_img(fft_log(f))

    mask = LIPF(rows,cols,32)
    f = dft_shift*mask
    s.append_img(ifft(f))
    s.append_img(fft_log(f))

    mask = LIPF(rows,cols,256)
    f = dft_shift*mask
    s.append_img(ifft(f))
    s.append_img(fft_log(f))

    #彩色图像
    img = get_examples_image(3)
    s.append_img(img)
    dft_shift = fft(img)
    rows,cols = img.shape[:2]
    s.append_img(fft_log(dft_shift))

    mask = LIPF(rows,cols,16,3)
    f = dft_shift*mask
    s.append_img(ifft(f))
    s.append_img(fft_log(f))

    mask = LIPF(rows,cols,32,3)
    f = dft_shift*mask
    s.append_img(ifft(f))
    s.append_img(fft_log(f))

    mask = LIPF(rows,cols,256,3)
    f = dft_shift*mask
    s.append_img(ifft(f))
    s.append_img(fft_log(f))

    s.show()