# =====================================================================
#  ESCUDERÍA GEIIA · TEMPORADA 2026
#  Notas de la sesión 6 · LISTAS Y BUCLES FOR
#
#  Material construido por el equipo, revisado y completado.
#  Todo lo que está comentado se puede descomentar para probarlo.
#  Corran el archivo así:   python notas/listas_y_for.py
# =====================================================================


# =====================================================================
#  PARTE 1 · LISTAS
# =====================================================================
#
#  Las tres ideas:
#
#   1. Una lista guarda varias cosas en una sola variable.
#   2. Cada elemento tiene una posición, y se empieza a contar en 0.
#   3. La lista se puede modificar después de creada: agregar, quitar,
#      cambiar. Esa es su diferencia principal con el texto.
#
# ---------------------------------------------------------------------


# --- 1.1 Cómo se escribe ---------------------------------------------
# Con corchetes y comas.

cast = ['Hamilton', 'Burr', 'Eliza', 'Angelica', 'George', 'Lafayette', 'Jefferson']


# --- 1.2 Puede mezclar tipos, aunque casi nunca conviene -------------

mezclada = [51, 'Burr', True, 'Angelica', 0.342, 'Lafayette']
#           int   str   bool     str      float     str

# Python te deja hacerlo. Pero si una lista tiene tipos mezclados,
# casi siempre es señal de que había que usar un diccionario.


# --- 1.3 Las posiciones empiezan en 0 --------------------------------

cast = ['Hamilton', 'Burr', 'Eliza', 'Angelica', 'George', 'Lafayette', 'Jefferson']
#           0          1       2         3           4          5            6
#          -7         -6      -5        -4          -3         -2           -1

# print(cast[0])    # Hamilton
# print(cast[6])    # Jefferson
# print(cast[-1])   # Jefferson  ← el último, sin tener que contar
# print(cast[-2])   # Lafayette

# Los índices negativos cuentan desde el final.
# cast[-N] es lo mismo que cast[len(cast) - N]


# --- 1.4 len() y el error más común ----------------------------------

# print(len(cast))   # 7  ← cuántos elementos hay

# OJO: len() da 7, pero la última posición es la 6.
# La última posición de cualquier lista es siempre  len - 1
# Esa resta de uno es la causa de casi todos los IndexError.

# print(cast[7])     # IndexError: list index out of range
# print(cast[-8])    # IndexError: también por el otro lado


# --- 1.5 Modificar la lista ------------------------------------------

# append() agrega al final
cast.append('Madison')

# ANTES:  [... 'Lafayette', 'Jefferson']
#                    5            6
# DESPUÉS:[... 'Lafayette', 'Jefferson', 'Madison']
#                    5            6           7


# remove() quita por valor, no por posición.
# Todo lo que estaba DESPUÉS se recorre hacia la IZQUIERDA.
cast.remove('George')

# ANTES:  ['Hamilton', 'Burr', 'Eliza', 'Angelica', 'George', 'Lafayette', ...]
#               0         1        2          3          4          5
# DESPUÉS:['Hamilton', 'Burr', 'Eliza', 'Angelica', 'Lafayette', ...]
#               0         1        2          3           4        ← se movió


# Cambiar un elemento: se asigna directo a su posición.
cast[4] = 'King George III'


# insert() mete en una posición concreta.
# Todo lo que estaba ahí y después se empuja hacia la DERECHA.
cast.insert(4, 'George')

# ANTES:  [... 'Angelica', 'King George III', 'Jefferson', 'Madison']
#                   3              4               5           6
# DESPUÉS:[... 'Angelica', 'George', 'King George III', 'Jefferson', 'Madison']
#                   3           4            5               6           7


# index() te dice en qué posición está algo
# print(cast.index('Madison'))

# in te dice si algo está o no, y devuelve True o False
# print('Burr' in cast)      # True
# print('Napoleón' in cast)  # False


# --- 1.6 Métodos de lista más usados ---------------------------------
#
#   lista.append(x)      agrega x al final
#   lista.insert(i, x)   mete x en la posición i
#   lista.remove(x)      quita la primera aparición de x
#   lista.index(x)       en qué posición está x
#   len(lista)           cuántos elementos tiene
#   x in lista           True o False
#
# ---------------------------------------------------------------------


# --- 1.7 Ejercicio resuelto: la mochila ------------------------------

mochila = ['agua', 'libretas', 'calculadora', 'lapiz', 'sacapuntas', 'cuaderno']

# print(mochila[0])     # la primera
# print(mochila[-1])    # la última
# print(len(mochila))   # cuántas son

mochila.append('borrador')
mochila.remove('agua')

# El de en medio, sin contar a mano:
mitad = len(mochila) // 2      # // porque el índice tiene que ser entero
# print(mochila[mitad])


