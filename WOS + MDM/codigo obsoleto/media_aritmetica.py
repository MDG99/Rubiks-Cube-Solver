import numpy as np


def media(img):
    w = img.shape[0]
    h = img.shape[1]

    pixel_quantity = w * h

    aux = np.zeros(3)
    for k in range(3):
        for i in range(1, w):
            for j in range(1, h):
                aux[k] = aux[k] + img[i, j, k]

        aux[k] = aux[k] / pixel_quantity

    return aux