import cv2
import numpy as np


def ajuste(path, names):
    # Imágenes
    O_rojo = names[0]
    O_verde = names[1]
    O_azul = names[2]
    O_amarillo = names[3]
    O_naranja = names[4]
    O_blanco = names[5]

    # Lectura
    img_r = cv2.imread(path + O_rojo)
    img_g = cv2.imread(path + O_verde)
    img_b = cv2.imread(path + O_azul)
    img_y = cv2.imread(path + O_amarillo)
    img_o = cv2.imread(path + O_naranja)
    img_w = cv2.imread(path + O_blanco)

    # Escalado
    img_r = cv2.resize(img_r, (0, 0), fx=0.10, fy=0.10)
    img_g = cv2.resize(img_g, (0, 0), fx=0.10, fy=0.10)
    img_b = cv2.resize(img_b, (0, 0), fx=0.10, fy=0.10)
    img_y = cv2.resize(img_y, (0, 0), fx=0.10, fy=0.10)
    img_o = cv2.resize(img_o, (0, 0), fx=0.10, fy=0.10)
    img_w = cv2.resize(img_w, (0, 0), fx=0.10, fy=0.10)

    # Recorte
    img_r = img_r[70:403, 0:321]
    img_g = img_g[70:403, 0:321]
    img_b = img_b[70:403, 0:321]
    img_y = img_y[70:403, 0:321]
    img_o = img_o[70:403, 0:321]
    img_w = img_w[70:403, 0:321]

    # Guardando
    cv2.imwrite(path + "img_r.jpg", img_r)
    cv2.imwrite(path + "img_g.jpg", img_g)
    cv2.imwrite(path + "img_b.jpg", img_b)
    cv2.imwrite(path + "img_y.jpg", img_y)
    cv2.imwrite(path + "img_o.jpg", img_o)
    cv2.imwrite(path + "img_w.jpg", img_w)

    # Obteniendo la media por cada color
    media_color(cv2.imread(path + "img_r.jpg"), "Rojo")
    media_color(cv2.imread(path + "img_g.jpg"), "Verde")
    media_color(cv2.imread(path + "img_b.jpg"), "Azul")
    media_color(cv2.imread(path + "img_y.jpg"), "Amarillo")
    media_color(cv2.imread(path + "img_o.jpg"), "Naranja")
    media_color(cv2.imread(path + "img_w.jpg"), "Blanco")


def ajuste_cubo(path, nombre, n_aux, n):
    # Lectura
    img = cv2.imread(path + nombre)
    # Escalado
    img = cv2.resize(img, (0, 0), fx=0.10, fy=0.10)
    # Recorte
    img = img[70:403, 0:321]
    # Guardando
    cv2.imwrite(path + f"{n_aux}_{n}.jpg", img)


def division_cubo(img):
    xi = 0
    xf = 321
    yi = 0
    yf = 333

    salto_x = int((xf - xi) / 3)
    salto_y = int((yf - yi) / 3)

    # Valores de la primera fila
    a = img[yi: yi + salto_y, xi: xi + salto_x]
    b = img[yi: yi + salto_y, xi + salto_x: xi + 2 * salto_x]
    c = img[yi: yi + salto_y, xi + 2 * salto_x: xf]

    # Valores de la segunda fila
    d = img[yi + salto_y: yi + 2 * salto_y, xi: xi + salto_x]
    e = img[yi + salto_y: yi + 2 * salto_y, xi + salto_x: xi + 2 * salto_x]
    f = img[yi + salto_y: yi + 2 * salto_y, xi + 2 * salto_x: xf]

    # Valores de la tercera fila
    g = img[yi + 2 * salto_y: yf, xi: xi + salto_x]
    h = img[yi + 2 * salto_y: yf, xi + salto_x: xi + 2 * salto_x]
    i = img[yi + 2 * salto_y: yf, xi + 2 * salto_x: xf]
    return a, b, c, d, e, f, g, h, i


