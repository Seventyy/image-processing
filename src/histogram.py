import numpy as np

def histogram_data(img):
    hist_data = np.linspace(0, 0, 256)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            intensity = img[x,y]
            hist_data[intensity] += 1
    return hist_data

def hist_to_img(hist_data):
    H_WIDTH = 256
    H_HEIGHT = 100

    max_value: int = 0
    for n in range(H_WIDTH):
        max_value = max(hist_data[n], max_value)

    hist_img = np.zeros([H_HEIGHT, H_WIDTH])
    for x in range(H_WIDTH):
        y_max = H_HEIGHT - int(hist_data[x] / max_value * H_HEIGHT)
        for y in range(y_max, H_HEIGHT):
            hist_img[y, x] = 255

    return hist_img