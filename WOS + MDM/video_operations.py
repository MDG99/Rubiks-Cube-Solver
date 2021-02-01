import cv2
import numpy

# Parámetros de configuración

# Región del cubo
xi = 100
xf = 439
yi = 20
yf = 455

dif_x = xf - xi
dif_y = yf - yi

salto_x = int(dif_x / 3)
salto_y = int(dif_y / 3)

# Configuración de la cámara
video = cv2.VideoCapture(2)
#video.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#video.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)


def draw_the_frame(image_to_draw, n):

    face = ["Up", "Down", "Right", "Left", "Front", "Back"]

    txt_to_write = f"Cara {face[n]}"

    #Texto
    cv2.putText(image_to_draw, txt_to_write,(500, 61), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

    # Cuadrícula
    cv2.line(image_to_draw, (xi + salto_x, yi), (xi + salto_x, yf), (255, 0, 0), 5)
    cv2.line(image_to_draw, (xi + 2 * salto_x, yi), (xi + 2 * salto_x, yf), (255, 0, 0),  5)
    cv2.line(image_to_draw, (xi, yi + salto_y), (xf, yi + salto_y), (255, 0, 0), 5)
    cv2.line(image_to_draw, (xi, yi + 2 * salto_y), (xf, yi + 2 * salto_y), (255, 0, 0), 5)

    cv2.rectangle(image_to_draw,  # Imagen a dibujar
                  (xi, yi),  # Coordenadas de la esquina superior izquierda
                  (xf, yf),  # Coordenadas de la esquina inferior derecha
                  (0, 0, 0),  # Color del rectángulo
                  thickness=2,  # Grosor del rectángulo
                  lineType=cv2.LINE_8)


def get_the_video(face):

    while True:

        ret, frame = video.read()
        draw_the_frame(frame, face)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            # Obtengo una nueva imagen sin dibujar
            _, frame = video.read()
            # Guardo en variables diferentes cada una de las regiones del cubo

            final_frame = frame[yi:yf, xi:xf]

            # Valores de la primera fila
            a = frame[yi: yi + salto_y, xi: xi + salto_x]
            b = frame[yi: yi + salto_y, xi + salto_x: xi + 2 * salto_x]
            c = frame[yi: yi + salto_y, xi + 2 * salto_x: xf]

            # Valores de la segunda fila
            d = frame[yi + salto_y: yi + 2 * salto_y, xi: xi + salto_x]
            e = frame[yi + salto_y: yi + 2 * salto_y, xi + salto_x: xi + 2 * salto_x]
            f = frame[yi + salto_y: yi + 2 * salto_y, xi + 2 * salto_x: xf]

            # Valores de la tercera fila
            g = frame[yi + 2 * salto_y: yf, xi: xi + salto_x]
            h = frame[yi + 2 * salto_y: yf, xi + salto_x: xi + 2 * salto_x]
            i = frame[yi + 2 * salto_y: yf, xi + 2 * salto_x: xf]


            break

    video.release()
    cv2.destroyAllWindows()

    return a, b, c, d, e, f, g, h, i, final_frame