def media(img):
    w = img.shape[0]
    h = img.shape[1]

    pixel_quantity = w * h

    aux = np.zeros(3)
    for k in range(3):
        for i in range(w):
            for j in range(h):
                aux[k] = aux[k] + img[i, j, k]

        aux[k] = aux[k] / pixel_quantity

    return aux


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


def media(img):
    w = img.shape[0]
    h = img.shape[1]

    aux = np.zeros((w, h, 3))
    for k in range(3):
        for i in range(1, w - 1):
            for j in range(1, h - 1):
                mask = [(1/9)*img[i - 1, j - 1, k], (1/9)*img[i - 1, j, k], (1/9)*img[i - 1, j + 1, k],
                        (1/9)*img[i, j - 1, k], (1/9)*img[i, j, k],
                        (1/9)*img[i, j + 1, k], (1/9)*img[i + 1, j - 1, k], (1/9)*img[i + 1, j, k],
                        (1/9)*img[i + 1, j + 1, k]]
                my_mean = np.sum(mask)
                aux.itemset((i, j, k), my_mean)

    return aux


def valores_M(img, banda_R, banda_G, banda_B):
    aux = media(img)

    banda_R = banda_R + aux[2]
    banda_G = banda_G + aux[1]
    banda_B = banda_B + aux[0]

    return banda_R, banda_G, banda_B


def media_color(img, color):

    banda_r = 0
    banda_g = 0
    banda_b = 0

    # Obteniendo el valor medio para cada color
    a, b, c, d, e, f, g, h, i = division_cubo(img)

    banda_r, banda_g, banda_b = valores_M(a, banda_r, banda_g, banda_b)
    banda_r, banda_g, banda_b = valores_M(b, banda_r, banda_g, banda_b)
    banda_r, banda_g, banda_b = valores_M(c, banda_r, banda_g, banda_b)
    banda_r, banda_g, banda_b = valores_M(d, banda_r, banda_g, banda_b)
    banda_r, banda_g, banda_b = valores_M(e, banda_r, banda_g, banda_b)
    banda_r, banda_g, banda_b = valores_M(f, banda_r, banda_g, banda_b)
    banda_r, banda_g, banda_b = valores_M(g, banda_r, banda_g, banda_b)
    banda_r, banda_g, banda_b = valores_M(h, banda_r, banda_g, banda_b)
    banda_r, banda_g, banda_b = valores_M(i, banda_r, banda_g, banda_b)

    banda_r = banda_r / 9
    banda_g = banda_g / 9
    banda_b = banda_b / 9

    print(color)
    print(round(banda_r))
    print(round(banda_g))
    print(round(banda_b))


def wos(img, M):
    # Aquí ya se está pasando la imagen filtrada con el filtro de la mediana
    w = img.shape[0]
    h = img.shape[1]

    aux = np.zeros((w, h, 3))

    for k in range(3):
        for i in range(w):
            for j in range(h):
                delta = []

                for p in range(6):
                    d = abs(img[i, j, k] - M[p][k])
                    delta.append(d)

                delta_min = min(delta)

                for r in range(6):
                    if delta[r] == delta_min:
                        aux.itemset((i, j, k), M[r][k])

    return aux


def mdm(img, M):
    Mejorado = [[255, 0, 0],  # Roj0
                [0, 255, 0],  # Verde
                [0, 0, 255],  # Azul
                [255, 255, 0],  # Amarillo
                [255, 128, 0],  # Naranja
                [255, 255, 255]]  # Blanco

    w = img.shape[0]
    h = img.shape[1]

    aux2 = np.zeros((w, h, 3))

    for i in range(w):
        for j in range(h):
            D = []

            for p in range(6):
                d = np.sqrt(
                    pow((img[i, j, 0] - M[p][0]), 2) +
                    pow((img[i, j, 1] - M[p][1]), 2) +
                    pow((img[i, j, 2] - M[p][2]), 2)
                    )
                D.append(d)

            D_min = min(D)

            for r in range(6):
                if D[r] == D_min:
                    aux2.itemset((i, j, 0), M[r][0])
                    aux2.itemset((i, j, 1), M[r][1])
                    aux2.itemset((i, j, 2), M[r][2])


    return aux2



