#Integer (int) - números enteros, sin decimales. Ej: 5, 20, -3.
#String (str) - texto. Ej: "Hola", "Rogelio".
#Print (print) - muestra algo en la pantalla. Ej: print("Hola").
#Booleano (bool) - solo puede ser Verdadero o Falso: True / False.
#Float (float) - números con decimales. Ej: 3.14, 7.5, -2.8.
#Input (input) - sirve para recibir información que escribe el usuario en el teclado.

#menu
print("""""
¿Qué ejercicio quieres ejecutar?

1 -- Ejercicios con if
2 -- Calificación con if
3 -- Calificación con if, elif y else
4 -- Número positivo, negativo o cero
""""")

ejercicio = int(input("¿Qué ejercicio quieres ejecutar? "))


if ejercicio == 1:
#Ejercicios con if
    edad = int(input("¿Cuántos años tienes? "))

    if edad >= 18:
        print("Puedes pasar")

    if edad < 18:
        print("No puedes pasar bro")


elif ejercicio == 2:

    Cali1 = int(input("Cuanto sacaste? "))

    if Cali1 >= 80:
        print("Has aprobado")

    if Cali1 < 80:
        print("NO has aprobado")


elif ejercicio == 3:
#ejercicios con if, elif y else
    Cali2 = int(input("¿Cuánto sacaste? "))

    if Cali2 > 80:
        print("alaaaa")

    elif Cali2 == 80:
        print("aprobado")

    else:
        print("reprobado")
        

elif ejercicio == 4:
    Numero = float(input("Dame un numero "))
    
    if Numero > 0:
        print("Tu numero es positivo")
        
    elif Numero < 0:
        print("Tu numero es negativo")
      
    #Aqui podemos poner else o elif, realmente no hace mucha diferencia    
    else:
        print("Tu numero es 0 lol")