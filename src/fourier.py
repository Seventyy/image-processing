import numpy as np
import math, cmath

def dft(arr):
    N = len(arr)
    w = cmath.exp(-2j*np.pi/N)

    result = []
    for n in range(N):
        val = 0
        for k in range(N):
            val += arr[k] * w**(n*k)
        result.append(val)
    
    return result

def idft(arr):
    N = len(arr)
    w = cmath.exp(2j*np.pi/N)

    result = []
    for n in range(N):
        val = 0
        for k in range(N):
            val += arr[k] * w**(n*k)
        result.append(val / N)
    
    return result

def fft(arr):
    N = len(arr)
    
    if N <= 1:
        return arr

    even = fft(arr[0::2])
    odd = fft(arr[1::2])

    T = []
    for k in range(N // 2):
        T.append(cmath.exp(-2j * math.pi * k / N) * odd[k])

    result = []
    for k in range(N // 2):
        result.append(even[k] + T[k])
    for k in range(N // 2):
        result.append(even[k] - T[k])

    return result

def ifft_unnorm(arr):
    N = len(arr)
    
    if N <= 1:
        return arr

    even = ifft_unnorm(arr[0::2])
    odd = ifft_unnorm(arr[1::2])

    T = []
    for k in range(N // 2):
        T.append(cmath.exp(2j * math.pi * k / N) * odd[k])

    result = []
    for k in range(N // 2):
        result.append(even[k] + T[k])
    for k in range(N // 2):
        result.append(even[k] - T[k])
    
    return result

def ifft(arr):
    N = len(arr)
    result = ifft_unnorm(arr)
    return [elem / N for elem in result]

def rearange(img):
    [H, W] = [elem // 2 for elem in img.shape]
    copy = img.copy()
    
    img[H:,W:] = copy[:H,:W]
    img[:H,W:] = copy[H:,:W]
    img[H:,:W] = copy[:H,W:]
    img[:H,:W] = copy[H:,W:]

    return img

def dft2d(img):
    by_rows = []
    rownum = 0
    for row in img:
        rownum += 1
        by_rows.append(dft(row))

    colnum = 0
    by_cols = []
    trows = np.transpose(by_rows)
    for col in trows:
        colnum += 1
        by_cols.append(dft(col))

    return rearange(np.array(np.transpose(by_cols), dtype=np.complex128))

def idft2d(img):
    by_rows = []
    rownum = 0
    for row in img:
        rownum += 1
        by_rows.append(idft(row))

    colnum = 0
    by_cols = []
    trows = np.transpose(by_rows)
    for col in trows:
        colnum += 1
        by_cols.append(idft(col))

    return np.array(np.transpose(by_cols), dtype=np.complex128)

def fft2d(img):
    by_rows = []
    for row in img:
        by_rows.append(fft(row))

    by_cols = []
    trows = np.transpose(by_rows)
    for col in trows:
        by_cols.append(fft(col))

    return rearange(np.array(np.transpose(by_cols), dtype=np.complex128))

def ifft2d(img):
    by_rows = []
    for row in img:
        by_rows.append(ifft(row))

    by_cols = []
    for col in np.transpose(by_rows):
        by_cols.append(ifft(col))

    return np.array(np.transpose(by_cols), dtype=np.complex128)
