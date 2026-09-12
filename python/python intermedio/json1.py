import json

tareas = [
    {"texto": "comprar pan; leche", "hecho": False},
    {"texto": "dormir", "hecho" : True}
]

#Guardar 
with open("tareas.json", "w") as f:
    json.dump(tareas, f, indent=2, ensure_ascii=False)

#Cargar
with open("tareas.json") as f:
    tareas = json.load(f)
    
print(tareas)
print(type(tareas[0]["hecho"]))

#Que es json.

#es un formato de tetxo para guardar datos estructurados
#lo entienden todos los lenguajes
#datos curiosos es que en json true y false se escribe con letras minusculas
#null en vez de none y solo se utiliza comillas dobles

#TAREA
#podamos cambiar nuestras funciones de guardar y cargar para que usen json. Borren
#todo el codigo de split, join y conversion que tenian
#agreguen una tarea que tenga punto y coma, acentos, si todo funciona 
#agreguen al fecha de hoy con datetime, les toca ustedes