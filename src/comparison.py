import numpy as np
import math

def mse(org_img, img):
    val = 0
    
    for y in range(org_img.shape[1]):
        for x in range(org_img.shape[0]):
            val += pow(int(org_img[x, y]) - int(img[x, y]), 2)
    val = val / (org_img.shape[0] * org_img.shape[1])
    
    return val

def pmse(org_img, img):
    val = 0
    img_max = 0
    
    for y in range(org_img.shape[1]):
        for x in range(org_img.shape[0]):
            val += pow(int(org_img[x, y]) - int(img[x, y]), 2)
            img_max = max(img_max, int(org_img[x,y]))
    val = val / (org_img.shape[0] * org_img.shape[1]) / pow(img_max, 2)
    
    return val

def snr(org_img, img):
    val = 0
    val_1 = 0
    val_2 = 0
    
    for y in range(org_img.shape[1]):
        for x in range(org_img.shape[0]):
            val_1 += pow(int(org_img[x, y]), 2)
            val_2 += pow(int(org_img[x, y]) - int(img[x, y]), 2)
    if val_2 == 0:
        return 0.0
    val = 10 * math.log(val_1 / val_2, 10)

    return val

def psnr(org_img, img):
    val = 0
    val_1 = 0
    val_2 = 0
    img_max = 0
    
    for y in range(org_img.shape[1]):
        for x in range(org_img.shape[0]):
            img_max = max(img_max, int(org_img[x,y]))
    
    for y in range(org_img.shape[1]):
        for x in range(org_img.shape[0]):
            val_1 += pow(img_max, 2)
            val_2 += pow(int(org_img[x, y]) - int(img[x, y]), 2)
    if val_2 == 0:
        return 0.0
    val = 10 * math.log(val_1 / val_2, 10)

    return val
    
def md(org_img, img):
    val = 0
    
    for y in range(org_img.shape[1]):
        for x in range(org_img.shape[0]):
            val = max(val, abs(int(org_img[x,y]) - int(img[x,y])))

    return val