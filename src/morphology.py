from typing import List, Tuple
import numpy as np

se_type = List[Tuple[int, int]]

def erosion(img, se: se_type):
    img_copy = img.copy()

    frame_size:int = 0
    for vec in se:
        frame_size = max(frame_size, abs(vec[0])) 
        frame_size = max(frame_size, abs(vec[1]))
            
    for y in range(frame_size, img.shape[1] - frame_size):
        for x in range(frame_size, img.shape[0] - frame_size):
            
            is_valid = True
            for i,j in se:
                if img_copy[y+j, x+i] == 1:
                    continue
                else:
                    is_valid = False
                    break
            
            img[y, x] = is_valid
    return img

def dilation(img, se:se_type):
    img_copy = img.copy()

    frame_size:int = 0
    for vec in se:
        frame_size = max(frame_size, abs(vec[0])) 
        frame_size = max(frame_size, abs(vec[1]))
            
    for y in range(frame_size, img.shape[1] - frame_size):
        for x in range(frame_size, img.shape[0] - frame_size):
            
            is_valid = False
            for i,j in se:
                if img_copy[y+j, x+i] == 1:
                    is_valid = True
                    break
            
            img[y, x] = is_valid
    return img

def opening(img, se:se_type):
    return dilation(erosion(img, se), se) 

def closing(img, se:se_type):
    return erosion(dilation(img, se), se) 

def hit_or_miss(img, se:(se_type, se_type)):
    img_copy = img.copy()

    frame_size:int = 0
    for vec in se[0]:
        frame_size = max(frame_size, abs(vec[0])) 
        frame_size = max(frame_size, abs(vec[1]))
    for vec in se[1]:
        frame_size = max(frame_size, abs(vec[0])) 
        frame_size = max(frame_size, abs(vec[1]))
            
    for y in range(frame_size, img.shape[1] - frame_size):
        for x in range(frame_size, img.shape[0] - frame_size):
            
            is_valid = True
            for i,j in se[1]:
                if img_copy[y+j, x+i] == 1:
                    continue
                else:
                    is_valid = False
                    break
            for i,j in se[0]:
                if img_copy[y+j, x+i] == 0:
                    continue
                else:
                    is_valid = False
                    break
            
            img[y, x] = is_valid
    return img

def get_sample_se_hmt(code) -> (se_type, se_type):
    if code == 'xiE':
        return ([
            ( 1, 0),
            ( 1, 1),
            ( 0, 1),
            ( 0,-1),
            ( 1,-1),
        ],[
            (-1, 1),
            (-1, 0),
            (-1,-1),
        ])
    elif code == 'xiS':
        return ([
            ( 1, 0),
            ( 1, 1),
            ( 0, 1),
            (-1, 1),
            (-1, 0),
        ],[
            (-1,-1),
            ( 0,-1),
            ( 1,-1),
        ])
    elif code == 'xiW':
        return ([
            ( 0, 1),
            (-1, 1),
            (-1, 0),
            (-1,-1),
            ( 0,-1),
        ],[
            ( 1, 0),
            ( 1, 1),
            ( 1,-1),
        ])
    elif code == 'xiN':
        return ([
            ( 1, 0),
            (-1, 0),
            (-1,-1),
            ( 0,-1),
            ( 1,-1),
        ],[
            ( 1, 1),
            ( 0, 1),
            (-1, 1),
        ])
    elif code == 'xiiN':
        return ([
            (-1, 0), 
            ( 1, 0),
        ],[
            ( 0, 0), 
            (-1, 1),
            ( 0, 1),
            ( 1, 1),
        ])
    elif code == 'xiiNE':
        return ([
            ( 1, 1),
            (-1,-1),
        ],[
            (-1, 0),
            ( 0, 0),
            (-1, 1),
            ( 0, 1),
        ])
    elif code == 'xiiE':
        return ([
            ( 0,-1),
            ( 0, 1),
        ],[
            ( 0, 0),
            (-1,-1), 
            (-1, 0),
            (-1, 1), 
        ])
    elif code == 'xiiSE':
        return ([
            ( 1,-1),
            (-1, 1),
        ],[
            (-1,-1),
            ( 0,-1), 
            (-1, 0),
            ( 0, 0), 
        ])
    elif code == 'xiiS':
        return ([
            ( 1, 0),
            (-1, 0),
        ],[
            (-1,-1),
            ( 0,-1),
            ( 1,-1),
            ( 0, 0),            
        ])
    elif code == 'xiiSW':
        return ([
            (-1,-1),
            ( 1, 1),
        ],[
            ( 0,-1),
            ( 1,-1),
            ( 0, 0),
            ( 1, 0),
        ])
    elif code == 'xiiW':
        return ([
            ( 0,-1),
            ( 0, 1),
        ],[
            ( 0, 0),
            ( 1,-1),
            ( 1, 0),
            ( 1, 1),
        ])
    elif code == 'xiiNW':
        return ([
            (-1, 1),
            ( 1,-1),
        ],[
            ( 0, 0),
            ( 1, 0),
            ( 0, 1),
            ( 1, 1),
        ])

def get_sample_se(code) -> se_type:
    if code == 'i':
        return [
            (0,0),
            (1,0)
        ]
    elif code == 'ii':
        return [
            (0,0),
            (0,1)
        ]
    elif code == 'iii':
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
    elif code == 'iv':
        return [
            ( 0, 0),

            ( 1, 0),
            ( 0, 1),
            (-1, 0),
            ( 0,-1),
        ]
    elif code == 'v':
        return [
            ( 0, 0),

            ( 1, 0),
            ( 0, 1),
        ]
    elif code == 'vi':
        return [
            ( 1, 0),
            ( 0, 1),
        ]
    elif code == 'vii':
        return [
            ( 0, 0),

            ( 1, 0),
            (-1, 0),
        ]
    elif code == 'viii':
        return [
            ( 1, 0),
            (-1, 0),
        ]
    elif code == 'ix':
        return [
            ( 0, 0),

            (-1, 0),
            (-1, 1),
        ]
    elif code == 'x':
        return [
            ( 0, 0),

            ( 0, 1),
            ( 1,-1),
        ]
    print('Error: unknown SE: ' + code)
    exit(1)