from image_operations import *

M = [[202, 79, 97],  # Rojo
     [90, 181, 73],  # Verde
     [49, 120, 189],  # Azul
     [168, 166, 56],  # Amarillo
     [196, 132, 93],  # Naranja
     [162, 164, 162]]  # Blanco


# Etapa de calibración
# Pre-procesamiento
def calibracion():
    ruta = "/home/mdg99/Escritorio/PDS_FinalProject/Rubiks-Cube-Solver/WOS + MDM/Imágenes/calibracion/"
    imagenes = ["ORIGINAL_ROJO.jpg",
                "ORIGINAL_VERDE.jpg",
                "ORIGINAL_AZUL.jpg",
                "ORIGINAL_AMARILLO.jpg",
                "ORIGINAL_NARANJA.jpg",
                "ORIGINAL_BLANCO.jpg"]

    ajuste(ruta, imagenes)


def ajuste_inicial_cubo(directorio, nombre):
    ruta = f"/home/mdg99/Escritorio/PDS_FinalProject/Rubiks-Cube-Solver/WOS + MDM/Imágenes/{directorio}/"
    imagenes = [f"{nombre}_cara1.jpg",
                f"{nombre}_cara2.jpg",
                f"{nombre}_cara3.jpg",
                f"{nombre}_cara4.jpg",
                f"{nombre}_cara5.jpg",
                f"{nombre}_cara6.jpg"]

    ajuste_cubo(ruta, imagenes[0], nombre, 1)
    ajuste_cubo(ruta, imagenes[1], nombre, 2)
    ajuste_cubo(ruta, imagenes[2], nombre, 3)
    ajuste_cubo(ruta, imagenes[3], nombre, 4)
    ajuste_cubo(ruta, imagenes[4], nombre, 5)
    ajuste_cubo(ruta, imagenes[5], nombre, 6)


def mediana_cubo(directorio, nombre):
    ruta = f"/home/mdg99/Escritorio/PDS_FinalProject/Rubiks-Cube-Solver/WOS + MDM/Imágenes/{directorio}/"
    imagenes = [f"{nombre}_1.jpg",
                f"{nombre}_2.jpg",
                f"{nombre}_3.jpg",
                f"{nombre}_4.jpg",
                f"{nombre}_5.jpg",
                f"{nombre}_6.jpg"]

    m_cara1 = mediana(cv2.imread(ruta + imagenes[0]))
    m_cara2 = mediana(cv2.imread(ruta + imagenes[1]))
    m_cara3 = mediana(cv2.imread(ruta + imagenes[2]))
    m_cara4 = mediana(cv2.imread(ruta + imagenes[3]))
    m_cara5 = mediana(cv2.imread(ruta + imagenes[4]))
    m_cara6 = mediana(cv2.imread(ruta + imagenes[5]))

    cv2.imwrite("m_cara1.jpg", m_cara1)
    cv2.imwrite("m_cara2.jpg", m_cara2)
    cv2.imwrite("m_cara3.jpg", m_cara3)
    cv2.imwrite("m_cara4.jpg", m_cara4)
    cv2.imwrite("m_cara5.jpg", m_cara5)
    cv2.imwrite("m_cara6.jpg", m_cara6)

    return m_cara1, m_cara2, m_cara3, m_cara4, m_cara5, m_cara6


def wos_cubo(caras_cubo, matriz):

    wos_cara1 = wos(caras_cubo[0], matriz)
    wos_cara2 = wos(caras_cubo[1], matriz)
    wos_cara3 = wos(caras_cubo[2], matriz)
    wos_cara4 = wos(caras_cubo[3], matriz)
    wos_cara5 = wos(caras_cubo[4], matriz)
    wos_cara6 = wos(caras_cubo[5], matriz)

    cv2.imwrite("wos_cara1.jpg", wos_cara1)
    cv2.imwrite("wos_cara2.jpg", wos_cara2)
    cv2.imwrite("wos_cara3.jpg", wos_cara3)
    cv2.imwrite("wos_cara4.jpg", wos_cara4)
    cv2.imwrite("wos_cara5.jpg", wos_cara5)
    cv2.imwrite("wos_cara6.jpg", wos_cara6)

    return wos_cara1, wos_cara2, wos_cara3, wos_cara4, wos_cara5, wos_cara6


def mdm_cubo(caras_cubo, matriz):

    mdm_cara1 = mdm(caras_cubo[0], matriz)
    mdm_cara2 = mdm(caras_cubo[1], matriz)
    mdm_cara3 = mdm(caras_cubo[2], matriz)
    mdm_cara4 = mdm(caras_cubo[3], matriz)
    mdm_cara5 = mdm(caras_cubo[4], matriz)
    mdm_cara6 = mdm(caras_cubo[5], matriz)

    cv2.imwrite("mdm_cara1.jpg", mdm_cara1)
    cv2.imwrite("mdm_cara2.jpg", mdm_cara2)
    cv2.imwrite("mdm_cara3.jpg", mdm_cara3)
    cv2.imwrite("mdm_cara4.jpg", mdm_cara4)
    cv2.imwrite("mdm_cara5.jpg", mdm_cara5)
    cv2.imwrite("mdm_cara6.jpg", mdm_cara6)

    return mdm_cara1, mdm_cara2, mdm_cara3, mdm_cara4, mdm_cara5, mdm_cara6


# Ajustes iniciales
#calibracion()
ajuste_inicial_cubo("cubo 1", "cubo_01")

# Mediana
m_cara1, m_cara2, m_cara3, m_cara4, m_cara5, m_cara6 = mediana_cubo("cubo 1", "cubo_01")
cubo = [m_cara1, m_cara2, m_cara3, m_cara4, m_cara5, m_cara6]

# WOS
wos_cara1, wos_cara2, wos_cara3, wos_cara4, wos_cara5, wos_cara6 = wos_cubo(cubo, M)
cubo_wos = [wos_cara1, wos_cara2, wos_cara3, wos_cara4, wos_cara5, wos_cara6]

# MDM
mdm_cara1, mdm_cara2, mdm_cara3, mdm_cara4, mdm_cara5, mdm_cara6 = mdm_cubo(cubo_wos, M)
cubo_mdm = [mdm_cara1, mdm_cara2, mdm_cara3, mdm_cara4, mdm_cara5, mdm_cara6]