# import numpy as np
import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
from filter import  TBLPF,fft,ifft,fft_log
from noise import add_sin_noise

if __name__ == "__main__":
    s = visualization(3,4)
    img = get_examples_image()
    noise = add_sin_noise(img,0.8,-34.5)
    img = normalization(img/255+noise)*255
    s.append_img(img)
    dft_shift = fft(img)
    rows,cols = img.shape[:2]
    s.append_img(fft_log(dft_shift))

    mask = TBLPF(rows,cols,8,10,[(100,100)])
    f = dft_shift*mask
    s.append_img(ifft(f))
    s.append_img(fft_log(f))

    mask = TBLPF(rows,cols,16,10,[(100,100)])
    f = dft_shift*mask
    s.append_img(ifft(f))
    s.append_img(fft_log(f))

    #彩色图像
    img = get_examples_image(3)
    img = normalization(img/255+np.stack([noise]*3,axis=2))*255

    s.append_img(img)

    dft_shift = fft(img)
    rows,cols = img.shape[:2]
    s.append_img(fft_log(dft_shift))

    mask = TBLPF(rows,cols,8,5,[(100,100)],3)
    f = dft_shift*mask
    s.append_img(ifft(f))
    s.append_img(fft_log(f))

    mask = TBLPF(rows,cols,16,3,[(100,100)],3)
    f = dft_shift*mask
    s.append_img(ifft(f))
    s.append_img(fft_log(f))
    s.show()