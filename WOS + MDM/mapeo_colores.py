import numpy as np

M = [[4, 52, 81],  # Azul ya
     [198, 51, 3],  # Roj0 ***
     [39, 169, 43],  # Verde pálido
     [228, 109, 6],  # Naranja ya
     [153, 163, 30],  # Amarillo ***
     [147, 165, 120],  # Blanco
     [27, 55, 17]
    ]  # Fondo



def mapeo(img):
    w = np.shape(img)[0]
    h = np.shape(img)[1]

    contador = np.zeros(7)

    for i in range(w):
        for j in range(h):

            if img[i, j, 2] == M[0][0] and img[i, j, 1] == M[0][1] and img[i, j, 0] == M[0][2]:
                contador[0] = contador[0] + 1

            if img[i, j, 2] == M[1][0] and img[i, j, 1] == M[1][1] and img[i, j, 0] == M[1][2]:
                contador[1] = contador[1] + 1

            if img[i, j, 2] == M[2][0] and img[i, j, 1] == M[2][1] and img[i, j, 0] == M[2][2]:
                contador[2] = contador[2] + 1

            if img[i, j, 2] == M[3][0] and img[i, j, 1] == M[3][1] and img[i, j, 0] == M[3][2]:
                contador[3] = contador[3] + 1

            if img[i, j, 2] == M[4][0] and img[i, j, 1] == M[4][1] and img[i, j, 0] == M[4][2]:
                contador[4] = contador[4] + 1

            if img[i, j, 2] == M[5][0] and img[i, j, 1] == M[5][1] and img[i, j, 0] == M[5][2]:
                contador[5] = contador[5] + 1

            if img[i, j, 2] == M[6][0] and img[i, j, 1] == M[6][1] and img[i, j, 0] == M[6][2]:
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
