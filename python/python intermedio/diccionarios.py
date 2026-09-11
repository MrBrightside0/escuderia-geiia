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
#    "pilotos" : ["Rodolfo","Rogelio","Joseph", "Katia", "Janeth"],
#    1 : "dos"
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
        
#marca una tarea como hecha
tareas[0]["hecha"] = True
print(tareas)        

#una lista de diccionarios es exactamente la forma de 
#un JSON, y JSON son la forma en la que viajan los
#datos por todo internet

#Tarea 
#Convertir la lista de textos en lista de diccionarios
#con texto y hecha. que la opcion 3 del menu por fin
#marque como completada en vez de borrarla
#Opcional para los valientes:
#que la opcion 5 diga cuantas tareas has hecho y cuantas pendientes