# =====================================================================
#  PARTE 2 · BUCLES FOR
# =====================================================================
#
#  Las tres ideas:
#
#   1. Un bucle repite un bloque de código. El sangrado decide qué se
#      repite y qué no.
#   2. for recorre algo que ya existe: una lista, o una cuenta de range.
#   3. range(5) da cinco números pero empieza en 0, así que llega al 4.
#      Misma lógica que los índices de las listas.
#
# ---------------------------------------------------------------------


# --- 2.1 El sangrado decide qué se repite ----------------------------

# Ejemplo 1 · "listo" DENTRO del bucle: se imprime siete veces
'''
for i in range(7):
    print(i)
    print("listo")
'''

# Ejemplo 2 · "Listo" FUERA del bucle: se imprime una sola vez
'''
for i in range(7):
    print(i)
print("Listo")
'''

# Es el mismo código con un sangrado distinto, y hace cosas distintas.


# --- 2.2 for sobre una lista -----------------------------------------

escuderia = ['Janeth', 'Rodolfo', 'Rogelio', 'Katia', 'Joseph']

'''
for e in escuderia:
    print("Hola, yo soy:", e)
print("Listo!")
'''

# En cada vuelta, la variable  e  vale un elemento distinto.
# El nombre de la variable lo eliges tú: e, nombre, piloto, lo que sea.


# --- 2.3 range con inicio, fin y paso --------------------------------
#
#   range(5)         0, 1, 2, 3, 4         cinco números desde 0
#   range(1, 11)     1, 2, ... 10          desde 1, se detiene ANTES del 11
#   range(0, 11, 2)  0, 2, 4, 6, 8, 10     de dos en dos
#
# El número final NUNCA se incluye. Por eso range(1, 11) llega al 10.

# Del 1 al 10:
'''
for i in range(1, 11):
    print(i)
'''

# Solo los pares · versión con if
'''
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
'''

# Solo los pares · versión con paso, sin if
'''
for i in range(2, 11, 2):
    print(i)
'''


# =====================================================================
#  PARTE 3 · ACUMULADORES
#  Lo que faltaba, y el puente hacia el while
# =====================================================================
#
#  Un acumulador es una variable que vive FUERA del bucle y se va
#  actualizando ADENTRO. Es el patrón más útil de toda la programación
#  básica: sirve para sumar, contar, y encontrar máximos.
#
# ---------------------------------------------------------------------


# --- 3.1 Sumar los números del 1 al 100 ------------------------------
#
# Esto NO suma, solo imprime cien líneas:
#     for i in range(100):
#         print(str(i) + " + 1 =", i + 1)
#
# Esto sí suma:

total = 0                    # el acumulador nace en cero, FUERA del bucle
for i in range(1, 101):
    total = total + i        # en cada vuelta se le agrega el número
# print(total)               # 5050

# Los tres pasos del patrón, siempre iguales:
#   1. crear la variable antes del bucle
#   2. actualizarla dentro del bucle
#   3. usarla después del bucle


# --- 3.2 Contar cuántos cumplen algo ---------------------------------

pares = 0
for i in range(1, 101):
    if i % 2 == 0:
        pares = pares + 1
# print("Números pares del 1 al 100:", pares)   # 50

# Atajo que verán mucho:  pares += 1  es lo mismo que  pares = pares + 1


# --- 3.3 Sumar y promediar una lista ---------------------------------

edades = [19, 21, 20, 22, 19]

suma = 0
for edad in edades:
    suma += edad

promedio = suma / len(edades)
# print("Suma:", suma, "· Promedio:", promedio)

# Nota: Python ya trae sum(edades) y len(edades) para esto.
# Se hace a mano una vez para entender qué está pasando por dentro.


# --- 3.4 Encontrar el mayor ------------------------------------------

mayor = edades[0]            # se empieza suponiendo que el primero es el mayor
for edad in edades:
    if edad > mayor:
        mayor = edad         # si aparece uno más grande, se reemplaza
# print("El mayor es:", mayor)


# =====================================================================
#  ERRORES QUE VAN A VER, Y QUÉ SIGNIFICAN
# =====================================================================
#
#   IndexError: list index out of range
#       Pidieron una posición que no existe. Recuerden: la última es len-1.
#
#   ValueError: list.remove(x): x not in list
#       Intentaron quitar algo que no estaba en la lista.
#
#   IndentationError
#       Falta el sangrado bajo el for, o está inconsistente. Cuatro espacios.
#
#   TypeError: list indices must be integers
#       Usaron un decimal como índice. Ahí va la división entera //
#
#   El bucle imprime de más o de menos
#       No es un error de Python: es el sangrado, o el rango.
#       Revisen si el print está dentro o fuera, y qué números da el range.
#
# =====================================================================