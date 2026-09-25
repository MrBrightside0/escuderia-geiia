import os
from funciones import separacion, juntar, formato, impresora, volver_al_menu, menu_principal, eleccion_de_menu, creditos

#VARIABLES:
#GENERALES 
task = []
opcion = 0
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
while opcion != 6:
    chequeo = formato(chequeo,tareas,hecho) 
    opcion = menu_principal()
    opcion, tareas, hecho = eleccion_de_menu(opcion, tareas, hecho, chequeo )

#POST 
task = juntar(task, tareas, hecho)    
creditos(tareas)

with open ("tarea.txt", "w") as f:
    for i in task:
        f.write(str(i) + "\n")