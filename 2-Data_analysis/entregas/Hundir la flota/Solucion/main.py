'''
Autor: Daniel Ortiz
Fecha: 28/07/2020
Programa que simula el famoso juego de hundir la flota.
El jugador vs la maquina.
El programa se in inicializa posicionando los barcos de ambos jugadores aleatoriamente
'''

# Importamos librerias
import numpy as np
import time

# Importamos modulos propios
from clases import Tablero
from funciones import clean_coors, choose_coor
from variables import DIMENSIONES, BARCOS, MENSAJES

# Se posicionan los barcos del jugador 1
print(MENSAJES["intro1"])
tabl_j1 = Tablero(1,DIMENSIONES,BARCOS)
tabl_j1.inicializa_tablero()
print(tabl_j1.tablero)

# Se posicionan los barcos del jugador 2
print(MENSAJES["intro2"])
tabl_j2 = Tablero(2,DIMENSIONES,BARCOS)
tabl_j2.inicializa_tablero()
print(tabl_j2.tablero_ini)

print(MENSAJES["intro3"])

# Establecemos el numero de vidas
vidas_j1 = np.count_nonzero(tabl_j1.tablero == "O")
vidas_j2 = vidas_j1

# Escoge dificultad
dificultad = int(input(MENSAJES["intro4"]))

# Cada vez que le toca al jugador, pasa por aquí
while True:

    # Menu del juego en el que el jugador elige opcion
    coor = input(MENSAJES["turno1"])

    # Si quiere salir
    if coor.lower() == 'salir':
        print(MENSAJES["salir"])
        break

    # Si quiere ver su tablero
    elif coor.lower() == 'mt':
        print(tabl_j1.tablero)
        continue

    # Si quiere ver el tablero de la maquina
    elif coor.lower() == 'tm':
        print(tabl_j2.tablero_ini)
        continue

    # Truco para debuguear
    elif coor.lower() == 'tmb':
        print(tabl_j2.tablero)
        continue

    # Si no se da ninguno de los casos anteriores, suponemos que es una coordenada
    try:
        coor = clean_coors(coor)
    except:
        # No ha introducido una coordenada correcta
        print(coor, "no se considera como coordenada.\
         \nPor favor, introduce de nuevo una coordenada en formato 'fila.columna' ")
        continue

    # Comprobamos si j1 impacta en j2
    tocado = tabl_j2.check_coor(coor)

    # Si ha dado a algún barco. Le vuelve a tocar
    if tocado:
        print(MENSAJES["tocado"])
        print(tabl_j2.tablero_ini)

        # Si le ha tocado, y ya no le quedan vidas, ha ganado j1 y termina el programa
        if tabl_j2.vidas == 0:
            print(MENSAJES["ganar"])
            break

        
    
    # Si no da a ningun barco, le toca a la maquina
    else:
        print(MENSAJES["agua"])

        turno_maquina = True

        # Le toca a la maquina tantas veces como acierte
        while turno_maquina:

            # Simulamos que piensa la maquina
            time.sleep(2)

            # Disparo aleatorio de la maquina
            coor_maq = choose_coor(tabl_j1, dificultad)
            coor_maq[0]+=1
            coor_maq[1]+=1

            # Comprobamos si nos da
            tocado_maq = tabl_j1.check_coor(coor_maq)

            # Si la maquina falla, termina el while y le toca a j1
            if not tocado_maq:
                turno_maquina = False
                print(MENSAJES["maquina_fallado"])

            # Si no, impacta y comprueba si le quedan vidas a j1
            else:
                print(MENSAJES["maquina_tocado"])

                if tabl_j1.vidas == 0:
                    print(MENSAJES["perder"])
                    break

        # Si hemos perdido, salimos también de este bucle
        if tabl_j1.vidas == 0:
            break

        # Imprimimos por pantalla el tablero rival
        print(MENSAJES["maquina_tablero"])
        print(tabl_j2.tablero_ini)
                



