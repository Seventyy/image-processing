import argparse
import numpy as np

def is_operation_transformation(args):
    ops = np.array([
        args.brightness,
        args.negative,
        args.contrast,

        args.hflip,
        args.vflip,
        args.dflip,

        args.shrink,
        args.enlarge,

        args.amean,
        args.adaptive,

        args.hraleigh,
        args.sexdeti,
        args.optsexdetn,
        args.okirsf,

        args.dilation,
        args.erosion,
        args.opening,
        args.closing,
        args.hit_or_miss
    ])
    for i in ops:
        if i == True:
            return True
    return False

def is_operation_comparison(args):
    ops = np.array([
        args.mse,
        args.pmse,
        args.snr,
        args.psnr,
        args.md,
        args.report
    ])
    for i in ops:
        if i == True:
            return True
    return False

def is_operation_analysis(args):
    ops = np.array([
        args.cmean,
        args.cvariance,
        args.cstdev,
        args.cvarcoi,
        args.cvarcoii,
        args.casyco,
        args.cflatco,
        args.centropy
    ])
    for i in ops:
        if i == True:
            return True
    return False

def parse_cli():
    parser = argparse.ArgumentParser(
        prog='imgproc',
        description='A lightweight image processing utility made in python.',
        usage='%(prog)s [-h] COMMAND -i INPUT [-o OUTPUT] [-c COMPARE] [-v VALUE] [-k KERNEL_SIZE] [-ch CHANNEL] [-p] [-a ALPHA] [-gm G_MIN]',
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-i', '--input', help='Path to the image source', required=True)
    parser.add_argument('-o', '--output', default='output.bmp', help='path to the image output, \'output.bmp\' by default. Used only in case of graphical operations')
    parser.add_argument('-c', '--compare', help='Path to the second image that the input will be compared to. Required by analysis methods. If unused, analysis will be performed on output')
    
    parser.add_argument('-v', '--value', help='A numerical value used in the --brightness and –-contrast operations')
    parser.add_argument('-k', '--kernel', default='1', help='Size of the kernel required by some commmands')
    parser.add_argument('-p', '--ptest', action='store_true', help='Makes the program carry out a performance test')
    parser.add_argument('-ch', '--channel', default='all', help='Selects the channel for the --histogram operation. Only \'R\', \'G\', \'B\' or \'all\' (default).')

    parser.add_argument('-a', '--alpha', default=120, help='Alpha coefficient used for --raleigh. 120 by default.')
    parser.add_argument('-gm', '--gmin', default=0, help='Minimum brightness used for --raleigh. 0 by default.')

    parser.add_argument('-m', '--mask', default='N', help='Mask type used for --sexdeti. \'N\' (default), \'NE\', \'E\' or \'SE\'.')

    parser.add_argument('-se', '--structural_element', help='An index from sample structural elements. Used for --dilation, --erosion, --opening, --closing, --hit_or_miss')

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
        help='Performs all analysis methods\n\n',
        action='store_true')

    # HISTOGRAM

    command_group.add_argument('--histogram',
        help='Creates a histogram of the channel specified by -ch\n\n',
        action='store_true')
    
    # QUALITY IMPROVEMENT

    command_group.add_argument('--hraleigh',
        help='Raleigh final probability density function. Takes the arguments -gm/--gmin and -a/--alpha\n\n',
        action='store_true')

    # IMAGE CHARACTERISTICS

    command_group.add_argument('--cmean',
        help='Mean characteristic',
        action='store_true')
    
    command_group.add_argument('--cvariance',
        help='Variance characteristic',
        action='store_true')

    command_group.add_argument('--cstdev',
        help='Standard deviation characteristic',
        action='store_true')

    command_group.add_argument('--cvarcoi',
        help='Variation coefficient I characteristic',
        action='store_true')

    command_group.add_argument('--cvarcoii',
        help='Variation coefficient II characteristic',
        action='store_true')

    command_group.add_argument('--casyco',
        help='Asymmetry coefficient characteristic',
        action='store_true')

    command_group.add_argument('--cflatco',
        help='Flattening coefficient characteristic',
        action='store_true')

    command_group.add_argument('--centropy',
        help='Information source entropy characteristic\n\n',
        action='store_true')

    # LINEAR IMAGE FILTRATION

    command_group.add_argument('--sexdeti',
        help='Extraction of deteials I. N, NE, E, SE filters\n\n',
        action='store_true')
    
    command_group.add_argument('--optsexdetn',
        help='Optimised extraction of deteials for north filter\n\n',
        action='store_true')

    # NON-LINEAR IMAGE FILTRATION

    command_group.add_argument('--okirsf',
        help='Kirsh operator',
        action='store_true')

    # MORPHOLOGICAL
    
    command_group.add_argument('--dilation', 
        help='Performs dilation operation on an input. Requires use of -se to provide structural element',
        action='store_true')
    
    command_group.add_argument('--erosion', 
        help='Performs erosion operation on an input. Requires use of -se to provide structural element',
        action='store_true')
    
    command_group.add_argument('--opening', 
        help='Performs opening operation on an input. Requires use of -se to provide structural element',
        action='store_true')
    
    command_group.add_argument('--closing', 
        help='Performs closing operation on an input. Requires use of -se to provide structural element',
        action='store_true')
    
    command_group.add_argument('--hit_or_miss', 
        help='Performs hit_or_miss operation on an input. Requires use of -se to provide structural element',
        action='store_true')
    

    # EDGECASES

    args = parser.parse_args()

    if not args.value and (args.brightness or args.contrast):
        parser.error('-v/--value argument is required for current command!')

    if is_operation_comparison(args) and not args.compare:
        parser.error('-c/--compare argument is required for current command!')
    
    if args.value and not (args.brightness or args.contrast):
        print('Ignoring -v/--value argument')

    if args.histogram and not args.channel:
        parser.error('-ch/--channel argument is required for current command!')

    if args.histogram and args.channel not in {'R', 'G', 'B', 'all'}:
        parser.error('-ch/--channel can only take R, G, B or all.')

    if args.sexdeti and args.mask not in {'N', 'NE', 'E', 'SE'}:
        parser.error('-m/--mask can only take N, NE, E or SE.')

    if True in [args.dilation, args.erosion, args.opening, args.closing, args.hit_or_miss] and not args.structural_element:
        parser.error('-se/--structural_element is required for current command!')

    if args.structural_element not in [None, 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']:
        parser.error('-se/--structural_element can only take a roman letter from i to x!')

    return args
