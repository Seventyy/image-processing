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
from histogram import *
from quality_improvement import *
from characteristics import *

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
    
    if args.cmean:
        return cmean(channel)
    
    if args.cvariance:
        return cvariance(channel)
    
    if args.cstdev:
        return cstdev(channel)
    
    if args.cvarcoi:
        return cvarcoi(channel)
    
    if args.casyco:
        return casyco(channel)
    
    if args.cflatco:
        return cflatco(channel)
    
    if args.cvarcoii:
        return cvarcoii(channel)
    
    if args.centropy:
        return centropy(channel)
    
    
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

def finalize_img(img):
    Image.fromarray(img.astype(np.uint8)).save(args.output)

def main():
    global args

    # INITIALIZATION

    args = parse_cli()
    image = Image.open(args.input)
    pixels_old = np.array(image)
    pixels_new = pixels_old.copy()

    if args.ptest:
        global start_time
        tracemalloc.start()
        start_time = time.process_time()
    
    # PROCESSING

    if is_command_elementary(args) or is_command_geometric(args) or is_command_noiserem(args):
        if len(pixels_new.shape) == 3:
            pixels_new = np.dstack((
                handle_operation(pixels_new[:,:,0]),
                handle_operation(pixels_new[:,:,1]),
                handle_operation(pixels_new[:,:,2])))
        else:
            pixels_new = handle_operation(pixels_new)

    if is_command_characteristics(args):
        if len(pixels_new.shape) == 3:
            print(handle_operation(pixels_new[:,:,0]))
            print(handle_operation(pixels_new[:,:,1]))
            print(handle_operation(pixels_new[:,:,2]))
        else:
            print(handle_operation(pixels_new))

    if is_command_analysis(args):
        compare_img = Image.open(args.compare)
        handle_analysis(pixels_old, np.array(compare_img))

    if args.histogram:
        if len(pixels_new.shape) == 2:
            print('WARNING: Image is monochrome, ignoring -ch/--channel argument')
            pixels_new = hist_to_img(histogram_data(pixels_new))
        elif args.channel == 'all':
            pixels_new = np.dstack((
                hist_to_img(histogram_data(pixels_new[:,:,0]), True),
                hist_to_img(histogram_data(pixels_new[:,:,1]), True),
                hist_to_img(histogram_data(pixels_new[:,:,2]), True)))
        else:
            channels = {'R' : 0, 'G': 1, 'B': 2}
            channel_no = channels[args.channel]
            pixels_new = hist_to_img(histogram_data(pixels_new[:,:,channel_no]))

    if args.hraleigh:
        g_min = float(args.gmin)
        alpha = float(args.alpha)

        if len(pixels_new.shape) == 3:
            pixels_new = np.dstack((
                hraleigh(pixels_new[:,:,0], histogram_data(pixels_new[:,:,0]), g_min, alpha),
                hraleigh(pixels_new[:,:,1], histogram_data(pixels_new[:,:,1]), g_min, alpha),
                hraleigh(pixels_new[:,:,2], histogram_data(pixels_new[:,:,2]), g_min, alpha)))
        else:
            pixels_new = hraleigh(pixels_new, histogram_data(pixels_new), g_min, alpha)

    # FINALIZATION

    if args.ptest:
        stop_memtest()
    if not is_command_analysis(args):
        finalize_img(pixels_new)

if __name__ == "__main__":
    main()