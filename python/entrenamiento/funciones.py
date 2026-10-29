
#Como se deben usar las funciones para codigo limpio

#def mostrar_menu():
#    #Esta funcion muestra el menu utilizando print bla bla
#def mostrar_tarea():    
#    #Esta funcion muestra la tarea utilizando print bla bla


#Formas de escribir las variables



#funcion: es una linea de codigo, que se puede reutilizar escribiendola una sola vez

#def mostrar_menu():
#    print("1. Agregar tarea")
#    print("2. Ver tareas")
#    print("3. Salir")
#    
#    
#opcion = 0    
#    
#while opcion != 3:
#    mostrar_menu()
#    opcion = int(input("Elige una opcion: "))
    
#anatomia de una funcion
#def saludar(nombre): #lo que esta entre parentesis se llama parametro
#    print("Hola, ", nombre)
#
#saludar("Jacobo")
#saludar("Melany")

#definir no es ejecutar, siempre hay que invocarla saludar()
#def saludar():
#    print("Hola")
    
#mostrar el resultado en pantalla
#def print_suma(a, b):
#    print(a + b)
#    
##entrega el resultado a quien lo llamo
#def return_suma(a, b):
#    return a + b
#    
#resultado = print_suma(6,3)
##print(resultado * 10) # error por que no tolera el dato salido de print con operaciones
#resultado = return_suma(2,3)
#
#print(resultado * 10)

#Lo que pasa dentro de una funcion, se queda dentro de la funcion
#pollo = 100
#
#def suma_tres_n(pollo,b,c):
#    print(pollo + b + c)
#    
#    
#suma_tres_n(2,pollo,pollo)
#print(pollo)

#Mostrando que regresa una funcion sin return
#def saludar(a,b):
#    print(a + b)
#   
#   
#print(type(saludar(1,2)))

#no se puede forzar a una funcion 
#def saludar():
#    print()
#saludar("Hola")


#Agregando texto a una lista
#def agregar_tarea(lista, texto):
#    lista.append(texto)
#    return lista
#    
#lista = ["hola", "dormir", "tarea"]    
#lista_modificada = agregar_tarea(lista,input("Cual es la tarea que quieres agregar? "))
#print(lista_modificada)

#=========================================================================================

#Tarea
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
def eleccion_de_menu():
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

tareas = []
opcion = 0

while opcion != 5:
    opcion = menu_principal()
    tareas = eleccion_de_menu()
                         
if len(tareas) != 0:     
    print("Termina tus tareas no seas flojo")
else:
    print("Bien hecho, puedes ver anime todo lo q quieras :3")    
