import json
def cargar_historial():
    """
    Carga el historial de partidas desde el archivo JSON.
    Devuelve una lista con las partidas guardadas.
    """

    try:
        with open("historial.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    
def guardar_historial(historial):
    with open("historial.json","w") as archivo:
      json.dump(historial, archivo, indent=4)
    
def crear_tablero():
    """
    Crea un tablero de juego vacío de 3x3. 
    Devuelve una lista con nueve casillas"""
    
    return["1", "2", "3", 
           "4", "5", "6",
           "7", "8", "9"] #Este es mi tablero
    
def dibujar_tablero(tablero): #Aqui yo quiero ya imprimir mi tablero
     """
     Muestra el tablero en la terminal. 
    Recibe el tablero y no devuelve nada
     """
    
     print(tablero[0], "|", tablero[1], "|", tablero[2])
     print("--+--+--")
     print(tablero[3], "|", tablero[4], "|", tablero[5])
     print("--+--+--")
     print(tablero[6], "|", tablero[7], "|", tablero[8])
    
    
#Poner la X
def poner_marca(tablero, posicion, marca):
    """
    Coloca una marca en el tablero en la posición indicada.
    Recibe el tablero, la posición y la marca.
    """
    tablero[posicion] = marca

    
def casilla_libre(tablero, posicion):
    """
    Comprueba si una casilla está libre.
    Devuelve True si la casilla está libre, False en caso contrario.
    """
    if tablero[posicion] == str(posicion + 1):
        return True
    else:
        return False
    
combinaciones = [[0, 1, 2], [3, 4, 5], [6, 7, 8], #filas
                 [0, 3, 6], [1, 4, 7], [2, 5, 8], #Columnas
                 [0, 4, 8], [2, 4, 6]] #Diagonales
     
def hay_ganador(tablero):
    """
    Comprueba si hay un ganador en el tablero.
    Devuelve la marca del ganador o None si no hay ganador.
    """

    for combinacion in combinaciones:
        if (tablero[combinacion[0]] != str(combinacion[0] + 1)
                and tablero[combinacion[0]] == tablero[combinacion[1]]
                and tablero[combinacion[1]] == tablero[combinacion[2]]):
            return tablero[combinacion[0]]

    return None

def tablero_lleno(tablero):
    """
    Comprueba si el tablero está lleno.
    Devuelve True si el tablero está lleno, False en caso contrario.
    """
    for posicion in range(9):
      if tablero[posicion] == str(posicion + 1):
          return False
      
    return True
  
