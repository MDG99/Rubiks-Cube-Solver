import cv2
from video_operations import get_the_video
from filtro import mediana
from operations import wos, mdm
from mapeo_colores import mapeo
from normalizar import normalizar
from prueba import media_color

def lectura_cara(n):

    a, b, c, d, e, f, g, h, i, final = get_the_video(n)

    mis_colores = []

    # Calculando la mediana de cada cuadrado
    a_m = mediana(a)
    b_m = mediana(b)
    c_m = mediana(c)
    d_m = mediana(d)
    e_m = mediana(e)
    f_m = mediana(f)
    g_m = mediana(g)
    h_m = mediana(h)
    i_m = mediana(i)
    final_m = mediana(final)

    # Aplicando el algoritmo WOS
    wos_a = wos(a_m)
    wos_b = wos(b_m)
    wos_c = wos(c_m)
    wos_d = wos(d_m)
    wos_e = wos(e_m)
    wos_f = wos(f_m)
    wos_g = wos(g_m)
    wos_h = wos(h_m)
    wos_i = wos(i_m)
    wos_final = wos(final_m)

    # Aplicando el algoritmo MDM
    mdm_a = mdm(wos_a)
    mdm_b = mdm(wos_b)
    mdm_c = mdm(wos_c)
    mdm_d = mdm(wos_d)
    mdm_e = mdm(wos_e)
    mdm_f = mdm(wos_f)
    mdm_g = mdm(wos_g)
    mdm_h = mdm(wos_h)
    mdm_i = mdm(wos_i)
    mdm_final = mdm(wos_final)

    mis_colores.append(mapeo(mdm_a))
    mis_colores.append(mapeo(mdm_b))
    mis_colores.append(mapeo(mdm_c))
    mis_colores.append(mapeo(mdm_d))
    mis_colores.append(mapeo(mdm_e))
    mis_colores.append(mapeo(mdm_f))
    mis_colores.append(mapeo(mdm_g))
    mis_colores.append(mapeo(mdm_h))
    mis_colores.append(mapeo(mdm_i))

    print(mis_colores)
    cv2.imwrite("a.jpg", a)
    #cv2.imwrite("a_suavizado.jpg", a_m)

    cv2.imwrite("wos_a.jpg", wos_a)
    cv2.imwrite("mdm_a.jpg", mdm_a)
    cv2.imwrite("wos_final.jpg", wos_final)
    cv2.imwrite("mdm_final.jpg", mdm_final)



lectura_cara(0)
#media_color()



