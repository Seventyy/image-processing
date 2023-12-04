import numpy as np

def sexdeti(img):
    N_filter = [
        [ 1,  1,  1],
        [ 1, -2,  1],
        [-1, -1, -1]
    ]

    NE_filter = [
        [ 1,  1,  1],
        [-1, -2,  1],
        [-1, -1,  1]
    ]

    E_filter = [
        [-1,  1,  1],
        [-1, -2,  1],
        [-1,  1,  1]
    ]

    SE_filter = [
        [-1, -1,  1],
        [-1, -2,  1],
        [ 1,  1,  1]
    ]

