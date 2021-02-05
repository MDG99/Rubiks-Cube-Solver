from video_operations import get_the_video
from media_aritmetica import media


def valores_M(img, banda_R, banda_G, banda_B):
    aux = media(img)

    banda_R = banda_R + aux[2]
    banda_G = banda_G + aux[1]
    banda_B = banda_B + aux[0]

    return banda_R, banda_G, banda_B

def media_color():
    banda_R = 0
    banda_G = 0
    banda_B = 0

    # Obteniendo el valor medio para cada color
    a, b, c, d, e, f, g, h, i, final = get_the_video(6)

    banda_R, banda_G, banda_B = valores_M(a, banda_R, banda_G, banda_B)



    ##
    #
    # print(round(banda_R))
    #     print(round(banda_G))
    #     print(round(banda_B))
    banda_R, banda_G, banda_B = valores_M(b, banda_R, banda_G, banda_B)
    #     print(round(banda_R/2))
    #     print(round(banda_G/2))
    #     print(round(banda_B/2))
    banda_R, banda_G, banda_B = valores_M(c, banda_R, banda_G, banda_B)
    #     print(round(banda_R/3))
    #     print(round(banda_G/3))
    #     print(round(banda_B/3))
    banda_R, banda_G, banda_B = valores_M(d, banda_R, banda_G, banda_B)
    #     print(round(banda_R/4))
    #     print(round(banda_G/4))
    #     print(round(banda_B/4))
    banda_R, banda_G, banda_B = valores_M(e, banda_R, banda_G, banda_B)
    #     print(round(banda_R/5))
    #     print(round(banda_G/5))
    #     print(round(banda_B/5))
    banda_R, banda_G, banda_B = valores_M(f, banda_R, banda_G, banda_B)
    #     print(round(banda_R/6))
    #     print(round(banda_G/6))
    #     print(round(banda_B/6))
    banda_R, banda_G, banda_B = valores_M(g, banda_R, banda_G, banda_B)
    #     print(round(banda_R/7))
    #     print(round(banda_G/7))
    #     print(round(banda_B/7))
    banda_R, banda_G, banda_B = valores_M(h, banda_R, banda_G, banda_B)
    #     print(round(banda_R/8))
    #     print(round(banda_G/8))
    #     print(round(banda_B/8))
    banda_R, banda_G, banda_B = valores_M(i, banda_R, banda_G, banda_B)
    #
    banda_R = banda_R / 9
    banda_G = banda_G / 9
    banda_B = banda_B / 9

    print(round(banda_R))
    print(round(banda_G))
    print(round(banda_B))
    #
    # ##