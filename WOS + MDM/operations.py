import numpy as np

M = [[17, 109, 149],  # Azul ya
     [246, 83, 20],  # Roj0 ***
     [69, 205, 84],  # Verde pálido
     [242, 129, 20],  # Naranja ya
     [183, 178, 52],  # Amarillo ***
     [158, 176, 130],  # Blanco
     [4, 17, 2]
    ]  # Fondo


Mejorado = [[0, 0, 255],  # Azul
            [255, 0, 0],  # Roj0
            [0, 255, 0],  # Verde
            [255, 128, 0],  # Naranja
            [255, 255, 0],  # Amarillo
            [255, 255, 255],  # Blanco
            [0, 0, 0]]  # Fondo

clases = np.shape(M)[0]


def wos(img):
    # Aquí ya se está pasando la imagen filtrada con el filtro de la mediana
    w = img.shape[0]
    h = img.shape[1]

    aux = np.zeros((w, h, 3))

    for k in range(3):
        for i in range(w):
            for j in range(h):
                delta = []

                for p in range(clases):
                    d = abs(img[i, j, k] - M[p][k])
                    delta.append(d)

                delta_min = min(delta)

                for r in range(clases):
                    if delta[r] == delta_min:
                        aux.itemset((i, j, k), M[r][k])

    return aux


def mdm(img):

    w = img.shape[0]
    h = img.shape[1]

    aux2 = np.zeros((w, h, 3))

    for i in range(w):
        for j in range(h):
            D = []

            for p in range(7):
                d = np.sqrt(
                    pow((img[i, j, 0] - M[p][0]), 2) +
                    pow((img[i, j, 1] - M[p][1]), 2) +
                    pow((img[i, j, 2] - M[p][2]), 2)
                    )
                D.append(d)

            D_min = min(D)

            for r in range(clases):
                if D[r] == D_min:
                    aux2.itemset((i, j, 0), M[r][0])
                    aux2.itemset((i, j, 1), M[r][1])
                    aux2.itemset((i, j, 2), M[r][2])


    return aux2
