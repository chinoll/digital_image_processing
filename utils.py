import numpy as np
from PIL import Image
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
    img = open_image("sample.png")
    print(img)
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