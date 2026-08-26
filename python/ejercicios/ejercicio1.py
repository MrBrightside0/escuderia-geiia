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

#---------------------------------------------------------------------------------------------
# Peticion de los datos 
print("")
nom = str(input("Cual es tu nombre?: ")) #nombre
edad= int(input("Cuantos anos tienes?: ")) #edad
horad= int(input("Cuantas horas duermes al dia?: ")) # cantidad de horas que uno duerme al dia 
print("Cuanto tiempo te tardas en ir a la uni?") #pedir tiempo de ida
ida= int(input("Horas: ")) #cantidad de horas que te tardas de ida a la uni
idam= int(input('Minutos: ')) #cantidad de minutos que te tardas de ida a la uni
print("Cuanto tiempo te tardas en volver de la uni a tu casa?") #pedir tiempo de vuelta a la casa
vuelta= int(input("Horas: ")) #cantidad de horas que te tardas de vuelta a la casa
vueltam= int(input("Minutos: ")) #cantidad de minutos que te tardas de vuelta a la casa

#---------------------------------------------------------------------------------------------
# Operaciones matematicas

Diav = edad*365 #de tu edad saca los dias vividos 
#Diav significa "dias vividos"

Diasd= int(Diav//(24/horad)) #la cantidad de dias vividos entre la fraccion que representa las horas dormidas del dia
#Diasd significa "dias dormidos"

shecm= 120*(( ida*60 + idam) + (vuelta*60 + vueltam ))#aqui se convirtio todos las horas en minutos y se les sumo a los minutos, sacando minutos 
#shecm significa "suma de heras en camino a minutos"

hec= int (shecm/60) #aqui simplemente estamos sacando la cantidad de horas completas en el camino
#hec significa "horas en camino"

mec= shecm%60 #aqui se saco el residuo de la division, que matematicamente te da la cantidad de minutos restantes
#hecm significa "minutos en camino"
#---------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------
# Impresion de los valores 
print ("")
print("=== FICHA DE PILOTO ===")
print ("")
print(nom + ", " + str(edad) + " anos")
print("Has vivido " + str(Diav) + " días")
print("De esos, has dormido " + str(Diasd) + " días completos")
print ("Este semestre vas a pasar " + str(hec) + " horas y " + str(mec) + " minutos en el camino")
print ("")
print("========================")
print ("")