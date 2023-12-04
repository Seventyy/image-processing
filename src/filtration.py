import numpy as np

kirsch_masks = np.array([
    [[ 5,  5,  5],
    [-3,  0, -3],
    [-3, -3, -3]],

    [[-3,  5,  5],
    [-3,  0,  5],
    [-3, -3, -3]],

    [[-3, -3,  5],
    [-3,  0,  5],
    [-3, -3,  5]],

    [[-3, -3, -3],
    [-3,  0,  5],
    [-3,  5,  5]],

    [[-3, -3, -3],
    [-3,  0, -3],
    [ 5,  5,  5]],

    [[-3, -3, -3],
    [ 5,  0, -3],
    [ 5,  5, -3]],

    [[ 5, -3, -3],
    [ 5,  0, -3],
    [ 5, -3, -3]],

    [[ 5,  5, -3],
    [ 5,  0, -3],
    [-3, -3, -3]]
])

sexdeti_masks = np.array([
    [[ 1,  1,  1],
    [  1, -2,  1],
    [ -1, -1, -1]],

    [[ 1,  1,  1],
    [ -1, -2,  1],
    [ -1, -1,  1]],

    [[-1,  1,  1],
    [ -1, -2,  1],
    [ -1,  1,  1]],

    [[-1, -1,  1],
    [ -1, -2,  1],
    [  1,  1,  1]]
])

sexdeti_mask_ids = {
    'N': 0,
    'NE': 1,
    'E': 2,
    'SE': 3
}

def sexdeti(img, mask_name):
    mask = sexdeti_masks[sexdeti_mask_ids[mask_name]]
    new_img = np.zeros_like(img)

    for x in range(1, img.shape[0] - 1):
        for y in range(1, img.shape[1] - 1):
            for i in range(3):
                for j in range(3):
                    val = mask[i, j] * img[x + i - 1, y + j - 1]
                    # print(val)
                    new_img[x, y] = val
                    # new_img[x, y] = max(min(val, 255), 0)

    return new_img

def okirsf(img):
    output_img = np.zeros(img.shape)

    for x in range(1, img.shape[0] - 1):
        for y in range(1, img.shape[1] - 1):
            max_msk = 0
            for mask in kirsch_masks:
                m_sum = 0
                for xi in range(3):
                    for yi in range(3):
                        pixel = img[x + xi - 1, y + yi - 1]
                        m_sum += pixel * mask[yi, xi]
                max_msk = max(max_msk, abs(m_sum))
            output_img[x, y] = max(1, max_msk)
    
    return output_img