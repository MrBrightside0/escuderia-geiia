#Lista: se accede por posicion
#piloto = ["Raul", 19, "datos"]
#print(piloto[0])
#piloto[0] = "Juan"
#print(piloto[0])

#Diccionarios
#piloto = {
#    "nombre" : "Raul",
#    "edad" : 19,
#    "capa" : "datos"
#}
#
#print(piloto["nombre"]) #Raul
#
##agregar datos
#piloto["equipo"] = "GEIIA"
#
#piloto["nombre"] = "Juan" #modificando datos
#piloto["edad"] = 29
#
##borrando datos
#print(piloto)
#
##borrar datos
#del piloto["capa"]
#print(piloto)

#key error y get
#piloto = {"nombre" : "Lopez", "edad" : 78, }
#
##keyError
##print(piloto["carrera"])
#
##get NO truena: devuelve None
#print(piloto.get("telefono", "no registrado"))
#
##preguntamos antes de tocar la puerta
#if "telefono" in piloto:
#    print(piloto["telefono"])
    
#Datos curiosos
#Si se puede tener otro tipo de dato como llave
#Se puede tener lista como valor de la llave 
#Se puede tener dos indices iguales (uno redefine al otro)
#y se pueden contar las llaves del diccionario

#diccionario = {
 #   "pilotos" : ["Rodolfo","Rogelio","Joseph", "Katia", "Janeth"],
 #   1 : "dos"
#}
#print(len(diccionario))

#Recorrer un diccionar
#for llave in piloto:
#    print(llave, " : ", piloto[llave])
#    
##las dos cosas a la vez
#for llave, valor in piloto.items():
#    print(llave + ": " + str(valor))
    
#TAREA investiguen que .keys(), .values()
"""
tareas = [
    {"texto" : "estudiar", "hecha" : False},
    {"texto" : "dormir", "hecha" : True}
]

#mostrarlos con marca
for t in tareas:
    #Orden Lectura
    #Segundo    #Primero      #Tercero
    marca = "x" if t["hecha"] else " "
    print("[" + marca + "] " + t["texto"])
    
#contar pendiente, el acumulador que veniamos usando
pendientes = 0
for t in tareas:
    if not t["hecha"]:
        pendientes += 1
"""  
#marca una tarea como hecha
#tareas[0]["hecha"] = True
#print(tareas)        

#una lista de diccionarios es exactamente la forma de 
#un JSON, y JSON son la forma en la que viajan los
#datos por todo internet

#Tarea 
#Convertir la lista de textos en lista de diccionarios
#con texto y hecha. que la opcion 3 del menu por fin
#marque como completada en vez de borrarla
#Opcional para los valientes:
#que la opcion 5 diga cuantas tareas has hecho y cuantas pendientes
'''
from tarea import volver_al_menu, menu_principal, eleccion_de_menu

task = []
opcion = 0
'''

import os
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
def formato(chequeo):
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
            print(tareas)
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

#=========================================== MAIN PROGRAMA 
#from tarea import volver_al_menu, menu_principal, eleccion_de_menu
#             VARIABLES:

#GENERALES 
task = []
opcion = 0
#DIVISORIAS
tareas = []
hecho = []
#DICCIONARIAS 
chequeo = []
llave = {}


#===================================

dir = os.path.dirname(__file__)
path = os.path.join(dir, "tarea.txt")

with open (path) as f:
    for i in f:
        task.append(i.strip())

#===================================

#        PROGRAMA 
    
tareas, hecho = separacion (tareas, hecho, task)

while opcion != 6:
    chequeo = formato(chequeo) 
    opcion = menu_principal()
    opcion, tareas, hecho = eleccion_de_menu(opcion, tareas, hecho, chequeo )

task = juntar(task, tareas, hecho)    

if len(tareas) != 0:     
    print("Termina tus tareas no seas flojo")
else:
    print("Bien hecho, puedes ver anime todo lo q quieras :3")    

with open ("tarea.txt", "w") as f:
    for i in task:
        f.write(str(i) + "\n")    