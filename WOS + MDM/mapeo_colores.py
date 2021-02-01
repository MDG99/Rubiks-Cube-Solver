import numpy as np

Mejorado = [[0, 0, 255],  # Azul
            [255, 0, 0],  # Rojo
            [0, 255, 0],  # Verde
            [255, 128, 0],  # Naranja
            [255, 255, 0],  # Amarillo
            [255, 255, 255],  # Blanco
            [0, 0, 0]]  # Fondo


def mapeo(img):
    w = np.shape(img)[0]
    h = np.shape(img)[1]

    contador = np.zeros(7)

    for i in range(w):
        for j in range(h):

            if img[i, j, 2] == Mejorado[0][0] and img[i, j, 1] == Mejorado[0][1] and img[i, j, 0] == Mejorado[0][2]:
                contador[0] = contador[0] + 1

            if img[i, j, 2] == Mejorado[1][0] and img[i, j, 1] == Mejorado[1][1] and img[i, j, 0] == Mejorado[1][2]:
                contador[1] = contador[1] + 1

            if img[i, j, 2] == Mejorado[2][0] and img[i, j, 1] == Mejorado[2][1] and img[i, j, 0] == Mejorado[2][2]:
                contador[2] = contador[2] + 1

            if img[i, j, 2] == Mejorado[3][0] and img[i, j, 1] == Mejorado[3][1] and img[i, j, 0] == Mejorado[3][2]:
                contador[3] = contador[3] + 1

            if img[i, j, 2] == Mejorado[4][0] and img[i, j, 1] == Mejorado[4][1] and img[i, j, 0] == Mejorado[4][2]:
                contador[4] = contador[4] + 1

            if img[i, j, 2] == Mejorado[5][0] and img[i, j, 1] == Mejorado[5][1] and img[i, j, 0] == Mejorado[5][2]:
                contador[5] = contador[5] + 1

            if img[i, j, 2] == Mejorado[6][0] and img[i, j, 1] == Mejorado[6][1] and img[i, j, 0] == Mejorado[6][2]:
                contador[6] = 1

    moda = max(contador)
    indice = 0

    for i in range(7):
        if contador[i] == moda:
            indice = i

    if indice == 0:
        return 'B'
    if indice == 1:
        return 'R'
    if indice == 2:
        return 'G'
    if indice == 3:
        return 'O'
    if indice == 4:
        return 'Y'
    if indice == 5:
        return 'W'
    if indice == 6:
        return 'k'
