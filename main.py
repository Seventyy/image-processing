import sys
import tracemalloc
import time

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

sys.path.insert(0, f'./src')
from cli import *
from operation_handling import *
from histogram import *

def main():

    # INITIALIZATION - loading arguments and files and starting tests

    args = parse_cli()
    image = Image.open(args.input)
    pixels_old = np.array(image)
    pixels_new = pixels_old.copy()
    target_type = pixels_old.dtype

    if len(pixels_new.shape) == 3 and not is_operation_comparison(args):
        R = pixels_new[:,:,0]
        G = pixels_new[:,:,1]
        B = pixels_new[:,:,2]

    compare_img = False
    pixels_compare = False
    if args.compare:
        compare_img = Image.open(args.compare)
        pixels_compare = np.array(compare_img)

    if args.ptest:
        print('The performance test has started.')
        tracemalloc.start() # TODO: check if not wrong, causes operations take up to 10 times longer
        start_time = time.process_time()
    
    # PROCESSING - transformation, comparison or analysis

    if is_operation_transformation(args):
        if len(pixels_new.shape) == 3:
            pixels_new = np.dstack((
                handle_transformation(args, R),
                handle_transformation(args, G),
                handle_transformation(args, B)))
        else:
            pixels_new = handle_transformation(args, pixels_new)

        # fourier has to be shown on plt
        if True in [args.fourier, args.fft, args.dft]:
            if len(pixels_new.shape) == 3:
                data = np.abs((pixels_new[:,:,0] + pixels_new[:,:,1] + pixels_new[:,:,2]) / 3)
            else:
                data = np.abs(pixels_new)

            [H, W] = [elem // 2 for elem in data.shape]
            extent = [-H, H, -W, W]

            minv = np.min(data)
            if (minv == 0.0):
                minv = 1.0

            cmap = plt.cm.inferno
            norm = LogNorm(vmin=minv, vmax=np.max(data))

            plt.figure(figsize=(10, 6))
            plt.imshow(data, cmap=cmap, norm=norm, extent=extent)
            plt.colorbar()
            plt.title('Fourier Transform Magnitude')
            plt.xlabel('Frequency (kx)')
            plt.ylabel('Frequency (ky)')
            plt.show()

            pixels_new = cmap(norm(data))[:,:,:3] * 255

    if is_operation_comparison(args):
        handle_comparison(args, pixels_old, pixels_compare)

    if is_operation_analysis(args):
        if len(pixels_new.shape) == 3:
            print(handle_analysis(args, R))
            print(handle_analysis(args, G))
            print(handle_analysis(args, B))
        else:
            print(handle_analysis(args, pixels_new))

    if args.histogram:  # exception due to complexity
        # target_type = np.uint8
        if target_type == bool:
            print('ERROR: Histogram for binary images is not supported!')
            exit(1)
        print(target_type)
        if len(pixels_new.shape) == 2:
            print('WARNING: Image is monochrome, ignoring -ch/--channel argument')
            pixels_new = hist_to_img(histogram_data(pixels_new))
        elif args.channel == 'all':
            pixels_new = np.dstack((
                hist_to_img(histogram_data(R)),
                hist_to_img(histogram_data(G)),
                hist_to_img(histogram_data(B))))
        else:
            channel_no = {'R':0, 'G':1, 'B':2}[args.channel]
            output = np.zeros([100, 256, 3])
            output[:,:,channel_no] = hist_to_img(histogram_data(pixels_new[:,:,channel_no]))
            pixels_new = output
    
    # FINALIZATION - finishing tests and saving files

    if args.ptest:
        current, peak = tracemalloc.get_traced_memory()
        print('The performance test has ended.')
        print('Memory: ' + f"{(peak)/1000:.2f}" + 'KB')
        print('Time: ' + f"{time.process_time() - start_time:.2f}" + 's')
        tracemalloc.stop()
    
    if is_operation_transformation(args) or args.histogram:
        Image.fromarray(pixels_new.astype(target_type)).save(args.output)

if __name__ == "__main__":
    main()