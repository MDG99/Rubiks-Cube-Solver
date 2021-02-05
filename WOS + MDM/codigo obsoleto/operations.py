import numpy as np

M = [[80, 206, 244],  # Azul ya
     [246, 83, 20],  # Roj0 ***
     [69, 205, 84],  # Verde pálido
     [242, 129, 20],  # Naranja ya
     [183, 178, 52],  # Amarillo ***
     [203, 219, 213],  # Blanco
     [4, 17, 2]
    ]  # Fondo


M_a = [[90, 218, 233],
       [127, 216, 162],
       [237, 156, 132],
       [213, 184, 123],
       [213, 218, 128],
       [204, 217, 219],
       [120, 149, 129]]

M_b = [[73, 220, 246],
       [136, 242, 173],
       [250, 157, 127],
       [245, 198, 125],
       [245, 239, 135],
       [224, 242, 235],
       [120, 150, 129]]

M_c = [[77, 220, 245],
       [131, 239, 172],
       [236, 159, 127],
       [241, 195, 126],
       [227, 231, 131],
       [224, 239, 229],
       [121, 147, 123]]

M_d = [[114, 225, 245],
       [129, 239, 173],
       [251, 164, 145],
       [246, 192, 134],
       [214, 227, 130],
       [217, 226, 219],
       [124, 151, 131]]

M_e = [[107, 225, 247],
       [128, 245, 175],
       [250, 166, 147],
       [250, 199, 140],
       [237, 239, 135],
       [220, 238, 228],
       [126, 154, 132]]

M_f = [[83, 214, 247],
       [121, 243, 162],
       [249, 152, 125],
       [249, 184, 115],
       [234, 231, 123],
       [216, 227, 219],
       [122, 148, 124]]

M_g = [[52, 185, 249],
       [90, 228, 139],
       [250, 120, 98],
       [244, 155, 90],
       [192, 202, 95],
       [182, 199, 193],
       [106, 134, 114]]

M_h = [[32, 176, 250],
       [79, 221, 125],
       [250, 108, 80],
       [247, 151, 77],
       [185, 200, 88],
       [174, 196, 186],
       [101, 131, 108]]

M_i = [[22, 169, 250],
       [78, 222, 123],
       [250, 106, 73],
       [244, 156, 73],
       [195, 201, 88],
       [179, 196, 186],
       [99, 127, 102]]


Mejorado = [[0, 0, 255],  # Azul
            [0, 255, 0],  # Roj0
            [255, 0, 0],# Verde
            [255, 128, 0],  # Naranja
            [255, 255, 0],  # Amarillo
            [255, 255, 255],  # Blanco
            [0, 0, 0]]  # Fondo


M_Cubo= [M_a, M_b, M_c, M_d, M_e, M_f, M_g, M_h, M_i, M]
clases = np.shape(M)[0]


def wos(img, cara):
    # Aquí ya se está pasando la imagen filtrada con el filtro de la mediana
    w = img.shape[0]
    h = img.shape[1]

    M_local = M_Cubo[cara]

    aux = np.zeros((w, h, 3))

    for k in range(3):
        for i in range(w):
            for j in range(h):
                delta = []

                for p in range(clases):
                    d = abs(img[i, j, k] - M_local[p][k])
                    delta.append(d)

                delta_min = min(delta)

                for r in range(clases):
                    if delta[r] == delta_min:
                        aux.itemset((i, j, k), M_local[r][k])

    return aux


def mdm(img, cara):

    w = img.shape[0]
    h = img.shape[1]

    aux2 = np.zeros((w, h, 3))

    M_local = M_Cubo[cara]
    for i in range(w):
        for j in range(h):
            D = []

            for p in range(7):
                d = np.sqrt(
                    pow((img[i, j, 0] - M_local[p][0]), 2) +
                    pow((img[i, j, 1] - M_local[p][1]), 2) +
                    pow((img[i, j, 2] - M_local[p][2]), 2)
                    )
                D.append(d)

            D_min = min(D)

            for r in range(clases):
                if D[r] == D_min:
                    aux2.itemset((i, j, 0), M_local[r][0])
                    aux2.itemset((i, j, 1), M_local[r][1])
                    aux2.itemset((i, j, 2), M_local[r][2])


    return aux2
