import sys
import tracemalloc
import time

from PIL import Image
import numpy as np

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

    compare_img = False
    pixels_compare = False
    if args.compare:
        compare_img = Image.open(args.compare)
        pixels_compare = np.array(compare_img)

    if args.ptest:
        global start_time
        tracemalloc.start()
        start_time = time.process_time()
    
    # PROCESSING - transformation, comparison or analysis

    if is_operation_transformation(args):
        if len(pixels_new.shape) == 3:
            pixels_new = np.dstack((
                handle_transformation(args, pixels_new[:,:,0]),
                handle_transformation(args, pixels_new[:,:,1]),
                handle_transformation(args, pixels_new[:,:,2])))
        else:
            pixels_new = handle_transformation(args, pixels_new)

    if is_operation_comparison(args):
        handle_comparison(args, pixels_old, pixels_compare)

    if is_operation_analysis(args):
        if len(pixels_new.shape) == 3:
            print(handle_analysis(args, pixels_new[:,:,0]))
            print(handle_analysis(args, pixels_new[:,:,1]))
            print(handle_analysis(args, pixels_new[:,:,2]))
        else:
            print(handle_analysis(args, pixels_new))

    if args.histogram:  # exception due to complexity
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

    # FINALIZATION - finishing tests and saving files

    if args.ptest:
        current, peak = tracemalloc.get_traced_memory()
        print('Memory: ' + f"{(peak)/1000:.2f}" + 'KB')
        print('Time: ' + f"{time.process_time() - start_time:.2f}" + 's')
        tracemalloc.stop()
    
    if is_operation_transformation(args) or args.histogram:
        Image.fromarray(pixels_new.astype(np.uint8)).save(args.output)

if __name__ == "__main__":
    main()