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

def normalization(data):
    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range

def transform_img(img):
    img = normalization(img)
    return img*255

class visualization:
    def __init__(self,x=None,y=None):
        plt.figure()
        self.x = x
        self.y = y
        self.showlist = []
    def append_img(self,img,transform=True):
        img = img.copy()
        if not transform:
            img[img < 0] = 0
            img[img > 255] = 255
        else:
            img = transform_img(img).astype(np.uint8)
        self.showlist.append((img,"img"))
    def append_hist(self,hist):
        self.showlist.append((hist.copy(),"hist"))
    def show(self):
        if self.x == None and self.y == None:
            self.x,self.y = getMN(len(self.showlist)) #自动计算x,y
        elif self.x != None and self.y == None:
            _,self.y = getMN(len(self.showlist),self.x)
        elif self.y != None and self.x == None:
            _,self.x = getMN(len(self.showlist),self.y)

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

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    if num % 6 != 1 and num % 6 != 5:
        return False
    for i in range(5,int(num**0.5)+1,6):
        if num % i == 0 or num % (i+2) == 0:
            return False
    return True

def getMN(num,n=None):
    #将num分解为MxN
    if num == 2:
        return 2,1
    if n == None:
        n = 1

    if is_prime(num):
        while True:
            if is_prime(num) and num % n == 0:
                num += 1
            else:
                break
    if n != 1:
        return n,num//n

    l = []
    while num != 1:
       for i in range(2,num+1):
           if num % i == 0:
                num //= i
                l.append(i)
                break
    if len(l) % 2 != 0:
        l.append(1)
    return int(np.prod(l[:len(l)//2])),int(np.prod(l[len(l)//2:]))