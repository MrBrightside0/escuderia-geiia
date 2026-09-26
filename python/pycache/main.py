import os
from funciones import separacion, juntar, formato, menu_principal, eleccion_de_menu, creditos

#VARIABLES:
#GENERALES 
task = []
opciones = ["1","2","3","4","5","6","7"]
opcion = 0
_=0
#DIVISORIAS
tareas = []
hecho = []
#DICCIONARIAS 
chequeo = []
llave = {}

#PRE
dir = os.path.dirname(__file__)
path = os.path.join(dir, "tarea.txt")
with open (path) as f:
    for i in f:
        task.append(i.strip())

tareas, hecho = separacion (tareas, hecho, task)

#PROG
while opcion != 7:
    chequeo = formato(chequeo,tareas,hecho) 
    opcion = menu_principal(_, opciones, opcion )
    opcion, tareas, hecho = eleccion_de_menu(opcion, tareas, hecho, chequeo, _ )

#POST 
task = juntar(task, tareas, hecho)    
creditos(tareas)

with open ("tarea.txt", "w") as f:
    for i in task:
        f.write(str(i) + "\n")