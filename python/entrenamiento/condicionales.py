edad = int(input("Tu edad:"))

if edad >= 18: #si se cumple esta condicion, se ejecuta despues de los puntos
    print("Eres mayor de edad")
elif edad >= 13: #si no se cumple la primera condicion, se ejcuta esta OJO SIEMPRE VA PRIMERO IF antes de ELIF
    print("Eres un adolescente")
else:  #si de plano ninguna opcion fue evrdadera se ejecuta esta SIEMPRE
    print("Eres menor")
    
print("Esto se impime siempre")

#calificacion = int(input("Tu calificacion:"))
#
#if calificacion > 90:
#    print("Excelente GG")
#elif calificacion >= 70:
#    print("Aprobaste")