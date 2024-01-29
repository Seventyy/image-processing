import numpy as np
import cmath
import math

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

def highpassedge(img, radius, angle):
    [N, M] = img.shape

    band_width = 15

    for x in range(N):
        for y in range(M):
            dist2 = (x - N // 2)**2 + (y - M // 2)**2
            if dist2 < radius**2:
                img[x,y] = 0
    
    for x in range(N):
        for y in range(M):
            r, theta = cartesian_to_polar(x-256, y-256)
            mirror_theta = (theta + 180) % 360
            if not(theta > angle - band_width/2 and theta < angle + band_width/2) and\
                not(mirror_theta > angle - band_width/2 and mirror_theta < angle + band_width/2):
                img[y, x] = 0

    return img

def cartesian_to_polar(x, y):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)

    theta_degrees = math.degrees(theta)
    theta_degrees = (theta_degrees + 360) % 360

    return r, theta_degrees

def phasefilter(img, k, l):
    [N, M] = img.shape

    mask = np.full((N, M), 1 + 1j)

    for n in range(N):
        for m in range(M):
            mask[n, m] = cmath.exp( 1j * ((-n*k*2*math.pi)/N + (-m*l*2*math.pi)/M + (k+l)*math.pi))
    
    for x in range(N):
        for y in range(M):
            # print(img[x, y] * mask[x, y])
            img[x, y] = img[x, y] * mask[x, y]
    
    return img
