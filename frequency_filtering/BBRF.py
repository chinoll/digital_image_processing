import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
from filter import BBRF,fft,ifft,fft_log
if __name__ == '__main__':
    s = visualization(2,4)
    img = get_examples_image()
    s.append_img(img)
    dft_shift = fft(img)
    rows,cols = img.shape[:2]
    mask = BBRF(rows,cols,128,60)
    f = dft_shift*mask
    s.append_img(ifft(f))
    s.append_img(fft_log(f))
    s.append_img(mask,True)

    # #彩色图像
    img = get_examples_image(3)
    s.append_img(img)
    dft_shift = fft(img)
    rows,cols = img.shape[:2]
    mask = BBRF(rows,cols,128,60,1,3)
    f = dft_shift*mask
    s.append_img(ifft(f))
    s.append_img(fft_log(f))
    s.append_img(mask,True)
    s.show()
