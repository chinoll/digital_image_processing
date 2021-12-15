import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
from kernel import *
from conv import *
from noise import *
if __name__ == '__main__':
    s = visualization(1,3)
    image = get_examples_image()
    s.append_img(image)
    x = add_saltpepper_noise(image, 0.25)
    kernel = ada_median()
    s.append_img(x)
    c = conv2d(x,kernel)
    s.append_img(c,True)
    s.show()