import os
import json
from funciones import separacion, juntar, formato, menu_principal, eleccion_de_menu, creditos, guardar, abrir

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
abrir(task)

tareas, hecho = separacion (tareas, hecho, task)

#PROG
while opcion != 7:
    chequeo = formato(chequeo,tareas,hecho) 
    opcion = menu_principal(_, opciones, opcion )
    opcion, tareas, hecho = eleccion_de_menu(opcion, tareas, hecho, chequeo, _ )

#POST 
task = juntar(task, tareas, hecho)    
creditos(tareas)

guardar(chequeo, task)   