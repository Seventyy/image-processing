def brightness(img, value: int):
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            img[x, y] = min(max(img[x, y] + value, 0), 255)
    return img

def negative(img):
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            img[x, y] = 255 - img[x, y]
    return img

def contrast(img, value: float):
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            raw = value * (img[x, y] - 125) + 125
            img[x, y] = max(min(raw, 255), 0)
    return img