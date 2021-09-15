

import numpy as np
import random
from variables import ORIENTATIONS, DIMENSIONES, BARCOS, CHARTAB

class Tablero:
    '''
    Clase donde se modeliza el tablero de un jugador.

    __init__(self, jugador_id, dimensiones, barcos)
    jugador_id: int
    dimensiones: tuple - (x,y)
    barcos: dict - diccionario con todos los barcos
    '''
    
    vidas = None

    def __init__(self, jugador_id, dimensiones, barcos):

        # Identificador numerico ed jugador
        self.jugador_id = jugador_id

        # Dimensiones del tablero
        self.dimensiones = dimensiones

        # Diccionario de barcos
        self.barcos = barcos

        # Tablero a rellenar de barcos
        self.tablero = np.full(fill_value = CHARTAB["water"], shape = dimensiones)

        # Tablero a usar en el juego, todo con agua
        self.tablero_ini = np.full(fill_value = CHARTAB["water"], shape = dimensiones)


    
    def inicializa_tablero(self):
        '''
        Metodo que posiciona los barcos en el tablero
        '''
        self.barcos_array = []
        for barco in self.barcos:
            eslora = self.barcos[barco]
        
            self.set_barco(eslora)

        self.vidas = np.count_nonzero(self.tablero == "O")



    def set_barco(self, eslora):
        '''
        Posiciona un barco de longitud "eslora" en el tablero
        input: eslora - int del (1,4)
        '''
        while True:

            # 'N' - 'S' - 'E' - 'O'
            orient = random.choice(ORIENTATIONS)

            # Posicion inicial del barco
            current_pos = np.random.randint(self.dimensiones[0], size = 2)
            
            fila = current_pos[0]
            col = current_pos[1]

            # Recogemos las 4 posiciones colindantes a corrent_pos
            coors_posiN = self.tablero[fila:fila - eslora:-1, col]
            coors_posiE = self.tablero[fila, col: col + eslora]
            coors_posiS = self.tablero[fila:fila + eslora, col]
            coors_posiO = self.tablero[fila, col: col - eslora:-1]

            # Comprobamos si esas posiciones son validas
            # Orientacion Norte
            if orient == 'N' and 0 <= fila - eslora < 10 and CHARTAB["boat"] not in coors_posiN:
                self.tablero[fila:fila - eslora:-1, col] = CHARTAB["boat"]
                return
            
            # Orientacion Este
            elif orient == 'E' and 0 <= col + eslora < 10 and CHARTAB["boat"] not in coors_posiE:
                self.tablero[fila, col: col + eslora] = CHARTAB["boat"]
                return
            
            # Orientacion Sur
            elif orient == 'S' and 0 <= fila + eslora < 10 and CHARTAB["boat"] not in coors_posiS:
                self.tablero[fila:fila + eslora, col] = CHARTAB["boat"]
                return
            
            # Orientacion Oeste
            elif orient == 'O' and 0 <= col - eslora < 10 and CHARTAB["boat"] not in coors_posiO:
                self.tablero[fila, col: col - eslora:-1] = CHARTAB["boat"]
                return
            
            # No cumple con las dimensiones del tablero, o hay un barco ahi
            # Probamos con otra coordenada
            else:
                continue



    def check_coor(self, coordenadas):
        '''
        Comprobamos si se ha impactado
        input: coordenadas - tupla de coordeadas x e y
        '''

        # Restamos 1 porque los arrays empiezan en 0, no en 1.
        fila = coordenadas[0] - 1
        col = coordenadas[1] - 1

        # Si hay un barco, impactamos y lo marcamos en el tablero
        if self.tablero[fila, col] == CHARTAB["boat"]:
            self.tablero[fila, col] = CHARTAB["hit"]
            self.tablero_ini[fila, col] = CHARTAB["hit"]
            self.vidas -= 1
            return True

        # Si no, lo marcamos en el tablero como fallo
        else:
            self.tablero[fila, col] = CHARTAB["fail"]
            self.tablero_ini[fila, col] = CHARTAB["fail"]
            return False

    def just_check_coor(self, coordenadas):
        '''
        Simplemente comprobamos si hay barco, sin sutituir nada en el tablero
        input: coordenadas - tupla de coordeadas x e y
        '''
        if self.tablero[coordenadas[0], coordenadas[1]] == CHARTAB["boat"]:
            return True
        else:
            return False

    def check_new_coor(self):
        '''
        Escogemos una coordenada aleatoria y comprobamos si
        en esa coordenada ya se habia disparado. En tal caso, elegimos otra coordenada
        '''
        while True:
            coor = np.random.randint(self.dimensiones[0], size = 2)

            if self.tablero[coor[0], coor[1]] not in (CHARTAB["hit"], CHARTAB["fail"]):
                return coor

