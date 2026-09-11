#mensaje = "afuera"

#def cambiar():
#    mensaje = "adentro"
#    print("dentro: ", mensaje)
#    
#cambiar()
#print("fuera: ", mensaje)

#3 tipos de casos
#caso 1: desde andetro, leer una afuera, si funciona
#caso 2: asignarle un valor, copia local
#caso 3: modificar una lista con append, si la cambia
#tareas = []
#
#def agregar(lista, texto):
#    lista.append(texto) #mover los muebles
#    
#agregar(tareas, "estudiar")
#print(tareas)
#
#def remplazar(lista):
#    lista = ["otra"]
#    
#remplazar(tareas)
#print(tareas)

#mal, es por flojos
contador_num = 0
#def sumar():
#    contador = contador + 1
#    
#sumar()
#bien, es por pensarle
def sumar(contador):
    return contador + 1

contador = sumar(contador_num)
print(contador)
