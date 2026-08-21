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

nom = str(input("Cual es tu nombre? : "))
edad= int(input("Cuantos anos tienes? : "))
print("Cuanto tiempo en horas te tardas en ir a la uni?")
ida= int(input("Horas: "))
idam= int(input('Minutos'))
print("Cuanto tiempo en horas te tardas en volver de la uni a tu casa?")
vuelta= int(input("Horas: "))
vueltam= int(input("Minutos: "))
Diav = int(edad)*365
Diasd= int(Diav)//3

ida_y_vulta_suma_de_horas= ida + vuelta
iyvsm= idam + vueltam 


print(nom + ", " + str(edad) + " anos")
print("Has vivido " + str(Diav) + " días")
print("De esos, has dormido " + str(Diasd) + " días completos")
print ("Este semestre vas a pasar " + str(ida_y_vulta_suma_de_horas) + " horas y " + str(iyvsm) + " minutos en el camino")
