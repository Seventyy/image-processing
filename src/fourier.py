import numpy as np
import math, cmath

def discrete_fourier(img):
    return img

def inverse_discrete_fourier(img):
    return img

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

def ifft(arr):
    N = len(arr)
    
    if N <= 1:
        return arr

    conj_exp_terms = [cmath.exp(2j * math.pi * k / N) for k in range(N)]
    
    even = ifft(arr[0::2])
    odd = ifft(arr[1::2])

    result = []
    for k in range(N // 2):
        result.append(even[k] + conj_exp_terms[k] * odd[k])
    for k in range(N // 2):
        result.append(even[k] - conj_exp_terms[k] * odd[k])

    return result

def transpose(arr):
    M = len(arr)
    N = len(arr[0])

    transposed = []
    for i in range(N):
        inner = []
        for j in range(M):
            inner.append(arr[j][i])
        transposed.append(inner)
    
    return transposed

def fft2d(img):
    by_rows = []
    for row in img:
        by_rows.append(fft(row))

    by_cols = []
    for col in np.transpose(by_rows):
        by_cols.append(fft(col))

    return np.array(transpose(by_cols), dtype=np.complex128)



def ifft2d(img):
    by_rows = []
    for row in img:
        by_rows.append(ifft(row))

    by_cols = []
    for col in np.transpose(by_rows):
        by_cols.append(ifft(col))

    return np.array(transpose(by_cols), dtype=np.complex128)

def normalize_output(org_image, result):
    min_val = np.min(org_image)
    max_val = np.max(org_image)
    normalized = (np.abs(result) - np.min(result)) / (np.max(result) - np.min(result)) * (max_val - min_val) + min_val
    return normalized

def normalize_output_log():
    magnitude_spectrum = np.log(np.abs(fft_result) + 1)
    magnitude_spectrum_normalized = (magnitude_spectrum - np.min(magnitude_spectrum)) / (np.max(magnitude_spectrum) - np.min(magnitude_spectrum)) * 255
    return magnitude_spectrum_normalized