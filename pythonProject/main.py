# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Tupla:
    # Arreglo de colores
    color = []
    # Arreglo de orientaciones
    orien = []

    def __init__(self, numTuplas):
        self.color = ["" for x in range(numTuplas)]
        self.orien = ["" for x in range(numTuplas)]


# 1 color y orientación para piezas centrales
class Central:
    def __init__(self):
        self.tupla = Tupla(1)


# 2 colores y 2 orientaciones para piezas laterales
class Lateral:
    def __init__(self):
        self.tupla = Tupla(2)


# 3 colores y 3 orientaciones para piezas laterales
class Esquina:
    def __init__(self):
        self.tupla = Tupla(3)


class Piezas:
    pieza_central = []
    pieza_lateral = []
    pieza_esquina = []

    def __init__(self):
        # self.pieza_central = [6]
        for i in range(0, 6):
            self.pieza_central.append(Central())

        # self.pieza_lateral = [12]
        for i in range(0, 12):
            self.pieza_lateral.append(Lateral())

        # self.pieza_esquina = [8]
        for i in range(0, 8):
            self.pieza_esquina.append(Esquina())

    def quienCentral(self, orient):
        esta = False
        color = " "
        i = 0
        while i < len(self.pieza_central) and not esta:
            j = 0
            while j < len(self.pieza_central[i].tupla.orien) and not esta:
                if self.pieza_central[i].tupla.orien[j] == orient:
                    esta = True
                    color = self.pieza_central[i].tupla.color[j]
                else:
                    j = j + 1
            i = i + 1
        return color

    def quienLateral(self, orient1, orient2, orientColor):
        esta = pos1 = pos2 = False
        i = 0
        color = " "
        while i < len(self.pieza_lateral) and not esta:
            j = 0
            while j < len(self.pieza_lateral[i].tupla.orien) and not pos1:
                if self.pieza_lateral[i].tupla.orien[j] == orient1:
                    pos1 = True
                else:
                    j = j + 1
            k = 0
            while k < len(self.pieza_lateral[i].tupla.orien) and not pos2:
                if self.pieza_lateral[i].tupla.orien[k] == orient2:
                    pos2 = True
                else:
                    k = k + 1
            if pos1 and pos2:
                if orient1 == orientColor:
                    color = self.pieza_lateral[i].tupla.color[j]
                else:
                    color = self.pieza_lateral[i].tupla.color[k]
                esta = True
            else:
                pos1 = False
                pos2 = False
                i = i + 1
        return color

    def quienEsquina(self, orient1, orient2, orient3, orientColor):
        esta = pos1 = pos2 = pos3 = False
        i = 0
        color = " "
        while i < len(self.pieza_esquina) and not esta:
            j = 0
            while j < len(self.pieza_esquina[i].tupla.orien) and not pos1:
                if self.pieza_esquina[i].tupla.orien[j] == orient1:
                    pos1 = True
                else:
                    j = j + 1
            k = 0
            while k < len(self.pieza_esquina[i].tupla.orien) and not pos2:
                if self.pieza_esquina[i].tupla.orien[k] == orient2:
                    pos2 = True
                else:
                    k = k + 1
            ll = 0
            while ll < len(self.pieza_esquina[i].tupla.orien) and not pos3:
                if self.pieza_esquina[i].tupla.orien[ll] == orient3:
                    pos3 = True
                else:
                    ll = ll + 1
            if pos1 and pos2 and pos3:
                if orient1 == orientColor:
                    color = self.pieza_esquina[i].tupla.color[j]
                elif orient2 == orientColor:
                    color = self.pieza_esquina[i].tupla.color[k]
                else:
                    color = self.pieza_esquina[i].tupla.color[ll]
                esta = True
            else:
                pos1 = False
                pos2 = False
                pos3 = False
                i = i + 1
        return color

    def imprimePieza(self):
        print(
            "    " + Piezas.quienEsquina(self, "U", "L", "B", "U") + Piezas.quienLateral(self, "U", "B", "U") +
            Piezas.quienEsquina(self, "U", "R", "B", "U"))
        print(
            "    " + Piezas.quienLateral(self, "U", "L", "U") + Piezas.quienCentral(self, "U") + Piezas.quienLateral(
                self, "U", "R", "U"))
        print(
            "    " + Piezas.quienEsquina(self, "U", "F", "L", "U") + Piezas.quienLateral(self, "U", "F", "U") +
            Piezas.quienEsquina(self, "U", "F", "R", "U"))
        print(
            "" + Piezas.quienEsquina(self, "L", "U", "B", "L") + Piezas.quienLateral(self, "L", "U", "L") +
            Piezas.quienEsquina(self, "L", "U", "F", "L") + " " + Piezas.quienEsquina(self, "F", "U", "L", "F") +
            Piezas.quienLateral(self, "F", "U", "F") + Piezas.quienEsquina(self, "F", "U", "R", "F") + " " +
            Piezas.quienEsquina(self, "F", "U", "R", "R") + Piezas.quienLateral(self, "R", "U", "R") +
            Piezas.quienEsquina(self, "R", "U", "B", "R") + " " + Piezas.quienEsquina(self, "B", "U", "R", "B") +
            Piezas.quienLateral(self, "B", "U", "B") + Piezas.quienEsquina(self, "B", "U", "L", "B"))
        print(
            "" + Piezas.quienLateral(self, "L", "B", "L") + Piezas.quienCentral(self, "L") + Piezas.quienLateral(
                self, "L", "F", "L") + " " + Piezas.quienLateral(self, "L", "F", "F") + Piezas.quienCentral(self, "F") +
            Piezas.quienLateral(self, "F", "R", "F") + " " + Piezas.quienLateral(self, "F", "R", "R") +
            Piezas.quienCentral(self, "R") + Piezas.quienLateral(self, "R", "B", "R") + " " +
            Piezas.quienLateral(self, "R", "B", "B") + Piezas.quienCentral(self, "B") +
            Piezas.quienLateral(self, "L", "B", "B") + " ")
        print(
            "" + Piezas.quienEsquina(self, "L", "D", "B", "L") + Piezas.quienLateral(self, "L", "D", "L") +
            Piezas.quienEsquina(self, "L", "D", "F", "L") + " " + Piezas.quienEsquina(self, "F", "D", "L", "F") +
            Piezas.quienLateral(self, "F", "D", "F") + Piezas.quienEsquina(self, "F", "D", "R", "F") + " " +
            Piezas.quienEsquina(self, "F", "D", "R", "R") + Piezas.quienLateral(self, "R", "D", "R") +
            Piezas.quienEsquina(self, "R", "D", "B", "R") + " " + Piezas.quienEsquina(self, "B", "D", "R", "B") +
            Piezas.quienLateral(self, "B", "D", "B") + Piezas.quienEsquina(self, "B", "D", "L", "B") + " ")
        print(
            "    " + Piezas.quienEsquina(self, "D", "L", "F", "D") + Piezas.quienLateral(self, "D", "F", "D") +
            Piezas.quienEsquina(self, "D", "F", "R", "D"))
        print(
            "    " + Piezas.quienLateral(self, "D", "L", "D") + Piezas.quienCentral(self, "D") + Piezas.quienLateral(
                self, "D", "R", "D"))
        print(
            "    " + Piezas.quienEsquina(self, "D", "L", "B", "D") + Piezas.quienLateral(self, "D", "B", "D") +
            Piezas.quienEsquina(self, "D", "R", "B", "D"))
        print("\n")

    def iniciaPiezas(self):
        # Piezas centrales:
        self.pieza_central[0].tupla.color[0] = "B"
        self.pieza_central[0].tupla.orien[0] = "R"
        self.pieza_central[1].tupla.color[0] = "Y"
        self.pieza_central[1].tupla.orien[0] = "F"
        self.pieza_central[2].tupla.color[0] = "R"
        self.pieza_central[2].tupla.orien[0] = "U"
        self.pieza_central[3].tupla.color[0] = "G"
        self.pieza_central[3].tupla.orien[0] = "L"
        self.pieza_central[4].tupla.color[0] = "O"
        self.pieza_central[4].tupla.orien[0] = "D"
        self.pieza_central[5].tupla.color[0] = "W"
        self.pieza_central[5].tupla.orien[0] = "B"
        # Piezas laterales:
        self.pieza_lateral[0].tupla.color[0] = "R"
        self.pieza_lateral[0].tupla.orien[0] = "U"
        self.pieza_lateral[0].tupla.color[1] = "Y"
        self.pieza_lateral[0].tupla.orien[1] = "F"
        self.pieza_lateral[1].tupla.color[0] = "B"
        self.pieza_lateral[1].tupla.orien[0] = "R"
        self.pieza_lateral[1].tupla.color[1] = "Y"
        self.pieza_lateral[1].tupla.orien[1] = "F"
        self.pieza_lateral[2].tupla.color[0] = "O"
        self.pieza_lateral[2].tupla.orien[0] = "D"
        self.pieza_lateral[2].tupla.color[1] = "Y"
        self.pieza_lateral[2].tupla.orien[1] = "F"
        self.pieza_lateral[3].tupla.color[0] = "G"
        self.pieza_lateral[3].tupla.orien[0] = "L"
        self.pieza_lateral[3].tupla.color[1] = "Y"
        self.pieza_lateral[3].tupla.orien[1] = "F"
        self.pieza_lateral[4].tupla.color[0] = "R"
        self.pieza_lateral[4].tupla.orien[0] = "U"
        self.pieza_lateral[4].tupla.color[1] = "B"
        self.pieza_lateral[4].tupla.orien[1] = "R"
        self.pieza_lateral[5].tupla.color[0] = "R"
        self.pieza_lateral[5].tupla.orien[0] = "U"
        self.pieza_lateral[5].tupla.color[1] = "G"
        self.pieza_lateral[5].tupla.orien[1] = "L"
        self.pieza_lateral[6].tupla.color[0] = "O"
        self.pieza_lateral[6].tupla.orien[0] = "D"
        self.pieza_lateral[6].tupla.color[1] = "B"
        self.pieza_lateral[6].tupla.orien[1] = "R"
        self.pieza_lateral[7].tupla.color[0] = "O"
        self.pieza_lateral[7].tupla.orien[0] = "D"
        self.pieza_lateral[7].tupla.color[1] = "G"
        self.pieza_lateral[7].tupla.orien[1] = "L"
        self.pieza_lateral[8].tupla.color[0] = "R"
        self.pieza_lateral[8].tupla.orien[0] = "U"
        self.pieza_lateral[8].tupla.color[1] = "W"
        self.pieza_lateral[8].tupla.orien[1] = "B"
        self.pieza_lateral[9].tupla.color[0] = "G"
        self.pieza_lateral[9].tupla.orien[0] = "L"
        self.pieza_lateral[9].tupla.color[1] = "W"
        self.pieza_lateral[9].tupla.orien[1] = "B"
        self.pieza_lateral[10].tupla.color[0] = "B"
        self.pieza_lateral[10].tupla.orien[0] = "R"
        self.pieza_lateral[10].tupla.color[1] = "W"
        self.pieza_lateral[10].tupla.orien[1] = "B"
        self.pieza_lateral[11].tupla.color[0] = "O"
        self.pieza_lateral[11].tupla.orien[0] = "D"
        self.pieza_lateral[11].tupla.color[1] = "W"
        self.pieza_lateral[11].tupla.orien[1] = "B"
        # Piezas de esquina:
        self.pieza_esquina[0].tupla.color[0] = "R"
        self.pieza_esquina[0].tupla.orien[0] = "U"
        self.pieza_esquina[0].tupla.color[1] = "Y"
        self.pieza_esquina[0].tupla.orien[1] = "F"
        self.pieza_esquina[0].tupla.color[2] = "B"
        self.pieza_esquina[0].tupla.orien[2] = "R"
        self.pieza_esquina[1].tupla.color[0] = "R"
        self.pieza_esquina[1].tupla.orien[0] = "U"
        self.pieza_esquina[1].tupla.color[1] = "Y"
        self.pieza_esquina[1].tupla.orien[1] = "F"
        self.pieza_esquina[1].tupla.color[2] = "G"
        self.pieza_esquina[1].tupla.orien[2] = "L"
        self.pieza_esquina[2].tupla.color[0] = "O"
        self.pieza_esquina[2].tupla.orien[0] = "D"
        self.pieza_esquina[2].tupla.color[1] = "Y"
        self.pieza_esquina[2].tupla.orien[1] = "F"
        self.pieza_esquina[2].tupla.color[2] = "B"
        self.pieza_esquina[2].tupla.orien[2] = "R"
        self.pieza_esquina[3].tupla.color[0] = "O"
        self.pieza_esquina[3].tupla.orien[0] = "D"
        self.pieza_esquina[3].tupla.color[1] = "Y"
        self.pieza_esquina[3].tupla.orien[1] = "F"
        self.pieza_esquina[3].tupla.color[2] = "G"
        self.pieza_esquina[3].tupla.orien[2] = "L"
        self.pieza_esquina[4].tupla.color[0] = "R"
        self.pieza_esquina[4].tupla.orien[0] = "U"
        self.pieza_esquina[4].tupla.color[1] = "B"
        self.pieza_esquina[4].tupla.orien[1] = "R"
        self.pieza_esquina[4].tupla.color[2] = "W"
        self.pieza_esquina[4].tupla.orien[2] = "B"
        self.pieza_esquina[5].tupla.color[0] = "R"
        self.pieza_esquina[5].tupla.orien[0] = "U"
        self.pieza_esquina[5].tupla.color[1] = "G"
        self.pieza_esquina[5].tupla.orien[1] = "L"
        self.pieza_esquina[5].tupla.color[2] = "W"
        self.pieza_esquina[5].tupla.orien[2] = "B"
        self.pieza_esquina[6].tupla.color[0] = "O"
        self.pieza_esquina[6].tupla.orien[0] = "D"
        self.pieza_esquina[6].tupla.color[1] = "B"
        self.pieza_esquina[6].tupla.orien[1] = "R"
        self.pieza_esquina[6].tupla.color[2] = "W"
        self.pieza_esquina[6].tupla.orien[2] = "B"
        self.pieza_esquina[7].tupla.color[0] = "O"
        self.pieza_esquina[7].tupla.orien[0] = "D"
        self.pieza_esquina[7].tupla.color[1] = "G"
        self.pieza_esquina[7].tupla.orien[1] = "L"
        self.pieza_esquina[7].tupla.color[2] = "W"
        self.pieza_esquina[7].tupla.orien[2] = "B"

    def movHorizontal(self, cara, signo):
        # signo = 0 --> giro con las manecillas del reloj
        # signo = 1 --> giro contra las manecillas del reloj
        movsH = ["F", "L", "B", "R"]
        for i in range(0, len(self.pieza_lateral)):
            for j in range(0, len(self.pieza_lateral[i].tupla.orien)):
                if self.pieza_lateral[i].tupla.orien[j] == cara:
                    for k in range(0, len(self.pieza_lateral[i].tupla.orien)):
                        if self.pieza_lateral[i].tupla.orien[k] != cara:
                            caraActual = self.pieza_lateral[i].tupla.orien[k]
                            caraNueva = 0
                            while caraActual != movsH[caraNueva]:
                                caraNueva = caraNueva + 1
                            if signo == 0:
                                caraNueva = caraNueva + 1
                            else:
                                caraNueva = caraNueva - 1
                            if caraNueva < 0:
                                caraNueva = 3
                            else:
                                if caraNueva > 3:
                                    caraNueva = 0
                            self.pieza_lateral[i].tupla.orien[k] = movsH[caraNueva]
        for i in range(0, len(self.pieza_esquina)):
            for j in range(0, len(self.pieza_esquina[i].tupla.orien)):
                if self.pieza_esquina[i].tupla.orien[j] == cara:
                    for k in range(0, len(self.pieza_esquina[i].tupla.orien)):
                        if self.pieza_esquina[i].tupla.orien[k] != cara:
                            caraActual = self.pieza_esquina[i].tupla.orien[k]
                            caraNueva = 0
                            while caraActual != movsH[caraNueva]:
                                caraNueva = caraNueva + 1
                            if signo == 0:
                                caraNueva = caraNueva + 1
                            else:
                                caraNueva = caraNueva - 1
                            if caraNueva < 0:
                                caraNueva = 3
                            else:
                                if caraNueva > 3:
                                    caraNueva = 0
                            self.pieza_esquina[i].tupla.orien[k] = movsH[caraNueva]


def main():
    cubo = Piezas()
    cubo.iniciaPiezas()
    cubo.imprimePieza()
    cubo.movHorizontal("U", 0)
    cubo.imprimePieza()


if __name__ == '__main__':
    main()