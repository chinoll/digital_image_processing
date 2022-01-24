import sys

sys.path.append("..")
sys.path.append(".")
from utils import *
import numpy as np

def rgb_to_hsi(img):
    R = img[:,:,0]
    G = img[:,:,1]
    B = img[:,:,2]
    def H():
        num = 0.5 * ((R - G) + (R - B))
        den = np.sqrt((R - G)**2 + (R - B) * (G - B)) + 1e-6
        theta = np.arccos(num/den)
        theta = np.where(den == 0, 0, theta)
        return np.where(B>G,2*np.pi-theta,theta)/(2*np.pi)
    def S():
        min_RGB = np.minimum(np.minimum(R, G), B)
        sum = R + G + B + 1e-6

        return 1 - 3 * min_RGB / sum
    def I():
        return (R+G+B)/3
    return np.stack([H(),S(),I()],axis=2)

def hsi_to_rgb(img):
    H = img[:,:,0]*360
    S = img[:,:,1]
    I = img[:,:,2]
    def RG():
        # BG扇区，角度在[0,120]
        R = np.where(H<=120,I*(1 + (S * np.cos(H*np.pi/180)) / np.cos((60 - H)*np.pi/180)),0)
        B = np.where(H<=120,I*(1 - S),0)
        G = np.where(H<=120,3*I - (R + B),0)
        return np.stack([R,G,B],axis=2)
    def GB():
        # BR扇区，角度在[120,240]
        h = H - 120
        bool_matrix = np.where(H > 120, True, False) & np.where(H <= 240, True, False)
        R = np.where(bool_matrix,I*(1-S),0)
        G = np.where(bool_matrix,I * (1 + (S * np.cos(h*np.pi/180)) / np.cos((60 - h)*np.pi/180)),0)
        B = np.where(bool_matrix,3 * I - (R + G),0)
        return np.stack([R,G,B],axis=2)
    def BR():
        # RB扇区，角度在[240,360]
        h = H - 240
        G = np.where(H > 240,I * (1 - S),0)
        B = np.where(H > 240,I * (1 + (S * np.cos(h*np.pi/180)) / np.cos((60 - h)*np.pi/180)),0)
        R = np.where(H > 240,3 * I - (G + B),0)
        return np.stack([R,G,B],axis=2)

    return RG()+GB()+BR()
if __name__ == "__main__":
    img = get_examples_image(3)/255
    s = visualization()
    s.append_img(img)
    hsi = rgb_to_hsi(img)
    s.append_img(hsi[:,:,0])
    s.append_img(hsi[:,:,1])
    s.append_img(hsi[:,:,2])
    s.append_img(hsi_to_rgb(hsi))

    s.show()