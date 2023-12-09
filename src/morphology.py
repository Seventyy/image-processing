from typing import List, Tuple
import numpy as np

se_type = List[Tuple[int, int]]

def dilation(img, se: se_type):
    img_copy = img.copy()

    frame_size:int = 0
    for vec in se:
        frame_size = max(frame_size, abs(vec[0])) 
        frame_size = max(frame_size, abs(vec[1]))

    for y in range(frame_size, img.shape[1] - frame_size):
        for x in range(frame_size, img.shape[0] - frame_size):
            
            img[x, y] = 1
    return img

def erosion(img, se:se_type):
    return img

def opening(img, se:se_type):
    return img

def closing(img, se:se_type):
    return img

def hit_or_miss(img, se_active:se_type, se_inactive:se_type):
    return img

def get_sample_se(code) -> se_type:
    match code:
        case 'i':
            return [
                (0,0),
                (1,0)
            ]
        case 'ii':
            return [
                (0,0),
                (0,1)
            ]
        case 'iii':
            return [
                ( 0, 0),

                ( 1, 0),
                ( 0, 1),
                (-1, 0),
                ( 0,-1),

                ( 1, 1),
                (-1, 1),
                (-1,-1),
                ( 1,-1),
            ]
        case 'iv':
            return [
                ( 0, 0),

                ( 1, 0),
                ( 0, 1),
                (-1, 0),
                ( 0,-1),
            ]
        case 'v':
            return [
                ( 0, 0),

                ( 1, 0),
                ( 0, 1),
            ]
        case 'vi':
            return [
                ( 1, 0),
                ( 0, 1),
            ]
        case 'vii':
            return [
                ( 0, 0),

                ( 1, 0),
                (-1, 0),
            ]
        case 'viii':
            return [
                ( 0, 0),

                ( 1, 0),
                (-1, 0),
            ]
        case 'ix':
            return [
                ( 0, 0),

                (-1, 0),
                (-1, 1),
            ]
        case 'x':
            return [
                ( 0, 0),

                ( 0, 1),
                ( 1,-1),
            ]
    print('Error: unknown SE: ' + code)
    exit(1)