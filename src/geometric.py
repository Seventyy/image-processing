import numpy as np

def hflip(img):
    img_copy = img.copy()
    for y in range(img.shape[1]):
        for x in range(img.shape[0]):
            img[x, y] = img_copy[img.shape[0] - x - 1, y]

def vflip(img):
    img_copy = img.copy()
    for y in range(img.shape[1]):
        for x in range(img.shape[0]):
            img[x, y] = img_copy[x, img.shape[0] - y - 1]

def dflip(img):
    img_copy = img.copy()
    for y in range(img.shape[1]):
        for x in range(img.shape[0]):
            img[x, y] = img_copy[img.shape[0] - x - 1, img.shape[0] - y - 1]

def __resize__(img, mul):
    nsize = (int(img.shape[0] * mul), int(img.shape[1] * mul))
    nimg = np.empty(nsize)

    for x in range(nsize[0]):
        for y in range(nsize[1]):
            nimg[x, y] = img[int(x / mul), int(y / mul)]

    return nimg

def shrink(img):
    return __resize__(img, 0.5)

def enlarge(img):
    return __resize__(img, 2)
