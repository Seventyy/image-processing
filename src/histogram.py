import numpy as np

def histogram(img):
    HEIGHT = 100

    hist_data = np.linspace(0, 0, 256)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            intensity = img[x,y]
            hist_data[intensity] += 1
    
    max_value: int = 0
    for n in range(256):
        max_value = max(hist_data[n], max_value)

    hist_img = np.ones([HEIGHT, 256]) * 255
    for x in range(256):
        y_max = HEIGHT - 1 - int(hist_data[x] / max_value * HEIGHT)
        for y in range(y_max, HEIGHT):
            hist_img[y, x] = 0

    return hist_img