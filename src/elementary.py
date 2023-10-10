def brightness(img, value: int):
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            img[x, y] = min(max(img[x, y] + value, 0), 255)