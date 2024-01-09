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

def grow(mask, img, error):
    four_adj = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1]
    ]
    [width, height] = img.shape
    changed = 0 # no of pixels changed
    
    for x in range(1, width-1):
        for y in range(1, height-1):
            if mask[x,y] == False:
                continue
            
            # compare pixels
            comp = img[x,y] # white pixel

            for adj in four_adj:
                new_val = img[x + adj[0], y + adj[1]]
                
                if mask[x + adj[0], y + adj[1]] == True:
                    continue
                
                if abs(int(new_val) - int(comp)) < error:
                    mask[x + adj[0], y + adj[1]] = True
                    changed += 1
    return [mask, changed]

def detect_region(region, img, error, seedx, seedy):
    # choose a seed
    # [seedx, seedy] = [0, 0]
    # while(True):
    #     seedx = random.randint(0, img.shape[0])
    #     seedy = random.randint(0, img.shape[1])
    #     if img[seedx, seedy]:
    #         break
    region[seedx, seedy] = 1

    frame = subframe(seedx, seedy, region.shape[0], region.shape[1])
    steps = 0

    # grow
    while (True):
        steps += 1
        print(f'step: {steps}')
        
        # growth of region in working frame
        [new, changed] = grow(frame.get(region).copy(), frame.get(img), error)
        frame.set(region, new)

        if changed == 0:
            break
        else:
            frame.try_expand(region)
    print([seedx, seedy])
    return region

def region_growing(img):
    [width, height] = img.shape
    
    error = 5
    seeds = [
        [184, 168],
        [68, 492]
    ]

    region = np.full(img.shape, False, dtype=bool)

    for s in seeds:
        new_region = np.full(img.shape, False, dtype=bool)
        new_region = detect_region(new_region, img, error, s[0], s[1])

        for x in range(width):
            for y in range(height):
                region[x,y] = new_region[x,y] or region[x,y]

    for x in range(width):
        for y in range(height):
            if region[x,y] == True:
                img[x,y] = 0
    return img