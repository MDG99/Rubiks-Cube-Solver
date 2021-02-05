
from video_operations import get_the_video
from media_aritmetica import media


def valores_M(img):
    aux = media(img)

    banda_R = aux[2]
    banda_G = aux[1]
    banda_B = aux[0]

    return banda_R, banda_G, banda_B

def media_color():

    # Obteniendo el valor medio para cada color
    a, b, c, d, e, f, g, h, i, final = get_the_video(6)

    banda_r, banda_g, banda_b = valores_M(a)
    print("Cara a")
    print(round(banda_r))
    print(round(banda_g))
    print(round(banda_b))
    banda_r, banda_g, banda_b = valores_M(b)
    print("Cara b")
    print(round(banda_r))
    print(round(banda_g))
    print(round(banda_b))
    banda_r, banda_g, banda_b = valores_M(c)
    print("Cara c")
    print(round(banda_r))
    print(round(banda_g))
    print(round(banda_b))
    banda_r, banda_g, banda_b = valores_M(d)
    print("Cara d")
    print(round(banda_r))
    print(round(banda_g))
    print(round(banda_b))
    banda_r, banda_g, banda_b = valores_M(e)
    print("Cara e")
    print(round(banda_r))
    print(round(banda_g))
    print(round(banda_b))
    banda_r, banda_g, banda_b = valores_M(f)
    print("Cara f")
    print(round(banda_r))
    print(round(banda_g))
    print(round(banda_b))
    banda_r, banda_g, banda_b = valores_M(g)
    print("Cara g")
    print(round(banda_r))
    print(round(banda_g))
    print(round(banda_b))
    banda_r, banda_g, banda_b = valores_M(h)
    print("Cara h")
    print(round(banda_r))
    print(round(banda_g))
    print(round(banda_b))
    banda_r, banda_g, banda_b = valores_M(i)
    print("Cara i")
    print(round(banda_r))
    print(round(banda_g))
    print(round(banda_b))


