def mostrar_menu():
    print("1. Agregar")
    print("2. Ver")
    print("3. Salir")
    
def agregar_tarea(lista,texto):
    lista.append(texto)
    
def contar_tareas(lista):
    return len(lista)


#dividir la tarea de gestor de tareas en dos archivos
#e improtar las funciones para que quede lo mas corto 
#posible en main.py.
#investiguen que __pycache__ y por que se crea al importar
#otras funciones de otros archivos