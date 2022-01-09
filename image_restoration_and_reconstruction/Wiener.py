import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
from filter import  TBLPF,fft,ifft,fft_log
from noise import add_sin_noise
import numpy as np

def wiener_filtering(img, h, K):
    '''
    维纳滤波
    :param img: 输入图像
    :param h: 退化函数
    :param K: 参数K(估计的功率谱)
    :return: 维纳滤波后的信号
    '''
    input_signal = np.copy(img)
    G = fft(input_signal,False)
    h_fft = fft(h)
    h_square = h_fft*np.conj(h_fft) #h^2
    # 维纳滤波 
    output_signal_fft = h_square / (h_square*h_fft + K) #(h^2)/(h^2*h+K)
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

    filter_img = wiener_filtering(img2,h,0.01)
    s.append_img(filter_img)
    s.show()
