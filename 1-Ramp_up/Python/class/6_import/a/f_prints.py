def f_print_sino_r(string):
    """ 
    Si no empieza por R el string y su tamaño no es 0
    muestra String. En caso contrario, muestra "No se muestra"
    """
    if len(string) > 0:  # si hay algún elemento
        if string[0] != "R":  # si el primer elemento es diferente a R
            print(string)
    else:
        print("No se muestra")