# =========================================================
#  arranque/mi_programa.py  ·  Escudería GEIIA · Viernes S1
#
#  Llena los tres huecos. No borres los comentarios: son el mapa.
#  Cuando funcione, córrelo así:   python arranque/mi_programa.py
# =========================================================

# --- 1. PREGUNTAR ---------------------------------------------------

nombre = input("¿Cómo te llamas? ")

# HUECO 1 · Cambia esta pregunta por la tuya.
#   Tiene que responderse con un número entero.
#   Ideas: horas que dormiste, canciones en tu playlist,
#          minutos que tardas al Tec, tazas de café de hoy.
respuesta = int(input("¿Cuántas horas dormiste? "))


# --- 2. DECIDIR -----------------------------------------------------

# HUECO 2 · Cambia el número, y el signo si hace falta.
#   Signos que puedes usar:   >   <   >=   <=   ==
if respuesta >= 7:

    # HUECO 3 · Qué contesta cuando la respuesta es "sí"
    print(nombre + ", vas bien. Nos vemos el miércoles.")

else:

    # HUECO 3 · Qué contesta cuando es "no"
    print(nombre + ", duérmete. El código sale mejor descansado.")


# --- 3. CERRAR ------------------------------------------------------

print("Fin del programa.")
