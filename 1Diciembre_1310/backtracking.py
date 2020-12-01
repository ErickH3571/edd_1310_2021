from Arrays import Array2D

class LaberintoADT:
    """
    0 Pasillo, 1 Pared, S Salida y E entrada
    pasillos es una tupla con coordenadas
    """
    def __init__(self, rens, cols, pasillos):
        self.__laberinto = Array2D(rens, cols, '1')
        for a in pasillos:
            self.__laberinto.set_item(a[0], a[1], '0')

    def to_string(self):
        self.__laberinto.to_string()
