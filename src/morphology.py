from typing import List
import numpy as np


def dilation(img, se):
    img_copy = img.copy()

    frame_size:int = 0
    for vec in se:
        frame_size = max(frame_size, abs(vec[0])) 
        frame_size = max(frame_size, abs(vec[1]))

    for y in range(frame_size, img.shape[1] - frame_size):
        for x in range(frame_size, img.shape[0] - frame_size):
            
            img[x, y] = 1
    return img

def erosion(img, se:List[(int,int)]):
    pass

def opening(img, se:List[(int,int)]):
    pass

def closing(img, se:List[(int,int)]):
    pass

def hit_or_miss(img, se_active:List[(int,int)], se_inactive:List[(int,int)]):
    pass

def get_sample_se(code):
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