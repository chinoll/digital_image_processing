import numpy as np
import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
from filter import laplace,fft,ifft,fft_log

if __name__ == "__main__":
    s = visualization(2,2)
    img = get_examples_image()
    s.append_img(img)
    rows,cols = img.shape[:2]
    fm = img - np.min(img)
    fs = fm/np.max(fm)
    img_k = np.zeros((2*rows,2*cols))
    img_k[:rows,:cols] = fs
    dft_shift = fft(img_k)

    mask = np.zeros_like(img_k)
    mask[:rows,:cols] = laplace(rows,cols)
    f = dft_shift*mask
    z = transform_img(ifft(f)[:rows,:cols])
    s.append_img(z+img)

    #彩色图像
    img = get_examples_image(3)
    s.append_img(img)

    fm = img - np.min(img)
    fs = fm/np.max(fm)
    img_k = np.zeros((2*rows,2*cols,3))
    img_k[:rows,:cols] = fs
    dft_shift = fft(img_k)

    mask = np.zeros_like(img_k)
    mask[:rows,:cols] = laplace(rows,cols,3)
    f = dft_shift*mask
    z = transform_img(ifft(f)[:rows,:cols])
    s.append_img(z+img)

    s.show()