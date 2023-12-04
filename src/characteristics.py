import numpy as np
import math
from histogram import *

def cmean(img):
    data = histogram_data(img)

    running_sum = 0
    for m in range(256):
        running_sum += m * data[m]
    
    return running_sum / len(img)**2

def cvariance(img):
    data = histogram_data(img)
    mean = cmean(img)

    running_sum = 0
    for m in range(256):
        running_sum += (m-mean)**2 * data[m]
    
    return running_sum / len(img)**2

def cstdev(img):
    return math.sqrt(cvariance(img)) 

def cvarcoi(img):
    return cstdev(img) / cmean(img)

def casyco(img):
    data = histogram_data(img)
    mean = cmean(img)

    running_sum = 0
    for m in range(256):
        running_sum += (m-mean)**3 * data[m]
    
    return running_sum / len(img)**2 / cstdev(img)**3

def cflatco(img):
    data = histogram_data(img)
    mean = cmean(img)

    running_sum = 0
    for m in range(256):
        running_sum += (m-mean)**4 * data[m]
    
    return running_sum / len(img)**2 / cstdev(img)**4 - 3

def cvarcoii(img):
    data = histogram_data(img)

    running_sum = 0
    for m in range(256):
        running_sum += data[m]**2
    
    return running_sum / len(img)**4

def centropy(img):
    data = histogram_data(img)

    running_sum = 0
    for m in range(256):
        if data[m] == 0: continue
        running_sum += data[m] * math.log2(data[m]/len(img)**2)
    
    return -running_sum / len(img)**2
