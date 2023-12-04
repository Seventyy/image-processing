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