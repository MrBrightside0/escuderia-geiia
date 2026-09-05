#CONTAR 
#Tenemos una lista del al 100 y queremos saber cuantos de esos numeros son pares
pares = 0
for i in range(1, 101):
    if i % 2 == 0:
        pares += 1 #pares = pares + 1
print(pares)

#PROMEDIAR sumar y dividir
edades = [19, 21, 20, 22, 19, 30, 43, 20] #la listas son objetos iterables
#iterable :  es aquel elemento que se puede recorrer con un bucle
suma = 0
#len() nos permite hacer un conteo de todo lo que esta dentro de una variable
#se usa principalmente en listas, tuplas y conjuntos
for edad in edades:
    suma += edad #+= suma = suma + edad
print(suma / len(edades))

#COMPARAR encontrar el mayor
mayor = edades[0]
for edad in edades:
    if edad > mayor:
        mayor = edad
print(mayor)