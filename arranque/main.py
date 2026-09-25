#Gestor de Tareas
from tareas import mostrar_menu, agregar_tarea, ver_tareas, borrar_tarea, cargar_tareas, estadisticas
from datetime import datetime

tareas = cargar_tareas() 
opcion = ""

while opcion != "4": #deja de correr al intoducir 4
    mostrar_menu() #Llamamos la función
    
    opcion = input("Elige:")
    if opcion =="1":
        tarea = input("¿Cual es tu nueva tarea :D ?") # preguntar al usuario por la tarea
        fecha= datetime.now().strftime("%Y-%m-%d") #Obtenemos la fecha y hora actual
        agregar_tarea(tareas, tarea, fecha) #meter la respuesta en la lista
        
    elif opcion == "2":  #Con esto podremos mostrar las tareas"
        ver_tareas(tareas)
        
    elif opcion == "3":
        borrar_tarea(tareas)
        
    elif opcion == "5": #Aqui van las estadisticas
        estadisticas(tareas)

pendientes = 0
for tarea in tareas:
    if tarea["completada"] == False:
        pendientes += 1
    if pendientes == 0:
        print( "¡Felicidades! No tienes tareas pendientes.")
    else:
     print("Recuerda que tienes", pendientes, "tareas pendientes. ¡Ánimo, tú puedes!")
    
print("Hasta luego, disfruta tu día :)")



# No olvidar-> Pycache es una carpeta que crea python de manera automatica para guardar 
# versiones compiladas de mis archivos de código en un formato intermedio llamado bytecode
#(bytecode es un lenguaje de bajo nivel que la máquina virtual de Python puede entender y 
# ejecutar más rápido que el código fuente original).

#Pycache se creal importar para varias cosas como: Optimizar la velocidad, ahorrar trabajo 
# y mejorar la organizacion.
# se puede evitar que se creen estas carpetas y esto no altera el funcionamiento del
# programa solo tendrá algunos efectos secundarios como que el programa se ejecute un poco 
# más lento y que no se pueda depurar el código de manera tan eficiente.