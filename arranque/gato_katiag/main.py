from juego import*
def pedir_nombre(marca):
    """
    Pide al jugador que introduzca su nombre.
    Recibe la marca del jugador y devuelve el nombre introducido.
    """
    nombre = input ("Jugador" + marca +", escribe tu nombre: ")
    return nombre

def pedir_jugada(tablero, nombre, marca):
 while True:
    jugada = input(nombre + ",elige una casilla (1-9):") 
    
    try:
     jugada = int(jugada) #Convierto de texto a numero
    except ValueError:
         print("Debes introducir un número del 1 al 9. >:(")
         continue
    if jugada < 1 or jugada > 9: 
        print("Elige un nunero del 1 al 9")
        continue
    posicion = jugada - 1
    
    if not casilla_libre(tablero, posicion):
         print("Esa casilla ya está ocupada. Elige otra.")
         continue
    return posicion

def mostrar_historial():
    historial = cargar_historial()

    if not historial:
        print("Todavía no hay partidas guardadas.")
        return
    for partida in historial:
        print("Jugador X:", partida["jugador_x"])
        print("Jugador O:", partida["jugador_o"])
        print("Resultado:", partida["ganador"])
        print("--------------------")
 
def jugar_partida(jugador_x, jugador_o):
     tablero = crear_tablero()
     marca = "X"
     nombre = jugador_x
     
     while True:
         dibujar_tablero(tablero)
         posicion =  pedir_jugada(tablero, nombre, marca)
         
         poner_marca(tablero, posicion, marca)
         ganador= hay_ganador(tablero)
         
         if ganador is not None:
             
          dibujar_tablero(tablero)
          print("Ganó", nombre)
          return ganador 
      
         if tablero_lleno(tablero): 
             dibujar_tablero(tablero)
             print ("Empate")
             return None
         
         if marca == "X":
             marca = "O"
             nombre = jugador_o
         else:
            marca = "X"
            nombre = jugador_x
            
def main():
    while True:
        print("\n🐱 GATO 🐱")
        print("1. Jugar")
        print("2. Ver historial")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre_x = pedir_nombre("X")
            nombre_o = pedir_nombre("O")

            resultado = jugar_partida(nombre_x, nombre_o)

            historial = cargar_historial()

            if resultado == "X":
                ganador = nombre_x
            elif resultado == "O":
                ganador = nombre_o
            else:
                ganador = "Empate"

            historial.append({
                "jugador_x": nombre_x,
                "jugador_o": nombre_o,
                "ganador": ganador
            })

            guardar_historial(historial)

        elif opcion == "2":
            mostrar_historial()

        elif opcion == "3":
            print("¡Gracias por jugar! 🐱")
            break

        else:
            print("Opción no válida.")


main()