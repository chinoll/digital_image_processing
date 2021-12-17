import numpy as np
import matplotlib.pyplot as plt
from numpy.core.numeric import NaN
import seaborn as sns
import sys
sys.path.append("..")
sys.path.append(".")
from utils import *
import cv2

# def rayleigh(a,b,size):
#     z = np.linspace(0, 10, 200)
#     n = a + b*np.sqrt(-2*np.log(z))
#     return n

# def gamma(shape=1,scale=1,size=None):
#     if shape == 0:
#         return np.zeros(size)
#     U = np.random.uniform(size=size)
#     X1,X2,X=None,None,None
#     X1 = pow(np.where(U <= 1 - shape,U,0),1/shape)
#     Y = -np.log((1 - np.where(U > 1 - shape,U,0))/shape)
#     X2 = pow(1-shape+shape*Y,1/shape)
#     return (X1+X2)*scale

def add_gaussian_noise(img, scale=10,p=1):
    '''
    高斯噪声
    '''
    img_ = img.copy()
    noise = np.random.normal(0, scale, size=img_.shape)
    mask = np.random.choice((0, 1), size=img_.shape, p=[p, 1 - p])
    img_ = np.where(mask == 0, img_ + noise, img_)
    return transform_img(img_)

def add_pepper_noise(img, p=0.5):
    '''
    胡椒噪声
    '''
    img_ = img.copy()
    mask = np.random.choice((0, 1), size=img_.shape, p=[p, 1 - p])
    if img_.ndim == 3:
        mask = np.stack([mask[:,:,0]] * 3, axis=2)
    img_ = np.where(mask == 0, 0, img_)
    return transform_img(img_)

def add_salt_noise(img, p=0.5):
    '''
    盐噪声
    '''
    img_ = img.copy()
    mask = np.random.choice((0, 1), size=img_.shape, p=[p, 1 - p])
    if img_.ndim == 3:
        mask = np.stack([mask[:,:,0]] * 3, axis=2)
    img_ = np.where(mask == 0, 255, img_)
    return transform_img(img_)

def add_saltpepper_noise(img, p=0.5):
    '''
    椒盐噪声
    '''
    img_ = img.copy()
    # p = 1 - p
    mask = np.random.choice((0, 1, 2), size=img_.shape, p=[p, p, 1 - 2 * p])
    if img_.ndim == 3:
        mask = np.stack([mask[:,:,0]] * 3, axis=2)
    img_ = np.where(mask == 0, 255, img_) # 盐噪声
    img_ = np.where(mask == 1, 0, img_) # 胡椒噪声
    return transform_img(img_)

def add_sin_noise(img, scale=1, angle=0):
    """
    add sin noise for image
    param: img: input image, 1 channel, dtype=uint8
    param: scale: sin scaler, smaller than 1, will enlarge, bigger than 1 will shrink
    param: angle: angle of the rotation
    return: output_img: output image is [0, 1] image which you could use as mask or any you want to
    """
    #ref url: https://blog.csdn.net/jasneik/article/details/115444216
    height, width = img.shape[:2]  # original image shape
    
    # convert all the angle
    if int(angle / 90) % 2 == 0:
        rotate_angle = angle % 90
    else:
        rotate_angle = 90 - (angle % 90)
    
    rotate_radian = np.radians(rotate_angle)    # convert angle to radian
    
    # get new image height and width
    new_height = int(np.ceil(height * np.cos(rotate_radian) + width * np.sin(rotate_radian)))
    new_width = int(np.ceil(width * np.cos(rotate_radian) + height * np.sin(rotate_radian))) 
    
    # if new height or new width less than orginal height or width, the output image will be not the same shape as input, here set it right
    if new_height < height:
        new_height = height
    if new_width < width:
        new_width = width
    
    # meshgrid
    u = np.arange(new_width)
    v = np.arange(new_height)
    u, v = np.meshgrid(u, v)
    
    # get sin noise image, you could use scale to make some difference, better you could add some shift
#     noise = abs(np.sin(u * scale))
    noise = 1 - np.sin(u * scale)
    
    # here use opencv to get rotation, better write yourself rotation function
    C1 = cv2.getRotationMatrix2D((new_width/2.0, new_height/2.0), angle, 1)
    new_img = cv2.warpAffine(noise, C1, (int(new_width), int(new_height)), borderValue=0)
    
    # ouput image should be the same shape as input, so caculate the offset the output image and the new image
    # I make new image bigger so that it will cover all output image
    
    offset_height = abs(new_height - height) // 2
    offset_width = abs(new_width - width) // 2
    img_dst = new_img[offset_height:offset_height + height, offset_width:offset_width+width]
    output_img = normalization(img_dst)
    
    return output_img