import numpy as np
import matplotlib.pyplot as plt
from numpy.core.numeric import NaN
import seaborn as sns
import sys
sys.path.append("..")
sys.path.append(".")
from utils import *


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

def add_gaussian_noise(img, scale=10,p=0.5):
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
    p = 1 - p
    mask = np.random.choice((0, 1, 2), size=img_.shape, p=[p, (1 - p)/2, (1 - p)/2])
    if img_.ndim == 3:
        mask = np.stack([mask[:,:,0]] * 3, axis=2)
    img_ = np.where(mask == 0, 255, img_) # 盐噪声
    img_ = np.where(mask == 1, 0, img_) # 胡椒噪声
    return transform_img(img_)

