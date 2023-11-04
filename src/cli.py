import argparse

def parse_cli():
    parser = argparse.ArgumentParser(
        prog='imgproc',
        description='A lightweight image processing utility made in python.',
        usage='%(prog)s [-h] COMMAND -i INPUT [-o OUTPUT] [-v VALUE]')

    parser.add_argument('-i', '--input', help='Path to the image source', required=True)
    parser.add_argument('-o', '--output', default='output.bmp', help='Path to the image output')
    parser.add_argument('-v', '--value', help='Numerical value required by some commands')

    command_group = parser.add_argument_group('commands').add_mutually_exclusive_group()
    command_group.required = True

    command_group.add_argument('--brightness',
        help='Brightens or dimms the image by an intiger number of shades specified in -v',
        action='store_true')

    command_group.add_argument('--negative',
        help='Inverts colors of the image',
        action='store_true')

    command_group.add_argument('--contrast',
        help='Modifies contrast by a float value in -v. Value of 1 will not change anything',
        action='store_true')

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
        help='Makes the image two times larger',
        action='store_true')
    
    command_group.add_argument('--amean',
        help='Performs an arithmetic mean filter with window size 2*v+1',
        action='store_true')
    
    command_group.add_argument('--adaptive',
        help='Performs an adaptive median filter with window size 2*v+1',
        action='store_true')
    
    command_group.add_argument('--mse',
        help='Performs mean square error analisys',
        action='store_true')

    command_group.add_argument('--pmse',
        help='Performs peak mean square error analisys',
        action='store_true')

    command_group.add_argument('--snr',
        help='Performs signal to noise ratio analisys',
        action='store_true')

    command_group.add_argument('--psnr',
        help='Performs peak signal to noise ratio analisys',
        action='store_true')

    command_group.add_argument('--md',
        help='Performs maximum difference analisys',
        action='store_true')



    
    
    
    
    

    return parser.parse_args()
