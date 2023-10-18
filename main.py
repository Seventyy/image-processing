import sys
from PIL import Image
import numpy as np
import argparse

sys.path.insert(0, f'./src')
from elementary import *
from cli import *
from img_io import *

def handle_command():
    if args.brightness:
        brightness(pixels, int(args.value))

    if args.negative:
        negative(pixels)

    if args.contrast:
        contrast(pixels, float(args.value))

def main():
    global image, pixels, args

    args = parse_cli()
    image = Image.open(args.input)
    pixels = np.array(image)

    init_img(pixels, image)
    handle_command()
    init_img(pixels, image)

if __name__ == "__main__":
    main()