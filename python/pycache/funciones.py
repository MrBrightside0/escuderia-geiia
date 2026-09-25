#====================================================================== SEPARACION
def separacion(tareas,hecho,task):
    cambio = 0
    for i in task:
        if cambio == 0:
            tareas.append(i)
            cambio += 1
        elif cambio == 1:
            hecho.append(int(i))
            cambio -= 1

    return tareas,hecho        

#===================================================================== CONCATENACION XD
def juntar (task, tareas, hecho):
    task = []
    for i in tareas:
            task.append(i)
            task.append(hecho[tareas.index(i)])
    return task         
#===================================================================== DICCIONARIO
def formato(chequeo,tareas,hecho):
    chequeo = []
    cambio = 0
    if len(tareas) != 0:
        for i in tareas:
            if cambio == 0:
                llave = {"trabajo" : i, "hecha": hecho[cambio]}
                cambio += 1
            else: 
                llave = {"trabajo" : i, "hecha": hecho[cambio]}
                cambio += 1
            chequeo.append(llave) 
    return chequeo    

#===================================================================== IMPRESORA 
def impresora(chequeo):
    for i in chequeo:
        if i["hecha"] == 1:
            marca = "x"
        else:
            marca = "" 
        print("[" + marca + "] " + i["trabajo"])

#===================================================================== CREDITOS

def creditos(tareas):
    if len(tareas) != 0:     
        print("Termina tus tareas no seas flojo")
    else:
        print("Bien hecho, puedes ver anime todo lo q quieras :3")    

#===================================================================== FUNCIONES
def volver_al_menu():
    print("""
    
    
    
    

    

    """)
    input("Volver a menu")

#-----------------------------------------------------------------------
def menu_principal():
    print("\033[3J\033[H\033[2J", end="")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Ver cantidad de tareas")
    print("4. Terminaste una tarea?")
    print("5. Quieres quitar una tarea? ")
    print("6. Salir")
    opcion = int(input("Elige: "))
    return opcion
#-----------------------------------------------------------------------
def eleccion_de_menu(opcion, tareas, hecho, chequeo):
    print("\033[3J\033[H\033[2J", end="") #te mueve la webada hasta que no se vea lo demas  


    if (opcion) == 1: #para agregar tareas

        tareas.append(input ( "Que nueva tarea tienes?: "))
        hecho.append(0)

        volver_al_menu()


    elif opcion == 2: #para revisar cuales tareas tienes 

        if len(tareas) == 0: # si no tienes tareas, te dice que no tienes 

            print("No tienes tareas ahora mismo")
            volver_al_menu()

        else:

            print("Estas son tus tareas: ")

            impresora(chequeo)

            volver_al_menu()

                
    elif (opcion) == 3: #para revisar cuantas tareas tienes 

        if len(tareas) == 0:  # si no tienes tareas, te dice que no tienes 

            print("No tienes tareas ahora mismo")
            volver_al_menu()

        else:

            print("Tu tienes: " + str(len(tareas)) + " tarea/s por hacer")
            volver_al_menu()


    elif opcion == 4: 

        if len(tareas) == 0:  # si no tienes tareas, te dice que no tienes 

            print("No tienes tareas ahora mismo")
            volver_al_menu()
        
        else: 
            impresora(chequeo)
            hecho[tareas.index(input("Que tarea quieres marcar como terminada?: "))] = 1
            volver_al_menu()
        
        

    elif opcion == 5: #para ver si quieres quitar una tarea terminada 

        if len(tareas) == 0:  # si no tienes tareas, te dice que no tienes 

            print("No tienes tareas ahora mismo")
            volver_al_menu()

        else:
            print(tareas)
            num = input("Que tarea quieres quitar?: ")
            hecho.remove(hecho[tareas.index(num)])
            tareas.remove(num)
            volver_al_menu()


    return opcion, tareas, hecho 

