import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
from conv import *
from kernel import *

if __name__ == "__main__":
    #钝化掩蔽和高提升滤波
    kernel = gauss_kernel(31,1,5) #K=1,sigma=5 的滤波器
    s = visualization(2,3)
    imgs = get_examples_image(3)
    s.append_img(imgs) #显示原图
    blur = convolve3d(imgs, kernel)
    s.append_img(blur) #显示低通滤波后的图像
    s.append_img(imgs - blur)
    temple = imgs - blur
    s.append_img(imgs + temple) #显示高提升滤波后的图像

    kernel = gauss_kernel(31,2,5) #K=2,sigma=5 的滤波器
    blur = convolve3d(imgs, kernel)
    temple = imgs - blur
    s.append_img(imgs + temple)
    kernel = gauss_kernel(31,3,5) #K=3,sigma=5 的滤波器
    blur = convolve3d(imgs, kernel)
    temple = imgs - blur
    s.append_img(imgs + temple)
    s.show()