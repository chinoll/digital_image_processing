import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
from kernel import *
from conv import *
from noise import *
if __name__ == '__main__':
    s = visualization(1,4)
    image = get_examples_image()
    s.append_img(image)
    x = add_gaussian_noise(image, 10,1)
    kernel = adaptive_local((3,3),x)
    s.append_img(x)
    c = conv2d(x,kernel)
    s.append_img(c,True)
    kernel = adaptive_local((3,3),x,1000)
    c = conv2d(c,kernel)
    s.append_img(c,True)
    s.show()