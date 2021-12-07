import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
from kernel import *
from conv import *
from noise import *
if __name__ == '__main__':
    kernel = contra_harmonic_mean((3,3),2)
    s = visualization(2,3)
    image = get_examples_image()
    s.append_img(image)
    x = add_pepper_noise(image)
    s.append_img(x)
    c = conv2d(x,kernel)
    s.append_img(c,True)

    #彩色图像
    image = get_examples_image(3)
    s.append_img(image)
    x = add_pepper_noise(image)
    s.append_img(x)
    c = conv2d(x,kernel)
    s.append_img(c,True)
    s.show()