import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
import numpy as np
def layer(img,R,w):
    '''
    彩色分层
    :param img: 输入图像
    :param R: 一个封闭球体的半径
    :param w: RGB彩色坐标
    :return: 分层后的图像
    '''
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if np.sum((img[i,j] - w)**2) > R**2:
                img[i,j] = 0.5
    return img
if __name__ == "__main__":
    img = get_examples_image(3)/255
    s = visualization(1,2)
    s.append_img(img)
    img = layer(img,0.2,np.array((0.6863,0.1608,0.1922))) #通过交互式确定的参数
    s.append_img(img)
    s.show()
