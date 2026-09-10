def volver_al_menu():
    print("""
    
    
    
    

    
    """)
    input("Volver a menu")
def menu_principal():
    print("\033[3J\033[H\033[2J", end="")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Ver cantidad de tareas")
    print("4. Terminaste una tarea? ")
    print("5. Salir")
    opcion = int(input("Elige: "))
    return opcion
def eleccion_de_menu(opcion,tareas):
    print("\033[3J\033[H\033[2J", end="") #te mueve la webada hasta que no se vea lo demas  
    if (opcion) == 1: #para agregar tareas
        tareas.append(input ( "Que nueva tarea tienes?: "))
        volver_al_menu()
    elif opcion == 2: #para revisar cuales tareas tienes 
        if len(tareas) == 0: # si no tienes tareas, te dice que no tienes 
            print("No tienes tareas ahora mismo")
            volver_al_menu()
        else:
            print("Estas son tus tareas: ")
            for i in tareas:
                print(i)
            volver_al_menu()    
    elif (opcion) == 3: #para revisar cuantas tareas tienes 
        if len(tareas) == 0:  # si no tienes tareas, te dice que no tienes 
            print("No tienes tareas ahora mismo")
            volver_al_menu()
        else:
            print("Tu tienes: " + str(len(tareas)) + " tarea/s por hacer")
            volver_al_menu()
    elif opcion == 4: #para ver si quieres quitar una tarea terminada 
        if len(tareas) == 0:  # si no tienes tareas, te dice que no tienes 
            print("No tienes tareas ahora mismo")
            volver_al_menu()
        else:
           print(tareas)
           tareas.remove(input("Que tarea terminaste?: "))
           volver_al_menu()
    return tareas    