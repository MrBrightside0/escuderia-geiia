#Precuacion correlo bajo tu propio riesgo
#i = 0
#while True:
#    i += 1
#    print(i)

#While: "mientras" mientras se cumpla una condicion, yo voy a seguir corriendo
#A diferencia del for, la condicion que tiene que estar aqui, tiene que ser 
#verdadera

#Quiero sumar los numeros del 1 al 100

#total = 0
#i = 0
#
#while i <= 100:
#    total = total + i
#    i = i + 1
#    
#print(total)

#Cuando uso for y cuando uso while?
#for : usenlo cuando sabes cuantas veces o si recorrer algo que existe
#ejemplo:  recorrer una lista de numeros del 1 al 100
#while: no sabemos cuantas veces, si no hasta que pase algo o si dependemos de algo
#pedir una contraseña hasta que sea correcta, un menu que se repite hasta que elijan salir
#o pongan la contrasena
#REGLA DE ORO: SI AMBOS SIRVEN EN UNA SITUACION USA FOR

tareas = []

def agregar_tarea():
    tarea = input("Añade una nuvea tarea: ")
    tareas.append(tarea)
    print ("Se agrego una nueva tarea")

def ver_tarea():
    if not tareas:
        print ("No tienes tareas pendientes :)")
    else:
        print("Tareas pendientes: ")
        for i, tarea in enumerate(tareas, 1):
            print(str(i)+ ". " + tarea)
        print()
        
def quitar_tarea():
    ver_tarea()
    if tareas:
        num = int(input("¿Qué número de tarea dese eliminar?"))
        eliminada = tareas.pop(num - 1)
        print ("Su tarea "+ eliminada + " fue eliminada con éxito")
        
        
def mostrar_menu():
      print("1. Agregar tarea")
      print("2. Ver tareas")
      print("3. Quitar Tarea")
      print("4. Salir")

opcion = ""
while opcion != "4":
    mostrar_menu()
    opcion = input("Elige: ")
  
    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        ver_tarea()
    elif opcion == "3":
        quitar_tarea()    
    elif opcion == "4":
        print ("Usted esta saliendo del programa")
    else:
        print ("Instrucción inválida")
 
        

#Terminar el menu de tareas y subirlo a su propia rama
#Agregar una linea mas que al salir imprima cuantas tareas quedaron pendientes

#Refactorizar la tarea del while con sus funciones