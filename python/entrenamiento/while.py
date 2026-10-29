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
opcion = 0

while opcion != 5:
    print("")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Ver cantidad de tareas")
    print("4. Terminaste una tarea? ")
    print("5. Salir")
    opcion = int(input("Elige: "))
    print("\033[3J\033[H\033[2J", end="") #te mueve la webada hasta que no se vea lo demas  
    if (opcion) == 1:
        tareas.append(input ( "Que nueva tarea tienes?: "))
    elif opcion == 2:
        if len(tareas) == 0:
            print("No tienes tareas ahora mismo")
        else:
            print("Estas son tus tareas: ")
            for i in tareas:
                print(i)
    elif int(opcion) == 3:
        if len(tareas) == 0:
            print("No tienes tareas ahora mismo")
        else:
            print("Tu tienes: " + str(len(tareas)) + " tarea/s por hacer")
    elif opcion == 4:
        print(tareas)
        tareas.remove(input("Que tarea terminaste?: "))

                         
if len(tareas) != 0:     
    print("Termina tus tareas no seas flojo")
else:
    print("Bien hecho, puedes ver anime todo lo q quieras :3")    

#Terminar el menu de tareas y subirlo a su propia rama
#Agregar una linea mas que al salir imprima cuantas tareas quedaron pendientes
