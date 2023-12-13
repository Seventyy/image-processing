import random
import numpy as np
from morphology import get_sample_se, dilation

class subframe:
    def __init__(self, startx, starty, width, height):
        self.max_x = width - 1
        self.max_y = height - 1

        self.x1 = max(startx - 2, 0)
        self.y1 = max(starty - 2, 0)
        self.x2 = min(startx + 2, self.max_x)
        self.y2 = min(starty + 2, self.max_y)

    def get(self, img):
        return img[self.x1:self.x2+1, self.y1:self.y2+1]

    def set(self, img1, img2):
        img1[self.x1:self.x2+1, self.y1:self.y2+1] = img2

    def is_full(self):
        return self.x1 == 0 and self.y1 == 0 and self.x2 == self.max_x and self.y2 == self.max_y

    def try_expand(self, img):
        x1 = self.x1+1
        x2 = self.x2-1
        y1 = self.y1+1
        y2 = self.y2-1

        if True in img[x1, y1:y2+1]:
            self.x1 = max(self.x1 - 1, 0)
        if True in img[x2, y1:y2+1]:
            self.x2 = min(self.x2 + 1, self.max_x)
        if True in img[x1:x2+1, y1]:
            self.y1 = max(self.y1 - 1, 0)
        if True in img[x1:x2+1, y2]:
            self.y2 = min(self.y2 + 1, self.max_y)

def detect_region(img):
    old_region = np.full(img.shape, False, dtype=bool)
    new_region = old_region.copy()
    se = get_sample_se('iii')

    # choose a seed
    [seedx, seedy] = [0, 0]
    while(True):
        seedx = random.randint(0, img.shape[0])
        seedy = random.randint(0, img.shape[1])
        if img[seedx, seedy]:
            break
    old_region[seedx, seedy] = 1

    frame = subframe(seedx, seedy, old_region.shape[0], old_region.shape[1])

    iters = 0
    # grow
    while (True):
        iters += 1
        print(iters)
        
        # dilation of pixels in working frame
        new = dilation(frame.get(old_region).copy(), se)
        frame.set(new_region, new)

        # intersection with orginal img
        for x in range(new_region.shape[0]):
            for y in range(new_region.shape[1]):
                new_region[x, y] = new_region[x, y] and img[x, y]

        if np.array_equal(new_region, old_region):
            break
        else:
            old_region = new_region.copy()
            frame.try_expand(new_region)
    
    return old_region

def region_growing(img):
    [width, height] = img.shape

    binary = np.full(img.shape, 0, dtype=bool)

    treshold = 170

    for x in range(width):
        for y in range(height):
            binary[x,y] = img[x,y] > treshold

    region = detect_region(binary)
    for x in range(width):
        for y in range(height):
            if region[x,y]:
                img[x,y] = 255
            elif binary[x,y]:
                img[x,y] = 128
            else:
                img[x,y] = 0
            # if not region[x,y]:
            #     img[x,y] = max(min(img[x,y] - 100, 155), 0)
    
    return img