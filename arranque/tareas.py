import json


def mostrar_menu(): #def cra la función, mi función aquí es mostrar
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Completar tarea")
    print("4. Salir")
    print("5. Ver estadísticas")


def agregar_tarea(lista, texto, fecha): #Diccionario pq ahora son más datos
    tarea = {
        "texto": texto, #claves o indices
        "fecha": fecha,
        "completada": False #False signififica que la tarea no esta completada, True que si lo esta
    }

    lista.append(tarea) #append me ayuda a añadir un elemento al final de la lista
    guardar_tareas(lista)  #Guardo toda la lista en el JSON


def ver_tareas(lista):
    for numero, tarea in enumerate(lista, start=1): #Recorro todas las tareas, enumerate le pone numero cada tarea

        if tarea["completada"]:
            estado = "COMPLETADA"
        else:
            estado = "PENDIENTE"

        print(numero, tarea["texto"], "|", tarea["fecha"], "|", estado) #imprimo la tarea y sus demás datos


def borrar_tarea(lista):
    ver_tareas(lista) #para que el usuario vea los numeros de las tareas y pueda elegir cual borrar

    numero = int(input("¿Cuál quieres marcar como completada :) ? ")) #Input recibe el numero de la tarea

    numero = numero - 1

    lista[numero]["completada"] = True #Busca la tarea y cambia su estado a completada

    guardar_tareas(lista)
    print("Esoo, la tarea esta marcada como completada. :D")
          
def guardar_tareas(lista):
    with open("tareas.json", "w", encoding="utf-8") as archivo: #abro el archivo en modo escritura, si no existe lo crea
        json.dump(lista, archivo, ensure_ascii=False, indent=4) #Lista de python a formato JSON


def cargar_tareas():
    try:
        with open("tareas.json", "r", encoding="utf-8") as archivo: # de JSON a lista de python, abro el archivo en modo lectura
            return json.load(archivo)

    except FileNotFoundError: #Evito que falle si no existe el archivo, si no existe lo crea y devuelve una lista vacia
        return []


def estadisticas(lista):
    completadas = 0 #Creo mis contadores
    pendientes = 0

    for tarea in lista: #Recorro 
        if tarea["completada"]:
            completadas += 1
        else:
            pendientes += 1

    print("Tareas hechas:", completadas)
    print("Tareas pendientes:", pendientes)