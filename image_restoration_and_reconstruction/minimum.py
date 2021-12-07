import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
from kernel import *
from conv import *
from noise import *
if __name__ == '__main__':
    kernel = minimum((3,3))
    s = visualization(1,3)
    image = get_examples_image()
    s.append_img(image)
    x = add_salt_noise(image, 0.1)
    s.append_img(x)
    c = conv2d(x,kernel)
    s.append_img(c,True)

    #彩色图像
    # image = get_examples_image(3)
    # s.append_img(image)
    # x = add_salt_noise(image, 0.1)
    # s.append_img(x)
    # c = conv2d(x,kernel)
    # s.append_img(c,True)
    # s.show()