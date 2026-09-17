#programa simple para saber en que año nacio alguien



#reminder de lo que ya vimos
#solo avisa una vez

    
#Principal funcion de las excepciones, es QUE INSISTAN
#def pedir_edad(mensaje):
#    while True:
#        try:
#            return int(input(mensaje))
#        except ValueError:
#            print("Eso no es un numero. Otra vez.")
#        
#edad = pedir_edad("Cual es tu edad? ")            
#print(f"Naciste en {2026 - edad}")


#import json
#
#tareas = [
#    {"texto": "comprar pan; leche", "hecho": False},
#    {"texto": "dormir", "hecho" : True}
#]
#
##1 comprar pan y leche
##2 dormir
#
##Guardar 
#with open("tareas.json", "w") as f:
#    json.dump(tareas, f, indent=2, ensure_ascii=False)




#Cargar
#with open("tareas.json") as f:
#    tareas = json.load(f)
#    
#print(tareas)
#
#
#"""
#FUNCIONM PARA VERIFICAR CARGA DE ARCHIVOS JSON
#
#import json
#
#def cargar():
#    try: 
#        with open("tareas.json") as f:
#            return json.load(f)
#    except FileNotFoundError:
#        return []
#    except json.JSONDecodeError:
#        print("El archivo esta danado, empieza de cero")
#        return []
#"""
#
##varios except de distintos errores
#try: 
#    i = int(input("Numeros de tarea: "))
#    tarea = tareas[i - 1]
#    tarea["hecho"] = True
#    
#except ValueError:
#    print("Eso no es un numero")
#    
#except IndexError:
#    print("No existe esa tarea")
#    
#except KeyError:
#    print("Esa tarea esta mal guardada")
    
    
    
#el except que atrapa todo, MALA PRACTICA
#try: 
#    resultado = int("abc")
#except:
#    pass

tareas = ["lavar", "estudiar", "dormir"]

#caso en el que el usuario escribe 0
i = 2
         #true             #false
if i <= len(tareas) and i > 0:
    print(tareas[i - 1])
else:
    print("Oye bro no estas en el rango")

#Para los datos que manejen con excepciones, sigan este orden
#1 - Existe? = escribieron algo, dieron enter o en blanco?
#2 - el del tipo correcto? - try/except value error al convertir 
#3 esta en rango? un if que compare contra len()

#tareas agregar las excepciones y casos posibles
#EL PROGRAMA TIENE QUE SER INQUEBRANTABLE