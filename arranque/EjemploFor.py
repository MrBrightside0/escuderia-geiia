#Bucles For 

#En pocas palabras "for" es un bucle o ciclo que se repite un número determinado de veces.
#Función: 

# Ejemplo sin "for" :(
# 5 veces print ("Hola") - es muuuy tardado o al menos da flojera ;(
    
#Ahora con hagamoslo con "for" :) yay
for i in range(5):
   print(i)

# print va incluido 

#for i in range(5):
   print(i)
#print("Fin")

# Pero que significa cada cosa en este codigo?
# veamos

# i es 

# range (5) es ...
0,1,2,3,4

# Entonces "for" puede traducirse como "Repite esto 5 veces y en cada vuelta i tendrá un número diferente"


# Range es como una lista de números por así decir : for in range(5) -> "ve pasando por esos números uno por uno"

# IMPORTANTE: range puede tener 3 partes: range (inicio, fin, paso)
# Ejemplo: 

#SALTOS: range (inicio, final, salto)
# Es como decir "Empieza aquí, termina antes de aquí y avanza de esta cantidad en esta cantidad" :D
# Ejemplo: 
for i in range(0, 10, 2):
    print(i)

# Es como subir escalones
# los escalones también se pueden bajar :O

# SALTO NEGATIVO: 
# Ejemplo: 
#for i in range(10, 0, -2):
    
    
#Ejemplos variados: 

for i in range(5):
    x= i*5
    print("i=", i, "x=", x)