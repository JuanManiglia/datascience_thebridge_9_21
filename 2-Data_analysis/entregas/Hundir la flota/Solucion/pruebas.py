



tabl_j1 = Tablero(1,DIMENSIONES,BARCOS)
tabl_j1.inicializa_tablero()
print(tabl_j1.tablero)
np.count_nonzero(tabl_j1.tablero == "O")


ini_coor = np.random.randint(10, size = 2)
orient = random.choice(orientations)

a = new_tab.tablero
eslora = 4
ini_coor_f = ini_coor[0]
ini_coor_c = ini_coor[1]


while True:

    # Orientacion Norte
    coors_posi = a[ini_coor_f:ini_coor_f - eslora:-1, ini_coor_c]
    if orient == 'N' and 0 <= ini_coor_f - eslora < 10 and 1 not in coors_posi:
        coors_posi = a[ini_coor_f:ini_coor_f - eslora:-1, ini_coor_c]

    # Orientacion Este
    coors_posi = a[ini_coor_f, ini_coor_c: ini_coor_c + eslora]
    elif orient == 'E' and 0 <= ini_coor_c + eslora < 10 and 1 not in coors_posi:
        coors_posi = a[ini_coor_f, ini_coor_c: ini_coor_c + eslora]

    # Orientacion Sur
    coors_posi = a[ini_coor_f:ini_coor_f + eslora, ini_coor_c]
    elif orient == 'S' and 0 <= ini_coor_f + eslora < 10 and 1 not in coors_posi:
        coors_posi = a[ini_coor_f:ini_coor_f + eslora, ini_coor_c]

    # Orientacion Oeste
    coors_posi = a[ini_coor_f, ini_coor_c: ini_coor_c - eslora:-1]
    elif orient == 'O' and 0 <= ini_coor_c - eslora < 10 and 1 not in coors_posi:
        coors_posi = a[ini_coor_f, ini_coor_c: ini_coor_c - eslora:-1]
    
    # No cumple con las dimensiones del tablero, o hay un barco ahi.
    else:
        continue

        






if 1 in coors_posi:
    print("Ya hay valor")

print(a)


