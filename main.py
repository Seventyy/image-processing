import sys
from PIL import Image
import numpy as np
import argparse
from decimal import Decimal

import tracemalloc
import time

sys.path.insert(0, f'./src')
from cli import *
from elementary import *
from geometric import *
from noise_removal import *
from analysis import *

def handle_operation(channel):
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
        return amean(channel, int(args.kernel))
    
    if args.adaptive:
        return adaptive(channel, int(args.kernel))
    
    return False

def handle_analysis(org_img, new_img):
    if args.report:
        args.mse = True
        args.pmse = True
        args.snr = True
        args.psnr = True
        args.md = True

    if len(org_img.shape) != len(new_img.shape):
        print('error: Cannot compare monochrome and colored pictures!')
        exit()

    if len(org_img.shape) == 3:
        channels_old = [org_img[:,:,0], org_img[:,:,1], org_img[:,:,2]]
        channels_new = [new_img[:,:,0], new_img[:,:,1], new_img[:,:,2]]
    else:
        channels_old = [org_img]
        channels_new = [new_img]

    if args.mse:
        mes = "MSE:"
        for ch in range(len(channels_old)):
            mes += " " + '%.2E' % Decimal(mse(channels_old[ch], channels_new[ch]))
        print(mes)

    if args.pmse:
        mes = "PMSE:"
        for ch in range(len(channels_old)):
            mes += " " + '%.2E' % Decimal(pmse(channels_old[ch], channels_new[ch]))
        print(mes)
        
    if args.snr:
        mes = "SNR:"
        for ch in range(len(channels_old)):
            mes += " " + '%.2E' % Decimal(snr(channels_old[ch], channels_new[ch]))
        print(mes)
    
    if args.psnr:
        mes = "PSNR:"
        for ch in range(len(channels_old)):
            mes += " " + '%.2E' % Decimal(psnr(channels_old[ch], channels_new[ch]))
        print(mes)

    if args.md:
        mes = "MD:"
        for ch in range(len(channels_old)):
            mes += " " + '%.2E' % Decimal(md(channels_old[ch], channels_new[ch]))
        print(mes)

def stop_memtest():
    current, peak = tracemalloc.get_traced_memory()
    print('Memory: ' + f"{(peak)/1000:.2f}" + 'KB')
    print('Time: ' + f"{time.process_time() - start_time:.2f}" + 's')
    tracemalloc.stop()

def main():
    global args

    # INITIALIZATION

    args = parse_cli()
    image = Image.open(args.input)
    pixels_old = np.array(image)
    pixels_new = pixels_old.copy()

    # ANALYSIS
    if args.ptest:
        global start_time
        tracemalloc.start()
        start_time = time.process_time()

    if is_command_analysis(args):
        compare_img = Image.open(args.compare)
        handle_analysis(pixels_old, np.array(compare_img))
        if args.ptest:
            stop_memtest()
        return

    # PROCESSING
    
    if len(pixels_new.shape) == 3:
        pixels_new = np.dstack((
            handle_operation(pixels_new[:,:,0]),
            handle_operation(pixels_new[:,:,1]),
            handle_operation(pixels_new[:,:,2])))
    else:
        pixels_new = handle_operation(pixels_new)
    
    if args.ptest:
        stop_memtest()

    # FINALIZATION

    Image.fromarray(pixels_new.astype(np.uint8)).save(args.output)

if __name__ == "__main__":
    main()