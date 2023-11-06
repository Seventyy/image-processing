import argparse

def is_command_analysis(args):
    return args.mse or args.pmse or args.snr or args.psnr or args.md or args.report

def parse_cli():
    parser = argparse.ArgumentParser(
        prog='imgproc',
        description='A lightweight image processing utility made in python.',
        usage='%(prog)s [-h] COMMAND -i INPUT [-o OUTPUT] [-c COMPARE] [-v VALUE] [-k KERNEL_SIZE]',
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-i', '--input', help='Path to the image source', required=True)
    parser.add_argument('-o', '--output', default='output.bmp', help='Path to the image output')
    parser.add_argument('-c', '--compare', help='Path to the second image that the input will be compared to. Required by analysis methods. If unused, analysis will be performed on output')
    
    parser.add_argument('-v', '--value', help='Numerical value required by some commands')
    parser.add_argument('-k', '--kernel', default='1', help='Size of the kernel required by some commmands')

    command_group = parser.add_argument_group('commands').add_mutually_exclusive_group()
    command_group.required = True

    # ELEMENTARY

    command_group.add_argument('--brightness',
        help='Brightens or dimms the image by an intiger number of shades specified in -v',
        action='store_true')

    command_group.add_argument('--negative',
        help='Inverts colors of the image',
        action='store_true')

    command_group.add_argument('--contrast',
        help='Modifies contrast by a float value in -v. Value of 1 will not change anything\n\n',
        action='store_true')

    # GEOMETRIC

    command_group.add_argument('--hflip',
        help='Flips the image horizontally',
        action='store_true')

    command_group.add_argument('--vflip',
        help='Flips the image vertically',
        action='store_true')

    command_group.add_argument('--dflip',
        help='Flips the image diagonally',
        action='store_true')

    command_group.add_argument('--shrink',
        help='Makes the image two times smaller',
        action='store_true')

    command_group.add_argument('--enlarge',
        help='Makes the image two times larger\n\n',
        action='store_true')
    
    # NOISE REMOVAL

    command_group.add_argument('--amean',
        help='Performs an arithmetic mean filter with window size 2*(-v)+1. Takes -k',
        action='store_true')
    
    command_group.add_argument('--adaptive',
        help='Performs an adaptive median filter with window size 2*(-v)+1. Takes -k\n\n',
        action='store_true')
    
    # ANALYSIS

    command_group.add_argument('--mse',
        help='Performs mean square error analysis',
        action='store_true')

    command_group.add_argument('--pmse',
        help='Performs peak mean square error analysis',
        action='store_true')

    command_group.add_argument('--snr',
        help='Performs signal to noise ratio analysis',
        action='store_true')

    command_group.add_argument('--psnr',
        help='Performs peak signal to noise ratio analysis',
        action='store_true')

    command_group.add_argument('--md',
        help='Performs maximum difference analysis',
        action='store_true')
    
    command_group.add_argument('--report',
        help='Performs all analysis methods',
        action='store_true')
    
    args = parser.parse_args()

    if not args.value and (args.brightness or args.contrast):
        parser.error('-v/--value argument is required for current command!')

    if is_command_analysis(args) and not args.compare:
        parser.error('-c/--compare argument is required for current command!')
    
    if args.value and not (args.brightness or args.contrast):
        print('Ignoring -v/--value argument')

    return args
