import numpy as np
import cmath

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

    for x in range(N):
        for y in range(M):
            dist2 = (x - N // 2)**2 + (y - M // 2)**2
            if dist2 < radius**2:
                img[x,y] = 0
    
    for x in range(N):
        for y in range(M):
            dist2 = (x - N // 2)**2 + (y - M // 2)**2
            if dist2 < radius**2:
                img[x,y] = 0
    


    
    band_width = 15
    
    # Calculate the bounds for the band
    band_left = int((N - band_width) / 2)
    band_right = int((N + band_width) / 2)
    
    # Iterate over each pixel in the image
    for x in range(N):
        for y in range(M):
            # Check if the pixel is within the band bounds
            if band_left <= x < band_right:
                # Calculate the new position based on the rotation
                new_x = int((x - N / 2) * cmath.cos(angle) - (y - M / 2) * cmath.sin(angle) + N / 2)
                new_y = int((x - N / 2) * cmath.sin(angle) + (y - M / 2) * cmath.cos(angle) + M / 2)
                
                # Check if the new position is within the image bounds
                if 0 <= new_x < N and 0 <= new_y < M:
                    img[x,y] = 0






    return img
    

def phasefilter(img, k, l):

    cmath.exp(j * ((-n*k*2*PI)/512 + (-m*l*2*PI)/512 + (k+l)*PI))

    return img
