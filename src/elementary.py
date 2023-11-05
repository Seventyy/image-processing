def brightness(img, value: int):
    lookup = []
    for n in range(256):
        new_val = n + value
        if (new_val < 0):
            new_val = 0
        if (new_val > 255):
            new_val = 255
        lookup.append(new_val)

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            img[x, y] = lookup[img[x,y]]
    return img

def negative(img):
    lookup = []
    for n in range(256):
        new_val = 255 - n
        lookup.append(new_val)

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            img[x, y] = lookup[img[x, y]]
    return img

def contrast(img, value: float):
    lookup = []
    for n in range(256):
        new_val = value * (n - 125) + 125
        if (new_val < 0):
            new_val = 0
        if (new_val > 255):
            new_val = 255
        lookup.append(new_val)

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            img[x, y] = lookup[img[x, y]]
    return img