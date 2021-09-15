

import numpy as np

def clean_coors(coors):
    '''
    Limpiamos el texto introducido por el usuario. Quitamos espacios,
    parentesis y sustituimos comas por puntos.
    input: entrada del usuario
    output: tupla en formato (fila, columna)
    '''
    coors = coors.replace(' ', '').replace('(', '').replace(')', '').replace(',', '.').replace("'", '')
    fila = int(coors.split('.')[0])
    col = int(coors.split('.')[1])

    return (fila, col)


def choose_coor(tablero, dificultad):
    '''
    La maquina escoge una coordenada de disparo en funcion de la dificultad del juego
    input:
        tablero: Tablero. Objeto de la clase Tablero donde se cumprueba el disparo
        dificultad: int. Del 1 al 3

    output: punto al que dispara
    '''

    # Escoge entre un unico punto
    if dificultad == 1:
        return tablero.check_new_coor()

    # Escoge entre dos puntos
    elif dificultad == 2:
        pt1 = tablero.check_new_coor()
        pt2 = tablero.check_new_coor()

        if tablero.just_check_coor(pt1):
            return pt1
        else:
            return pt2

    # Escoge entre tres puntos
    elif dificultad == 3:
        pt1 = tablero.check_new_coor()
        pt2 = tablero.check_new_coor()
        pt3 = tablero.check_new_coor()

        if tablero.just_check_coor(pt1):
            return pt1
        elif tablero.just_check_coor(pt2):
            return pt2
        else:
            return pt3



