

ORIENTATIONS = ("N", "S", "E", "O") 
DIMENSIONES = (10,10)
BARCOS = {
    "barco_1_1": 1,
    "barco_1_2": 1,
    "barco_1_3": 1,
    "barco_1_4": 1,
    "barco_2_1": 2,
    "barco_2_2": 2,
    "barco_2_3": 2,
    "barco_3_1": 3,
    "barco_3_2": 3,
    "barco_4_1": 4,
}

CHARTAB = {
    "boat": "O",
    "water": " ",
    "hit": "X",
    "fail": "-"
}

MENSAJES = {
    "intro1": "¡Bienvenido al Hundir la Flota! Dispondrás de un tablero con: \
    \n 4 barcos de 1 de eslora \
    \n 3 barcos de 2 de eslora \
    \n 2 barcos de 3 de eslora \
    \n 1 barco de 4 de eslora . \
    \n\n Los barcos se posicionarán aleatoriamente en el tablero, al igual que los de la maquina." +
    "Así queda tu tablero de barcos:\n",

    "intro2": "\nEste es el tablero de tu contrincante:",

    "intro3": "\nEl juego es sencillo. Tendrás que ir introduciendo coordenadas por pantalla, " +
    "hasta que hundas todos los barcos del rival.\n\nLas coordenadas se introducen separandolas" +
    " por puntos. Por ejemplo, si queremos la disparar a la primera fila, columna 8, introduciríamos" +
    " por pantalla '1.8'.\n\n¿Listo? A jugar!",

    "intro4": "\nLo primero de todo, escoge una dificultad:\nFácil: 1\nMedio: 2\nDificil: 3\n",

    "turno1": "\nIntroduce una coordenada en formato 'fila.columna'. \nRecuerda que siempre puedes seleccionar:\n1. Salir: 'salir'" +
    "\n2. Ver mi tablero: 'mt'\n3. Ver tablero maquina: 'tm'\n",
    "tocado": "\n¡BOOM! TOCADO! Has impactado en un barco de la máquina.\n\n¡Te sigue tocando!",
    "agua": "\n¡AGUA! Has fallado. Le toca a la maquina",

    "maquina_tocado": "\nNOS HA IMPACTADO DE LLENO!!! Le vuelve a tocar a la maquina",
    "maquina_fallado": "\n¡Ha fallado! Nos vuelve a tocar",
    "maquina_tablero": "\nMira cómo estás dejando el tablero rival",

    "salir": "\n¡Nos vemos pronto!",
    "ganar": "\n¡GANASTE! Enhorabuena, eres un auténtico grumete!",
    "perder": "\n¡LOSER! Has palmado. Tienes que practicar un poco más"

}