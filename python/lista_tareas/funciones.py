import os
import json
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

#===================================================================== CONTADOR

def contador(hecho):
    listo = 0
    nolisto = 0
    for i in hecho:
        if i == 1:
            listo += 1
        elif i == 0:
            nolisto += 1
    print("Tienes hechas: " + str(listo) + " tareas")
    print("Te faltan: " + str(nolisto) + " tareas")          



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
def menu_principal(_, opciones, opcion ):
    print("\033[3J\033[H\033[2J", end="")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Ver cantidad de tareas")
    print("4. Terminaste una tarea?")
    print("5. Quieres quitar una tarea? ")
    print("6. Ver cuantas tareas tienes listas y cuantas no")
    print("7. Salir")
    opcion = int(falesafemenu(_, opciones))
    return opcion
#-----------------------------------------------------------------------
def eleccion_de_menu(opcion, tareas, hecho, chequeo, _,):
    print("\033[3J\033[H\033[2J", end="") #te mueve la webada hasta que no se vea lo demas  


    if (opcion) == 1: #para agregar tareas

        impresora(chequeo)
        tareas.append(failsafet1(_, tareas))
        hecho.append(0)

        volver_al_menu()


    elif opcion == 2: #para revisar cuales tareas tienes 

        if len(tareas) == 0: # si no tienes tareas, te dice que no tienes 

            print("No tienes tareas ahora mismo")
            volver_al_menu()

        else:

            print("Estas son tus tareas: ")

            impresora(chequeo)
            _ = input() 
            volver_al_menu()

                
    elif (opcion) == 3: #para revisar cuantas tareas tienes 

        if len(tareas) == 0:  # si no tienes tareas, te dice que no tienes 

            print("No tienes tareas ahora mismo")
            volver_al_menu()

        else:

            print("Tu tienes: " + str(len(tareas)) + " tarea/s en la lista")
            volver_al_menu()


    elif opcion == 4: # Para marcar si ya se termino una tarea 

        if len(tareas) == 0:  # si no tienes tareas, te dice que no tienes 

            print("No tienes tareas ahora mismo")
            volver_al_menu()

        elif hecho.count(1) == len(hecho):
            print("Todas las tareas estan hechas")
            volver_al_menu()

        else: 
            impresora(chequeo)
            hecho[tareas.index(failsafe4(_, hecho, tareas ))] = 1
            volver_al_menu()
        
        

    elif opcion == 5: #para ver si quieres quitar una tarea terminada 

        if len(tareas) == 0:  # si no tienes tareas, te dice que no tienes 

            print("No tienes tareas ahora mismo")
            volver_al_menu()

        else:
            impresora(chequeo)
            num = failsafet5(_, tareas, opcion)
            hecho.remove(hecho[tareas.index(num)])
            tareas.remove(num)
            volver_al_menu()

    elif opcion == 6: #para ver cuales tareas estan terminadas y cuales no 
        
        contador(hecho)
        volver_al_menu()
                
                


    return opcion, tareas, hecho 

#========================================================================= Fail Safe, para tareas 5 

def failsafet5(_, tareas, opcion):
    safe = 0
    while safe == 0:
       
        safe = 0
        if opcion == 5:
            _ = input("Que tarea quieres quitar?: ")

        if _ in tareas:
            safe = 1
        else:
            print ("La tarea no existe")

    safe = 0        
    return _     

#========================================================================= Fail Safe, para tareas 1  

def failsafet1(_, tareas):
    safe = 0
    while safe == 0:
    
            _ = input ( "Que nueva tarea tienes?: ")

            if _ in tareas:
                safe = 0
                print ("Esta tarea ya existe, pon una que no exista")
            else:
                safe = 1

    
    return _

#========================================================================= Fail Safe, para menu  

def falesafemenu(_, opciones):
    safe = 0
    while safe == 0:
        
        _ = input("Elige: ")
    
        if _ in opciones:
             safe = 1
        else:
            print ("Selecciona un numero que este en las opciones")
        
    return _


#========================================================================= Fail Safe, para tareas 4
def failsafe4(_, hecho, tareas ):
    safe = 0
    while safe == 0:
             
        _ = input("Que tarea quieres marcar como terminada?: ")

        if _ in tareas:
            if hecho[tareas.index(_)] == 1:
                    print ("La tarea ya esta marcada como terminada, selecciona otra")
            else:
                safe = 1
        else:
            print ("La tarea no existe")        
    return _

#========================================================================= Guardar tareas 
def abrir(task):
    dir = os.path.dirname(__file__)
    path = os.path.join(dir, "tarea.txt")
    with open (path) as f:
        for i in f:
            task.append(i.strip())

#========================================================================= Guardar tareas 

def guardar(chequeo, task):
    with open ("tarea.txt", "w") as f:
        for i in task:
            f.write(str(i) + "\n")

    with open("tareas.json","w") as f:
        json.dump(chequeo, f, indent=4) 