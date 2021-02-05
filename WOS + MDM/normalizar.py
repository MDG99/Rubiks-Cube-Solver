import numpy as np


def normalizar(img):
    w = img.shape[0]
    h = img.shape[1]

    aux = np.zeros((w, h, 3))
    for k in range(3):
        for i in range(w):
            for j in range(h):
                aux = img[i, j, k] / max(img[i, j])

    return aux
