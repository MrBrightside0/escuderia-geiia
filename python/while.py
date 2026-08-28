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
opcion = ""

while opcion != "3":
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Salir")
    opcion = input("Elige: ")
    
print("Adios")

#Terminar el menu de tareas y subirlo a su propia rama
#Agregar una linea mas que al salir imprima cuantas tareas quedaron pendientes