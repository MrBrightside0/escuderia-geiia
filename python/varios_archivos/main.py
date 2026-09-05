from tareas import mostrar_menu, agregar_tarea

tareas = []
mostrar_menu()
agregar_tarea(tareas, "estudiar")
print(tareas)

#mandamos a llamar todo, nunca recomendable, usa mas recursos
import random
random.choice([1,2,3])

#llamamos a la funcion especifica que queremos usar, caso recomendable
from random import choice
choice([1,2,3])

from tareas import *
choice
# trae todo sin prefijo.
# NO la usen: no se sabe
# de dónde salió cada cosa.
