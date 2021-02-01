import numpy as np

M = [[35, 131, 169],  # Azul
     [166, 97, 62],  # Roj0
     [64, 159, 96],  # Verde
     [167, 141, 61],  # Naranja
     [158, 166, 78],  # Amarillo
     [153, 162, 154],  # Blanco
     [87, 106, 77]]  # Fondo

M2 = [[53, 180, 183],  # Azul
      [183, 116, 74],  # Roj0
      [84, 180, 112],  # Verde
      [176, 153, 66],  # Naranja
      [163, 169, 72],  # Amarillo
      [153, 164, 156],  # Blanco
      [135, 149, 125]]  # Fondo


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

    aux = np.zeros((w, h, 3))

    for i in range(w):
        for j in range(h):
            D = []

            for p in range(clases):
                d = pow(
                    pow((img[i, j, 0] - M[p][0]), 2) + pow((img[i, j, 1] - M[p][1]), 2) + pow((img[i, j, 2] - M[p][2]),
                                                                                              2), 1 / 2)
                D.append(d)

            D_min = min(D)

            for r in range(clases):
                if D[r] == D_min:
                    aux.itemset((i, j, 0), Mejorado[r][0])
                    aux.itemset((i, j, 1), Mejorado[r][1])
                    aux.itemset((i, j, 2), Mejorado[r][2])


    return aux
