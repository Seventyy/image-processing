import numpy as np
import math

def hraleigh(img, hist, g_min: float = 0, alpha: float = 120):
    N = img.shape[0] * img.shape[1]
    E = math.exp(1)

    lookup = np.zeros([256])

    for intensity in range(256):
        val: float = 0

        for hist_int in range(intensity+1):
            val += hist[hist_int]
        val = val / N

        if val == 0.0:
            lookup[intensity] = 255
            continue

        val = 2 * alpha**2 * math.log(1/val, E)
        val = -g_min + math.sqrt(val)
        lookup[intensity] = 255 - int(max(min(val, 255.0), 0.0))

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            img[x,y] = lookup[img[x,y]]

    return img