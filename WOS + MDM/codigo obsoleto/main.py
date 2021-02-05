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
    wos_a = wos(a_m, 0)
    wos_b = wos(b_m, 1)
    wos_c = wos(c_m, 2)
    wos_d = wos(d_m, 3)
    wos_e = wos(e_m, 4)
    wos_f = wos(f_m, 5)
    wos_g = wos(g_m, 6)
    wos_h = wos(h_m, 7)
    wos_i = wos(i_m, 8)
    #wos_final = wos(final_m)

    # Aplicando el algoritmo MDM
    mdm_a = mdm(wos_a, 0)
    mdm_b = mdm(wos_b, 1)
    mdm_c = mdm(wos_c, 2)
    mdm_d = mdm(wos_d, 3)
    mdm_e = mdm(wos_e, 4)
    mdm_f = mdm(wos_f, 5)
    mdm_g = mdm(wos_g, 6)
    mdm_h = mdm(wos_h, 7)
    mdm_i = mdm(wos_i, 8)
    #mdm_final = mdm(wos_final)

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
    cv2.imwrite("final_suavizado.jpg", final_m)

    cv2.imwrite("wos_a.jpg", wos_a)
    cv2.imwrite("wos_b.jpg", wos_b)
    cv2.imwrite("wos_c.jpg", wos_c)
    cv2.imwrite("wos_d.jpg", wos_d)
    cv2.imwrite("wos_e.jpg", wos_e)
    cv2.imwrite("wos_f.jpg", wos_f)
    cv2.imwrite("wos_g.jpg", wos_g)
    cv2.imwrite("wos_h.jpg", wos_h)
    cv2.imwrite("wos_i.jpg", wos_i)

    cv2.imwrite("mdm_a.jpg", mdm_a)
    cv2.imwrite("mdm_b.jpg", mdm_b)
    cv2.imwrite("mdm_c.jpg", mdm_c)
    cv2.imwrite("mdm_d.jpg", mdm_d)
    cv2.imwrite("mdm_e.jpg", mdm_e)
    cv2.imwrite("mdm_f.jpg", mdm_f)
    cv2.imwrite("mdm_g.jpg", mdm_g)
    cv2.imwrite("mdm_h.jpg", mdm_h)
    cv2.imwrite("mdm_i.jpg", mdm_i)





lectura_cara(0)
#media_color()



