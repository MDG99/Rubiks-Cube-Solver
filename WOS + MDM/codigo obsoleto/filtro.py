import numpy as np


def mediana(img):

    w = img.shape[0]
    h = img.shape[1]

    aux = np.zeros((w, h, 3))
    for k in range(3):
        for i in range(1, w - 1):
            for j in range(1, h - 1):
                mask = [img[i - 1, j - 1, k], img[i - 1, j, k], img[i - 1, j + 1, k], img[i, j - 1, k], img[i, j, k],
                        img[i, j + 1, k], img[i + 1, j - 1, k], img[i + 1, j, k], img[i + 1, j + 1, k]]
                mask.sort()
                aux.itemset((i, j, k), mask[4])

    return aux
