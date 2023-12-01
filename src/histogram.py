import numpy as np

def write_histogram(img):
    # Histogram dimensions
    H_HEIGHT = 100
    H_WIDTH = 256

    hist_data = np.linspace(0, 0, H_WIDTH)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            intensity = img[x,y]
            hist_data[intensity] += 1
    
    max_value: int = 0
    for n in range(H_WIDTH):
        max_value = max(hist_data[n], max_value)

    hist_img = np.ones([H_HEIGHT, H_WIDTH]) * (H_WIDTH-1)
    for x in range(H_WIDTH):
        y_max = H_HEIGHT - int(hist_data[x] / max_value * H_HEIGHT)
        for y in range(y_max, H_HEIGHT):
            hist_img[y, x] = 0

    return hist_img

def read_histogram(hist):
    HEIGHT = hist.shape[0]
    WIDTH = hist.shape[1]
    
    hist_data = np.linspace(0, 0, 256)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if hist[y, x] == 0:
                hist_data[x] = HEIGHT - y
                break
    
    return hist_data