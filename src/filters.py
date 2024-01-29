import numpy as np

def lowpass(img, radius):
    [N, M] = img.shape

    for x in range(N):
        for y in range(M):
            dist2 = (x - N // 2)**2 + (y - M // 2)**2
            if dist2 > radius**2:
                img[x,y] = 0

    return img

def highpass(img, radius):
    [N, M] = img.shape

    for x in range(N):
        for y in range(M):
            dist2 = (x - N // 2)**2 + (y - M // 2)**2
            if dist2 < radius**2:
                img[x,y] = 0
                
    return img

def bandpass(img, r1, r2):
    [N, M] = img.shape

    for x in range(N):
        for y in range(M):
            dist2 = (x - N // 2)**2 + (y - M // 2)**2
            if dist2 < r1**2 or dist2 > r2**2:
                img[x,y] = 0
                
    return img

def bandcut(img, r1, r2):
    [N, M] = img.shape

    for x in range(N):
        for y in range(M):
            dist2 = (x - N // 2)**2 + (y - M // 2)**2
            if dist2 > r1**2 and dist2 < r2**2:
                img[x,y] = 0
                
    return img

def highpassedge(img):
    return img

def phasefilter(img):
    return img
