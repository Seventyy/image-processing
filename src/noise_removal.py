import numpy as np

def amean(img, n):
    img_copy = img.copy()
    for y in range(n, img.shape[1] - n):
        for x in range(n, img.shape[0] - n):
            running_sum = 0
            for j in range(-n, n+1):
                for i in range(-n, n+1):
                    running_sum += img_copy[x+i, y+j]
            img[x, y] = running_sum / ((2*n+1) * (2*n+1))
    return img

def adaptive(img, n):
    img_copy = img.copy()
    
    z_min = 0
    z_max = 0
    z_med = 0
    z_xy = 0
    s_max = n # extents
    
    for y in range(s_max, img.shape[1] - s_max):
        for x in range(s_max, img.shape[0] - s_max):
            s = 1
            while(True):    
                values = []
                
                for j in range(-s, s+1):
                    for i in range(-s, s+1):
                        values.append(img_copy[x+i, y+j])

                values.sort()
                z_min = int(values[0])
                z_max = int(values[int(values.__len__())-1])
                z_med = int(values[int(values.__len__()/2)])
                z_xy = int(img_copy[x,y])
                
                a1 = z_med - z_min
                a2 = z_med - z_max
                if a1 > 0 and a2 < 0:
                    
                    b1 = z_xy - z_min
                    b2 = z_xy - z_max
                    if b1 > 0 and b2 < 0:
                        img[x, y] = np.clip(z_xy, 0, 255)
                    else:
                        img[x, y] = np.clip(z_med, 0, 255)
                else:
                    s += 1
                    if s <= s_max:
                        continue
                    else:
                        img[x, y] = np.clip(z_xy, 0, 255)
                break
    return img
