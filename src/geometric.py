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

def shrink(img):
    img = np.delete(img, range(0, img.shape[0], 2), axis=0)
    img = np.delete(img, range(0, img.shape[1], 2), axis=1)

def enlarge(img):
    print(img)
    for x in range(img.shape[0]):
        img = np.insert(img, x, range(0,512), axis=1)
    print(img)
