import numpy as np
from PIL import Image
#图片规范化，讲小于0的值设为0，大于255的值设为255
def normalize_image(image):
    return np.minimum(np.maximum(image, 0),255).astype(np.uint8)

def get_examples_image(channel=1):
    try:
        img = Image.open("sample.jpg")
    except:
        img = Image.open("../sample.jpg")
    
    if channel == 1:
        img = img.convert('L')
    return np.array(img).astype(np.float32)