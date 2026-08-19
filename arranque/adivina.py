# =========================================================
#  arranque/adivina.py  ·  Escudería GEIIA · Viernes S1
#
#  NO LO CORRAS TODAVÍA.
#  Léelo de arriba abajo y escribe en una hoja las cuatro
#  líneas que crees que va a imprimir. Luego lo corremos.
# =========================================================

a = 3 #variable: lugar donde se guarda un valor especifico
#integer int 
nombre = "Katia"
edad = 17
b = "hola soy un string"
#string str es una cadena de texto
c= True #1
d= False #0 
#booleanos bool datos olo verdaderos o falsos

e= .03 
#float numeros con punto decimal
# print() sirve para mostrar información en la consola
print("Hola mundo")
# Se pueden combinar variables de distintos tipos usando +. 
nombre = "Katia"
saludo = "Hola" + nombre
print (saludo)

#También se pueden usar f-strings para combinar texto y variables.
edad = 17
print(f"Hola {nombre}, tienes {edad} años.")

# input () perimte recibir información escrita por el usuario
nombre = input("¿Cuál es tu nombre? ")
print (f"Hola {nombre}, bienvenido a la escudería GEIIA.")
# if permite tomar decisiones.
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")



print(a + b)
print("a + b")

nombre = "GEIIA"
print(nombre * 2)
print(nombre + " " + str(a))
