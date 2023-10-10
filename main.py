import sys
from PIL import Image
import numpy as np

# modules
sys.path.insert(0, f'./src')
from elementary import *

image = Image.open("imgs/mandril.bmp")

pixels = np.array(image.getdata())

def initalise_image():
    global pixels, image
    if pixels.ndim == 1:
        numColorChannels = 1
        pixels = pixels.reshape(image.size[1], image.size[0])
    else:
        numColorChannels = pixels.shape[1]
        pixels = pixels.reshape(image.size[1], image.size[0], numColorChannels)

def finalise_image():
    global pixels, image
    Image.fromarray(pixels.astype(np.uint8)).save("output.bmp")

def handle_command():
    global pixels, image
    command_name = sys.argv[1]
    
    match command_name:
        case "--help":
            print("here be help!")
            exit
        case "--brightness":
            brightness(pixels, int(sys.argv[2]))
        case "--negative":
            negative(pixels)
        case "--contrast":
            contrast(pixels, float(sys.argv[2]))

initalise_image()
handle_command()
finalise_image()








# from PIL import Image
# import numpy as np

# image = Image.open("imgs/mandril.bmp")

# pixels = np.array(image.getdata())

# def initalise_images():
#     if pixels.ndim == 1: #grayscale
#         numColorChannels = 1
#         pixels = pixels.reshape(image.size[1], image.size[0])
#     else:
#         numColorChannels = pixels.shape[1]
#         pixels = pixels.reshape(image.size[1], image.size[0], numColorChannels)

# pixels = pixels / 2 # Example processing (decrease brightness)

# newIm = Image.fromarray(pixels.astype(np.uint8))

# newIm.save("output.bmp")
