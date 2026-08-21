#Un programa que hace cuentas sobre tu propia vida y te imprime una ficha.

#nombre, edad, horas que duermes al día,
#minutos que tardas en llegar a la UANL(ida)

#Lo que tiene que calcular e imprimir
#Días vividos — edad por 365.
#Horas vividas — y de ahí, cuántas has pasado dormido.
#Días completos dormidos — las horas dormidas convertidas a días, redondeado con round().
#Traslado en un semestre — ida y vuelta, cinco días a la semana, dieciséis semanas. El total en minutos, convertido a horas y minutos con // y %.
#Una ficha impresa que junte todo con concatenación.

#SOLO USAR LO VISTO EN CLASE

#Ejemplo de salida
#=== FICHA DE PILOTO ===
#Ana, 19 años
#Has vivido 6935 días
#De esos, has dormido 2312 días completos
#Este semestre vas a pasar 26 horas y 40 minutos en el camino


#Tareita roger
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))
horas_dormir = float(input("¿Cuántas horas duermes al día? "))
minutos_uanl = int(input("¿Cuántos minutos tardas en llegar a la UANL? "))

#dias vividos
dias_vividos = edad * 365

#horas vividas
horas_vividas = dias_vividos * 24

#horas dormidas
horas_dormidas = horas_vividas * horas_dormir

#dias completos dormidos
dias_dormidos = round(horas_dormidas / 24)

#traslado en un semestre
minutos_semestre = minutos_uanl * 2 * 5 * 16
horas_semestre = minutos_semestre // 60
minutos_restantes = minutos_semestre % 60

#Ficha
print("=== FICHA DE PILOTO ===")
print(nombre + ", " + str(edad) + " años")
print("Has vivido " + str(dias_vividos) + " días")
print("De esos, has dormido " + str(dias_dormidos) + " días completos")
print("Este semestre vas a pasar " + str(horas_semestre) + " horas y " + str(minutos_restantes) + " minutos en el camino")