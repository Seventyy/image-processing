import numpy as np
from PIL import Image

def init_img(pixels, image):
    if pixels.ndim == 1:
        numColorChannels = 1
        pixels = pixels.reshape(image.size[1], image.size[0])
    else:
        numColorChannels = pixels.shape[1]
        pixels = pixels.reshape(image.size[1], image.size[0], numColorChannels)

def finish_img(pixels, image):
    Image.fromarray(pixels.astype(np.uint8)).save("output.bmp")