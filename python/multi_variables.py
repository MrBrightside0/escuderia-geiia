#Definiendo multivariables
#v1 , v2 = 2, 3
#print(v1)
#print(v2)

#Listas, se asignan por orden
#comidas_del_dia = ["cereal", "arroz", "huevo"]
#
#desayuno, comida, cena = comidas_del_dia
#print(desayuno)
#print(comida)
#print(cena)

#intercambiar variables
#a = 1
#b = 2
#a , b = b, a
#print(a, b)

#Cuando usarlo: cuando las variables que estamos utilizando, estan relacionadas
#x, y = 0, 0 o desayuno, comida, cena = comidas_del_dia
#Cuando no: cuando no tienne nada que ver
#nombre, contador, activo = "Ana", 0, True

#utilizandolo en contadores
#escuderia = ["rogelio", "rodolfo", "joseph", "katia", "janeth"]
#
#for i, nombre in enumerate(escuderia):
#    print(i + 1, nombre)

#funcion de varias variables
#def multiplicar_3_numeros(a,b,c):
#    a = a * 3
#    b = b * 9
#    c = c * 0
#    return c,b,a
#
#n1, n2 , n3 = multiplicar_3_numeros(1,2,3)
#
#print(n1)
#print(n2)
#print(n3)

n1, n2, n3 = input(" : "), input(" ; "), input(" [ ")
print(n1, n2, n3)