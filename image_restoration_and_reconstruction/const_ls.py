import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
from filter import  TBLPF,fft,ifft,fft_log
from noise import add_sin_noise
import numpy as np
def wiener_filtering(img, h,gamma):
    '''
    约束最小二乘方滤波
    :param img: 输入图像
    :param h: 退化函数
    :param gamma: 估计的一个参数
    :return: 维纳滤波后的信号
    '''
    if img.shape[0] % 2 != 0:
        #删除一行
        img = np.delete(img,img.shape[0]-1,0)
    if img.shape[1] % 2 != 0:
        #删除一列
        img = np.delete(img,img.shape[1]-1,1)

    input_signal = np.copy(img)
    G = fft(input_signal,False)
    h_fft = fft(h)
    h_square = np.conj(h_fft)*h_fft #h^2

    p = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
    p = np.pad(p,((0,img.shape[0]-p.shape[0]),(0,img.shape[1]-p.shape[1])),'constant')
    p_fft = fft(p)**2
    output_signal_fft = np.conj(h_fft) / (h_square + gamma*p_fft)
    return ifft(output_signal_fft * G,False)

if __name__ == "__main__":
    s = visualization(1,3)
    img = get_examples_image()


    noise = add_sin_noise(img,0.8,-34.5)
    img2 = normalization(img/255+noise)*255
    s.append_img(img)
    s.append_img(img2)

    image_fft =  fft(img)
    image_add_noise_fft =  fft(img2)
    h = np.fft.ifft2(image_add_noise_fft / image_fft)

    filter_img = wiener_filtering(img2,h,1e-5)
    s.append_img(filter_img)
    s.show()