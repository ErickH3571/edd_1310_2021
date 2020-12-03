from Arrays import Array2D
from Stack import Stack

class LaberintoADT:
    """
    0 Pasillo, 1 Pared, S Salida y E entrada
    pasillos es una tupla con coordenadas
    Entrada en tupla (5,1)
    Salida (2,5)
    """
    def __init__(self, rens, cols, pasillos, entrada, salida):
        self.__laberinto = Array2D(rens, cols, '1')
        for a in pasillos:
            self.__laberinto.set_item(a[0], a[1], '0')
        self.set_entrada(entrada[0], entrada[1])
        self.set_salida(salida[0], salida[1])
        self.__camino = Stack()

    def to_string(self):
        self.__laberinto.to_string()

    """
    Establece la entrada, poniendo una E en la matriz, verificar limites perifericos
    """
    def set_entrada(self, ren, col):
            self.__laberinto.set_item(ren, col, 'E')

    def set_salida(self, ren, col):
            self.__laberinto.set_item(ren, col, 'S')

    def es_salida(self, ren, col):
            return self.__laberinto.get_item(ren, col) == 'S'

    def buscar_entrada( self ):
        encontrado = False
        for renglon in range(self.__laberinto.get_num_rows()):
            for columna in range(self.__laberinto.get_num_cols()):
                tope = self.__camino.peek() #Tupla   tope=(2,1)
                if self.__laberinto.get_item(renglon, columna )=='E':
                    self.__camino.push(tuple(renglon,columna))
                    encontrado = True
        return encontrado

    def set_previa( self , pos_previa ):
        self.__previa = pos_previa

    def get_previa( self ):
        return self.__previa

    def resolver_laberinto ( self ):
        #Aplicar reglas
