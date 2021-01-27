import cv2
import numpy as np
from video_operations import get_the_video
from filtro import mediana

a, b, c, d, e, f, g, h, i = get_the_video(1)


a_m = mediana(a)

cv2.imwrite("a.jpg", a)
cv2.imwrite("a_suavizado.jpg", a_m)

# cv2.imwrite("b.jpg", cara_1[1])
# cv2.imwrite("c.jpg", cara_1[2])
# cv2.imwrite("d.jpg", cara_1[3])
# cv2.imwrite("e.jpg", cara_1[4])
# cv2.imwrite("f.jpg", cara_1[5])
# cv2.imwrite("g.jpg", cara_1[6])
# cv2.imwrite("h.jpg", cara_1[7])
# cv2.imwrite("i.jpg", cara_1[8])
