
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