import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
#图片规范化，将小于0的值设为0，大于255的值设为255
def normalize_image(image):
    return np.minimum(np.maximum(image, 0),255).astype(np.uint8)

def open_image(name):
    try:
        img = Image.open(name)
    except:
        img = Image.open("../" + name)
    return img
def get_examples_image(channel=1):
    img = open_image("sample.jpg")
    if channel == 1:
        img = img.convert('L')
    else:
        img = img.convert("RGB")

    return np.array(img).astype(np.float32)

def get_examples_image2(channel=1):
    img = open_image("sample2.jpg")
    
    if channel == 1:
        img = img.convert('L')
    else:
        img = img.convert("RGB")

    return np.array(img).astype(np.float32)
def transform_img(img):
    k = 255/(np.max(img)-np.min(img))
    img = k*(img-np.min(img))
    return img

class visualization:
    def __init__(self,x,y):
        plt.figure()
        self.x = x
        self.y = y
        self.showlist = []
    def append_img(self,img,transform=False):
        img = img.copy()
        if not transform:
            img[img < 0] = 0
            img[img > 255] = 255
        else:
            img = transform_img(img)
        self.showlist.append((img.astype(np.uint8),"img"))
    def append_hist(self,hist):
        self.showlist.append((hist.copy(),"hist"))
    def show(self):
        for i in range(self.x):
            for j in range(self.y):
                plt.subplot(self.x,self.y,i*self.y+j+1)
                if len(self.showlist) > 0:
                    img,type = self.showlist.pop(0)
                    if type == "img":
                        plt.imshow(img,cmap="gray")
                    elif type == "hist":
                        plt.hist(img.reshape(-1),bins=256,range=(0,256))
                else:
                    plt.axis("off")
        plt.show()