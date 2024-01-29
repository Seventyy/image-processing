from decimal import Decimal
import numpy as np

from elementary import *
from geometric import *
from noise_removal import *
from comparison import *
from quality_improvement import *
from filtration import *
from characteristics import *
from morphology import *
from segmentation import *
from fourier import *
from filters import *

def handle_transformation(args, channel):
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

    if args.hraleigh:
        return hraleigh(channel, histogram_data(channel), float(args.gmin), float(args.alpha))

    if args.sexdeti:
        return sexdeti(channel, args.mask)

    if args.optsexdetn:
        return optsexdetn(channel)

    if args.okirsf:
        return okirsf(channel)

    if args.dilation:
        return dilation(channel, get_sample_se(args.structural_element))

    if args.erosion:
        return erosion(channel, get_sample_se(args.structural_element))

    if args.opening:
        return opening(channel, get_sample_se(args.structural_element))

    if args.closing:
        return closing(channel, get_sample_se(args.structural_element))

    if args.hit_or_miss:
        return hit_or_miss(channel, get_sample_se_hmt(args.structural_element))

    if args.region_growing:
        txt = []
        txt.extend(args.seed.split(' '))
        seeds = []
        for pair in txt:
            [x, y] = pair.split(',')
            seeds.append([int(x), int(y)])
        print(seeds)

        return region_growing(channel, seeds, int(args.error))

    if args.m3:
        [x, y] = args.point.split(',')
        return m3(channel, get_sample_se(args.structural_element), [int(x),int(y)])

    # fourier

    if args.dft:
        return dft2d(channel)
    
    if args.fft:
        return fft2d(channel)

    # filters

    if True in [args.lowpassf, args.highpassf, args.bandpassf, args.bandcutf, args.edgehpf, args.phasef]:
        
        transform = fft2d(channel)
        if args.bandpassf or args.bandcutf:
            [r1, r2] = sorted([float(r.strip()) for r in args.radius.split(',')])

        if args.lowpassf:
            result = lowpass(transform, float(args.radius))
        if args.highpassf:
            result = highpass(transform, float(args.radius))
        if args.bandpassf:
            result = bandpass(transform, r1, r2)
        if args.bandcutf:
            result = bandcut(transform, r1, r2)
        if args.edgehpf:
            result = highpassedge(transform)
        if args.phasef:
            result = phasefilter(transform)
        
        if args.fourier:
            return result
        else:
            return np.abs(ifft2d(result))
    
    print('Error! Transformation not recognized!')
    exit(1)

def handle_comparison(args, org_img, new_img):
    if args.report:
        args.mse = True
        args.pmse = True
        args.snr = True
        args.psnr = True
        args.md = True

    if len(org_img.shape) != len(new_img.shape):
        print('error: Cannot compare monochrome and colored pictures!')
        exit(1)

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

def handle_analysis(args, channel):
    if args.cmean:
        return cmean(channel)
    
    if args.cvariance:
        return cvariance(channel)
    
    if args.cstdev:
        return cstdev(channel)
    
    if args.cvarcoi:
        return cvarcoi(channel)

    if args.cvarcoii:
        return cvarcoii(channel)
    
    if args.casyco:
        return casyco(channel)
    
    if args.cflatco:
        return cflatco(channel)
    
    if args.centropy:
        return centropy(channel)
    
    print('Error! Analysis not recognized!')
    exit(1)