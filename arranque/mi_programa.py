def mostrar_menu(): #Definimos la función
    print("1. Agregar tarea")
    print("2. Mostrar tareas") 
    print("3. Borrar tarea")
    print("4. Salir")
    
def agregar_tarea(lista, texto):
    lista.append(texto)
    
def ver_tareas(lista):
    for tarea in lista:
        print (tarea)
    
def borrar_tarea (lista):
    for numero, tarea in enumerate(lista, start=1):
        print(numero, tarea)
    
    numero = int(input("¿Cual quieres borrar?"))
    numero = numero - 1  #restamos 1 para que coincida con el índice de la lista
    lista.pop(numero) #borramos la tarea de la lista con la ayudad de "pop"
    
tareas = []
opcion = ""

while opcion != "4": #deja de correr al intoducir 4
    mostrar_menu() #Llamamos la función
    
    opcion = input("Elige:")
    if opcion =="1":
        tarea = input("¿Cual es tu nueva tarea :D ?") # preguntar al usuario por la tarea
        agregar_tarea(tareas, tarea) #meter la respuesta en la lista
        
    elif opcion == "2":  #Con esto podremos mostrar las tareas"
        ver_tareas(tareas)
        
    elif opcion == "3":
        borrar_tarea(tareas)
        
print("Hasta luego, disfruta tu día :)")
print("Tienes", len(tareas), "tareas pendientes") 
