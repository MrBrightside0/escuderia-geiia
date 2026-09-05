#AND y OR y NOT

#Programa para verificar si alguien puede pasar a un bar
edad = int(input("Cual es tu edad? "))
tiene_credencial = bool(int(input("Tienes credencial (0 no 1 si) ")))

#AND nos va aregresar verdadero SI TODAS SUS CONDICIONES SE CUMPLEN
if edad >= 18 and tiene_credencial:
    print("Puedes pasar")
else:
    print("no puedes pasar")
    
#Programa para verificar si alguien puede obtener descuentos
#OR regresa True o verdadero si almenos UNA de sus condiciones se cumple
if edad < 13 or edad > 65:
    print("Entrada con descuento")
else:
    print("no tienes descuento")
    
#not invierte un true or false
print(not True)
print(not False)