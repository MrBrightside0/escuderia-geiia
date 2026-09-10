from tarea import volver_al_menu, menu_principal, eleccion_de_menu

tareas = []
opcion = 0

while opcion != 5:
    opcion = menu_principal()
    tareas = eleccion_de_menu(opcion,tareas)
                         
if len(tareas) != 0:     
    print("Termina tus tareas no seas flojo")
else:
    print("Bien hecho, puedes ver anime todo lo q quieras :3")    