import sys
from PIL import Image
import numpy as np
import argparse

sys.path.insert(0, f'./src')
from cli import *
from img_io import *
from elementary import *
from geometric import *
from noise_removal import *
from analysis import *

def handle_command(channel):
    if args.brightness:
        return brightness(channel, int(args.value))

    if args.negative:
        return negative(channel)

    if args.contrast:
        return contrast(channel, float(args.value))
    
    if args.hflip:
        return hflip(channel)

    if args.vflip:
        return vflip(channel)

    if args.dflip:
        return dflip(channel)

    if args.shrink:
        return shrink(channel)

    if args.enlarge:
        return enlarge(channel)
    
    if args.amean:
        return amean(channel, int(args.value))
    
    if args.adaptive:
        return adaptive(channel, int(args.value))
    
    if args.mse:
        return mse(channel)
    
    if args.pmse:
        return pmse(channel)
    
    if args.snr:
        return snr(channel)
    
    if args.psnr:
        return psnr(channel)
    
    if args.md:
        return md(channel)

def main():
    global image, pixels, args

    args = parse_cli()
    image = Image.open(args.input)
    pixels = np.array(image)
    
    # init_img(pixels, image)

    if len(pixels.shape) == 3:
        pixels = np.dstack((
            handle_command(pixels[:,:,0]),
            handle_command(pixels[:,:,1]),
            handle_command(pixels[:,:,2])))
    else:
        pixels = handle_command(pixels)

    finish_img(pixels, image)

if __name__ == "__main__":
    main()